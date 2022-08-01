using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;
using SoulsFormats;


namespace EREnemyOnslaught
{
    internal static partial class Program
    {
        const string ER_VANILLA_PATH = @"C:\Steam\steamapps\common\ELDEN RING (Vanilla Unpacked)\Game";
        const string ER_MODDING_PATH = @"C:\Steam\steamapps\common\ELDEN RING (Modding)\Game";
        const string ER_DIST_PATH = ER_MODDING_PATH + @"\OnslaughtMod";
        const float CLONE_X_OFFSET = 0.5f;

        static string GetModdingPath(string path)
        {
            return Path.Combine(ER_MODDING_PATH, path);
        }

        static string GetVanillaPath(string path)
        {
            return Path.Combine(ER_VANILLA_PATH, path);
        }

        static string GetDistPath(string path)
        {
            return Path.Combine(ER_DIST_PATH, path);
        }

        static void Main()
        {
            Console.WriteLine("Starting...");

            // Copy oo2core_6_win64.dll
            if (!File.Exists("oo2core_6_win64.dll"))
                File.Copy(Path.Combine(ER_VANILLA_PATH, "oo2core_6_win64.dll"), "oo2core_6_win64.dll");

            //DupeCharacters();
            GenerateMSBs(
                //"m10_00_00_00.msb.dcx",
                "m11_00_00_00.msb.dcx",
                "m11_05_00_00.msb.dcx",
                "m12_01_00_00.msb.dcx",
                "m14_00_00_00.msb.dcx",
                "m15_00_00_00.msb.dcx",  // Haligtree
                "m16_00_00_00.msb.dcx",  // Volcano Manor
                "m19_00_00_00.msb.dcx",  // Stone Platform
                "m60_51_36_00.msb.dcx",  // Redmane Castle
                "m60_13_09_02.msb.dcx"  // Radahn large tile
            );

            #region Param Edits
            string regulationPath = GetVanillaPath("regulation.bin");
            BND4 parambnd = SFUtil.DecryptERRegulation(regulationPath);
            List<PARAMDEF> paramdefs = LoadParamdefs("Defs");
            ChangeBossTeams(parambnd, paramdefs);
            AddRennalaGraceParams(parambnd, paramdefs);
            SFUtil.EncryptERRegulation(GetModdingPath("regulation.bin"), parambnd);
            File.Copy(GetModdingPath("regulation.bin"), GetDistPath("regulation.bin"), overwrite: true);
            Console.WriteLine("Wrote modded `regulation.bin`.");
            #endregion

            #region Text Edits
            BND4 itemMsgbnd = BND4.Read(Path.Combine(ER_VANILLA_PATH, @"msg\engus\item.msgbnd.dcx"));
            AddBossNames(itemMsgbnd);
            Console.WriteLine("Added new boss names to text.");
            AddNewGraceText(itemMsgbnd);
            Console.WriteLine("Added new grace names to text.");
            itemMsgbnd.Write(GetModdingPath(@"msg\engus\item.msgbnd.dcx"));
            Console.WriteLine("Wrote modded `msg/engus/item.msgbnd.dcx`.");
            File.Copy(GetModdingPath(@"msg\engus\item.msgbnd.dcx"), GetDistPath(@"msg\engus\item.msgbnd.dcx"), overwrite: true);
            #endregion

            Console.WriteLine("Done. Press Enter to close.");
            Console.ReadLine();
        }

        static void GenerateMSBs(params string[] onlyMaps)
        {
            string mapDir = GetVanillaPath(@"map\mapstudio");
            foreach (string msbFile in Directory.GetFiles(mapDir))
            {
                if (!msbFile.EndsWith(".msb.dcx"))
                    continue;  // non-MSB file

                if (onlyMaps.Length > 0 && !onlyMaps.Contains(Path.GetFileName(msbFile)))
                    continue;  // ignore map

                Console.WriteLine($"Reading vanilla MSB: {Path.GetFileName(msbFile)}");
                MSBE msb = MSBE.Read(msbFile);

                // Add new Rennala grace to m14.
                if (msbFile.EndsWith("m14_00_00_00.msb.dcx"))
                {
                    AddNewRennalaGrace(msb);
                }

                // Duplicate characters.
                List<MSBE.Part.Enemy> clonedCharacters = new List<MSBE.Part.Enemy>();
                foreach (var character in msb.Parts.Enemies)
                {
                    MSBE.Part.Enemy duped = CloneCharacter(character);
                    if (duped != null)
                        clonedCharacters.Add(duped);
                }
                msb.Parts.Enemies.AddRange(clonedCharacters);

                // Duplicate regions.
                List<MSBE.Region> clonedRegions = new List<MSBE.Region>();
                foreach (var region in msb.Regions.GetEntries())
                {
                    MSBE.Region clone = CloneRegion(region);
                    if (clone != null)
                        clonedRegions.Add(clone);
                }
                foreach (var region in clonedRegions)
                    msb.Regions.Add(region);

                // Duplicate spawners.
                List<MSBE.Event.Generator> clonedSpawners = new List<MSBE.Event.Generator>();
                foreach (var spawner in msb.Events.Generators)
                {
                    MSBE.Event.Generator clone = CloneSpawner(spawner, msb.Regions);
                    if (clone != null)
                        clonedSpawners.Add(clone);
                }
                msb.Events.Generators.AddRange(clonedSpawners);

                string outputMsbFile = Path.Combine(@"map\mapstudio", Path.GetFileName(msbFile));
                msb.Write(GetModdingPath(outputMsbFile));
                File.Copy(GetModdingPath(outputMsbFile), GetDistPath(outputMsbFile), overwrite: true);
                Console.WriteLine($" --> Wrote modded MSB: {outputMsbFile}");
            }
        }

