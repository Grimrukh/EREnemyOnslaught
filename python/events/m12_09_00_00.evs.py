"""
Regal Ancestor Arena

linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m12_09_00_00_entities import *


# TODO: A lot of tricky animal events going on here. Probably just blindly duplicate everything.
#  Good news is that this map has heaps of available ID ranges for clones and flags.


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegalAncestorSpiritCommonEvents()
    RegalAncestorSpiritDies()
    RegalAncestorSpiritBattleTrigger()
    ReturnToSiofraRiver()

    # ORIGINAL
    AnimalDies(0, animal=Characters.Deer0, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(1, animal=Characters.Deer1, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(2, animal=Characters.Deer2, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(3, animal=Characters.Deer3, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(4, animal=Characters.Deer4, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(5, animal=Characters.Deer5, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(6, animal=Characters.Deer6, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(7, animal=Characters.Boar0, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(8, animal=Characters.Boar1, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(9, animal=Characters.Boar2, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(10, animal=Characters.Boar3, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(11, animal=Characters.Boar4, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(12, animal=Characters.Boar5, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(13, animal=Characters.Boar6, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(14, animal=Characters.WildMouflon0, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(15, animal=Characters.WildMouflon1, request_animal_recount_flag=12092859)  # TODO: typo?
    AnimalDies(16, animal=Characters.WildMouflon2, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(17, animal=Characters.WildMouflon3, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(18, animal=Characters.WildMouflon4, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(19, animal=Characters.WildMouflon5, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(20, animal=Characters.WildMouflon6, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(21, animal=Characters.Springhare0, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(22, animal=Characters.Springhare1, request_animal_recount_flag=12092859)  # TODO: typo?
    AnimalDies(23, animal=Characters.Springhare2, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(24, animal=Characters.Springhare3, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(25, animal=Characters.Springhare4, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(26, animal=Characters.Springhare5, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalDies(27, animal=Characters.Springhare6, request_animal_recount_flag=Flags.RequestAnimalRecount)
    AnimalStartsFloating(0, request_flag=Flags.AncestorRequestWarpToAnimal0, animal=Characters.Deer0)
    AnimalStartsFloating(1, request_flag=Flags.AncestorRequestWarpToAnimal1, animal=Characters.Deer1)
    AnimalStartsFloating(2, request_flag=Flags.AncestorRequestWarpToAnimal2, animal=Characters.Deer2)
    AnimalStartsFloating(3, request_flag=Flags.AncestorRequestWarpToAnimal3, animal=Characters.Deer3)
    AnimalStartsFloating(4, request_flag=Flags.AncestorRequestWarpToAnimal4, animal=Characters.Deer4)
    AnimalStartsFloating(5, request_flag=Flags.AncestorRequestWarpToAnimal5, animal=Characters.Deer5)
    AnimalStartsFloating(6, request_flag=Flags.AncestorRequestWarpToAnimal6, animal=Characters.Deer6)
    AnimalStartsFloating(7, request_flag=Flags.AncestorRequestWarpToAnimal7, animal=Characters.Boar0)
    AnimalStartsFloating(8, request_flag=Flags.AncestorRequestWarpToAnimal8, animal=Characters.Boar1)
    AnimalStartsFloating(9, request_flag=Flags.AncestorRequestWarpToAnimal9, animal=Characters.Boar2)
    AnimalStartsFloating(10, request_flag=Flags.AncestorRequestWarpToAnimal10, animal=Characters.Boar3)
    AnimalStartsFloating(11, request_flag=Flags.AncestorRequestWarpToAnimal11, animal=Characters.Boar4)
    AnimalStartsFloating(12, request_flag=Flags.AncestorRequestWarpToAnimal12, animal=Characters.Boar5)
    AnimalStartsFloating(13, request_flag=Flags.AncestorRequestWarpToAnimal13, animal=Characters.Boar6)
    AnimalStartsFloating(14, request_flag=Flags.AncestorRequestWarpToAnimal14, animal=Characters.WildMouflon0)
    AnimalStartsFloating(15, request_flag=Flags.AncestorRequestWarpToAnimal15, animal=Characters.WildMouflon1)
    AnimalStartsFloating(16, request_flag=Flags.AncestorRequestWarpToAnimal16, animal=Characters.WildMouflon2)
    AnimalStartsFloating(17, request_flag=Flags.AncestorRequestWarpToAnimal17, animal=Characters.WildMouflon3)
    AnimalStartsFloating(18, request_flag=Flags.AncestorRequestWarpToAnimal18, animal=Characters.WildMouflon4)
    AnimalStartsFloating(19, request_flag=Flags.AncestorRequestWarpToAnimal19, animal=Characters.WildMouflon5)
    AnimalStartsFloating(20, request_flag=Flags.AncestorRequestWarpToAnimal20, animal=Characters.WildMouflon6)
    AnimalStartsFloating(21, request_flag=Flags.AncestorRequestWarpToAnimal21, animal=Characters.Springhare0)
    AnimalStartsFloating(22, request_flag=Flags.AncestorRequestWarpToAnimal22, animal=Characters.Springhare1)
    AnimalStartsFloating(23, request_flag=Flags.AncestorRequestWarpToAnimal23, animal=Characters.Springhare2)
    AnimalStartsFloating(24, request_flag=Flags.AncestorRequestWarpToAnimal24, animal=Characters.Springhare3)
    AnimalStartsFloating(25, request_flag=Flags.AncestorRequestWarpToAnimal25, animal=Characters.Springhare4)
    AnimalStartsFloating(26, request_flag=Flags.AncestorRequestWarpToAnimal26, animal=Characters.Springhare5)
    AnimalStartsFloating(27, request_flag=Flags.AncestorRequestWarpToAnimal27, animal=Characters.Springhare6)
    AncestorWarpsToAnimal(0, request_flag=Flags.AncestorRequestWarpToAnimal0, animal=Characters.Deer0, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(1, request_flag=Flags.AncestorRequestWarpToAnimal1, animal=Characters.Deer1, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(2, request_flag=Flags.AncestorRequestWarpToAnimal2, animal=Characters.Deer2, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(3, request_flag=Flags.AncestorRequestWarpToAnimal3, animal=Characters.Deer3, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(4, request_flag=Flags.AncestorRequestWarpToAnimal4, animal=Characters.Deer4, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(5, request_flag=Flags.AncestorRequestWarpToAnimal5, animal=Characters.Deer5, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(6, request_flag=Flags.AncestorRequestWarpToAnimal6, animal=Characters.Deer6, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(7, request_flag=Flags.AncestorRequestWarpToAnimal7, animal=Characters.Boar0, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(8, request_flag=Flags.AncestorRequestWarpToAnimal8, animal=Characters.Boar1, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(9, request_flag=Flags.AncestorRequestWarpToAnimal9, animal=Characters.Boar2, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(10, request_flag=Flags.AncestorRequestWarpToAnimal10, animal=Characters.Boar3, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(11, request_flag=Flags.AncestorRequestWarpToAnimal11, animal=Characters.Boar4, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(12, request_flag=Flags.AncestorRequestWarpToAnimal12, animal=Characters.Boar5, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(13, request_flag=Flags.AncestorRequestWarpToAnimal13, animal=Characters.Boar6, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(14, request_flag=Flags.AncestorRequestWarpToAnimal14, animal=Characters.WildMouflon0, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(15, request_flag=Flags.AncestorRequestWarpToAnimal15, animal=Characters.WildMouflon1, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(16, request_flag=Flags.AncestorRequestWarpToAnimal16, animal=Characters.WildMouflon2, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(17, request_flag=Flags.AncestorRequestWarpToAnimal17, animal=Characters.WildMouflon3, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(18, request_flag=Flags.AncestorRequestWarpToAnimal18, animal=Characters.WildMouflon4, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(19, request_flag=Flags.AncestorRequestWarpToAnimal19, animal=Characters.WildMouflon5, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(20, request_flag=Flags.AncestorRequestWarpToAnimal20, animal=Characters.WildMouflon6, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(21, request_flag=Flags.AncestorRequestWarpToAnimal21, animal=Characters.Springhare0, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(22, request_flag=Flags.AncestorRequestWarpToAnimal22, animal=Characters.Springhare1, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(23, request_flag=Flags.AncestorRequestWarpToAnimal23, animal=Characters.Springhare2, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(24, request_flag=Flags.AncestorRequestWarpToAnimal24, animal=Characters.Springhare3, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(25, request_flag=Flags.AncestorRequestWarpToAnimal25, animal=Characters.Springhare4, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(26, request_flag=Flags.AncestorRequestWarpToAnimal26, animal=Characters.Springhare5, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpsToAnimal(27, request_flag=Flags.AncestorRequestWarpToAnimal27, animal=Characters.Springhare6, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorWarpAttack3014()
    SetUpAncestorAnimals(0, animal_group=CharacterGroups.RegalAncestorAnimals)
    AncestorRequestsAnimalSpawn(
        0,
        six_animal_max_flag=12092850,
        eight_animal_max_flag=12092851,
        ten_animal_max_flag=12092852,
        do_not_spawn_flag=Flags.DoNotSpawnAnimals,
        ancestor_spirit=Characters.RegalAncestorSpirit,
        animal_group=CharacterGroups.RegalAncestorAnimals,
    )
    SpawnAnimals(
        0,
        six_animal_max_flag=12092850,
        eight_animal_max_flag=12092851,
        ten_animal_max_flag=12092852,
        do_not_spawn_flag=Flags.DoNotSpawnAnimals,
        spawn_animals_0_1_2=12092855,
        spawn_animals_3_4=12092856,
        spawn_animals_5_6=12092857,
        ancestor=Characters.RegalAncestorSpirit,
        all_animals=CharacterGroups.RegalAncestorAnimals,
        all_deer=CharacterGroups.RegalAncestorDeer,
        all_boars=CharacterGroups.RegalAncestorBoars,
        all_wild_mouflons=CharacterGroups.RegalAncestorWildMouflons,
        all_springhares=CharacterGroups.RegalAncestorSpringhares,
        deer_0=Characters.Deer0,
        deer_1=Characters.Deer1,
        deer_2=Characters.Deer2,
        deer_3=Characters.Deer3,
        deer_4=Characters.Deer4,
        deer_5=Characters.Deer5,
        deer_6=Characters.Deer6,
        boar_0=Characters.Boar0,
        boar_1=Characters.Boar1,
        boar_2=Characters.Boar2,
        boar_3=Characters.Boar3,
        boar_4=Characters.Boar4,
        boar_5=Characters.Boar5,
        boar_6=Characters.Boar6,
        wild_mouflon_0=Characters.WildMouflon0,
        wild_mouflon_1=Characters.WildMouflon1,
        wild_mouflon_2=Characters.WildMouflon2,
        wild_mouflon_3=Characters.WildMouflon3,
        wild_mouflon_4=Characters.WildMouflon4,
        wild_mouflon_5=Characters.WildMouflon5,
        wild_mouflon_6=Characters.WildMouflon6,
        springhare_0=Characters.Springhare0,
        springhare_1=Characters.Springhare1,
        springhare_2=Characters.Springhare2,
        springhare_3=Characters.Springhare3,
        springhare_4=Characters.Springhare4,
        springhare_5=Characters.Springhare5,
        springhare_6=Characters.Springhare6,
        deer_spawner_0=Spawners.DeerSpawner0,
        deer_spawner_1=Spawners.DeerSpawner1,
        deer_spawner_2=Spawners.DeerSpawner2,
        deer_spawner_3=Spawners.DeerSpawner3,
        deer_spawner_4=Spawners.DeerSpawner4,
        deer_spawner_5=Spawners.DeerSpawner5,
        deer_spawner_6=Spawners.DeerSpawner6,
        boar_spawner_0=Spawners.BoarSpawner0,
        boar_spawner_1=Spawners.BoarSpawner1,
        boar_spawner_2=Spawners.BoarSpawner2,
        boar_spawner_3=Spawners.BoarSpawner3,
        boar_spawner_4=Spawners.BoarSpawner4,
        boar_spawner_5=Spawners.BoarSpawner5,
        boar_spawner_6=Spawners.BoarSpawner6,
        wild_mouflon_spawner_0=Spawners.WildMouflonSpawner0,
        wild_mouflon_spawner_1=Spawners.WildMouflonSpawner1,
        wild_mouflon_spawner_2=Spawners.WildMouflonSpawner2,
        wild_mouflon_spawner_3=Spawners.WildMouflonSpawner3,
        wild_mouflon_spawner_4=Spawners.WildMouflonSpawner4,
        wild_mouflon_spawner_5=Spawners.WildMouflonSpawner5,
        wild_mouflon_spawner_6=Spawners.WildMouflonSpawner6,
        springhare_spawner_0=Spawners.SpringhareSpawner0,
        springhare_spawner_1=Spawners.SpringhareSpawner1,
        springhare_spawner_2=Spawners.SpringhareSpawner2,
        springhare_spawner_3=Spawners.SpringhareSpawner3,
        springhare_spawner_4=Spawners.SpringhareSpawner4,
        springhare_spawner_5=Spawners.SpringhareSpawner5,
        springhare_spawner_6=Spawners.SpringhareSpawner6,
        request_animal_recount_flag=Flags.RequestAnimalRecount,
    )
    AncestorAnimalEffectCheck(
        0,
        request_flag=Flags.RequestAnimalRecount,
        ancestor_spirit=Characters.RegalAncestorSpirit,
        deer_group=CharacterGroups.RegalAncestorDeer,
        boar_group=CharacterGroups.RegalAncestorBoars,
        wild_mouflon_group=CharacterGroups.RegalAncestorWildMouflons,
        springhare_group=CharacterGroups.RegalAncestorSpringhares,
        animal_group=CharacterGroups.RegalAncestorAnimals,
    )
    AncestorReactivates(0, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorFirstAnimalLifeDrain(
        0, ancestor_spirit=Characters.RegalAncestorSpirit, all_animals=CharacterGroups.RegalAncestorAnimals
    )
    AncestorSecondAnimalLifeDrain(
        0, 
        ancestor_spirit=Characters.RegalAncestorSpirit, 
        animal_group=CharacterGroups.RegalAncestorAnimals, 
        first_life_drain_done_flag=Flags.AncestorFirstAnimalLifeDrainDone,
    )
    AncestorThirdPlusAnimalLifeDrain(
        0, 
        ancestor_spirit=Characters.RegalAncestorSpirit, 
        animal_group=CharacterGroups.RegalAncestorAnimals, 
        first_life_drain_done_flag=Flags.AncestorFirstAnimalLifeDrainDone,
        second_life_drain_done_flag=Flags.AncestorSecondAnimalLifeDrainDone,
    )
    CreateAncestorProjectileOwner(0, projectile_dummy=Characters.AncestorProjectileOwner)
    AncestorLifeDrainProjectiles(0, ancestor_spirit=Characters.RegalAncestorSpirit)
    RequestAncestorProjectile(0, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092300)
    RequestAncestorProjectile(1, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092301)
    RequestAncestorProjectile(2, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092302)
    RequestAncestorProjectile(3, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092303)
    RequestAncestorProjectile(4, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092304)
    RequestAncestorProjectile(5, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092305)
    RequestAncestorProjectile(6, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092306)
    RequestAncestorProjectile(7, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092307)
    RequestAncestorProjectile(8, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092308)
    RequestAncestorProjectile(9, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092309)
    RequestAncestorProjectile(10, request_animal_count_flag=Flags.ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092310)
    RequestAncestorProjectile(11, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092311)
    RequestAncestorProjectile(12, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092312)
    RequestAncestorProjectile(13, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092313)
    RequestAncestorProjectile(14, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092314)
    RequestAncestorProjectile(15, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092315)
    RequestAncestorProjectile(16, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092316)
    RequestAncestorProjectile(17, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092317)
    RequestAncestorProjectile(18, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092318)
    RequestAncestorProjectile(19, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092319)
    RequestAncestorProjectile(20, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092320)
    RequestAncestorProjectile(21, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092321)
    RequestAncestorProjectile(22, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092322)
    RequestAncestorProjectile(23, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092323)
    RequestAncestorProjectile(24, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092324)
    RequestAncestorProjectile(25, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092325)
    RequestAncestorProjectile(26, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092326)
    RequestAncestorProjectile(27, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092327)
    RequestAncestorProjectile(28, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092328)
    RequestAncestorProjectile(29, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092329)
    RequestAncestorProjectile(30, request_animal_count_flag=Flags.ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092330)
    RequestAncestorProjectile(31, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092331)
    RequestAncestorProjectile(32, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092332)
    RequestAncestorProjectile(33, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092333)
    RequestAncestorProjectile(34, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092334)
    RequestAncestorProjectile(35, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092335)
    RequestAncestorProjectile(36, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092336)
    RequestAncestorProjectile(37, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092337)
    RequestAncestorProjectile(38, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092338)
    RequestAncestorProjectile(39, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092339)
    RequestAncestorProjectile(40, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092340)
    RequestAncestorProjectile(41, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092341)
    RequestAncestorProjectile(42, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092342)
    RequestAncestorProjectile(43, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092343)
    RequestAncestorProjectile(44, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092344)
    RequestAncestorProjectile(45, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092345)
    RequestAncestorProjectile(46, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092346)
    RequestAncestorProjectile(47, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092347)
    RequestAncestorProjectile(48, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092348)
    RequestAncestorProjectile(49, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092349)
    RequestAncestorProjectile(50, request_animal_count_flag=Flags.ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092350)

    # CLONE. Not even bothering to use different slots for most, as they don't use their flags.
    AnimalDies(0, animal=Characters.CLONE_Deer0, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(1, animal=Characters.CLONE_Deer1, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(2, animal=Characters.CLONE_Deer2, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(3, animal=Characters.CLONE_Deer3, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(4, animal=Characters.CLONE_Deer4, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(5, animal=Characters.CLONE_Deer5, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(6, animal=Characters.CLONE_Deer6, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(7, animal=Characters.CLONE_Boar0, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(8, animal=Characters.CLONE_Boar1, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(9, animal=Characters.CLONE_Boar2, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(10, animal=Characters.CLONE_Boar3, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(11, animal=Characters.CLONE_Boar4, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(12, animal=Characters.CLONE_Boar5, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(13, animal=Characters.CLONE_Boar6, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(14, animal=Characters.CLONE_WildMouflon0, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(15, animal=Characters.CLONE_WildMouflon1, request_animal_recount_flag=12092859)  # TODO: typo?
    AnimalDies(16, animal=Characters.CLONE_WildMouflon2, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(17, animal=Characters.CLONE_WildMouflon3, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(18, animal=Characters.CLONE_WildMouflon4, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(19, animal=Characters.CLONE_WildMouflon5, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(20, animal=Characters.CLONE_WildMouflon6, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(21, animal=Characters.CLONE_Springhare0, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(22, animal=Characters.CLONE_Springhare1, request_animal_recount_flag=12092859)  # TODO: typo?
    AnimalDies(23, animal=Characters.CLONE_Springhare2, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(24, animal=Characters.CLONE_Springhare3, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(25, animal=Characters.CLONE_Springhare4, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(26, animal=Characters.CLONE_Springhare5, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalDies(27, animal=Characters.CLONE_Springhare6, request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount)
    AnimalStartsFloating(0, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal0, animal=Characters.CLONE_Deer0)
    AnimalStartsFloating(1, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal1, animal=Characters.CLONE_Deer1)
    AnimalStartsFloating(2, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal2, animal=Characters.CLONE_Deer2)
    AnimalStartsFloating(3, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal3, animal=Characters.CLONE_Deer3)
    AnimalStartsFloating(4, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal4, animal=Characters.CLONE_Deer4)
    AnimalStartsFloating(5, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal5, animal=Characters.CLONE_Deer5)
    AnimalStartsFloating(6, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal6, animal=Characters.CLONE_Deer6)
    AnimalStartsFloating(7, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal7, animal=Characters.CLONE_Boar0)
    AnimalStartsFloating(8, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal8, animal=Characters.CLONE_Boar1)
    AnimalStartsFloating(9, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal9, animal=Characters.CLONE_Boar2)
    AnimalStartsFloating(10, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal10, animal=Characters.CLONE_Boar3)
    AnimalStartsFloating(11, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal11, animal=Characters.CLONE_Boar4)
    AnimalStartsFloating(12, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal12, animal=Characters.CLONE_Boar5)
    AnimalStartsFloating(13, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal13, animal=Characters.CLONE_Boar6)
    AnimalStartsFloating(14, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal14, animal=Characters.CLONE_WildMouflon0)
    AnimalStartsFloating(15, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal15, animal=Characters.CLONE_WildMouflon1)
    AnimalStartsFloating(16, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal16, animal=Characters.CLONE_WildMouflon2)
    AnimalStartsFloating(17, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal17, animal=Characters.CLONE_WildMouflon3)
    AnimalStartsFloating(18, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal18, animal=Characters.CLONE_WildMouflon4)
    AnimalStartsFloating(19, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal19, animal=Characters.CLONE_WildMouflon5)
    AnimalStartsFloating(20, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal20, animal=Characters.CLONE_WildMouflon6)
    AnimalStartsFloating(21, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal21, animal=Characters.CLONE_Springhare0)
    AnimalStartsFloating(22, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal22, animal=Characters.CLONE_Springhare1)
    AnimalStartsFloating(23, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal23, animal=Characters.CLONE_Springhare2)
    AnimalStartsFloating(24, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal24, animal=Characters.CLONE_Springhare3)
    AnimalStartsFloating(25, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal25, animal=Characters.CLONE_Springhare4)
    AnimalStartsFloating(26, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal26, animal=Characters.CLONE_Springhare5)
    AnimalStartsFloating(27, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal27, animal=Characters.CLONE_Springhare6)
    AncestorWarpsToAnimal(0, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal0, animal=Characters.CLONE_Deer0, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(1, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal1, animal=Characters.CLONE_Deer1, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(2, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal2, animal=Characters.CLONE_Deer2, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(3, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal3, animal=Characters.CLONE_Deer3, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(4, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal4, animal=Characters.CLONE_Deer4, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(5, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal5, animal=Characters.CLONE_Deer5, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(6, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal6, animal=Characters.CLONE_Deer6, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(7, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal7, animal=Characters.CLONE_Boar0, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(8, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal8, animal=Characters.CLONE_Boar1, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(9, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal9, animal=Characters.CLONE_Boar2, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(10, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal10, animal=Characters.CLONE_Boar3, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(11, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal11, animal=Characters.CLONE_Boar4, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(12, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal12, animal=Characters.CLONE_Boar5, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(13, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal13, animal=Characters.CLONE_Boar6, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(14, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal14, animal=Characters.CLONE_WildMouflon0, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(15, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal15, animal=Characters.CLONE_WildMouflon1, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(16, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal16, animal=Characters.CLONE_WildMouflon2, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(17, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal17, animal=Characters.CLONE_WildMouflon3, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(18, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal18, animal=Characters.CLONE_WildMouflon4, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(19, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal19, animal=Characters.CLONE_WildMouflon5, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(20, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal20, animal=Characters.CLONE_WildMouflon6, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(21, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal21, animal=Characters.CLONE_Springhare0, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(22, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal22, animal=Characters.CLONE_Springhare1, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(23, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal23, animal=Characters.CLONE_Springhare2, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(24, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal24, animal=Characters.CLONE_Springhare3, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(25, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal25, animal=Characters.CLONE_Springhare4, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(26, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal26, animal=Characters.CLONE_Springhare5, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpsToAnimal(27, request_flag=Flags.CLONE_AncestorRequestWarpToAnimal27, animal=Characters.CLONE_Springhare6, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorWarpAttack3014()
    SetUpAncestorAnimals(0, animal_group=CharacterGroups.CLONE_RegalAncestorAnimals)
    AncestorRequestsAnimalSpawn(
        0,
        six_animal_max_flag=12092850,
        eight_animal_max_flag=12092851,
        ten_animal_max_flag=12092852,
        do_not_spawn_flag=Flags.CLONE_DoNotSpawnAnimals,
        ancestor_spirit=Characters.CLONE_RegalAncestorSpirit,
        animal_group=CharacterGroups.CLONE_RegalAncestorAnimals,
    )
    SpawnAnimals(
        10,  # flag 12092869
        six_animal_max_flag=12092850,
        eight_animal_max_flag=12092851,
        ten_animal_max_flag=12092852,
        do_not_spawn_flag=Flags.CLONE_DoNotSpawnAnimals,
        spawn_animals_0_1_2=12092855,
        spawn_animals_3_4=12092856,
        spawn_animals_5_6=12092857,
        ancestor=Characters.CLONE_RegalAncestorSpirit,
        all_animals=CharacterGroups.CLONE_RegalAncestorAnimals,
        all_deer=CharacterGroups.CLONE_RegalAncestorDeer,
        all_boars=CharacterGroups.CLONE_RegalAncestorBoars,
        all_wild_mouflons=CharacterGroups.CLONE_RegalAncestorWildMouflons,
        all_springhares=CharacterGroups.CLONE_RegalAncestorSpringhares,
        deer_0=Characters.CLONE_Deer0,
        deer_1=Characters.CLONE_Deer1,
        deer_2=Characters.CLONE_Deer2,
        deer_3=Characters.CLONE_Deer3,
        deer_4=Characters.CLONE_Deer4,
        deer_5=Characters.CLONE_Deer5,
        deer_6=Characters.CLONE_Deer6,
        boar_0=Characters.CLONE_Boar0,
        boar_1=Characters.CLONE_Boar1,
        boar_2=Characters.CLONE_Boar2,
        boar_3=Characters.CLONE_Boar3,
        boar_4=Characters.CLONE_Boar4,
        boar_5=Characters.CLONE_Boar5,
        boar_6=Characters.CLONE_Boar6,
        wild_mouflon_0=Characters.CLONE_WildMouflon0,
        wild_mouflon_1=Characters.CLONE_WildMouflon1,
        wild_mouflon_2=Characters.CLONE_WildMouflon2,
        wild_mouflon_3=Characters.CLONE_WildMouflon3,
        wild_mouflon_4=Characters.CLONE_WildMouflon4,
        wild_mouflon_5=Characters.CLONE_WildMouflon5,
        wild_mouflon_6=Characters.CLONE_WildMouflon6,
        springhare_0=Characters.CLONE_Springhare0,
        springhare_1=Characters.CLONE_Springhare1,
        springhare_2=Characters.CLONE_Springhare2,
        springhare_3=Characters.CLONE_Springhare3,
        springhare_4=Characters.CLONE_Springhare4,
        springhare_5=Characters.CLONE_Springhare5,
        springhare_6=Characters.CLONE_Springhare6,
        deer_spawner_0=Spawners.CLONE_DeerSpawner0,
        deer_spawner_1=Spawners.CLONE_DeerSpawner1,
        deer_spawner_2=Spawners.CLONE_DeerSpawner2,
        deer_spawner_3=Spawners.CLONE_DeerSpawner3,
        deer_spawner_4=Spawners.CLONE_DeerSpawner4,
        deer_spawner_5=Spawners.CLONE_DeerSpawner5,
        deer_spawner_6=Spawners.CLONE_DeerSpawner6,
        boar_spawner_0=Spawners.CLONE_BoarSpawner0,
        boar_spawner_1=Spawners.CLONE_BoarSpawner1,
        boar_spawner_2=Spawners.CLONE_BoarSpawner2,
        boar_spawner_3=Spawners.CLONE_BoarSpawner3,
        boar_spawner_4=Spawners.CLONE_BoarSpawner4,
        boar_spawner_5=Spawners.CLONE_BoarSpawner5,
        boar_spawner_6=Spawners.CLONE_BoarSpawner6,
        wild_mouflon_spawner_0=Spawners.CLONE_WildMouflonSpawner0,
        wild_mouflon_spawner_1=Spawners.CLONE_WildMouflonSpawner1,
        wild_mouflon_spawner_2=Spawners.CLONE_WildMouflonSpawner2,
        wild_mouflon_spawner_3=Spawners.CLONE_WildMouflonSpawner3,
        wild_mouflon_spawner_4=Spawners.CLONE_WildMouflonSpawner4,
        wild_mouflon_spawner_5=Spawners.CLONE_WildMouflonSpawner5,
        wild_mouflon_spawner_6=Spawners.CLONE_WildMouflonSpawner6,
        springhare_spawner_0=Spawners.CLONE_SpringhareSpawner0,
        springhare_spawner_1=Spawners.CLONE_SpringhareSpawner1,
        springhare_spawner_2=Spawners.CLONE_SpringhareSpawner2,
        springhare_spawner_3=Spawners.CLONE_SpringhareSpawner3,
        springhare_spawner_4=Spawners.CLONE_SpringhareSpawner4,
        springhare_spawner_5=Spawners.CLONE_SpringhareSpawner5,
        springhare_spawner_6=Spawners.CLONE_SpringhareSpawner6,
        request_animal_recount_flag=Flags.CLONE_RequestAnimalRecount,
    )
    AncestorAnimalEffectCheck(
        0,
        request_flag=Flags.CLONE_RequestAnimalRecount,
        ancestor_spirit=Characters.CLONE_RegalAncestorSpirit,
        deer_group=CharacterGroups.CLONE_RegalAncestorDeer,
        boar_group=CharacterGroups.CLONE_RegalAncestorBoars,
        wild_mouflon_group=CharacterGroups.CLONE_RegalAncestorWildMouflons,
        springhare_group=CharacterGroups.CLONE_RegalAncestorSpringhares,
        animal_group=CharacterGroups.CLONE_RegalAncestorAnimals,
    )
    AncestorReactivates(0, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    AncestorFirstAnimalLifeDrain(
        4, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit, all_animals=CharacterGroups.CLONE_RegalAncestorAnimals
    )  # slot 4
    AncestorSecondAnimalLifeDrain(
        4,
        ancestor_spirit=Characters.CLONE_RegalAncestorSpirit, 
        animal_group=CharacterGroups.CLONE_RegalAncestorAnimals, 
        first_life_drain_done_flag=Flags.CLONE_AncestorFirstAnimalLifeDrainDone,
    )  # slot 4
    AncestorThirdPlusAnimalLifeDrain(
        0, 
        ancestor_spirit=Characters.CLONE_RegalAncestorSpirit, 
        animal_group=CharacterGroups.CLONE_RegalAncestorAnimals, 
        first_life_drain_done_flag=Flags.CLONE_AncestorFirstAnimalLifeDrainDone,
        second_life_drain_done_flag=Flags.CLONE_AncestorSecondAnimalLifeDrainDone,
    )
    CreateAncestorProjectileOwner(0, projectile_dummy=Characters.AncestorProjectileOwner)
    AncestorLifeDrainProjectiles(0, ancestor_spirit=Characters.CLONE_RegalAncestorSpirit)
    RequestAncestorProjectile(0, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092300)
    RequestAncestorProjectile(1, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092301)
    RequestAncestorProjectile(2, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092302)
    RequestAncestorProjectile(3, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092303)
    RequestAncestorProjectile(4, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092304)
    RequestAncestorProjectile(5, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092305)
    RequestAncestorProjectile(6, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092306)
    RequestAncestorProjectile(7, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092307)
    RequestAncestorProjectile(8, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092308)
    RequestAncestorProjectile(9, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092309)
    RequestAncestorProjectile(10, request_animal_count_flag=Flags.CLONE_ProjectileRequest_LowAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092310)
    RequestAncestorProjectile(11, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092311)
    RequestAncestorProjectile(12, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092312)
    RequestAncestorProjectile(13, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092313)
    RequestAncestorProjectile(14, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092314)
    RequestAncestorProjectile(15, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092315)
    RequestAncestorProjectile(16, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092316)
    RequestAncestorProjectile(17, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092317)
    RequestAncestorProjectile(18, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092318)
    RequestAncestorProjectile(19, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092319)
    RequestAncestorProjectile(20, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092320)
    RequestAncestorProjectile(21, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092321)
    RequestAncestorProjectile(22, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092322)
    RequestAncestorProjectile(23, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092323)
    RequestAncestorProjectile(24, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092324)
    RequestAncestorProjectile(25, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092325)
    RequestAncestorProjectile(26, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092326)
    RequestAncestorProjectile(27, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092327)
    RequestAncestorProjectile(28, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092328)
    RequestAncestorProjectile(29, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092329)
    RequestAncestorProjectile(30, request_animal_count_flag=Flags.CLONE_ProjectileRequest_MediumAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092330)
    RequestAncestorProjectile(31, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092331)
    RequestAncestorProjectile(32, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092332)
    RequestAncestorProjectile(33, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092333)
    RequestAncestorProjectile(34, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092334)
    RequestAncestorProjectile(35, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092335)
    RequestAncestorProjectile(36, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092336)
    RequestAncestorProjectile(37, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092337)
    RequestAncestorProjectile(38, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092338)
    RequestAncestorProjectile(39, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092339)
    RequestAncestorProjectile(40, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092340)
    RequestAncestorProjectile(41, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092341)
    RequestAncestorProjectile(42, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092342)
    RequestAncestorProjectile(43, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092343)
    RequestAncestorProjectile(44, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092344)
    RequestAncestorProjectile(45, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092345)
    RequestAncestorProjectile(46, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092346)
    RequestAncestorProjectile(47, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092347)
    RequestAncestorProjectile(48, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092348)
    RequestAncestorProjectile(49, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092349)
    RequestAncestorProjectile(50, request_animal_count_flag=Flags.CLONE_ProjectileRequest_HighAnimalCount, owner_entity=Characters.AncestorProjectileOwner, source_entity=12092350)


@ContinueOnRest(12092848)
def ReturnToSiofraRiver():
    """Event 12092848"""
    GotoIfFlagEnabled(Label.L0, flag=Flags.RegalAncestorSpiritDead)
    DeleteAssetVFX(Assets.AEG099_065_9000, erase_root=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(Flags.RegalAncestorSpiritDead))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(Assets.AEG099_065_9000)
    CreateAssetVFX(Assets.AEG099_065_9000, vfx_id=190, model_point=1300)
    OR_2.Add(MultiplayerPending())
    OR_2.Add(Multiplayer())
    AND_2.Add(not OR_2)
    AND_2.Add(ActionButtonParamActivated(action_button_id=9526, entity=Assets.AEG099_065_9000))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(PLAYER, 60460)
    Wait(2.5)
    SetRespawnPoint(respawn_point=12022201)
    SaveRequest()
    WarpToMap(game_map=SIOFRA_RIVER, player_start=12022201)


@ContinueOnRest(12092800)
def RegalAncestorSpiritDies():
    """Event 12092800"""
    if FlagEnabled(Flags.RegalAncestorSpiritDead):
        return

    AND_1.Add(HealthRatio(Characters.RegalAncestorSpirit) <= 0.0)
    AND_1.Add(HealthRatio(Characters.CLONE_AncestorSpirit) <= 0.0)
    MAIN.Await(AND_1)
    
    DisableFlag(Flags.ProjectileRequest_LowAnimalCount)
    DisableFlag(Flags.ProjectileRequest_MediumAnimalCount)
    DisableFlag(Flags.ProjectileRequest_HighAnimalCount)
    Kill(CharacterGroups.RegalAncestorAnimals)
    Wait(2.0)
    PlaySoundEffect(Characters.RegalAncestorSpirit, 77777777, sound_type=SoundType.s_SFX)

    AND_2.Add(CharacterDead(Characters.RegalAncestorSpirit))
    AND_2.Add(CharacterDead(Characters.CLONE_RegalAncestorSpirit))
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=Characters.RegalAncestorSpirit, banner_type=BannerType.LegendFelled)
    EnableFlag(Flags.RegalAncestorSpiritDead)
    EnableFlag(9133)
    if PlayerInOwnWorld():
        EnableFlag(91133)
    AwardItemLot(48000000, host_only=True)


@RestartOnRest(12092810)
def RegalAncestorSpiritBattleTrigger():
    """Event 12092810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.RegalAncestorSpiritDead)
    DisableCharacter(Characters.RegalAncestorSpirit)
    DisableAnimations(Characters.RegalAncestorSpirit)
    Kill(Characters.RegalAncestorSpirit)
    DisableCharacter(Characters.CLONE_RegalAncestorSpirit)
    DisableAnimations(Characters.CLONE_RegalAncestorSpirit)
    Kill(Characters.CLONE_RegalAncestorSpirit)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.RegalAncestorSpirit)
    DisableAI(Characters.CLONE_RegalAncestorSpirit)
    AND_2.Add(FlagEnabled(12092805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12092800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.RegalAncestorSpirit)
    EnableAI(Characters.CLONE_RegalAncestorSpirit)
    SetNetworkUpdateRate(Characters.RegalAncestorSpirit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_RegalAncestorSpirit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.RegalAncestorSpirit, name=NameText.RegalAncestorSpirit, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_RegalAncestorSpirit, name=NameText.CLONE_RegalAncestorSpirit, bar_slot=0)


@ContinueOnRest(12092849)
def RegalAncestorSpiritCommonEvents():
    """Event 12092849"""
    CommonFunc_ControlBossMusic(
        0,
        boss_dead_flag=Flags.RegalAncestorSpiritDead,
        bgm_boss_conv_param_id=467000,
        host_in_battle=12090805,
        summon_in_battle=12090806,
        extra_required_flag=0,
        phase_two_flag=Flags.AncestorInPhaseTwo,
        useless_phase_two_check=0,
        use_stop_type_1=0,
    )
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.RegalAncestorSpiritDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=12092800,
        host_entered_fog_flag=12092805,
        boss_characters=12095800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.RegalAncestorSpiritDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=12092800,
        host_entered_fog_flag=12092805,
        summon_entered_fog_flag=12092806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.RegalAncestorSpiritDead, fog_asset=Assets.AEG099_002_9000, model_point=8, required_flag=0)
    CommonFunc_ControlBossMusic(0, Flags.RegalAncestorSpiritDead, 467000, 12092805, 12092806, 0, Flags.AncestorInPhaseTwo, 0, 0)


