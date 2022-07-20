using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using SoulsFormats;


namespace EREnemyOnslaught
{
    internal class Program
    {
        const string ER_VANILLA_PATH = @"C:\Steam\steamapps\common\ELDEN RING (Vanilla Unpacked)\Game";
        const string ER_MODDING_PATH = @"C:\Steam\steamapps\common\ELDEN RING (Modding)\Game";
        const string ER_DIST_PATH = ER_MODDING_PATH + @"\OnslaughtMod";

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
            DupeCharacters(
                //"m10_00_00_00.msb.dcx",
                //"m11_00_00_00.msb.dcx",
                "m14_00_00_00.msb.dcx"
            );


            #region Param Edits
            string regulationPath = GetVanillaPath("regulation.bin");
            BND4 parambnd = SFUtil.DecryptERRegulation(regulationPath);
            List<PARAMDEF> paramdefs = LoadParamdefs("Defs");
            ChangeBossTeams(parambnd, paramdefs);
            //AddRennalaGraceParams(parambnd, paramdefs);
            SFUtil.EncryptERRegulation(GetModdingPath("regulation.bin"), parambnd);
            File.Copy(GetModdingPath("regulation.bin"), GetDistPath("regulation.bin"), overwrite: true);
            Console.WriteLine("Wrote modded `regulation.bin`.");
            #endregion

            #region Text Edits
            BND4 itemMsgbnd = BND4.Read(Path.Combine(ER_VANILLA_PATH, @"msg\engus\item.msgbnd.dcx"));
            AddBossNames(itemMsgbnd);
            //AddNewGraceText(itemMsgbnd);
            itemMsgbnd.Write(GetModdingPath(@"msg\engus\item.msgbnd.dcx"));
            File.Copy(GetModdingPath(@"msg\engus\item.msgbnd.dcx"), GetDistPath(@"msg\engus\item.msgbnd.dcx"), overwrite: true);
            #endregion

            Console.WriteLine("Done. Press Enter to close.");
            Console.ReadLine();
        }

        static void DupeCharacters(params string[] onlyMaps)
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
                    //AddNewRennalaGrace(msb);
                    MoveRennalaGrace(msb);

