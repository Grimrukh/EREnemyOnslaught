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
            #region m10_00_00_00 (Stormveil Castle)
            [10000800] = new CloneInfo(10000801, new Vector4(-231.069f, 74.125f, 351.944f, -30.807f)),  // Godrick the Grafted
            [10000850] = new CloneInfo(10000851, new Vector4(-24.959f, -1.365f, -21.452f, -93.901f)),  // Margit, the Fell Omen
            [10000280] = new CloneInfo(10000380, new Vector4(-218.870f, 67.811f, 103.709f, -122.757f)),  // Grafted Scion
            [10000291] = new CloneInfo(10000292, new Vector4(-261.773f, 13.846f, 145.737f, 158.013f), new Vector4(-256.515f, 13.846f, 147.659f, 158.013f)),  // Ulcerated Tree Spirit
            [10000498] = new CloneInfo(10000499, new Vector4(-298.527f, -24.369f, 91.299f, 138.522f)),  // Crucible Knight
            [10000289] = new CloneInfo(10000288, new Vector4(-124.775f, 37.132f, 116.347f, 19.858f)),  // Lion Guardian
            #endregion

            #region m10_01_00_00 (Chapel of Anticipation)
            [10010800] = new CloneInfo(10010801, new Vector4(-44.921f, 21.325f, -39.876f, -7.205f), new Vector4(-38.681f, 21.325f, -39.087f, -7.205f)),  // Grafted Scion
            [10012810] = new CloneInfo(10012811, new Vector4(-42.210f, 21.377f, -42.055f, -98.064f), new Vector4(-42.907f, 21.377f, -37.131f, -98.064f)),  // Grafted Scion (position after first time)
            #endregion

            #region m11_00_00_00 (Leyndell, Royal Capital)
            // TODO: Can't move minibosses properly because I can't load this map.
            [11000389] = new CloneInfo(11000330),  // Erdtree Avatar
            [11000399] = new CloneInfo(11000331),  // Lion Guardian
            [11000495] = new CloneInfo(11000332),  // Crucible Knight
            [11000496] = new CloneInfo(11000333),  // Crucible Knight
            [11000497] = new CloneInfo(11000334),  // Ulcerated Tree Spirit
            [11000498] = new CloneInfo(11000335),  // Guardian Golem
            [11000484] = new CloneInfo(11000336),  // Black Knife Assassin
            [11000393] = new CloneInfo(11000337),  // Black Blade Kindred
            [11000800] = new CloneInfo(11000801, new Vector4(44.052f, 64.963f, -419.682f, 142.331f), new Vector4(38.468f, 64.963f, -423.992f, 142.331f)),  // Morgott, the Omen King (estimated from m11_05)
            [11000850] = new CloneInfo(11000851, new Vector4(-134.334f, 31.128f, -386.582f, 0f), new Vector4(-129.671f, 31.128f, -386.582f, 0f)),  // Godfrey Phantom (estimated from m11_05)
            #endregion

            #region m11_05_00_00 (Leyndell, Ashen Capital)
            [11050801] = new CloneInfo(11050803, new Vector4(39.053f, 64.963f, -423.966f, -76.133f), new Vector4(43.975f, 64.963f, -419.814f, -4.977f)),  // Godfrey (before Hoarah Loux)
            [11050800] = new CloneInfo(11050802),  // Hoarah Loux
            [11052815] = new CloneInfo(11052813, new Vector4(28.830f, 64.978f, -411.535f, 142.805f)),  // new Godfrey position
            [11052816] = new CloneInfo(11052814, new Vector4(34.600f, 64.978f, -407.156f, 142.805f)),  // new Godfrey clone position
            [11050850] = new CloneInfo(11050858, new Vector4(-131.471f, 31.030f, -384.865f, 89.980f), new Vector4(-131.469f, 31.030f, -388.253f, 89.980f)),  // Sir Gideon Ofnir (data variants are using lower IDs)
            #endregion

            #region m11_10_00_00 (Roundtable Hold)
            [11100785] = new CloneInfo(11100786, new Vector4(-260.442f, -32.610f, -279.591f, 60.079f), new Vector4(-267.170f, -32.610f, -268.438f, 60.079f)),  // Mad Tongue Alberich (invader)
            [11102385] = new CloneInfo(11102387, new Vector4(-260.442f, -32.610f, -279.591f, 60.079f), new Vector4(-267.170f, -32.610f, -268.438f, 60.079f)),  // Alberich invasion point
            #endregion

            #region m12_01_00_00 (Ainsel River)
            [12010400] = new CloneInfo(12010450, new Vector4(18.331f, -182.710f, -52.475f, -57.083f), new Vector4(12.220f, -182.710f, -61.915f, -57.083f)),  // Malformed Star 1
            [12010401] = new CloneInfo(12010451, new Vector4(287.052f, -80.652f, 106.993f, -143.411f)),  // Malformed Star 2
            [12010420] = new CloneInfo(12010470, new Vector4(-430.882f, -373.640f, -539.544f, -94.105f)),  // Ulcerated Tree Spirit before Astel
            [12010421] = new CloneInfo(12010471, new Vector4(-366.853f, -292.897f, -303.518f, -19.373f)),  // Onyx Lord
            [12010800] = new CloneInfo(12010803),  // Dragonkin Soldier of Nokstella (Health Pool)
            [12010801] = new CloneInfo(12010804, new Vector4(-122.336f, -224.499f, 136.190f, -2.957f)),  // Dragonkin Soldier of Nokstella (Phase One)
            [12010802] = new CloneInfo(12010805, new Vector4(-122.336f, -224.499f, 136.190f, -2.957f)),  // Dragonkin Soldier of Nokstella (Phase Two)
            [12010850] = new CloneInfo(12010851, new Vector4(-206.860f, -317.072f, -305.404f, -139.372f)),  // Dragonkin Soldier (Lake of Rot)
            #endregion

            #region m12_02_00_00 (Siofra River)
            [12020800] = new CloneInfo(12020802, new Vector4(1250.571f, -619.693f, 1952.741f, -6.903f)),  // Gargoyle (Greatsword)
            [12020801] = new CloneInfo(12020803, new Vector4(1268.214f, -588.073f, 1961.700f, 6.547f)),  // Gargoyle (Twinblade)
            [12020830] = new CloneInfo(12020831, new Vector4(1214.904f, -748.081f, 1727.575f, -4.073f)),  // Dragonkin Soldier
            [12020850] = new CloneInfo(12020851),  // Mimic Tear (c0000) - moved to matching Silver Tear when appropriate
            [12020860] = new CloneInfo(12020861, new Vector4(999.926f, -617.556f, 1140.269f, 127.904f), new Vector4(1002.875f, -617.556f, 1145.339f, 112.068f)),  // Mimic Tear (Silver Tear)
            [12020221] = new CloneInfo(12020222),  // Red Wolf
            [12020430] = new CloneInfo(12020435),  // Crucible Knight
            [12020431] = new CloneInfo(12020436),  // Crucible Knight
            [12020434] = new CloneInfo(12020437),  // Crucible Knight
            #endregion

            #region m12_03_00_00 (Deeproot Depths)
            [12030390] = new CloneInfo(12030392, new Vector4(-884.021f, 96.674f, -318.571f, -67.325f), new Vector4(-884.890f, 96.986f, -323.016f, -84.863f)),  // Crucible Knight Siluria
            [12030391] = new CloneInfo(12030393, new Vector4(-190.235f, 92.580f, -668.571f, 75.265f)),  // Erdtree Avatar
            [12030800] = new CloneInfo(12030820, new Vector4(-366.281f, 149.469f, -205.729f, 42.094f)),  // FirstFiasChampion
            [12030810] = new CloneInfo(12030830, new Vector4(-366.130f, 149.433f, -205.263f, 30.812f)),  // SorcererRogier
            [12030811] = new CloneInfo(12030831, new Vector4(-363.291f, 149.447f, -202.929f, 36.757f)),  // LioneltheLionhearted
            [12030812] = new CloneInfo(12030832, new Vector4(-361.566f, 149.496f, -209.763f, 63.770f)),  // LionelSidekick2
            [12030813] = new CloneInfo(12030833, new Vector4(-379.685f, 149.359f, -198.492f, 19.121f)),  // LionelSidekick1
            [12030814] = new CloneInfo(12030834),  // UnknownFiasChampion (hidden; moved into place, if used at all)
            [12030850] = new CloneInfo(12030851, new Vector4(-386.807f, 150.160f, -276.864f, 52.404f)),  // LichdragonFortissax
            #endregion

            #region m12_04_00_00 (Astel)
            [12040800] = new CloneInfo(12040801, new Vector4(-70.951f, -106.481f, -142.481f, 30f)),  // Astel
            #endregion

            #region m12_05_00_00 (Mohgwyn Dynasty Palace)
            [12050800] = new CloneInfo(12050801, new Vector4(1529.703f, -501.027f, 1248.235f, -64.391f), new Vector4(1527.465f, -501.027f, 1243.568f, -64.391f)),  // Mohg, Lord of Blood
            #endregion

            // NOTE: No special entiteis to handle in m12_07_00_00 (Siofra River Start).

            #region m12_08_00_00 (Ancestor Spirit Arena)
            [12080800] = new CloneInfo(12080801, new Vector4(1561f, -1736.050f, 1068.033f, -12.443f), new Vector4(1549.666f, -1736.050f, 1037.133f, -12.443f)),  // Ancestor Spirit
            #endregion

            #region m12_09_00_00 (Regal Ancestor Spirit Arena)
            [12090800] = new CloneInfo(12090801, new Vector4(1208.429f, -1538.411f, 1919.207f, 47.921f)),  // Regal Ancestor Spirit
            [12093200] = new CloneInfo(12093300),  // DeerSpawner0 
            [12093201] = new CloneInfo(12093301),  // DeerSpawner1 
            [12093202] = new CloneInfo(12093302),  // DeerSpawner2 
            [12093203] = new CloneInfo(12093303),  // DeerSpawner3 
            [12093204] = new CloneInfo(12093304),  // DeerSpawner4 
            [12093205] = new CloneInfo(12093305),  // DeerSpawner5 
            [12093206] = new CloneInfo(12093306),  // DeerSpawner6 
            [12093220] = new CloneInfo(12093320),  // BoarSpawner0 
            [12093221] = new CloneInfo(12093321),  // BoarSpawner1 
            [12093222] = new CloneInfo(12093322),  // BoarSpawner2 
            [12093223] = new CloneInfo(12093323),  // BoarSpawner3 
            [12093224] = new CloneInfo(12093324),  // BoarSpawner4 
            [12093225] = new CloneInfo(12093325),  // BoarSpawner5 
            [12093226] = new CloneInfo(12093326),  // BoarSpawner6 
            [12093240] = new CloneInfo(12093340),  // WildMouflonSpawner0 
            [12093241] = new CloneInfo(12093341),  // WildMouflonSpawner1 
            [12093242] = new CloneInfo(12093342),  // WildMouflonSpawner2 
            [12093243] = new CloneInfo(12093343),  // WildMouflonSpawner3 
            [12093244] = new CloneInfo(12093344),  // WildMouflonSpawner4 
            [12093245] = new CloneInfo(12093345),  // WildMouflonSpawner5 
            [12093246] = new CloneInfo(12093346),  // WildMouflonSpawner6 
            [12093260] = new CloneInfo(12093360),  // SpringhareSpawner0 
            [12093261] = new CloneInfo(12093361),  // SpringhareSpawner1 
            [12093262] = new CloneInfo(12093362),  // SpringhareSpawner2 
            [12093263] = new CloneInfo(12093363),  // SpringhareSpawner3 
            [12093264] = new CloneInfo(12093364),  // SpringhareSpawner4 
            [12093265] = new CloneInfo(12093365),  // SpringhareSpawner5 
            [12093266] = new CloneInfo(12093366),  // SpringhareSpawner6
            [12090200] = new CloneInfo(12090300),  // Deer0
            [12090201] = new CloneInfo(12090301),  // Deer1
            [12090202] = new CloneInfo(12090302),  // Deer2
            [12090203] = new CloneInfo(12090303),  // Deer3
            [12090204] = new CloneInfo(12090304),  // Deer4
            [12090205] = new CloneInfo(12090305),  // Deer5
            [12090206] = new CloneInfo(12090306),  // Deer6
            [12090220] = new CloneInfo(12090320),  // Boar0
            [12090221] = new CloneInfo(12090321),  // Boar1
            [12090222] = new CloneInfo(12090322),  // Boar2
            [12090223] = new CloneInfo(12090323),  // Boar3
            [12090224] = new CloneInfo(12090324),  // Boar4
            [12090225] = new CloneInfo(12090325),  // Boar5
            [12090226] = new CloneInfo(12090326),  // Boar6
            [12090240] = new CloneInfo(12090340),  // WildMouflon0
            [12090241] = new CloneInfo(12090341),  // WildMouflon1
            [12090242] = new CloneInfo(12090342),  // WildMouflon2
            [12090243] = new CloneInfo(12090343),  // WildMouflon3
            [12090244] = new CloneInfo(12090344),  // WildMouflon4
            [12090245] = new CloneInfo(12090345),  // WildMouflon5
            [12090246] = new CloneInfo(12090346),  // WildMouflon6
            [12090260] = new CloneInfo(12090360),  // Springhare0
            [12090261] = new CloneInfo(12090361),  // Springhare1
            [12090262] = new CloneInfo(12090362),  // Springhare2
            [12090263] = new CloneInfo(12090363),  // Springhare3
            [12090264] = new CloneInfo(12090364),  // Springhare4
            [12090265] = new CloneInfo(12090365),  // Springhare5
            [12090266] = new CloneInfo(12090366),  // Springhare6
            #endregion

            #region m13_00_00_00 (Crumbling Farum Azula)
            [13000496] = new CloneInfo(13000497, new Vector4(120.253f, -32.690f, 397.691f, 111.161f), new Vector4(115.771f, -32.791f, 404.200f, 111.161f)),  // Draconic Tree Sentinel
            [13000800] = new CloneInfo(13000802),  // Maliketh Phase Two
            [13000801] = new CloneInfo(13000803, new Vector4(198.570f, -32.511f, 378.754f, 99.665f), new Vector4(195.375f, -32.511f, 369.344f, 116.612f)),  // Maliketh Phase One
            [13000830] = new CloneInfo(13000831, new Vector4(17.664f, 1009.676f, 316.889f, 75.706f), new Vector4(11.360f, 1009.676f, 341.630f, 75.706f)),  // Dragonlord Placidusax
            [13000850] = new CloneInfo(13000860),  // Godskin Duo health pool
            [13000851] = new CloneInfo(13000861, new Vector4(-17.829f, -39.035f, 395.546f, -105.138f)),  // Godskin Duo Apostle
            [13000852] = new CloneInfo(13000862, new Vector4(-21.471f, -38.500f, 409.073f, -104.655f)),  // Godskin Duo Noble
            [13003851] = new CloneInfo(13003853),  // Godskin Apostle spawner
            [13003852] = new CloneInfo(13003854),  // Godskin Noble spawner
            [13000495] = new CloneInfo(13000330, new Vector4(130.449f, -125.512f, 453.245f, 178.723f), new Vector4(149.933f, -126.542f, 458.432f, 165.092f)),  // Ancient Dragon (lower platform)
            [13000490] = new CloneInfo(13000331, new Vector4(), new Vector4()),  // Ancient Dragon (upper curve)
            [13000494] = new CloneInfo(13000332, new Vector4(-162.066f, -51.302f, 284.397f, 31.851f)),  // Ancient Dragon (side platform)
            [13000295] = new CloneInfo(13000335, new Vector4(50.966f, -80.500f, 618.847f, 174.425f)),  // Crucible Knight
            [13000296] = new CloneInfo(13000336, new Vector4(96.947f, -130.930f, 541.670f, 99.615f)),  // Crucible Knight
            [13000369] = new CloneInfo(13000339, new Vector4(-60.815f, -68.316f, 98.943f, 17.127f)),  // Giant Wormface
            #endregion

            #region m14_00_00_00 (Academy of Raya Lucaria)
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
            // Red Wolf
            [14000850] = new CloneInfo(14000851, new Vector4(149.847f, 110.182f, -224.778f, -93.632f), new Vector4(149.101f, 110.182f, -220.903f, -93.632f)), // Red Wolf of Radagon
            [14002856] = new CloneInfo(14002857, new Vector4(152.379f, 110.197f, -220.576f, -87.560f), new Vector4(152.552f, 110.197f, -224.625f, -87.560f)),  // Red Wolf first position
            // Other
            [14000499] = new CloneInfo(14000498, new Vector4(119.404f, 129.084f, -53.635f, -67.959f), new Vector4(117.987f, 129.084f, -57.134f, -67.959f)),  // Moongrum (Carian Knight)
            #endregion

            #region m15_00_00_00 (Haligtree)
            // MALENIA
            [15000800] = new CloneInfo(15000810, new Vector4(-19.105f, 52.343f, 469.117f, -77.392f)),  // Malenia
            [15000801] = new CloneInfo(15000811, new Vector4(-19.105f, 52.343f, 469.117f, -77.392f)),  // Unused "swap" Malenia spirit
            [15000802] = new CloneInfo(15000812, new Vector4(-19.105f, 52.343f, 469.117f, -77.392f)),  // Temporary Malenia spirits
            [15000803] = new CloneInfo(15000813, new Vector4(-19.105f, 52.343f, 469.117f, -77.392f)),
            [15000804] = new CloneInfo(15000814, new Vector4(-19.105f, 52.343f, 469.117f, -77.392f)),
            [15000805] = new CloneInfo(15000815, new Vector4(-19.105f, 52.343f, 469.117f, -77.392f)),
            [15002812] = new CloneInfo(15002813, new Vector4(-23.278f, 52.134f, 470.961f, -132.706f)),  // Malenia start position first time
            [15002814] = new CloneInfo(15002817, new Vector4(-3.943f, 50.807f, 493.917f, -132.626f)),  // Malenia start position after first time
            // LORETTA
            [15000850] = new CloneInfo(15000851, new Vector4(170.475f, 431.748f, 307.111f, -10.115f)),  // Loretta
            [15002860] = new CloneInfo(15002861, new Vector4(184.504f, 431.894f, 278.272f, 22.549f)),  // Loretta start position after first time
            // OTHER
            [15000392] = new CloneInfo(15000395, new Vector4(-1.401f, 211.421f, 608.525f, -70.207f), new Vector4(-2.577f, 211.421f, 601.708f, -94.581f)),  // Putrid Avatar (door)
            [15000393] = new CloneInfo(15000396, new Vector4(134.123f, 212.958f, 472.271f, 9.726f)),  // Putrid Avatar (battlement)
            [15000398] = new CloneInfo(15000399, new Vector4(18.614f, 179.795f, 457.245f, -91.005f)),  // Ulcerated Tree Spirit

            #endregion

            #region m16_00_00_00 (Volcano Manor)
            [16000800] = new CloneInfo(16000802, new Vector4(85.891f, -439.508f, -120.969f, -162.615f), new Vector4(106.285f, -439.508f, -119.676f, 167.795f)),  // Rykard (Phase Two)
            [16000801] = new CloneInfo(16000803, new Vector4(85.891f, -439.508f, -120.969f, -162.615f), new Vector4(106.285f, -439.508f, -119.676f, 167.795f)),  // Rykard (Phase One)
            [16002831] = new CloneInfo(16002832, new Vector4(85.891f, -439.508f, -120.969f, -162.615f), new Vector4(106.285f, -439.508f, -119.676f, 167.795f)),  // Rykard Phase Two move point
            [16000850] = new CloneInfo(16000851, new Vector4(59.896f, 7.023f, -205.541f, 107.623f), new Vector4(56.589f, 7.023f, -212.446f, 121.034f)),  // Godskin Noble
            [16000860] = new CloneInfo(16000862, new Vector4(221.695f, -132.944f, -262.066f, -125.258f)),  // Iron Virgin 1
            [16000861] = new CloneInfo(16000863, new Vector4(250.684f, -133.499f, -251.213f, 170.014f)),  // Iron Virgin 2
            [16000510] = new CloneInfo(16000511, new Vector4(33.000f, -54.670f, -185.826f, 54.469f)),  // Magma Wyrm
            #endregion

            #region m18_00_00_00 (Stranded Graveyard / Fringefolk Hero's Grave)
            [18000350] = new CloneInfo(18000352),  // Grafted Scion
            [18000351] = new CloneInfo(18000353),  // Grafted Scion
            [18000850] = new CloneInfo(18000851, new Vector4(-37.142f, 9.104f, 45.619f, -160.753f)),  // Soldier of Godrick
            #endregion

            #region m19_00_00_00 (Stone Platform)
            // Elden Beast (801-804 used by Elden Beast stuff)
            [19000800] = new CloneInfo(19000805, new Vector4(206.755f, -719.985f, -689.934f, 155.434f), new Vector4(220.386f, -719.985f, -683.703f, 155.434f)),
            // Radagon (811 used by something else)
            [19000810] = new CloneInfo(19000812, new Vector4(198.376f, 102.257f, -623.591f, 110.279f)),
            #endregion

            #region m35_00_00_00
            [35000800] = new CloneInfo(35000801, new Vector4(75.117f, -298.550f, -83.080f, -117.328f), new Vector4(72.899f, -298.550f, -78.977f, -119.587f)),  // Mohg
            #endregion

            #region Liurnia
            [1033410340] = new CloneInfo(1033410341),  // RedWolf 
            [1033410350] = new CloneInfo(1033410352),  // GlintstoneDragon0 
            [1033410351] = new CloneInfo(1033410353),  // GlintstoneDragon1 

            [1033420800] = new CloneInfo(1033420801),  // Alecto (Evergaol)

            [1033430800] = new CloneInfo(1033430801),  // Erdtree Avatar

            [1033450800] = new CloneInfo(1033450801),  // Troll (Evergaol)

            [1034420800] = new CloneInfo(1034420801),  // Glintstone Dragon Adula (plateau)
            [1034420340] = new CloneInfo(1034420341),  // Glintstone Dragon (minor)

            [1034450800] = new CloneInfo(1034450801, new Vector4(-37.301f, 237.685f, 34.946f, 60.295f)),  // Glintstone Dragon Smarag

            [1034500800] = new CloneInfo(1034500801, new Vector4(10.063f, 455.024f, 36.713f, -107.379f)),  // Glintstone Dragon Adula (Ranni's Rise)
            #endregion

            #region Caelid
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
            #endregion

            #region Mountaintops
            [1052520801] = new CloneInfo(1052520803, new Vector4(-337.454f, 1859.962f, -374.085f, -37.187f)),  // Fire Giant (Phase One/Two)
            [1052520800] = new CloneInfo(1052520802),  // Fire Giant (Phase Three)
            #endregion

            #region Catacombs
            [30000800] = new CloneInfo(30000801),
            
            [30010800] = new CloneInfo(30010801),
            
            [30020800] = new CloneInfo(30020801),

            [30030800] = new CloneInfo(30030820),  // Snail
            [30030801] = new CloneInfo(30030821),  // Snail summons
            [30030805] = new CloneInfo(30030825),
            [30030806] = new CloneInfo(30030826),
            [30030802] = new CloneInfo(30030822),
            [30030803] = new CloneInfo(30030823),
            [30030804] = new CloneInfo(30030824),
            [30030807] = new CloneInfo(30030827),
            [30030808] = new CloneInfo(30030828),
            [30030809] = new CloneInfo(30030829),
            [30030810] = new CloneInfo(30030830),
            [30033801] = new CloneInfo(30033811),  // Snail summon spawners
            [30033802] = new CloneInfo(30033812),
            [30033803] = new CloneInfo(30033813),
            [30033804] = new CloneInfo(30033814),
            [30033805] = new CloneInfo(30033815),
            [30033806] = new CloneInfo(30033816),

            [30040800] = new CloneInfo(30040801),

            [30050800] = new CloneInfo(30050801),
            [30050850] = new CloneInfo(30050851),

            [30070800] = new CloneInfo(30070801),

            [30080800] = new CloneInfo(30080801),

            [30090800] = new CloneInfo(30090801),

            // Crucible Knight Ordovis and friend
            [30100800] = new CloneInfo(30100802, new Vector4(-112.033f, 761.696f, 352.485f, -18.650f)),
            [30100801] = new CloneInfo(30100803, new Vector4(-96.853f, 761.726f, 354.661f, 21.637f)),

            [30110800] = new CloneInfo(30110801),

            [30120800] = new CloneInfo(30120802),
            [30120801] = new CloneInfo(30120803),

            [30130800] = new CloneInfo(30130801),

            // Erdtree Burial Watchdogs
            [30140800] = new CloneInfo(30140802),
            [30140801] = new CloneInfo(30140803),

            [30150800] = new CloneInfo(30150801),

            [30160800] = new CloneInfo(30160801),

            [30170800] = new CloneInfo(30170801),

            [30180800] = new CloneInfo(30180801),

            [30190800] = new CloneInfo(30190801),

            // Mimic Tear
            [30200800] = new CloneInfo(30200802),
            [30200801] = new CloneInfo(30200803),
            #endregion
        };

        public readonly static Dictionary<int, int> CloneEntityGroupIDs = new Dictionary<int, int>()
        {
            [13005851] = 13005852,  // Godskin Duo

            // Regal Ancestor Spirit animal groups
            [12095200] = 12095210,  // All Animals 
            [12095201] = 12095211,  // Deer 
            [12095202] = 12095212,  // Boars 
            [12095203] = 12095213,  // WildMouflons 
            [12095204] = 12095214,  // Springhares 

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

        // Maps (new) Spawner Entity IDs to lists of part entity IDs and coordinates of new region X/Y/Z/rotY,
        // which will be created automatically and assigned to the Spawner by name.
        public readonly static Dictionary<int, Vector4[]> NewSpawnerInfo = new Dictionary<int, Vector4[]>()
        {
            [13003853] = new Vector4[] { new Vector4(-19.919f, -39.078f, 402.534f, -105.597f) },  // Godskin Duo Apostle spawner
            [13003854] = new Vector4[] { new Vector4(-19.919f, -39.078f, 402.534f, -105.597f) },  // Godskin Duo Noble spawner
        };
        
        public readonly static Dictionary<int, string> NewNPCNames = new Dictionary<int, string>()
        {
            // m10_00_00_00
            [902130010] = "Cousin Merbit",
            [904750010] = "Godefroy the Gratuitous",

            // m10_01_00_00
            [904690010] = "Grafted Scion",

            // m11_00_00_00
            [902130012] = "Somehow, Cousin Merbit Returned",
            [904720012] = "Mysterious Foreshadowed Stranger",  // phantom

            // m11_05_00_00
            [904720010] = "Mysterious Foreshadowed Stranger",
            [904720011] = "Eric, Father of Merbit and Mulg, Husband of Rhonda, Uncle of Mazohr, Former Roommate of Ryktar",
            [132401] = "Sir Giddy-Up Ofnir, the Idiot",

            // m12_01_00_00
            [904650010] = "Dragonkin Soldier of Nokron",
            [904650611] = "Dragonkin Soldier",  // Lake of Rot

            // m12_02_00_00
            [904770000] = "Valiant Gargoyles (Greatsword)",
            [904770001] = "Valiant Gargoyles (Twinblade)",
            [904650610] = "Dragonkin Soldier",

            // m12_03_00_00
            [904510010] = "Lichdragon Fortissavan",
            [902500610] = "Crucible Knight Joanna",

            // m12_04_00_00
            [904620001] = "Astels... I Hate These Guys",  // shared health bar

            // m12_05_00_00
            [904800010] = "Mulg, Lord of Gazpacho Soup",

            // m13_00_00_00
            [903575000] = "Oneskin, Twoskin",
            [903575010] = "Threeskin, Fourskin",
            [902110010] = "Beast Clergyman",
            [902110011] = "Big the Cat",
            [904520010] = "Dragonlord Dan",

            // m14_00_00_00
            [902030010] = "Rhonda, Queen of the White Dust",
            [902030011] = "Rhonda, Queen of the White Dust",
            [903181010] = "Ginger Sif",

            // m15_00_00_00
            [902120010] = "Malonia, Middle Finger of Miyazaki",

            // m16_00_00_00
            [904710010] = "A Second God-Devouring Serpent",
            [904710011] = "Ryktar, Definitely Also Devoured On Purpose",
            [903570010] = "Fred Durst",

            // m18_00_00_00
            [904311010] = "A Second Soldier of Godrick",

            // m19_00_00_00
            [902190010] = "Ragadon of the Awkward Love Triangle",

            // m35_00_00_00
            [904800012] = "Mulg, the Other Omen",

            // m60_52_38_00
            [904730010] = "Moonmurderer Mazohr",

            // Overworld
            [904502610] = "Glintstone Dragon Samantha",

            // Generic
            [902500300] = "Crucible Knights Ordovis and Osmodis",
            [902500301] = "Lesser Crucible Knights",
            [903700300] = "Depraved Perfurmers",
            [904260304] = "Erdtree Burial Watchdogs",
            [904260305] = "Erdtree Burial Watchdogs",
        };
    }
}