@RestartOnRest(12092200)
def AnimalDies(_, animal: uint, request_animal_recount_flag: uint):
    """Event 12092200"""
    AND_1.Add(CharacterHasSpecialEffect(animal, Effects.AnimalActive))
    AND_1.Add(HealthRatio(animal) == 0.0)
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(animal, Effects.AnimalActive)
    EnableFlag(request_animal_recount_flag)
    Restart()


@RestartOnRest(12092230)
def AnimalStartsFloating(_, request_flag: uint, animal: uint):
    """Animal starts floating in preparation for Ancestor Spirit to spawn out of it and kill it."""
    AND_1.Add(FlagEnabled(request_flag))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(animal, Effects.AnimalActive)
    EnableInvincibility(animal)
    DisableAnimations(animal)
    DisableGravity(animal)
    DisableAI(animal)
    SetNetworkUpdateRate(animal, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(animal, 20000, wait_for_completion=True)
    ForceAnimation(animal, 20001, loop=True)
    Wait(15.0)
    Restart()


@RestartOnRest(12092260)
def AncestorWarpsToAnimal(_, request_flag: uint, animal: uint, ancestor_spirit: uint):
    """Event 12092260"""
    AND_1.Add(FlagEnabled(request_flag))
    AND_1.Add(CharacterHasSpecialEffect(ancestor_spirit, Effects.Ancestor_WarpToAnimalRequest))
    
    MAIN.Await(AND_1)
    
    DisableFlag(request_flag)
    DisableAnimations(ancestor_spirit)
    Move(
        ancestor_spirit,
        destination=animal,
        destination_type=CoordEntityType.Character,
        model_point=260,
        short_move=True,
    )

    # Ancestor Spirit does attack 3037 if player is between 7 and 40 units away, or 3014 otherwise.
    AND_15.Add(EntityWithinDistance(entity=20000, other_entity=animal, radius=40.0))
    AND_15.Add(EntityBeyondDistance(entity=20000, other_entity=animal, radius=7.0))
    SkipLinesIfConditionTrue(2, AND_15)
    ForceAnimation(ancestor_spirit, 3014)
    SkipLines(1)
    ForceAnimation(ancestor_spirit, 3037)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(3, character=ancestor_spirit, special_effect=13601)
    AddSpecialEffect(ancestor_spirit, 13613)
    AddSpecialEffect(ancestor_spirit, 13618)
    Goto(Label.L0)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(3, character=ancestor_spirit, special_effect=13602)
    AddSpecialEffect(ancestor_spirit, 13614)
    AddSpecialEffect(ancestor_spirit, 13619)
    Goto(Label.L0)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(3, character=ancestor_spirit, special_effect=13603)
    AddSpecialEffect(ancestor_spirit, 13615)
    AddSpecialEffect(ancestor_spirit, 13620)
    Goto(Label.L0)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(2, character=ancestor_spirit, special_effect=13604)
    AddSpecialEffect(ancestor_spirit, 13616)
    AddSpecialEffect(ancestor_spirit, 13621)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(animal, 20002, wait_for_completion=True)
    DisableAI(animal)
    EnableGravity(animal)
    DisableCharacter(animal)
    DisableInvincibility(animal)
    Kill(animal)
    SetNetworkUpdateRate(animal, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    EnableAnimations(ancestor_spirit)
    DisableFlag(request_flag)
    Restart()


@RestartOnRest(12092290)
def AncestorWarpAttack3014():
    """Event 12092290"""
    AND_1.Add(FlagEnabled(Flags.AncestorRequestWarpAttack3014))
    AND_1.Add(CharacterHasSpecialEffect(Characters.RegalAncestorSpirit, Effects.Ancestor_WarpToAnimalRequest))
    
    MAIN.Await(AND_1)
    
    DisableFlag(Flags.AncestorRequestWarpAttack3014)
    DisableAnimations(Characters.RegalAncestorSpirit)
    Move(
        Characters.RegalAncestorSpirit,
        destination=12092308,
        destination_type=CoordEntityType.Region,
        model_point=0,
        short_move=True,
    )
    ForceAnimation(Characters.RegalAncestorSpirit, 3014)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        3,
        character=Characters.RegalAncestorSpirit,
        special_effect=13601,
    )
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13613)
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13618)
    Goto(Label.L0)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        3,
        character=Characters.RegalAncestorSpirit,
        special_effect=13602,
    )
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13614)
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13619)
    Goto(Label.L0)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        3,
        character=Characters.RegalAncestorSpirit,
        special_effect=13603,
    )
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13615)
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13620)
    Goto(Label.L0)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        2,
        character=Characters.RegalAncestorSpirit,
        special_effect=13604,
    )
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13616)
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13621)

    # --- Label 0 --- #
    DefineLabel(0)

    EnableAnimations(Characters.RegalAncestorSpirit)
    DisableFlag(Flags.AncestorRequestWarpAttack3014)
    Restart()