                List<MSBE.Part.Enemy> dupedEnemies = new List<MSBE.Part.Enemy>();
                foreach (var character in msb.Parts.Enemies)
                {
                    string modelName = Models.CharacterModels[character.ModelName];
                    if (Models.IgnoreModels.Contains(modelName))
                    {
                        Console.WriteLine($"    Ignoring: {character.Name} ({modelName})");
                        continue;
                    }
                    if (DoNotCloneEntityIDs.Contains(character.EntityID))
                    {
                        Console.WriteLine($"    Ignoring Entity ID: {character.Name} ({modelName} | {character.EntityID})");
                        continue;
                    }
                    //Console.WriteLine($"   Character: {character.Name} ({modelName}) | {character.EntityID} | {string.Join(", ", character.EntityGroupIDs)}");

                    // Duplicate.
                    MSBE.Part.Enemy duped = (MSBE.Part.Enemy)character.DeepCopy();
                    duped.Name += " (Clone)";

                    // Update or nullify entity ID and talk ID, but not group entity IDs.
                    if (CloneEntityIDs.ContainsKey(duped.EntityID))
                    {
                        Console.WriteLine($"    Updating entity ID of '{duped.Name}' from {duped.EntityID} to {CloneEntityIDs[duped.EntityID]}");
                        duped.EntityID = CloneEntityIDs[duped.EntityID];
                    }
                    else
                    {
                        duped.EntityID = 0;
                    }                        
                    
                    duped.TalkID = 0;

                    // Offset X a tiny bit to avoid weird collision issues.
                    duped.Position = new System.Numerics.Vector3(duped.Position.X + 0.5f, duped.Position.Y, duped.Position.Z);

                    dupedEnemies.Add(duped);
                }
                msb.Parts.Enemies.AddRange(dupedEnemies);
                string outputMsbFile = Path.Combine(@"map\mapstudio", Path.GetFileName(msbFile));
                msb.Write(GetModdingPath(outputMsbFile));
                File.Copy(GetModdingPath(outputMsbFile), GetDistPath(outputMsbFile), overwrite: true);
                Console.WriteLine($" --> Wrote modded MSB: {outputMsbFile}");
            }
        }

        static void MoveRennalaGrace(MSBE m14)
        {
            // Move post-Rennala grace outside library and make permanent.

            // In Elden Ring, chr/obj position is the same, thankfully.
            System.Numerics.Vector3 position = new System.Numerics.Vector3(95.878f, 154.105f, -59.438f);

            MSBE.Part.Enemy graceChr = m14.Parts.Enemies.Find(x => x.EntityID == 14000950);
            MSBE.Part.Asset graceObj = m14.Parts.Assets.Find(x => x.EntityID == 14001950);

            graceChr.Position = position;
            graceChr.CollisionPartName = "h009000";
            Console.WriteLine("Move Rennala grace chr.");

            MSBE.Part.Asset statue = m14.Parts.Assets.Find(x => x.Name == "AEG250_120_5000");

            graceObj.Unk1.DrawGroups = statue.Unk1.DrawGroups;
            graceObj.Unk1.DisplayGroups = new uint[8];
            graceObj.Unk1.CollisionMask = new uint[32];
            graceObj.EntityGroupIDs = new int[] { 0, 0, 0, 0, 0, 0, 0, 0 };
            graceObj.Position = position;
            graceObj.UnkPartNames = new string[] { "h009000", "", "h009000", "", "h009000", "" };
            Console.WriteLine("Moved Rennala grace obj.");

            Console.WriteLine("Move Site of Grace outside Rennala fight in m14.");
        }

        static void AddNewRennalaGrace(MSBE m14)
        {
            // Can't get this to work. Character/VFX won't appear.

            // In Elden Ring, chr/obj position is the same, thankfully.
            System.Numerics.Vector3 position = new System.Numerics.Vector3(95.878f, 154.105f, -59.438f);
            
            MSBE.Part.Enemy sourceGraceChr = m14.Parts.Enemies.Find(x => x.EntityID == 14000953);
            MSBE.Part.Asset sourceGraceObj = m14.Parts.Assets.Find(x => x.EntityID == 14001953);
            
            MSBE.Part.Enemy newChr = (MSBE.Part.Enemy)sourceGraceChr.DeepCopy();
            newChr.EntityID = 14000954;
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
            newObj.EntityID = 14001954;
            newObj.EntityGroupIDs = new int[] { 0, 0, 0, 0, 0, 0, 0, 0 };
            newObj.Position = position;
            //newObj.UnkPartNames = new string[] { "h009000", "", "h009000", "", "h009000", "" };
            newObj.Name = "AEG099_060_9004";
            newObj.Unk08 = 9004;
            m14.Parts.Assets.Add(newObj);
            Console.WriteLine($"Added new grace obj with entity ID: {newObj.EntityID}");

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

            PARAM.Row newGrace = new PARAM.Row(bonfireWarpParam.Rows.Find(x => x.ID == 140003));
            newGrace.ID = 140004;
            newGrace["bonfireSubCategorySortId"].Value = 40;
            newGrace["eventflagId"].Value = 71404;
            newGrace["bonfireEntityId"].Value = 14001954;  // new grace obj
            newGrace["posX"].Value = 97.690f;
            newGrace["posY"].Value = 154.093f;  // not used, apparently
            newGrace["posZ"].Value = -54.869f;
            newGrace["textId1"].Value = 140004;  // new text ID

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

            placeNames[140004] = "Outside the Grand Library";

            placeNamesFile.Bytes = placeNames.Write();
        }

        /// <summary>
        /// Load ParamDefs from Paramdex XMLs.
        /// </summary>
        /// <returns></returns>
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

        readonly static Dictionary<int, int> CloneEntityIDs = new Dictionary<int, int>()
        {
            [10000800] = 10000801,  // Godrick the Grafted
            [10000850] = 10000851,  // Margit, the Fell Omen

            [11000850] = 11000851,  // Godfrey, Elden Lord (Phantom)

            // TODO: Ignoring Rennala's summons until clone handles them properly.
            [14000800] = 14000802,  // Rennala Phase 2
            [14000801] = 14000803,  // Rennala Phase 1
            //[14000840] = 14000834,  // Rennala summons
            //[14000841] = 14000835,  // Rennala summons
            //[14000842] = 14000836,  // Rennala summons
            //[14000843] = 14000837,  // Rennala summons
            //[14000844] = 14000838,  // Rennala summons
            //[14000845] = 14000839,  // Rennala summons
            //[14000846] = 14000847,  // Rennala summons

            [14000850] = 14000851,  // Red Wolf of Radagon
        };

        readonly static HashSet<int> DoNotCloneEntityIDs = new HashSet<int>()
        {
            14000700,  // Rennala NPC
            14000701,  // Rennala NPC 2
            14000710,  // Sellen (human)
            14000711,  // Sellen face-ball NPC
            14000712,  // Sellen (human)
            14000713,  // Sellen (human)
            14000715,  // Unknown
            14000716,  // Unknown
            14000720,  // Naked man
            
            // Rennala's Phase 2 summons
            14000840,
            14000841,
            14000842,
            14000843,
            14000844,
            14000845,
            14000846,
        };

        readonly static Dictionary<int, string> NewNPCNames = new Dictionary<int, string>()
        {
            [902030010] = "Rhonda, Queen of the White Dust",
            [902130010] = "Uncle Merbit",
            [903181010] = "Ginger Sif",
            [904750010] = "Godefroy the Gratuitous",
        };
    }
}