        /// <summary>
        /// Clone given `character` according to information in `EntityInfo`.
        /// 
        /// Returns `null` if the character should not be cloned.
        /// </summary>
        /// <param name="character"></param>
        /// <param name="name"></param>
        /// <param name="overrideEntityID"></param>
        /// <returns></returns>
        static MSBE.Part.Enemy CloneCharacter(MSBE.Part.Enemy character, string name = null, int overrideEntityID = -1)
        {
            // Do NOT clone characters with entity ID ending in 7XX *unless* they explicitly appear in Clones.
            if (!Clones.ContainsKey(character.EntityID))
            {
                int modEntityID = character.EntityID % 1000;
                if (700 <= modEntityID && modEntityID <= 799)
                    return null;
            }
            
            string modelName = Models.CharacterModels[character.ModelName];
            if (Models.IgnoreModels.Contains(modelName))
            {
                Console.WriteLine($"    Ignoring: {character.Name} ({modelName})");
                return null;
            }
            if (overrideEntityID == -1 && DoNotCloneEntityIDs.Contains(character.EntityID))
            {
                Console.WriteLine($"    Ignoring Entity ID: {character.Name} ({modelName} | {character.EntityID})");
                return null;
            }

            // Duplicate.
            MSBE.Part.Enemy clone = (MSBE.Part.Enemy)character.DeepCopy();
            if (name != null)
                clone.Name = name;
            else
                clone.Name += " (Clone)";

            // Use manually specified entity ID and transform, if given.
            if (Clones.ContainsKey(character.EntityID))
            {
                CloneInfo info = Clones[character.EntityID];
                clone.EntityID = overrideEntityID != -1 ? overrideEntityID : info.cloneEntityID;
                SetNewTransform(character, info.newSourceTransform, setDefaultXOffset: false);
                SetNewTransform(clone, info.cloneTransform, setDefaultXOffset: true);
            }
                
            Console.WriteLine($"    CHARACTER: '{character.Name}' ({character.EntityID}) -> '{clone.Name}' ({clone.EntityID})");

            // Update or leave group entity IDs.
            List<int> newEntityGroupIDs = new List<int>();
            foreach (int groupID in clone.EntityGroupIDs)
            {
                if (CloneEntityGroupIDs.ContainsKey(groupID))
                {
                    Console.WriteLine($"        Entity Group ID {groupID} -> {CloneEntityGroupIDs[groupID]}");
                    newEntityGroupIDs.Add(CloneEntityGroupIDs[groupID]);
                }
                else
                    newEntityGroupIDs.Add(groupID);
            }
            clone.EntityGroupIDs = newEntityGroupIDs.ToArray();

            // Nullify Talk ID (anything with a talk ID should eventually be ignored).
            clone.TalkID = 0;

            return clone;
        }

        static MSBE.Region CloneRegion(MSBE.Region region)
        {
            // Region MUST be in `Clones` to clone.
            if (!Clones.ContainsKey(region.EntityID))
                return null;

            // Duplicate.
            MSBE.Region clone = region.DeepCopy();
            clone.Name += " (Clone)";
            CloneInfo info = Clones[region.EntityID];
            clone.EntityID = info.cloneEntityID;
            SetNewTransform(region, info.newSourceTransform);
            SetNewTransform(clone, info.cloneTransform);
            Console.WriteLine($"    REGION: '{region.Name}' ({region.EntityID}) -> '{clone.Name}' ({clone.EntityID})");

            return clone;
        }

