using System.Collections.Generic;
using System.Numerics;

namespace EREnemyOnslaught
{
    internal static partial class Program
    {
        public class CloneInfo
        {
            public int cloneEntityID;
            public Vector4? cloneTransform;  // if null, transform will not be changed
            public Vector4? newSourceTransform;  // if not null, original entity will be moved to here

            public CloneInfo(int cloneEntityID, Vector4? cloneTransform = null, Vector4? newSourceTransform = null)
            {
                this.cloneEntityID = cloneEntityID;
                this.cloneTransform = cloneTransform;
                this.newSourceTransform = newSourceTransform;
            }
        }

        public readonly static Dictionary<int, CloneInfo> Clones = new Dictionary<int, CloneInfo>()
        {
            // m10_00_00_00 (Stormveil Castle)
            [10000800] = new CloneInfo(10000801, new Vector4(-231.069f, 74.125f, 351.944f, -30.807f)),  // Godrick the Grafted
            [10000850] = new CloneInfo(10000851, new Vector4(-24.959f, -1.365f, -21.452f, -93.901f)),  // Margit, the Fell Omen

            // m11_00_00_00 (Leyndell, Royal Capital)
            [11000800] = new CloneInfo(11000801, new Vector4(44.052f, 64.963f, -419.682f, 142.331f), new Vector4(38.468f, 64.963f, -423.992f, 142.331f)),  // Morgott, the Omen King (estimated from m11_05)
            [11000850] = new CloneInfo(11000851, new Vector4(-134.334f, 31.128f, -386.582f, 0f), new Vector4(-129.671f, 31.128f, -386.582f, 0f)),  // Godfrey Phantom (estimated from m11_05)

            // m11_05_00_00 (Leyndell, Ashen Capital)
            [11050801] = new CloneInfo(11050803, new Vector4(39.053f, 64.963f, -423.966f, -76.133f), new Vector4(43.975f, 64.963f, -419.814f, -4.977f)),  // Godfrey (before Hoarah Loux)
            [11050800] = new CloneInfo(11050802),  // Hoarah Loux
            [11052815] = new CloneInfo(11052813, new Vector4(28.830f, 64.978f, -411.535f, 142.805f)),  // new Godfrey position
            [11052816] = new CloneInfo(11052814, new Vector4(34.600f, 64.978f, -407.156f, 142.805f)),  // new Godfrey clone position
            [11050850] = new CloneInfo(11050858, new Vector4(-131.471f, 31.030f, -384.865f, 89.980f), new Vector4(-131.469f, 31.030f, -388.253f, 89.980f)),  // Sir Gideon Ofnir (variants are using lower IDs)

            // m12_01_00_00 (Ainsel River)
            [12010400] = new CloneInfo(12010450, new Vector4(18.331f, -182.710f, -52.475f, -57.083f), new Vector4(12.220f, -182.710f, -61.915f, -57.083f)),  // Malformed Star 1
            [12010401] = new CloneInfo(12010451, new Vector4(287.052f, -80.652f, 106.993f, -143.411f)),  // Malformed Star 2
            [12010420] = new CloneInfo(12010470, new Vector4(-430.882f, -373.640f, -539.544f, -94.105f)),  // Ulcerated Tree Spirit before Astel
            [12010421] = new CloneInfo(12010471, new Vector4(-366.853f, -292.897f, -303.518f, -19.373f)),  // Onyx Lord
            [12010800] = new CloneInfo(12010803),  // Dragonkin Soldier of Nokstella (Health Pool)
            [12010801] = new CloneInfo(12010804, new Vector4(-122.336f, -224.499f, 136.190f, -2.957f)),  // Dragonkin Soldier of Nokstella (Phase One)
            [12010802] = new CloneInfo(12010805, new Vector4(-122.336f, -224.499f, 136.190f, -2.957f)),  // Dragonkin Soldier of Nokstella (Phase Two)
            [12010850] = new CloneInfo(12010851, new Vector4(-206.860f, -317.072f, -305.404f, -139.372f)),  // Dragonkin Soldier (Lake of Rot)

            // m12_02_00_00 (Siofra River)
            [12020800] = new CloneInfo(12020802),  // Gargoyle 1
            [12020801] = new CloneInfo(12020803),  // Gargoyle 2
            [12020830] = new CloneInfo(12020831),  // Dragonkin Soldier
            [12020850] = new CloneInfo(12020851),  // Mimic Tear (c0000)
            [12020860] = new CloneInfo(12020861),  // Mimic Tear (Silver Tear)

            // m12_03_00_00 (Deeproot Depths)
            [12030390] = new CloneInfo(12030392),  // Crucible Knight Siluria
            [12030391] = new CloneInfo(12030393),  // Erdtree Avatar
            [12030800] = new CloneInfo(12030820),  // FiasChampion0
            [12030810] = new CloneInfo(12030830),  // SorcererRogier
            [12030811] = new CloneInfo(12030831),  // LioneltheLionhearted
            [12030812] = new CloneInfo(12030832),  // LionelSidekick2
            [12030813] = new CloneInfo(12030833),  // LionelSidekick1
            [12030814] = new CloneInfo(12030834),  // UnknownFiasChampion
            [12030850] = new CloneInfo(12030851),  // LichdragonFortissax

            // m12_04_00_00 (Astel)
            [12040800] = new CloneInfo(12040801),  // Astel

            // m12_05_00_00 (Mohgwyn Dynasty Palace)
            [12050800] = new CloneInfo(12050801),  // Mohg, Lord of Blood

            // m12_08_00_00 (Ancestor Spirit Arena)
            [12080800] = new CloneInfo(12080801),  // Ancestor Spirit

            // m13_00_00_00 (Crumbling Farum Azula)
            [13000496] = new CloneInfo(13000497),  // Draconic Tree Sentinel
            [13000800] = new CloneInfo(13000802),  // Maliketh Phase Two
            [13000801] = new CloneInfo(13000803, new Vector4(198.570f, -32.511f, 378.754f, 99.665f), new Vector4(195.375f, -32.511f, 369.344f, 116.612f)),  // Maliketh Phase One
            [13000830] = new CloneInfo(13000831, new Vector4(17.664f, 1009.676f, 316.889f, 75.706f), new Vector4(11.360f, 1009.676f, 341.630f, 75.706f)),  // Dragonlord Placidusax
            [13000850] = new CloneInfo(13000860),  // Godskin Duo health pool
            [13000851] = new CloneInfo(13000861),  // Godskin Duo Apostle
            [13000852] = new CloneInfo(13000862),  // Godskin Duo Noble
            // TODO: Clone spawners with new region locations. Also check cloned IDs are available.
            [13003851] = new CloneInfo(13003853),  // Godskin Apostle spawner
            [13003852] = new CloneInfo(13003854),  // Godskin Noble spawner

            // m14_00_00_00 (Academy of Raya Lucaria)
            // RENNALA
            [14000800] = new CloneInfo(14000802, new Vector4(71.080f, -838.729f, -24.445f, 82.298f), new Vector4(69.962f, -838.729f, -19.720f, 69.307f)),  // Rennala Phase 2
            [14000801] = new CloneInfo(14000803, new Vector4(40.043f, 154.097f, -28.652f, -125.235f), new Vector4(43.280f, 154.097f, -18.753f, -125.235f)),  // Rennala Phase 1
            // RENNALA STUDENTS
            [14000810] = new CloneInfo(14000860),
            [14000811] = new CloneInfo(14000861),
            [14000812] = new CloneInfo(14000862),
            [14000813] = new CloneInfo(14000863),
            [14000814] = new CloneInfo(14000864),
            [14000815] = new CloneInfo(14000865),
            [14000816] = new CloneInfo(14000866),
            [14000817] = new CloneInfo(14000867),
            [14000818] = new CloneInfo(14000868),
            [14000819] = new CloneInfo(14000869),
            [14000820] = new CloneInfo(14000870),
            [14000821] = new CloneInfo(14000871),
            [14000822] = new CloneInfo(14000872),
            [14000823] = new CloneInfo(14000873),
            [14000824] = new CloneInfo(14000874),
            [14000825] = new CloneInfo(14000875),
            [14000826] = new CloneInfo(14000876),
            [14000827] = new CloneInfo(14000877),
            [14000828] = new CloneInfo(14000878),
            [14000829] = new CloneInfo(14000879),
            [14000830] = new CloneInfo(14000880),
            [14000831] = new CloneInfo(14000881),
            [14000832] = new CloneInfo(14000882),
            [14000833] = new CloneInfo(14000883),
            // Rennala student spawners (using same regions)
            [14003810] = new CloneInfo(14003710),
            [14003811] = new CloneInfo(14003711),
            [14003812] = new CloneInfo(14003712),
            [14003813] = new CloneInfo(14003713),
            [14003814] = new CloneInfo(14003714),
            [14003815] = new CloneInfo(14003715),
            [14003816] = new CloneInfo(14003716),
            [14003817] = new CloneInfo(14003717),
            [14003818] = new CloneInfo(14003718),
            // Rennala summons
            [14000840] = new CloneInfo(14000890),  // Bloodhound Knight
            [14000841] = new CloneInfo(14000891),  // Wolf0
            [14000842] = new CloneInfo(14000892),  // Wolf1
            [14000843] = new CloneInfo(14000893),  // Wolf2
            [14000844] = new CloneInfo(14000894),  // Wolf3
            [14000845] = new CloneInfo(14000895),  // Troll
            [14000846] = new CloneInfo(14000896),  // Dragon

            [14000850] = new CloneInfo(14000851, new Vector4(149.847f, 110.182f, -224.778f, -93.632f), new Vector4(149.101f, 110.182f, -220.903f, -93.632f)), // Red Wolf of Radagon
            [14002856] = new CloneInfo(14002857, new Vector4(152.379f, 110.197f, -220.576f, -87.560f), new Vector4(152.552f, 110.197f, -224.625f, -87.560f)),  // Red Wolf first position

            [15000800] = new CloneInfo(15000806),  // Malenia  TODO: Move

            // m16_00_00_00 (Volcano Manor)
            [16000800] = new CloneInfo(16000802, new Vector4(85.891f, -439.508f, -120.969f, -162.615f), new Vector4(106.285f, -439.508f, -119.676f, 167.795f)),  // Rykard (Phase Two)
            [16000801] = new CloneInfo(16000803, new Vector4(85.891f, -439.508f, -120.969f, -162.615f), new Vector4(106.285f, -439.508f, -119.676f, 167.795f)),  // Rykard (Phase One)
            [16002831] = new CloneInfo(16002832, new Vector4(85.891f, -439.508f, -120.969f, -162.615f), new Vector4(106.285f, -439.508f, -119.676f, 167.795f)),  // Rykard Phase Two move point
            [16000850] = new CloneInfo(16000851, new Vector4(59.896f, 7.023f, -205.541f, 107.623f), new Vector4(56.589f, 7.023f, -212.446f, 121.034f)),  // Godskin Noble
            [16000860] = new CloneInfo(16000862, new Vector4(221.695f, -132.944f, -262.066f, -125.258f)),  // Iron Virgin 1
            [16000861] = new CloneInfo(16000863, new Vector4(250.684f, -133.499f, -251.213f, 170.014f)),  // Iron Virgin 2

            // m19_00_00_00 (Stone Platform)
            // Elden Beast (801-804 used by Elden Beast stuff)
            [19000800] = new CloneInfo(19000805, new Vector4(206.755f, -719.985f, -689.934f, 155.434f), new Vector4(220.386f, -719.985f, -683.703f, 155.434f)),
            // Radagon (811 used by something else)
            [19000810] = new CloneInfo(19000812, new Vector4(198.376f, 102.257f, -623.591f, 110.279f)),

            // Caelid
            [1051360800] = new CloneInfo(1051360802, new Vector4(90.810f, 91.750f, 34.136f, 12.908f)),  // Redmane Castle duo boss (Leonine Misbegotten) 
            [1051360801] = new CloneInfo(1051360803, new Vector4(97.482f, 105.500f, 38.728f, 93.109f)),  // Redmane Castle duo boss (Crucible Knight)
            // RADAHN
            [1052380800] = new CloneInfo(1052380801, new Vector4(-435.286f, 34.595f, 86.675f, 96.100f)),  // Starscourge Radahn
            [1052380899] = new CloneInfo(1052380898),  // Starscourge Raddahn meteor angle dummy (c0000)
            [1052380200] = new CloneInfo(1052380201),  // summon
            [1052380260] = new CloneInfo(1052380261),  // summon
            [1052380280] = new CloneInfo(1052380281),  // summon
            [1052380300] = new CloneInfo(1052380301),  // summon
            [1052380320] = new CloneInfo(1052380321),  // summon
            [1052380340] = new CloneInfo(1052380341),  // summon
            [1052380220] = new CloneInfo(1052380221),  // summon
            [1052380240] = new CloneInfo(1052380241),  // summon

            // Mountaintops
            [1052520801] = new CloneInfo(1052520803, new Vector4(-337.454f, 1859.962f, -374.085f, -37.187f)),  // Fire Giant (Phase One/Two)
            [1052520800] = new CloneInfo(1052520802),  // Fire Giant (Phase Three)
        };

