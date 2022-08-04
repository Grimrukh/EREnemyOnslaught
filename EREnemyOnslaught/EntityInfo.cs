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

            // NOTE: No special entities to handle in m12_07_00_00 (Siofra River Start).

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
            [35000850] = new CloneInfo(35000851, new Vector4(-204.708f, -153.846f, -306.088f, -135.587f), new Vector4(-202.921f, -153.846f, -307.839f, -135.587f)),  // Esgar
            #endregion

            #region Limgrave / Weeping Peninsula
            [1041370340] = new CloneInfo(1041370341, new Vector4(46.312f, 158.010f, 75.708f, 87.283f)),  // Guardian Golem
            [1041372340] = new CloneInfo(1041372341, new Vector4(48.062f, 155.011f, 74.530f, 0f)),  // and trigger region

            [1042360800] = new CloneInfo(1042360801, new Vector4(-15.967f, 90.233f, 52.275f, -35.597f)),  // Tree Sentinel

            [1042380800] = new CloneInfo(1042380801, new Vector4(123.558f, 183.694f, 47.226f, 134.359f)),  // Deathrite Bird
            [1042380850] = new CloneInfo(1042380851, new Vector4(10.343f, 188.006f, 88.935f, 130.245f), new Vector4(12.089f, 188.006f, 90.998f, 130.245f)),  // Bell-Bearing Hunter

            [1043300800] = new CloneInfo(1043300801),  // Leonine Misbegotten

            [1043330800] = new CloneInfo(1043330801),  // Erdtree Avatar

            [1043340340] = new CloneInfo(1043340341),  // Demi-Human Queen 

            [1043360800] = new CloneInfo(1043360801, new Vector4(-89.866f, 65.068f, 65.892f, 21.199f)),  // Agheel

            [1043370340] = new CloneInfo(1043370342, new Vector4(60.691f, 90.880f, -95.624f, -89.772f)),  // Night's Cavalry
            [1043370341] = new CloneInfo(1043370343, new Vector4(62.261f, 90.990f, -94.327f, -87.915f)),  // and horse

            [1043400200] = new CloneInfo(1043400201),  // Guardian Golem

            [1047380299] = new CloneInfo(1047380297),  // Lion Guardian

            [1042330800] = new CloneInfo(1042330801),  // Ancient Hero of Zamor (Evergaol)

            [1042370800] = new CloneInfo(1042370801),  // Crucible Knight (Evergaol)

            [1044350800] = new CloneInfo(1044350801),  // Bloodhound Knight (Evergaol)
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

            [1035420800] = new CloneInfo(1035420801, new Vector4(-38.849f, 269.155f, -12.055f, 44.135f)),  // Omenkiller

            [1035500800] = new CloneInfo(1035500801, new Vector4(-32.985f, 430.946f, 97.375f, -70.682f)),  // Loretta

            [1036450340] = new CloneInfo(1036450341, new Vector4(-79.161f, 237.557f, 26.946f, -64.883f)),  // Deathrite Bird

            [1036480340] = new CloneInfo(1036480342, new Vector4(37.775f, 321.602f, 27.538f, 34.351f)),  // Night's Cavalry
            [1036480341] = new CloneInfo(1036480343, new Vector4(34.496f, 321.577f, 26.488f, 35.401f)),  // and horse

            [1036500340] = new CloneInfo(1036500341),  // Red Wolf
            [1036500800] = new CloneInfo(1036500801),  // Onyx Lord (Evergaol)

            [1037420340] = new CloneInfo(1037420341, new Vector4(-65.198f, 237.647f, 84.754f, -96.931f)),  // Deathrite Bird

            [1037460800] = new CloneInfo(1037460801, new Vector4(-48.897f, 398.292f, 11.946f, -101.466f), new Vector4(-48.158f, 398.292f, 8.302f, -101.466f)),  // Bell-Bearing Hunter

            [1038460340] = new CloneInfo(1038460341, new Vector4(94.425f, 247.617f, 44.989f, -27.670f)),  // Guardian Golem

            [1038480800] = new CloneInfo(1038480801),  // Erdtree Avatar

            [1039430340] = new CloneInfo(1039430342, new Vector4(-119.097f, 252.115f, -14.508f, -52.904f)),  // Night's Cavalry
            [1039430341] = new CloneInfo(1039430343, new Vector4(-117.365f, 251.947f, -14.129f, -52.904f)),  // and horse

            [1039440800] = new CloneInfo(1039440801, new Vector4(-75.760f, 294.788f, -54.586f, -23.798f)),  // Tibia Mariner

            [1039480340] = new CloneInfo(1039480341),  // Troll

            [1039510800] = new CloneInfo(1039510802, new Vector4(-8.315f, 756.418f, -102.654f, -133.421f)),  // Night's Cavalry
            [1039510801] = new CloneInfo(1039510803, new Vector4(-7.967f, 754.993f, -102.381f, -133.217f)),  // and horse

            [1038410800] = new CloneInfo(1038410801),  // Adan, Thief of Fire (Everagaol)
            #endregion

            #region Altus Plateau
            [1035530800] = new CloneInfo(1035530801, new Vector4(12.650f, 824.102f, -77.946f, 166.660f)),  // Magma Wyrm
            
            [1036540800] = new CloneInfo(1036540801, new Vector4(102.266f, 1048.271f, -40.923f, 178.064f)),  // Fallingstar Beast

            [1037510800] = new CloneInfo(1037510801, new Vector4(91.524f, 711.600f, 60.454f, 31.040f)),  // Ancient Dragon Lansseax (west)

            [1037530800] = new CloneInfo(1037530801, new Vector4(17.712f, 901.338f, -93.704f, 40.495f)),  // Demi-Human Queen

            [1037540810] = new CloneInfo(1037540811, new Vector4(-30.081f, 857.116f, -60.175f, 128.392f)),  // Ulcerated Tree Spirit
            [1037540341] = new CloneInfo(1037540342, new Vector4(74.079f, 931.970f, 72.843f, -14.060f)),  // Grafted Scion

            [1038520340] = new CloneInfo(1038520341, new Vector4(-51.929f, 792.940f, -21.334f, -73.012f)),  // Tibia Mariner
            [1038520350] = new CloneInfo(1038520351, new Vector4(-39.888f, 792.783f, -24.137f, -72.182f)),  // Giant Skeleton Torso

            [1038540400] = new CloneInfo(1038540401, new Vector4(30.322f, 730.431f, 50.403f, -70.936f)),  // Maleigh Marais

            [1039520400] = new CloneInfo(1039520401, new Vector4(28.190f, 771.836f, 54.728f, -70.325f), new Vector4(29.019f, 771.836f, 57.046f, -70.325f)),  // Sanguine Noble

            [1040520800] = new CloneInfo(1040520801, new Vector4(51.817f, 884.000f, 9.096f, -80.198f), new Vector4(51.335f, 884f, 5.594f, -89.354f)),  // Black Knife Assassin

            [1041500800] = new CloneInfo(1041500801, new Vector4(40.033f, 833.699f, 115.255f, 55.553f)),  // Fallingstar Beast

            [1041510410] = new CloneInfo(1041510411),  // Giant Miranda Flower

            [1041510800] = new CloneInfo(1041510802, new Vector4(91.641f, 851.270f, -38.015f, 85.293f)),  // Tree Sentinel Duo (Left)
            [1041510801] = new CloneInfo(1041510803, new Vector4(92.240f, 851.311f, -46.437f, 93.573f)),  // Tree Sentinel Duo (Right)

            [1041520800] = new CloneInfo(1041520801, new Vector4(32.142f, 920.477f, -78.896f, 33.399f)),  // Ancient Dragon Lansseax (east)

            [1041530800] = new CloneInfo(1041530801, new Vector4(-74.592f, 784.957f, 36.986f, -33.459f)),  // Wormface

            [1042500300] = new CloneInfo(1042500301, new Vector4(-41.693f, 684.995f, 67.740f, -115.543f)),  // Ulcerated Tree Spirit

            [1042510300] = new CloneInfo(1042510301, new Vector4(41.110f, 880.269f, 82.568f, 50.509f), new Vector4(32.828f, 880.269f, 88.856f, 12.221f)),  // Gargoyle

            [1042550800] = new CloneInfo(1042550801, new Vector4(-30.954f, 968.164f, -37.932f, -11.389f)),  // Godskin Apostle

            [1043530800] = new CloneInfo(1043530801),  // Bell-Bearing Hunter

            [1044530800] = new CloneInfo(1044530801),  // Deathrite Bird

            [1045520800] = new CloneInfo(1045520801, new Vector4(25.714f, 1023.759f, 45.294f, -145.248f), new Vector4(30.288f, 1024.047f, 42.166f, -145.248f)),  // Draconic Tree Sentinel
            [1045520200] = new CloneInfo(1045520210),  // Guardian Golem
            [1045520202] = new CloneInfo(1045520212),  // Guardian Golem

            [1039500800] = new CloneInfo(1039500801),  // Godefroy (Evergaol)
            #endregion

            #region Caelid
            [1051360800] = new CloneInfo(1051360802, new Vector4(90.810f, 91.750f, 34.136f, 12.908f)),  // Redmane Castle duo boss (Leonine Misbegotten) 
            [1051360801] = new CloneInfo(1051360803, new Vector4(97.482f, 105.500f, 38.728f, 93.109f)),  // Redmane Castle duo boss (Crucible Knight)
            [1051360291] = new CloneInfo(1051360293),  // Lion Guardian
            [1051360292] = new CloneInfo(1051360294),  // Lion Guardian
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

            [1048410800] = new CloneInfo(1048410801, new Vector4(-89.996f, 225.781f, -69.942f, -2.860f)),  // Bell-Bearing Hunter

            [1047400800] = new CloneInfo(1047400801),  // Putrid Avatar

            [1048370800] = new CloneInfo(1048370801, new Vector4(-22.378f, 115.230f, -50.638f, 143.753f)),  // Decaying Ekzykes

            [1049370800] = new CloneInfo(1049370802),  // Night's Cavalry
            [1049370801] = new CloneInfo(1049370803),  // and horse
            [1049370299] = new CloneInfo(1049370298),  // Lion Guardian
            [1049370850] = new CloneInfo(1049370851),  // Deathrite Bird

            [1049380800] = new CloneInfo(1049380801, new Vector4(-25.055f, 65.975f, 46.699f, 81.940f)),  // Commander O'Neil

            [1049390800] = new CloneInfo(1049390810, new Vector4(92.200f, 83.522f, 85.510f, -29.649f)),  // Nox Duo
            [1049390801] = new CloneInfo(1049390811, new Vector4(102.351f, 83.649f, 87.403f, 16.687f)),

            [1051400800] = new CloneInfo(1051400801),  // Putrid Avatar

            [1051430800] = new CloneInfo(1051430801, new Vector4(-7.218f, 334.658f, -19.671f, -56.548f), new Vector4(-15.926f, 336.654f, -22.923f, -38.521f)),  // Gargoyle (Bestial Sanctum)

            [1049390850] = new CloneInfo(1049390851),  // Battle Mage (Evergaol)

            [1052410850] = new CloneInfo(1052410852, new Vector4(9.373f, 221.391f, 119.834f, -8.995f)),  // Night's Cavalry
            [1052410851] = new CloneInfo(1052410853, new Vector4(8.873f, 219.046f, 121.173f, -9.111f)),  // and horse
            #endregion

            #region Mountaintops
            [1049520800] = new CloneInfo(1049520801),  // Gargoyle (Forbidden Lands)

            [1051550300] = new CloneInfo(1051550301),  // Guardian Golem

            [1051570800] = new CloneInfo(1051570810, new Vector4(80.319f, 1632.0f, 211.005f, -18.200f), new Vector4(75.942f, 1632.0f, 209.566f, -18.2f)),  // Commander Niall
            [1051570801] = new CloneInfo(1051570811, new Vector4(77.177f, 1632.0f, 206.721f, -26.253f)),  // Knight 1
            [1051570802] = new CloneInfo(1051570812, new Vector4(84.972f, 1632.0f, 209.167f, -18.009f)),  // Knight 2

            [1052520801] = new CloneInfo(1052520803, new Vector4(-337.454f, 1859.962f, -374.085f, -37.187f)),  // Fire Giant (Phase One/Two)
            [1052520800] = new CloneInfo(1052520802),  // Fire Giant (Phase Three)

            [1054560800] = new CloneInfo(1054560801, new Vector4(37.749f, 1620.359f, -257.495f, -173.023f)),  // Borealis
            [1054562820] = new CloneInfo(1054562840, new Vector4(-61.578f, 1620.184f, -294.852f, 150f)),  // Borealis appearance points
            [1054562821] = new CloneInfo(1054562841, new Vector4(-36.884f, 1620.187f, -250.605f, 135f)),
            [1054562822] = new CloneInfo(1054562842, new Vector4(-0.380f, 1618.527f, -213.091f, 130f)),
            [1054562823] = new CloneInfo(1054562843, new Vector4(31.460f, 1620.184f, -180.204f, 145f)),
            [1054562824] = new CloneInfo(1054562844, new Vector4(19.465f, 1620.184f, -172.957f, 125f)),
            [1054562825] = new CloneInfo(1054562845, new Vector4(63.988f, 1620.184f, -117.742f, 125.684f)),

            [1048570800] = new CloneInfo(1048570801),  // Deathrite Bird
            [1048570250] = new CloneInfo(1048570240),  // Black Knife Assassin
            [1048570251] = new CloneInfo(1048570241),  // Black Knife Assassin
            [1048570252] = new CloneInfo(1048570242),  // Black Knife Assassin
            [1048570253] = new CloneInfo(1048570243),  // Black Knife Assassin
            [1048570254] = new CloneInfo(1048570244),  // Black Knife Assassin
            [1048570255] = new CloneInfo(1048570245),  // Black Knife Assassin
            [1048570256] = new CloneInfo(1048570246),  // Black Knife Assassin

            [1248550800] = new CloneInfo(1248550802),  // Night's Cavalry
            [1248550810] = new CloneInfo(1248550812),  // and horse
            [1248550801] = new CloneInfo(1248550803),  // Night's Cavalry
            [1248550811] = new CloneInfo(1248550813),  // and horse

            [1050560800] = new CloneInfo(1050560801, new Vector4(21.156f, 1255.064f, -6.692f, -133.980f)),  // Great Wyrm Theodorix
            [1050560300] = new CloneInfo(1050560301),  // Red Wolf

            [1051530180] = new CloneInfo(1051530181),  // Bloody Finger Okina

            [1051570310] = new CloneInfo(1051570312),  // Lion Guardian
            [1051570311] = new CloneInfo(1051570313),  // Lion Guardian
            [1051570421] = new CloneInfo(1051570422),  // Tibia Mariner

            [1052550390] = new CloneInfo(1052550391),  // Chief Guardian Arghanthy

            [1053560800] = new CloneInfo(1053560801),  // Vyke (Evergaol)
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

            [30060800] = new CloneInfo(30060801),

            [30070800] = new CloneInfo(30070801),

            [30080450] = new CloneInfo(30080451),  // Grave Warden Duelist
            [30080800] = new CloneInfo(30080801),  // Ancient Hero of Zamor

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

            #region Caves
            [31000800] = new CloneInfo(31000801, new Vector4(26.603f, 53.102f, 56.115f, -132.769f)),  // Patches (complicated events, will definitely be buggy)

            [31010800] = new CloneInfo(31010801),  // Runebear

            [31020800] = new CloneInfo(31020801),  // Giant Miranda Flower

            [31030800] = new CloneInfo(31030801),  // Beastman

            [31040800] = new CloneInfo(31040801),  // Cleanrot Knight

            [31060800] = new CloneInfo(31060810),  // Crystalian Duo
            [31060801] = new CloneInfo(31060811),

            [31070800] = new CloneInfo(31070810),  // Kindred of Rot Duo
            [31070801] = new CloneInfo(31070811),

            [31090800] = new CloneInfo(31090801),  // Demi-Human Queen Margot

            [31100800] = new CloneInfo(31100810),  // Beastman Duo
            [31100801] = new CloneInfo(31100811),

            [31110800] = new CloneInfo(31110810, new Vector4(-148.502f, 127.071f, 140.750f, -97.856f)),  // Putrid Crystalian Trio
            [31110801] = new CloneInfo(31110811, new Vector4(-145.477f, 126.956f, 127.938f, -142.303f)),
            [31110802] = new CloneInfo(31110812, new Vector4(-139.216f, 127.277f, 130.033f, -153.251f)),

            [31120800] = new CloneInfo(31120801),  // Leonine Misbegotten

            [31150800] = new CloneInfo(31150810),  // Demi-Human Beastman Duo
            [31150801] = new CloneInfo(31150811),

            [31170800] = new CloneInfo(31170801),  // Guardian Golem

            [31180800] = new CloneInfo(31180810, new Vector4(-96.070f, 791.448f, 183.653f, -95.496f)),  // Miranda the Blighted Bloom
            [31180801] = new CloneInfo(31180811, new Vector4(-92.763f, 790.507f, 184.897f, 58.068f)),  // Omenkiller
            [31180400] = new CloneInfo(31180401, new Vector4(0.337f, 796.292f, 182.008f, 32.869f)),  // Malformed Star

            [31190800] = new CloneInfo(31190801, new Vector4(127.782f, 623.473f, -23.569f, -67.646f)),  // Black Knife Assassin
            [31190850] = new CloneInfo(31190851, new Vector4(103.195f, 627.262f, -44.531f, -30.279f)),  // Necromancer Garris
            [31190380] = new CloneInfo(31190383),  // Garris snail
            [31190381] = new CloneInfo(31190384),  // Garris snail
            [31190382] = new CloneInfo(31190385),  // Garris snail
            [31193820] = new CloneInfo(31193822),  // Garris snail spawner 0
            [31193821] = new CloneInfo(31193823),  // Garris snail spawner 1

            [31200800] = new CloneInfo(31200810, new Vector4(179.505f, 86.969f, 150.240f, 42.049f)),  // Cleanrot Knight Duo
            [31200801] = new CloneInfo(31200811, new Vector4(160.878f, 85.821f, 147.109f, -67.262f)),

            [31210800] = new CloneInfo(31210801),  // Gravewarden Duelist

            // TODO: Spiritcaller Cave (snails and Godskins)
            #endregion

            #region Tunnels
            [32000800] = new CloneInfo(32000801),  // Scaly Misbegotten

            [32010800] = new CloneInfo(32010801),  // Mine Troll

            [32020800] = new CloneInfo(32020801),  // Crystalian

            [32040800] = new CloneInfo(32040801),  // Mine Troll

            [32050800] = new CloneInfo(32050810, new Vector4(62.569f, 777.627f, -43.987f, 93.638f)),  // Crystalian Duo
            [32050801] = new CloneInfo(32050811, new Vector4(57.861f, 777.708f, -44.676f, -121.453f)),

            [32070800] = new CloneInfo(32070801, new Vector4(-25.139f, 89.415f, 157.544f, -18.911f), new Vector4(-14.447f, 89.819f, 159.712f, 2.933f)),  // Magma Wyrm

            [32080800] = new CloneInfo(32080801, new Vector4(-63.849f, 123.909f, 235.002f, -118.530f)),  // Fallingstar Beast

            // Astel, Stars of Darkness
            [32110800] = new CloneInfo(32110820, new Vector4(63.898f, 1207.515f, 149.428f, 14.521f), new Vector4(41.165f, 1207.515f, 149.500f, -10.892f)),
            [32110801] = new CloneInfo(32110821),  // Astel (grab move copy)
            [32110802] = new CloneInfo(32110822),  // Astel (grab move copy)
            [32110803] = new CloneInfo(32110823),  // Astel (grab move copy)
            [32110804] = new CloneInfo(32110824),  // Astel (grab move copy)
            [32110805] = new CloneInfo(32110825),  // Astel (grab move copy)
            [32110806] = new CloneInfo(32110826),  // Astel (grab move copy)
            [32110807] = new CloneInfo(32110827),  // Astel (grab move copy)
            [32110808] = new CloneInfo(32110828),  // Astel (grab move copy)
            #endregion

            #region Divine Towers
            [34110280] = new CloneInfo(34110281),  // Godskin Noble (Liurnia)

            [34120800] = new CloneInfo(34120801, new Vector4(-46.343f, 711.356f, -195.716f, 176.217f)),  // Onyx Lord (West Altus)

            [34130800] = new CloneInfo(34130801, new Vector4(75.057f, 36.310f, -95.709f, 178.414f), new Vector4(79.058f, 36.310f, -95.672f, -179.405f)),  // Godskin Apostle (Caelid)

            [34140850] = new CloneInfo(34140852, new Vector4(587.596f, -373.485f, -330.139f, 45.647f)),  // Omen Twins (East Altus)
            [34140851] = new CloneInfo(34140853, new Vector4(595.989f, -373.485f, -336.553f, 66.351f)),
            #endregion

            #region m39_20_00_00 (Ruin-Strewn Precipice)
            [39200800] = new CloneInfo(39200801, new Vector4(-114.822f, 353.113f, -1302.301f, -28.413f)),  // Magma Wyrm Makar
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

            [1051575801] = 1051575802,  // Commander Niall's Knights
        };

        public readonly static HashSet<int> DoNotCloneEntityIDs = new HashSet<int>()
        {
            // Any entity ID ending in 7XX is ignored, unless it appears in `Clones`.

            // Gideon battle variants
            11050851,
            11050852,
            11050853,
            11050854,
            11050855,
            11050856,
            11050857,

            31000850,  // Copy of Patches boss

            // Greyoll the Giant Dragon
            1050400800,

            // Self-Copying Erdtree Avatar in Mountaintops
            1052560800,
            1052560801,
            1052560802,
            1052560803,
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
            [904720012] = "Mysterious Stranger",  // phantom

            // m11_05_00_00
            [904720010] = "Mysterious Stranger",
            [904720011] = "Eddy Loux, Father of Merbit and Mulg, Husband of Rhonda, Uncle of Mazohr, Former Roommate of Ryktar",
            [132401] = "Sir Goomba Ofnir, the Idiot",

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
            [902110011] = "Fluffy the Cat... of Death",
            [904520010] = "Dragonlord Daniel",

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
            [902190010] = "Ragadon of the Weird Love Triangle",

            // m35_00_00_00
            [904800012] = "Mulg the Hangry",
            [138601] = "Esther, Priestess of Earwax",

            // m60_52_38_00
            [904730010] = "Meteorman Mazohr",

            // Overworld
            [904502610] = "Glintstone Dragon Samantha",
            [904503610] = "Boris, the Uncomfortably Cold",
            [904510610] = "Ancient Dragon Larry",  // both appearances
            [904130610] = "Demi-Human Queen Marge",
            [903560610] = "Stretch Dude",
            [904500610] = "Flying Dragon Alberto",
            [904501610] = "Decaying Edna",
            [903050610] = "Commander O'Connell",
            [904911610] = "Great Wyrm Womble-Bomble",
            [904500611] = "Flying Dragon Graham",
            [903253510] = "Royal Knight Laurie",
            [903050510] = "Commander O'Farrell",
            [904760010] = "Fire Giantess",
            [904502611] = "Glintstone Dragon Adeline",

            // Generic
            [902500300] = "Crucible Knights Ordovis and Olga",
            [902500301] = "Lesser Crucible Knights",
            [903700300] = "Perfumers Tricia and Helga",
            [904260304] = "Erdtree Burial Watchdogs",
            [904260305] = "Erdtree Burial Watchdogs",
            [130901] = "Patches' Less Handsome Twin Brother",
            [904130311] = "Demi-Human Queen Margaret",
            [903350313] = "Putrid Crystalian (Spear)",
            [903350312] = "Putrid Crystalian (Ringblade)",
            [903350314] = "Putrid Crystalian (Staff)",
            [903350316] = "Very Putrid Crystalian (Spear)",
            [903350315] = "Very Putrid Crystalian (Ringblade)",
            [903350317] = "Very Putrid Crystalian (Staff)",
            [904480310] = "Miranda and Myrtle the Blighted Blooms",
            [904820310] = "Omenkiller Duo",
            [137601] = "Necromancer Garth",
            [903800311] = "Cleanrot Knights: Alpha Team",
            [903800312] = "Cleanrot Knights: Beta Team",
            [904620320] = "Why Did It Have To Be Astels?",
            [902140000] = "Fell Twins",
            [902140001] = "Fell Twins",

            // m39_20_00_00
            [904910010] = "Magma Wyrm Molkor",
        };
    }
}