        static MSBE.Event.Generator CloneSpawner(MSBE.Event.Generator spawner, MSBE.PointParam msbRegions)
        {
            // Spawner entity ID MUST appear in `Clones`.
            if (!Clones.ContainsKey(spawner.EntityID))
            {
                Console.WriteLine($"    Ignoring Spawner with Entity ID: {spawner.Name} ({spawner.EntityID})");
                return null;
            }

            // Duplicate spawner.
            MSBE.Event.Generator clone = (MSBE.Event.Generator)spawner.DeepCopy();
            clone.Name += " (Clone)";

            // Update or nullify entity ID.
            clone.EntityID = Clones[spawner.EntityID].cloneEntityID;
            Console.WriteLine($"    SPAWNER: '{spawner.Name}' ({spawner.EntityID}) -> '{clone.Name}' ({clone.EntityID})");
            
            // Rename non-empty character part names to Clones.
            for (int i = 0; i < clone.SpawnPartNames.Length; i++)
            {
                if (clone.SpawnPartNames[i] != null)
                    clone.SpawnPartNames[i] += " (Clone)";
            }

            if (NewSpawnerInfo.ContainsKey(clone.EntityID))
            {
                // Create new regions at given coordinates and assign their names.
                for (int i = 0; i < NewSpawnerInfo[clone.EntityID].Length; i++)
                {
                    Vector4 newRegionTransform = NewSpawnerInfo[clone.EntityID][i];
                    // Find original region, clone it with new position, and assign its name to Spawner region names.
                    string originalRegionName = spawner.SpawnRegionNames[i];
                    MSBE.Region originalRegion = msbRegions.GetEntries().Find(region => region.Name == originalRegionName);
                    MSBE.Region cloneRegion = originalRegion.DeepCopy();
                    cloneRegion.Position = new Vector3(newRegionTransform.X, newRegionTransform.Y, newRegionTransform.Z);
                    cloneRegion.Rotation = new Vector3(0f, newRegionTransform.W, 0f);
                    cloneRegion.Name += " (Clone)";
                    msbRegions.Add(cloneRegion);
                    clone.SpawnRegionNames[i] = cloneRegion.Name;
                }
            }
            // Otherwise, use same spawn regions.

            return clone;
        }

        static void SetNewTransform(MSBE.Part part, Vector4? newTransform, bool setDefaultXOffset = true)
        {
            if (newTransform.HasValue)
            {
                Vector4 transform = newTransform.Value;
                part.Position = new Vector3(transform.X, transform.Y, transform.Z);
                part.Rotation = new Vector3(0f, transform.W, 0f);
                Console.WriteLine($"        Set new transform for part '{part.Name}' ({part.EntityID})");
            }
            else if (setDefaultXOffset)
            {
                // Offset X a tiny bit to avoid weird collision issues.
                part.Position = new Vector3(part.Position.X + CLONE_X_OFFSET, part.Position.Y, part.Position.Z);
            }
        }

        static void SetNewTransform(MSBE.Region region, Vector4? newTransform)
        {
            if (newTransform.HasValue)
            {
                Vector4 transform = newTransform.Value;
                region.Position = new Vector3(transform.X, transform.Y, transform.Z);
                region.Rotation = new Vector3(0f, transform.W, 0f);
                Console.WriteLine($"        Set new transform for region '{region.Name}' ({region.EntityID})");
            }
        }

        static void AddNewRennalaGrace(MSBE m14)
        {
            // In Elden Ring, chr/obj position is the same, thankfully.
            Vector3 position = new System.Numerics.Vector3(95.878f, 154.105f, -59.438f);
            
            MSBE.Part.Enemy sourceGraceChr = m14.Parts.Enemies.Find(x => x.EntityID == 14000953);
            MSBE.Part.Asset sourceGraceObj = m14.Parts.Assets.Find(x => x.EntityID == 14001953);
            MSBE.Part.Player sourceGracePlayer = m14.Parts.Players.Find(x => x.EntityID == 14000983);

            MSBE.Part.Enemy newChr = (MSBE.Part.Enemy)sourceGraceChr.DeepCopy();
            newChr.EntityID = 14000955;
            newChr.Position = position;
            newChr.CollisionPartName = "h009000"; 
            newChr.Name = "c1000_9008";
            newChr.Unk08 = 9008;
            m14.Parts.Enemies.Add(newChr);
            Console.WriteLine($"Added new grace chr with entity ID: {newChr.EntityID}");

            MSBE.Part.Asset statue = m14.Parts.Assets.Find(x => x.Name == "AEG250_120_5000");

            MSBE.Part.Asset newObj = (MSBE.Part.Asset)sourceGraceObj.DeepCopy();
            newObj.Unk1.DrawGroups = statue.Unk1.DrawGroups;
            newObj.Unk1.DisplayGroups = new uint[8];
            newObj.Unk1.CollisionMask = new uint[32];
            newObj.EntityID = 14001955;
            newObj.EntityGroupIDs = new int[] { 0, 0, 0, 0, 0, 0, 0, 0 };
            newObj.Position = position;
            //newObj.UnkPartNames = new string[] { "h009000", "", "h009000", "", "h009000", "" };
            newObj.Name = "AEG099_060_9004";
            newObj.Unk08 = 9004;
            m14.Parts.Assets.Add(newObj);
            Console.WriteLine($"Added new grace obj with entity ID: {newObj.EntityID}");

            MSBE.Part.Player newPlayer = (MSBE.Part.Player)sourceGracePlayer.DeepCopy();
            newPlayer.EntityID = 14000985;
            newPlayer.Position = new System.Numerics.Vector3(97.690f, 154.093f, -54.869f);
            newPlayer.Rotation = new System.Numerics.Vector3(0f, 150f, 0f);
            newPlayer.Name = "c0000_9004";
            newPlayer.Unk08 = 9004;
            m14.Parts.Players.Add(newPlayer);
            Console.WriteLine($"Added new grace player spawn with entity ID: {newPlayer.EntityID}");

            Console.WriteLine("Added new Site of Grace outside Rennala fight in m14.");

            // Resort parts.
            m14.Parts.Enemies.Sort((x, y) => x.Name.CompareTo(y.Name));
            m14.Parts.Assets.Sort((x, y) => x.Name.CompareTo(y.Name));
        }