@RestartOnRest(12092295)
def SetUpAncestorAnimals(_, animal_group: uint):
    """Event 12092295"""
    SetLockOnPoint(character=animal_group, lock_on_model_point=220, state=False)
    DisableAnimations(animal_group)


@RestartOnRest(12092854)
def AncestorRequestsAnimalSpawn(
    _,
    six_animal_max_flag: uint,
    eight_animal_max_flag: uint,
    ten_animal_max_flag: uint,
    do_not_spawn_flag: uint,
    ancestor_spirit: uint,
    animal_group: uint,
):
    """Event 12092854"""
    MAIN.Await(CharacterHasSpecialEffect(ancestor_spirit, Effects.AnimalSpawnRequest))
    
    DisableFlag(six_animal_max_flag)
    DisableFlag(eight_animal_max_flag)
    DisableFlag(ten_animal_max_flag)

    # Enables one of the three maximum flags:
    #  - if <5 animals are active, max is six
    #  - if <10 animals are active, max is eight
    #  - if >=10 animals are active, max is ten

    AND_15.Add(CharacterHasSpecialEffect(
        animal_group, Effects.AnimalActive, target_comparison_type=ComparisonType.LessThan, target_count=5.0
    ))
    SkipLinesIfConditionFalse(2, AND_15)
    EnableFlag(ten_animal_max_flag)
    Goto(Label.L0)

    AND_14.Add(CharacterHasSpecialEffect(
        animal_group, Effects.AnimalActive, target_comparison_type=ComparisonType.LessThan, target_count=10.0
    ))
    SkipLinesIfConditionFalse(2, AND_14)
    EnableFlag(eight_animal_max_flag)
    Goto(Label.L0)

    AND_13.Add(CharacterHasSpecialEffect(
        animal_group,
        Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=10.0,
    ))
    SkipLinesIfConditionFalse(2, AND_13)
    EnableFlag(six_animal_max_flag)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(animal_group, 13643)
    DisableFlag(do_not_spawn_flag)
    Wait(2.0)  # allow spawn event time to spawn
    EnableFlag(do_not_spawn_flag)
    Restart()