        public readonly static Dictionary<int, int> CloneEntityGroupIDs = new Dictionary<int, int>()
        {
            [13005851] = 13005852,  // Godskin Duo

            [14005810] = 14005812,  // Rennala Students
            [14005811] = 14005813,  // Rennala Students (Unknown subgroup?)
            [14005820] = 14005830,  // Rennala Summons
        };

        public readonly static HashSet<int> DoNotCloneEntityIDs = new HashSet<int>()
        {
            // TODO: Starting to seem like I should ignore any entity ending in 7XX (NPCs).

            // m14_00_00_00
            14000710,  // SorceressSellen0
            14000712,  // SorceressSellen1
            14000713,  // SorceressSellen2
            14000730,  // SorceressSellen3
            14000720,  // BoctheSeamster
            14000740,  // SorcererThops
            14000715,  // WitchHunterJerren0
            14000716,  // WitchHunterJerren1
            14000717,  // WitchHunterJerren2
            14000700,  // RennalaNPC1
            14000701,  // RennalaNPC2
            14000711,  // GravenSchool (Sellen)

            // Malenia spirits (for now)
            15000801,
            15000802,
            15000803,
            15000804,
            15000805,

            // Volcano Manor NPCs
            16000710,  // Patches
            16000730,  // KnightDiallos
            16000750,  // RecusantBernahl
            16000700,  // Tanith0
            16000701,  // Tanith1
            16000770,  // RykardHatingSpirit
            16000720,  // RyatheScout0
            16000722,  // RyatheScout1
            16000740,  // Crucible Knight
            16000741,  // Crucible Knight

            // Redmane Castle NPCs
            1051360700,  // WitchHunterJerren0
            1051360701,  // WitchHunterJerren1
            1051360705,  // Alexander
            1051360715,  // LionelTheLionhearted
            1051360725,  // GreatHornedTragoth
            1051360730,  // Okina
            1051360735,  // FingerMaidenTherolina

            // Radahn arena NPCs
            1052380726,  // BlaiddNPC
            1052380699,  // CleanrotKnight
            1052380706,  // AlexanderNPC

            // Gideon battle variants
            11050851,
            11050852,
            11050853,
            11050854,
            11050855,
            11050856,
            11050857,
        };

        public readonly static Dictionary<int, string> NewNPCNames = new Dictionary<int, string>()
        {
            [902030010] = "Rhonda, Queen of the White Dust",
            [902030011] = "Rhonda, Queen of the White Dust",
            [902130010] = "Uncle Merbit",
            [903181010] = "Ginger Sif",
            [904750010] = "Godefroy the Gratuitous",
            [904710010] = "Yet Another God-Devouring Serpent",
            [904710011] = "Ryktar, Definitely Also Intended to Be Devoured",
            [904730010] = "Moonman Mazohr",
            [904770000] = "Valiant Gargoyles (Greatsword)",
            [904770001] = "Valiant Gargoyles (Twinblade)",
            [902120010] = "Malonia, Middle Finger of Miyazaki",
            [904520010] = "Dragonlord Eric",
        };
    }
}