        static void ChangeBossTeams(BND4 parambnd, List<PARAMDEF> paramdefs)
        {
            // Change all NPCs with "Boss" team to "Enemy" team so duped bosses don't hurt each other.
            BinderFile npcParamFile = parambnd.Files.Find(x => x.Name == $@"N:\GR\data\Param\param\GameParam\NpcParam.param");
            PARAM npcParam = PARAM.Read(npcParamFile.Bytes);
            npcParam.ApplyParamdefCarefully(paramdefs);

            foreach (var row in npcParam.Rows)
            {
                byte oldTeamType = (byte)row["teamType"].Value;
                if (oldTeamType == 7)
                {
                    //Console.WriteLine($"{row.ID}: {oldTeamType} -> 6");
                    row["teamType"].Value = 6;  // Enemy
                }
            }
            Console.WriteLine("Changed boss teams (7) to enemy (6).");
            npcParamFile.Bytes = npcParam.Write();
        }

        static void AddRennalaGraceParams(BND4 parambnd, List<PARAMDEF> paramdefs)
        {
            BinderFile bonfireWarpFile = parambnd.Files.Find(x => x.Name == $@"N:\GR\data\Param\param\GameParam\BonfireWarpParam.param");
            PARAM bonfireWarpParam = PARAM.Read(bonfireWarpFile.Bytes);
            bonfireWarpParam.ApplyParamdefCarefully(paramdefs);

            PARAM.Row newGrace = new PARAM.Row(bonfireWarpParam.Rows.Find(x => x.ID == 140003))
            {
                ID = 140005  // to match entity ID
            };
            newGrace["bonfireSubCategorySortId"].Value = 40;
            newGrace["eventflagId"].Value = 71405;
            newGrace["bonfireEntityId"].Value = 14001955;  // new grace obj
            newGrace["posX"].Value = 97.690f;  // icon position on map
            newGrace["posY"].Value = 154.093f;
            newGrace["posZ"].Value = -54.869f;
            newGrace["textId1"].Value = 140005;  // new text ID

            bonfireWarpParam.Rows.Add(newGrace);
            bonfireWarpParam.Rows.Sort((x, y) => x.ID.CompareTo(y.ID));

            Console.WriteLine("Added bonfire warp params for new Rennala grace.");
            bonfireWarpFile.Bytes = bonfireWarpParam.Write();
        }

        static void AddBossNames(BND4 item)
        {
            BinderFile npcNamesFile = item.Files.Find(x => x.Name.EndsWith("NpcName.fmg"));
            FMG npcNames = FMG.Read(npcNamesFile.Bytes);

            foreach (KeyValuePair<int, string> idText in NewNPCNames)
                npcNames.Entries.Add(new FMG.Entry(idText.Key, idText.Value));

            npcNamesFile.Bytes = npcNames.Write();
        }

        static void AddNewGraceText(BND4 item)
        {
            BinderFile placeNamesFile = item.Files.Find(x => x.Name.EndsWith("PlaceName.fmg"));
            FMG placeNames = FMG.Read(placeNamesFile.Bytes);

            placeNames[140005] = "Outside the Grand Library";

            placeNamesFile.Bytes = placeNames.Write();
        }

        static List<PARAMDEF> LoadParamdefs(string defsDirectory)
        {
            List<PARAMDEF> defs = new List<PARAMDEF>();
            foreach (string file in Directory.GetFiles(defsDirectory))
            {
                PARAMDEF paramdef = PARAMDEF.XmlDeserialize(file);
                defs.Add(paramdef);
            }
            return defs;
        }
    }
}