@RestartOnRest(12092859)
def SpawnAnimals(
    _,
    six_animal_max_flag: uint,
    eight_animal_max_flag: uint,
    ten_animal_max_flag: uint,
    do_not_spawn_flag: uint,
    spawn_animals_0_1_2: uint,
    spawn_animals_3_4: uint,
    spawn_animals_5_6: uint,
    ancestor: uint,
    all_animals: uint,
    all_deer: uint,
    all_boars: uint,
    all_wild_mouflons: uint,
    all_springhares: uint,
    deer_0: uint,  # 28 animal instances
    deer_1: uint,
    deer_2: uint,
    deer_3: uint,
    deer_4: uint,
    deer_5: uint,
    deer_6: uint,
    boar_0: uint,
    boar_1: uint,
    boar_2: uint,
    boar_3: uint,
    boar_4: uint,
    boar_5: uint,
    boar_6: uint,
    wild_mouflon_0: uint,
    wild_mouflon_1: uint,
    wild_mouflon_2: uint,
    wild_mouflon_3: uint,
    wild_mouflon_4: uint,
    wild_mouflon_5: uint,
    wild_mouflon_6: uint,
    springhare_0: uint,
    springhare_1: uint,
    springhare_2: uint,
    springhare_3: uint,
    springhare_4: uint,
    springhare_5: uint,
    springhare_6: uint,
    deer_spawner_0: uint,  # 28 spawners
    deer_spawner_1: uint,
    deer_spawner_2: uint,
    deer_spawner_3: uint,
    deer_spawner_4: uint,
    deer_spawner_5: uint,
    deer_spawner_6: uint,
    boar_spawner_0: uint,
    boar_spawner_1: uint,
    boar_spawner_2: uint,
    boar_spawner_3: uint,
    boar_spawner_4: uint,
    boar_spawner_5: uint,
    boar_spawner_6: uint,
    wild_mouflon_spawner_0: uint,
    wild_mouflon_spawner_1: uint,
    wild_mouflon_spawner_2: uint,
    wild_mouflon_spawner_3: uint,
    wild_mouflon_spawner_4: uint,
    wild_mouflon_spawner_5: uint,
    wild_mouflon_spawner_6: uint,
    springhare_spawner_0: uint,
    springhare_spawner_1: uint,
    springhare_spawner_2: uint,
    springhare_spawner_3: uint,
    springhare_spawner_4: uint,
    springhare_spawner_5: uint,
    springhare_spawner_6: uint,
    request_animal_recount_flag: uint,
):
    """Event 12092859"""
    if ThisEventSlotFlagDisabled():
        EnableFlag(do_not_spawn_flag)
        Restart()
    
    MAIN.Await(FlagDisabled(do_not_spawn_flag))
    
    DisableFlag(spawn_animals_0_1_2)
    DisableFlag(spawn_animals_3_4)
    DisableFlag(spawn_animals_5_6)
    EnableRandomFlagInRange(flag_range=(spawn_animals_0_1_2, spawn_animals_5_6))

    # Spawn `deer_2` if Ancestor has effect 13645 and no deer are active.
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=ancestor, special_effect=Effects.FirstDeerRequest)
    GotoIfCharacterHasSpecialEffect(
        Label.L0,
        character=all_deer,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(deer_2)
    EnableAI(deer_2)
    ForceSpawnerToSpawn(spawner=deer_spawner_2)
    WaitFrames(frames=1)
    AddSpecialEffect(deer_2, 13643)
    AddSpecialEffect(deer_2, Effects.AnimalActive)
    DisableAnimations(deer_2)
    Goto(Label.L20)

    # --- Label 0 --- #
    DefineLabel(0)

    # Spawn `boar_0` if Ancestor has effect 13646 and no boar are active.
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L1, character=ancestor, special_effect=Effects.FirstBoarRequest)
    SkipLinesIfCharacterHasSpecialEffect(
        8,
        character=all_boars,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(boar_0)
    EnableAI(boar_0)
    ForceSpawnerToSpawn(spawner=boar_spawner_0)
    WaitFrames(frames=1)
    AddSpecialEffect(boar_0, 13643)
    AddSpecialEffect(boar_0, Effects.AnimalActive)
    DisableAnimations(boar_0)
    Goto(Label.L20)

    # TODO: Code will never reach this "first Springhare" section.
    GotoIfCharacterHasSpecialEffect(
        Label.L1,
        character=all_springhares,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(springhare_0)
    EnableAI(springhare_0)
    ForceSpawnerToSpawn(spawner=springhare_spawner_0)
    WaitFrames(frames=1)
    AddSpecialEffect(springhare_0, 13643)
    AddSpecialEffect(springhare_0, Effects.AnimalActive)
    DisableAnimations(springhare_0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # Spawn `wild_mouflon_0` if Ancestor has effect 13647 and no deer are active.
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L2, character=ancestor, special_effect=Effects.FirstWildMouflonRequest)
    GotoIfCharacterHasSpecialEffect(
        Label.L2,
        character=all_wild_mouflons,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(wild_mouflon_0)
    EnableAI(wild_mouflon_0)
    ForceSpawnerToSpawn(spawner=wild_mouflon_spawner_0)
    WaitFrames(frames=1)
    AddSpecialEffect(wild_mouflon_0, 13643)
    AddSpecialEffect(wild_mouflon_0, Effects.AnimalActive)
    DisableAnimations(wild_mouflon_0)

    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagDisabled(spawn_animals_0_1_2):
        GotoIfFlagEnabled(Label.L3, flag=spawn_animals_3_4)
        GotoIfFlagEnabled(Label.L4, flag=spawn_animals_5_6)

    # Enable animals

    SkipLinesIfCharacterHasSpecialEffect(8, character=deer_0, special_effect=Effects.AnimalActive)
    EnableCharacter(deer_0)
    EnableAI(deer_0)
    ForceSpawnerToSpawn(spawner=deer_spawner_0)
    WaitFrames(frames=1)
    AddSpecialEffect(deer_0, 13643)
    AddSpecialEffect(deer_0, Effects.AnimalActive)
    DisableAnimations(deer_0)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=boar_0, special_effect=Effects.AnimalActive)
    EnableCharacter(boar_0)
    EnableAI(boar_0)
    ForceSpawnerToSpawn(spawner=boar_spawner_0)
    WaitFrames(frames=1)
    AddSpecialEffect(boar_0, 13643)
    AddSpecialEffect(boar_0, Effects.AnimalActive)
    DisableAnimations(boar_0)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=wild_mouflon_0, special_effect=Effects.AnimalActive)
    EnableCharacter(wild_mouflon_0)
    EnableAI(wild_mouflon_0)
    ForceSpawnerToSpawn(spawner=wild_mouflon_spawner_0)
    WaitFrames(frames=1)
    AddSpecialEffect(wild_mouflon_0, 13643)
    AddSpecialEffect(wild_mouflon_0, Effects.AnimalActive)
    DisableAnimations(wild_mouflon_0)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=springhare_0, special_effect=Effects.AnimalActive)
    EnableCharacter(springhare_0)
    EnableAI(springhare_0)
    ForceSpawnerToSpawn(spawner=springhare_spawner_0)
    WaitFrames(frames=1)
    AddSpecialEffect(springhare_0, 13643)
    AddSpecialEffect(springhare_0, Effects.AnimalActive)
    DisableAnimations(springhare_0)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=deer_1, special_effect=Effects.AnimalActive)
    EnableCharacter(deer_1)
    EnableAI(deer_1)
    ForceSpawnerToSpawn(spawner=deer_spawner_1)
    WaitFrames(frames=1)
    AddSpecialEffect(deer_1, 13643)
    AddSpecialEffect(deer_1, Effects.AnimalActive)
    DisableAnimations(deer_1)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=boar_1, special_effect=Effects.AnimalActive)
    EnableCharacter(boar_1)
    EnableAI(boar_1)
    ForceSpawnerToSpawn(spawner=boar_spawner_1)
    WaitFrames(frames=1)
    AddSpecialEffect(boar_1, 13643)
    AddSpecialEffect(boar_1, Effects.AnimalActive)
    DisableAnimations(boar_1)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=wild_mouflon_1, special_effect=Effects.AnimalActive)
    EnableCharacter(wild_mouflon_1)
    EnableAI(wild_mouflon_1)
    ForceSpawnerToSpawn(spawner=wild_mouflon_spawner_1)
    WaitFrames(frames=1)
    AddSpecialEffect(wild_mouflon_1, 13643)
    AddSpecialEffect(wild_mouflon_1, Effects.AnimalActive)
    DisableAnimations(wild_mouflon_1)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=springhare_1, special_effect=Effects.AnimalActive)
    EnableCharacter(springhare_1)
    EnableAI(springhare_1)
    ForceSpawnerToSpawn(spawner=springhare_spawner_1)
    WaitFrames(frames=1)
    AddSpecialEffect(springhare_1, 13643)
    AddSpecialEffect(springhare_1, Effects.AnimalActive)
    DisableAnimations(springhare_1)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=deer_2, special_effect=Effects.AnimalActive)
    EnableCharacter(deer_2)
    EnableAI(deer_2)
    ForceSpawnerToSpawn(spawner=deer_spawner_2)
    WaitFrames(frames=1)
    AddSpecialEffect(deer_2, 13643)
    AddSpecialEffect(deer_2, Effects.AnimalActive)
    DisableAnimations(deer_2)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=boar_2, special_effect=Effects.AnimalActive)
    EnableCharacter(boar_2)
    EnableAI(boar_2)
    ForceSpawnerToSpawn(spawner=boar_spawner_2)
    WaitFrames(frames=1)
    AddSpecialEffect(boar_2, 13643)
    AddSpecialEffect(boar_2, Effects.AnimalActive)
    DisableAnimations(boar_2)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=wild_mouflon_2, special_effect=Effects.AnimalActive)
    EnableCharacter(wild_mouflon_2)
    EnableAI(wild_mouflon_2)
    ForceSpawnerToSpawn(spawner=wild_mouflon_spawner_2)
    WaitFrames(frames=1)
    AddSpecialEffect(wild_mouflon_2, 13643)
    AddSpecialEffect(wild_mouflon_2, Effects.AnimalActive)
    DisableAnimations(wild_mouflon_2)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=springhare_2, special_effect=Effects.AnimalActive)
    EnableCharacter(springhare_2)
    EnableAI(springhare_2)
    ForceSpawnerToSpawn(spawner=springhare_spawner_2)
    WaitFrames(frames=1)
    AddSpecialEffect(springhare_2, 13643)
    AddSpecialEffect(springhare_2, Effects.AnimalActive)
    DisableAnimations(springhare_2)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)

    SkipLinesIfCharacterHasSpecialEffect(8, character=wild_mouflon_3, special_effect=Effects.AnimalActive)
    EnableCharacter(wild_mouflon_3)
    EnableAI(wild_mouflon_3)
    ForceSpawnerToSpawn(spawner=wild_mouflon_spawner_3)
    WaitFrames(frames=1)
    AddSpecialEffect(wild_mouflon_3, 13643)
    AddSpecialEffect(wild_mouflon_3, Effects.AnimalActive)
    DisableAnimations(wild_mouflon_3)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=deer_3, special_effect=Effects.AnimalActive)
    EnableCharacter(deer_3)
    EnableAI(deer_3)
    ForceSpawnerToSpawn(spawner=deer_spawner_3)
    WaitFrames(frames=1)
    AddSpecialEffect(deer_3, 13643)
    AddSpecialEffect(deer_3, Effects.AnimalActive)
    DisableAnimations(deer_3)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=springhare_3, special_effect=Effects.AnimalActive)
    EnableCharacter(springhare_3)
    EnableAI(springhare_3)
    ForceSpawnerToSpawn(spawner=springhare_spawner_3)
    WaitFrames(frames=1)
    AddSpecialEffect(springhare_3, 13643)
    AddSpecialEffect(springhare_3, Effects.AnimalActive)
    DisableAnimations(springhare_3)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=boar_3, special_effect=Effects.AnimalActive)
    EnableCharacter(boar_3)
    EnableAI(boar_3)
    ForceSpawnerToSpawn(spawner=boar_spawner_3)
    WaitFrames(frames=1)
    AddSpecialEffect(boar_3, 13643)
    AddSpecialEffect(boar_3, Effects.AnimalActive)
    DisableAnimations(boar_3)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=wild_mouflon_4, special_effect=Effects.AnimalActive)
    EnableCharacter(wild_mouflon_4)
    EnableAI(wild_mouflon_4)
    ForceSpawnerToSpawn(spawner=wild_mouflon_spawner_4)
    WaitFrames(frames=1)
    AddSpecialEffect(wild_mouflon_4, 13643)
    AddSpecialEffect(wild_mouflon_4, Effects.AnimalActive)
    DisableAnimations(wild_mouflon_4)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=deer_4, special_effect=Effects.AnimalActive)
    EnableCharacter(deer_4)
    EnableAI(deer_4)
    ForceSpawnerToSpawn(spawner=deer_spawner_4)
    WaitFrames(frames=1)
    AddSpecialEffect(deer_4, 13643)
    AddSpecialEffect(deer_4, Effects.AnimalActive)
    DisableAnimations(deer_4)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=springhare_4, special_effect=Effects.AnimalActive)
    EnableCharacter(springhare_4)
    EnableAI(springhare_4)
    ForceSpawnerToSpawn(spawner=springhare_spawner_4)
    WaitFrames(frames=1)
    AddSpecialEffect(springhare_4, 13643)
    AddSpecialEffect(springhare_4, Effects.AnimalActive)
    DisableAnimations(springhare_4)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=boar_4, special_effect=Effects.AnimalActive)
    EnableCharacter(boar_4)
    EnableAI(boar_4)
    ForceSpawnerToSpawn(spawner=boar_spawner_4)
    WaitFrames(frames=1)
    AddSpecialEffect(boar_4, 13643)
    AddSpecialEffect(boar_4, Effects.AnimalActive)
    DisableAnimations(boar_4)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfCharacterHasSpecialEffect(8, character=springhare_5, special_effect=Effects.AnimalActive)
    EnableCharacter(springhare_5)
    EnableAI(springhare_5)
    ForceSpawnerToSpawn(spawner=springhare_spawner_5)
    WaitFrames(frames=1)
    AddSpecialEffect(springhare_5, 13643)
    AddSpecialEffect(springhare_5, Effects.AnimalActive)
    DisableAnimations(springhare_5)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=wild_mouflon_5, special_effect=Effects.AnimalActive)
    EnableCharacter(wild_mouflon_5)
    EnableAI(wild_mouflon_5)
    ForceSpawnerToSpawn(spawner=wild_mouflon_spawner_5)
    WaitFrames(frames=1)
    AddSpecialEffect(wild_mouflon_5, 13643)
    AddSpecialEffect(wild_mouflon_5, Effects.AnimalActive)
    DisableAnimations(wild_mouflon_5)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=boar_5, special_effect=Effects.AnimalActive)
    EnableCharacter(boar_5)
    EnableAI(boar_5)
    ForceSpawnerToSpawn(spawner=boar_spawner_5)
    WaitFrames(frames=1)
    AddSpecialEffect(boar_5, 13643)
    AddSpecialEffect(boar_5, Effects.AnimalActive)
    DisableAnimations(boar_5)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=deer_5, special_effect=Effects.AnimalActive)
    EnableCharacter(deer_5)
    EnableAI(deer_5)
    ForceSpawnerToSpawn(spawner=deer_spawner_5)
    WaitFrames(frames=1)
    AddSpecialEffect(deer_5, 13643)
    AddSpecialEffect(deer_5, Effects.AnimalActive)
    DisableAnimations(deer_5)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=springhare_6, special_effect=Effects.AnimalActive)
    EnableCharacter(springhare_6)
    EnableAI(springhare_6)
    ForceSpawnerToSpawn(spawner=springhare_spawner_6)
    WaitFrames(frames=1)
    AddSpecialEffect(springhare_6, 13643)
    AddSpecialEffect(springhare_6, Effects.AnimalActive)
    DisableAnimations(springhare_6)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=wild_mouflon_6, special_effect=Effects.AnimalActive)
    EnableCharacter(wild_mouflon_6)
    EnableAI(wild_mouflon_6)
    ForceSpawnerToSpawn(spawner=wild_mouflon_spawner_6)
    WaitFrames(frames=1)
    AddSpecialEffect(wild_mouflon_6, 13643)
    AddSpecialEffect(wild_mouflon_6, Effects.AnimalActive)
    DisableAnimations(wild_mouflon_6)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=boar_6, special_effect=Effects.AnimalActive)
    EnableCharacter(boar_6)
    EnableAI(boar_6)
    ForceSpawnerToSpawn(spawner=boar_spawner_6)
    WaitFrames(frames=1)
    AddSpecialEffect(boar_6, 13643)
    AddSpecialEffect(boar_6, Effects.AnimalActive)
    DisableAnimations(boar_6)
    Goto(Label.L20)

    SkipLinesIfCharacterHasSpecialEffect(8, character=deer_6, special_effect=Effects.AnimalActive)
    EnableCharacter(deer_6)
    EnableAI(deer_6)
    ForceSpawnerToSpawn(spawner=deer_spawner_6)
    WaitFrames(frames=1)
    AddSpecialEffect(deer_6, 13643)
    AddSpecialEffect(deer_6, Effects.AnimalActive)
    DisableAnimations(deer_6)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)

    EnableFlag(request_animal_recount_flag)

    # If too many animals have effect 13643, enable 'do not spawn' flag and remove 13643 from all of them.
    # The max animal count varies depending on three flags passed in.
    AND_10.Add(FlagEnabled(six_animal_max_flag))
    AND_10.Add(CharacterHasSpecialEffect(
        all_animals,
        13643,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=6.0,
    ))
    AND_11.Add(FlagEnabled(eight_animal_max_flag))
    AND_11.Add(CharacterHasSpecialEffect(
        all_animals,
        13643,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=8.0,
    ))
    AND_12.Add(FlagEnabled(ten_animal_max_flag))
    AND_12.Add(CharacterHasSpecialEffect(
        all_animals,
        13643,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=10.0,
    ))
    OR_10.Add(AND_10)
    OR_10.Add(AND_11)
    OR_10.Add(AND_12)
    SkipLinesIfConditionFalse(2, OR_10)
    EnableFlag(do_not_spawn_flag)
    RemoveSpecialEffect(all_animals, 13643)

    Restart()


