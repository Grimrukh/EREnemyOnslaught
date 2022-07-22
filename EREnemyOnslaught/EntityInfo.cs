using System.Collections.Generic;
using System.Numerics;

namespace EREnemyOnslaught
{
    internal static partial class Program
    {
        public readonly static Dictionary<int, int> CloneEntityIDs = new Dictionary<int, int>()
        {
            [10000800] = 10000801,  // Godrick the Grafted
            [10000850] = 10000851,  // Margit, the Fell Omen

            [11000850] = 11000851,  // Godfrey, Elden Lord (Phantom)

            // RENNALA
            [14000800] = 14000802,  // Rennala Phase 2
            [14000801] = 14000803,  // Rennala Phase 1
            // Rennala students
            [14000810] = 14000860,
            [14000811] = 14000861,
            [14000812] = 14000862,
            [14000813] = 14000863,
            [14000814] = 14000864,
            [14000815] = 14000865,
            [14000816] = 14000866,
            [14000817] = 14000867,
            [14000818] = 14000868,
            [14000819] = 14000869,
            [14000820] = 14000870,
            [14000821] = 14000871,
            [14000822] = 14000872,
            [14000823] = 14000873,
            [14000824] = 14000874,
            [14000825] = 14000875,
            [14000826] = 14000876,
            [14000827] = 14000877,
            [14000828] = 14000878,
            [14000829] = 14000879,
            [14000830] = 14000880,
            [14000831] = 14000881,
            [14000832] = 14000882,
            [14000833] = 14000883,
            // Rennala student spawners
            [14003810] = 14003710,
            [14003811] = 14003711,
            [14003812] = 14003712,
            [14003813] = 14003713,
            [14003814] = 14003714,
            [14003815] = 14003715,
            [14003816] = 14003716,
            [14003817] = 14003717,
            [14003818] = 14003718,
            // Rennala summons
            [14000840] = 14000890,  // Bloodhound Knight
            [14000841] = 14000891,  // Wolf0
            [14000842] = 14000892,  // Wolf1
            [14000843] = 14000893,  // Wolf2
            [14000844] = 14000894,  // Wolf3
            [14000845] = 14000895,  // Troll
            [14000846] = 14000896,  // Dragon

            [14000850] = 14000851,  // Red Wolf of Radagon
            [14002856] = 14002857,  // Red Wolf first position

            [15000800] = 15000806,  // Malenia

            [16000800] = 16000802,  // Rykard (Phase Two)
            [16000801] = 16000803,  // Rykard (Phase One)
            [16002831] = 16002832,  // Rykard Phase Two move point
            [16000850] = 16000851,  // Godskin Noble
            [16000860] = 16000862,  // Iron Virgin 1
            [16000861] = 16000863,  // Iron Virgin 2

            [1051360800] = 1051360802,  // Redmane Castle duo boss (Leonine Misbegotten) 
            [1051360801] = 1051360803,  // Redmane Castle duo boss (Crucible Knight)

            [1052380800] = 1052380801,  // Starscourge Radahn
            [1052380899] = 1052380898,  // Starscourge Raddahn meteor angle dummy (c0000)
            [1052380200] = 1052380201,  // summon
            [1052380260] = 1052380261,  // summon
            [1052380280] = 1052380281,  // summon
            [1052380300] = 1052380301,  // summon
            [1052380320] = 1052380321,  // summon
            [1052380340] = 1052380341,  // summon
            [1052380220] = 1052380221,  // summon
            [1052380240] = 1052380241,  // summon
        };

        public readonly static Dictionary<int, int> CloneEntityGroupIDs = new Dictionary<int, int>()
        {
            [14005810] = 14005812,  // Rennala Students
            [14005811] = 14005813,  // Rennala Students (Unknown subgroup?)
            [14005820] = 14005830,  // Rennala Summons
        };

        public readonly static HashSet<int> DoNotCloneEntityIDs = new HashSet<int>()
        {
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
        };

        public readonly static Dictionary<int, (Vector3 position, float rotationY)> NewTransforms = new Dictionary<int, (Vector3, float)>()
        {
            [10000801] = (new Vector3(-231.069f, 74.125f, 351.944f), -30.807f),  // Godrick Clone
            [10000851] = (new Vector3(-24.959f, -1.365f, -21.452f), -93.901f),  // Margit Clone

            [14000800] = (new Vector3(69.962f, -838.729f, -19.720f), 69.307f),  // Rennala Phase Two
            [14000802] = (new Vector3(71.080f, -838.729f, -24.445f), 82.298f),  // Rennala Phase Two Clone
            [14000801] = (new Vector3(43.280f, 154.097f, -18.753f), -125.235f),  // Rennala Phase One
            [14000803] = (new Vector3(40.043f, 154.097f, -28.652f), -125.235f),  // Rennala Phase One Clone
            [14000850] = (new Vector3(149.101f, 110.182f, -220.903f), -93.632f),  // Red Wolf of Radagon
            [14000851] = (new Vector3(149.847f, 110.182f, -224.778f), -93.632f),  // Red Wolf of Radagon Clone
            [14002856] = (new Vector3(152.552f, 110.197f, -224.625f), -87.560f),  // Red Wolf of Radagon (First Point)
            [14002857] = (new Vector3(152.379f, 110.197f, -220.576f), -87.560f),  // Red Wolf of Radagon Clone (First Point)

            [16000800] = (new Vector3(106.285f, -439.508f, -119.676f), 167.795f),  // Rykard Phase Two
            [16000802] = (new Vector3(85.891f, -439.508f, -120.969f), -162.615f),  // Rykard Phase Two (Clone)
            [16000801] = (new Vector3(106.285f, -439.508f, -119.676f), 167.795f),  // Rykard Phase One
            [16000803] = (new Vector3(85.891f, -439.508f, -120.969f), -162.615f),  // Rykard Phase One (Clone)
            [16002831] = (new Vector3(106.285f, -439.508f, -119.676f), 167.795f),  // Rykard Phase Two move point
            [16002832] = (new Vector3(85.891f, -439.508f, -120.969f), -162.615f),  // Rykard Phase Two (Clone) move point
            [16000850] = (new Vector3(56.589f, 7.023f, -212.446f), 121.034f),  // Godskin Noble
            [16000851] = (new Vector3(59.896f, 7.023f, -205.541f), 107.623f),  // Godskin Noble Clone
            [16000862] = (new Vector3(221.695f, -132.944f, -262.066f), -125.258f),  // Iron Virgin 1 Clone
            [16000863] = (new Vector3(250.684f, -133.499f, -251.213f), 170.014f),  // Iron Virgin 2 Clone

            [1051360802] = (new Vector3(90.810f, 91.750f, 34.136f), 12.908f),  // Redmane Castle Leonine Misbegotten Clone
            [1051360803] = (new Vector3(97.482f, 105.500f, 38.728f), 93.109f),  // Redmane Castle Crucible Knight Clone
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
            [902120010] = "Malonia, Middle Finger of Miyazaki",
        };
    }
}