@RestartOnRest(12092860)
def AncestorAnimalEffectCheck(
    _,
    request_flag: uint,
    ancestor_spirit: uint,
    deer_group: uint,
    boar_group: uint,
    wild_mouflon_group: uint,
    springhare_group: uint,
    animal_group: uint,
):
    """Event 12092860"""
    DisableFlag(request_flag)
    
    MAIN.Await(FlagEnabled(request_flag))
    
    AND_1.Add(CharacterHasSpecialEffect(deer_group, Effects.AnimalActive, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_1)
    AddSpecialEffect(ancestor_spirit, Effects.Ancestor_NoDeerActive)
    SkipLines(1)
    RemoveSpecialEffect(ancestor_spirit, Effects.Ancestor_NoDeerActive)

    AND_2.Add(CharacterHasSpecialEffect(boar_group, Effects.AnimalActive, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_2)
    AddSpecialEffect(ancestor_spirit, Effects.Ancestor_NoBoarsActive)
    SkipLines(1)
    RemoveSpecialEffect(ancestor_spirit, Effects.Ancestor_NoBoarsActive)

    AND_3.Add(CharacterHasSpecialEffect(wild_mouflon_group, Effects.AnimalActive, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_3)
    AddSpecialEffect(ancestor_spirit, Effects.Ancestor_NoWildMouflonsActive)
    SkipLines(1)
    RemoveSpecialEffect(ancestor_spirit, Effects.Ancestor_NoWildMouflonsActive)

    AND_4.Add(CharacterHasSpecialEffect(springhare_group, Effects.AnimalActive, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_4)
    AddSpecialEffect(ancestor_spirit, Effects.Ancestor_NoSpringharesActive)
    SkipLines(1)
    RemoveSpecialEffect(ancestor_spirit, Effects.Ancestor_NoSpringharesActive)

    AND_5.Add(CharacterHasSpecialEffect(
        animal_group,
        Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=5.0,
    ))
    SkipLinesIfConditionTrue(2, AND_5)
    AddSpecialEffect(ancestor_spirit, Effects.Ancestor_LessThanFiveAnimalsActive)
    SkipLines(1)
    RemoveSpecialEffect(ancestor_spirit, Effects.Ancestor_LessThanFiveAnimalsActive)

    DisableFlag(Flags.ProjectileRequest_LowAnimalCount)
    DisableFlag(Flags.ProjectileRequest_MediumAnimalCount)
    DisableFlag(Flags.ProjectileRequest_HighAnimalCount)
    SkipLinesIfCharacterHasSpecialEffect(
        3,
        character=animal_group,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=20,
    )
    SkipLinesIfCharacterHasSpecialEffect(
        4,
        character=animal_group,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=13,
    )
    SkipLinesIfCharacterHasSpecialEffect(
        5,
        character=animal_group,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    SkipLines(5)
    EnableFlag(Flags.ProjectileRequest_HighAnimalCount)
    SkipLines(3)
    EnableFlag(Flags.ProjectileRequest_MediumAnimalCount)
    SkipLines(1)
    EnableFlag(Flags.ProjectileRequest_LowAnimalCount)
    Restart()


@RestartOnRest(12092861)
def AncestorReactivates(_, ancestor_spirit: uint):
    """Event 12092861"""
    MAIN.Await(CharacterHasSpecialEffect(ancestor_spirit, Effects.Ancestor_Reactivate))
    
    EnableAnimations(ancestor_spirit)
    ReplanAI(ancestor_spirit)
    Restart()


@RestartOnRest(Flags.AncestorFirstAnimalLifeDrainDone)
def AncestorFirstAnimalLifeDrain(_, ancestor_spirit: uint, all_animals: uint):
    """I think this is the healing effect. I didn't realize it killed ALL animals, though."""
    MAIN.Await(CharacterHasSpecialEffect(ancestor_spirit, Effects.Ancestor_AnimalLifeDrainRequest))
    
    AddSpecialEffect(ancestor_spirit, Effects.Ancestor_FirstHeal)
    AddSpecialEffect(ancestor_spirit, Effects.FirstBoarRequest)
    AddSpecialEffect(all_animals, Effects.AnimalDrained)
    Kill(all_animals)
    Wait(1.0)
    EnableThisSlotFlag()
    EnableFlag(Flags.AncestorInPhaseTwo)


@RestartOnRest(Flags.AncestorSecondAnimalLifeDrainDone)
def AncestorSecondAnimalLifeDrain(_, ancestor_spirit: uint, animal_group: uint, first_life_drain_done_flag: uint):
    """Event Flags.AncestorSecondAnimalLifeDrainDone"""
    AND_1.Add(FlagEnabled(first_life_drain_done_flag))
    AND_1.Add(CharacterHasSpecialEffect(ancestor_spirit, Effects.Ancestor_AnimalLifeDrainRequest))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(ancestor_spirit, Effects.Ancestor_SecondHeal)
    AddSpecialEffect(ancestor_spirit, Effects.FirstWildMouflonRequest)
    AddSpecialEffect(animal_group, Effects.AnimalDrained)
    Kill(animal_group)
    Wait(1.0)
    EnableThisSlotFlag()


@RestartOnRest(12092864)
def AncestorThirdPlusAnimalLifeDrain(
    _,
    ancestor_spirit: uint,
    animal_group: uint,
    first_life_drain_done_flag: uint,
    second_life_drain_done_flag: uint,
):
    """Event 12092864"""
    AND_1.Add(FlagEnabled(first_life_drain_done_flag))
    AND_1.Add(FlagEnabled(second_life_drain_done_flag))
    AND_1.Add(CharacterHasSpecialEffect(ancestor_spirit, Effects.Ancestor_AnimalLifeDrainRequest))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(ancestor_spirit, Effects.Ancestor_ThirdPlusHeal)
    AddSpecialEffect(animal_group, Effects.AnimalDrained)
    Kill(animal_group)
    Wait(1.0)
    Restart()  # I don't think this can actually repeat (probably in AI).


@RestartOnRest(12092865)
def AncestorLifeDrainProjectiles(_, ancestor_spirit: uint):
    """Event 12092865"""
    MAIN.Await(CharacterHasSpecialEffect(ancestor_spirit, Effects.Ancestor_AnimalLifeDrainRequest))
    
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092300,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092301,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092302,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092303,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092304,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092305,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092306,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092307,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092308,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092309,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092310,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092311,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092312,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092313,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092314,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092315,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092316,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092317,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092318,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092319,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092320,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092321,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092322,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092323,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092324,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092325,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092326,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092327,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092328,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092329,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092330,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092331,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092332,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092333,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092334,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092335,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092336,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092337,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092338,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092339,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092340,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092341,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092342,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092343,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092344,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092345,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092346,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092347,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092348,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092349,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileOwner,
        source_entity=12092350,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Restart()


@RestartOnRest(12092910)
def CreateAncestorProjectileOwner(_, projectile_dummy: uint):
    """Event 12092910"""
    CreateProjectileOwner(entity=projectile_dummy)


@RestartOnRest(12092920)
def RequestAncestorProjectile(_, request_animal_count_flag: uint, owner_entity: uint, source_entity: uint):
    """Event 12092920"""
    SkipLinesIfUnsignedEqual(2, left=request_animal_count_flag, right=Flags.ProjectileRequest_MediumAnimalCount)
    SkipLinesIfUnsignedEqual(2, left=request_animal_count_flag, right=Flags.ProjectileRequest_HighAnimalCount)
    OR_1.Add(FlagEnabled(Flags.ProjectileRequest_LowAnimalCount))
    OR_1.Add(FlagEnabled(Flags.ProjectileRequest_MediumAnimalCount))
    OR_1.Add(FlagEnabled(Flags.ProjectileRequest_HighAnimalCount))
    AND_1.Add(CharacterAlive(Characters.RegalAncestorSpirit))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=246700900,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # Wait less time before restarting if more animals are active.
    SkipLinesIfFlagEnabled(3, Flags.ProjectileRequest_MediumAnimalCount)
    SkipLinesIfFlagEnabled(4, Flags.ProjectileRequest_HighAnimalCount)
    WaitRandomSeconds(min_seconds=8.0, max_seconds=10.0)
    SkipLines(3)
    WaitRandomSeconds(min_seconds=6.0, max_seconds=8.0)
    SkipLines(1)
    WaitRandomSeconds(min_seconds=4.0, max_seconds=6.0)
    Restart()
