"""DONE
Sellia Hideaway

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
from .entities.m31_11_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31110000, asset=Assets.AEG099_060_9000)
    Event_31112800()
    Event_31112801(0, Characters.Crystalian0)
    Event_31112801(1, Characters.Crystalian1)
    Event_31112801(2, Characters.Crystalian2)
    Event_31112801(3, Characters.CLONE_Crystalian0)
    Event_31112801(4, Characters.CLONE_Crystalian1)
    Event_31112801(5, Characters.CLONE_Crystalian2)
    Event_31112810()
    Event_31112811()
    SwapCrystalianHealthBar(0, Characters.Crystalian0, Characters.Crystalian0, NameText.Crystalian0,
                            NameText.CLONE_Crystalian0, 0)
    SwapCrystalianHealthBar(1, Characters.Crystalian1, Characters.Crystalian1, NameText.Crystalian1,
                            NameText.CLONE_Crystalian1, 1)
    SwapCrystalianHealthBar(2, Characters.Crystalian2, Characters.Crystalian2, NameText.Crystalian2,
                            NameText.CLONE_Crystalian2, 2)
    Event_31112849()

    CommonFunc_90005646(
        0,
        flag=31110800,
        left_flag=31112840,
        cancel_flag__right_flag=31112841,
        asset=Assets.AEG099_065_9000,
        player_start=31112840,
        area_id=31,
        block_id=11,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_91005600(0, flag=31112800, asset=31111695, model_point=5)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005525(0, flag=31110600, asset=Assets.AEG027_069_1000)
    CommonFunc_90005525(0, flag=31110601, asset=Assets.AEG027_069_1001)
    CommonFunc_90005525(0, flag=31110602, asset=31111602)
    CommonFunc_90005525(0, flag=31110603, asset=Assets.AEG027_069_1003)
    Event_31112400()
    Event_31113700(0, 31110700)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.GlintstoneMiner0,
        animation_id=30006,
        animation_id_1=20006,
        region=31112200,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.GlintstoneMiner1,
        animation_id=30003,
        animation_id_1=20003,
        region=31112201,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.GlintstoneMiner2,
        animation_id=30001,
        animation_id_1=20001,
        region=31112202,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.GlintstoneMiner3,
        region=31112208,
        radius=2.0,
        seconds=0.0,
        animation_id=1707,
    )
    Event_31112208()
    Event_31112250(
        0,
        character=Characters.GlintstoneMiner4,
        region=31112209,
        radius=5.0,
        seconds=0.0,
        animation_id=3031,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=31110210,
        animation_id=30002,
        animation_id_1=20002,
        region=31112210,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.GlintstoneMiner5,
        animation_id=30007,
        animation_id_1=20007,
        region=31112213,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=31110215, region=31112215, radius=2.0, seconds=0.0,
                                                 animation_id=0)
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.GlintstoneMiner6,
        animation_id=30002,
        animation_id_1=20002,
        region=31112216,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=31110217,
        animation_id=30002,
        animation_id_1=20002,
        region=31112217,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.GlintstoneMiner7,
        animation_id=30004,
        animation_id_1=20004,
        region=31112223,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.RayaLucariaScholar0,
        region=31112280,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.RayaLucariaScholar1,
        region=31112285,
        radius=2.0,
        seconds=3.0,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.RayaLucariaScholar3,
        region=31112285,
        radius=2.0,
        seconds=3.5,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Snail0, region=31112240, radius=2.0,
                                                 seconds=0.0, animation_id=0)
    Event_31112250(1, character=Characters.Snail1, region=31112241, radius=3.0, seconds=0.0, animation_id=3011)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Snail2, region=31112240, radius=2.0,
                                                 seconds=0.0, animation_id=0)
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.Snail3,
        inactive_animation=30001,
        active_animation=20001,
        radius=8.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.Snail4,
        inactive_animation=30001,
        active_animation=20001,
        radius=10.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.Snail5,
        inactive_animation=30001,
        active_animation=20001,
        radius=10.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    Event_31112250(2, character=Characters.Snail6, region=31112251, radius=2.0, seconds=0.0, animation_id=3011)
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.Snail7,
        animation_id=30000,
        animation_id_1=20000,
        region=31112256,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.Snail8,
        animation_id=30000,
        animation_id_1=20000,
        region=31112256,
        radius=1.0,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Snail9, region=31112300, radius=2.0,
                                                 seconds=0.0, animation_id=0)
    Event_31112240(0, character=Characters.Snail9)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Snail10, region=31112262, radius=2.0,
                                                 seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Snail11, region=31112262, radius=2.0,
                                                 seconds=0.0, animation_id=0)
    Event_31112245(0, character=Characters.Snail10)
    Event_31112245(1, character=Characters.Snail11)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Revenant, region=31112300, radius=2.0,
                                                 seconds=0.0, animation_id=0)
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(0, 31110310, 30006, 20006, 31112213, 2.0, 1.0, 0, 0, 0, 0)


@RestartOnRest(31112208)
def Event_31112208():
    """Event 31112208"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(Characters.GlintstoneMiner3, 8081)
    AddSpecialEffect(Characters.GlintstoneMiner3, 8082)
    AddSpecialEffect(Characters.GlintstoneMiner3, 5000)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=Characters.GlintstoneMiner3, other_entity=PLAYER, radius=4.0))
    AND_4.Add(CharacterHasSpecialEffect(Characters.GlintstoneMiner3, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90160))
    AND_5.Add(CharacterHasSpecialEffect(Characters.GlintstoneMiner3, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90162))
    AND_6.Add(CharacterHasSpecialEffect(Characters.GlintstoneMiner3, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90161))
    AND_7.Add(CharacterHasSpecialEffect(Characters.GlintstoneMiner3, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.GlintstoneMiner3, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.GlintstoneMiner3, 90160))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(Characters.GlintstoneMiner3, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.GlintstoneMiner3))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GlintstoneMiner3, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GlintstoneMiner3, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GlintstoneMiner3, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GlintstoneMiner3, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GlintstoneMiner3, state_info=260))
    OR_2.Add(CharacterInsideRegion(character=Characters.GlintstoneMiner3, region=31112207))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)

    MAIN.Await(OR_2)

    RemoveSpecialEffect(Characters.GlintstoneMiner3, 8081)
    RemoveSpecialEffect(Characters.GlintstoneMiner3, 8082)
    RemoveSpecialEffect(Characters.GlintstoneMiner3, 5000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31112240)
def Event_31112240(_, character: uint):
    """Event 31112240"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=6.0))
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)

    MAIN.Await(OR_2)

    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31112245)
def Event_31112245(_, character: uint):
    """Event 31112245"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=character, region=31112263))
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)

    MAIN.Await(OR_2)

    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31112250)
def Event_31112250(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31112250"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)

    MAIN.Await(OR_2)

    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(31112310)
def Event_31112310(_, character: uint):
    """Event 31112310"""
    AddSpecialEffect(character, 8087)


@RestartOnRest(31112301)
def Event_31112301():
    """Event 31112301"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(31110301, 8081)
    AddSpecialEffect(31110301, 8082)
    AddSpecialEffect(31110301, 5000)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=31110301, other_entity=PLAYER, radius=4.0))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(31110301, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=31110301))

    MAIN.Await(OR_2)

    RemoveSpecialEffect(31110301, 8081)
    RemoveSpecialEffect(31110301, 8082)
    RemoveSpecialEffect(31110301, 5000)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@ContinueOnRest(31112400)
def Event_31112400():
    """Event 31112400"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=31118700)
    DisableAsset(Assets.AEG099_264_1000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9533, entity=Assets.AEG099_264_1000))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(31118700))

    MAIN.Await(OR_1)

    GotoIfFlagEnabled(Label.L9, flag=31118700)
    AND_2.Add(PlayerHasGood(8169))
    GotoIfConditionTrue(Label.L3, input_condition=AND_2)
    DisplayDialog(text=30080, anchor_entity=Assets.AEG099_264_1000)
    Wait(1.399999976158142)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(PLAYER, 60010)
    Wait(2.799999952316284)
    DisplayDialog(text=208169, anchor_entity=Assets.AEG099_264_1000)

    # --- Label 9 --- #
    DefineLabel(9)
    ForceAnimation(Assets.AEG099_264_1000, 1)
    EnableNetworkFlag(31118700)


@RestartOnRest(31112800)
def Event_31112800():
    """Event 31112800"""
    if FlagEnabled(31110800):
        return
    AND_1.Add(CharacterDead(Characters.Crystalian0))
    AND_1.Add(CharacterDead(Characters.Crystalian1))
    AND_1.Add(CharacterDead(Characters.Crystalian2))
    AND_1.Add(CharacterDead(Characters.CLONE_Crystalian0))
    AND_1.Add(CharacterDead(Characters.CLONE_Crystalian1))
    AND_1.Add(CharacterDead(Characters.CLONE_Crystalian2))

    MAIN.Await(AND_1)

    Wait(3.0)
    KillBossAndDisplayBanner(character=Characters.Crystalian0, banner_type=BannerType.EnemyFelled)
    EnableFlag(31110800)
    EnableFlag(9246)
    if PlayerInOwnWorld():
        EnableFlag(61246)


@RestartOnRest(31112801)
def Event_31112801(_, crystalian: uint):
    """Event 31112801"""
    if FlagEnabled(31110800):
        return

    MAIN.Await(HealthValue(crystalian) <= 0)

    Wait(4.0)
    PlaySoundEffect(crystalian, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31112810)
def Event_31112810():
    """Event 31112810"""
    GotoIfFlagDisabled(Label.L0, flag=31110800)
    DisableCharacter(Characters.Crystalian0)
    DisableCharacter(Characters.Crystalian1)
    DisableCharacter(Characters.Crystalian2)
    DisableAnimations(Characters.Crystalian0)
    DisableAnimations(Characters.Crystalian1)
    DisableAnimations(Characters.Crystalian2)
    Kill(Characters.Crystalian0)
    Kill(Characters.Crystalian1)
    Kill(Characters.Crystalian2)
    DisableCharacter(Characters.CLONE_Crystalian0)
    DisableCharacter(Characters.CLONE_Crystalian1)
    DisableCharacter(Characters.CLONE_Crystalian2)
    DisableAnimations(Characters.CLONE_Crystalian0)
    DisableAnimations(Characters.CLONE_Crystalian1)
    DisableAnimations(Characters.CLONE_Crystalian2)
    Kill(Characters.CLONE_Crystalian0)
    Kill(Characters.CLONE_Crystalian1)
    Kill(Characters.CLONE_Crystalian2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Crystalian0)
    DisableAI(Characters.Crystalian1)
    DisableAI(Characters.Crystalian2)
    DisableAI(Characters.CLONE_Crystalian0)
    DisableAI(Characters.CLONE_Crystalian1)
    DisableAI(Characters.CLONE_Crystalian2)
    ForceAnimation(Characters.Crystalian0, 30001)
    ForceAnimation(Characters.Crystalian1, 30001)
    ForceAnimation(Characters.Crystalian2, 30000)
    ForceAnimation(Characters.CLONE_Crystalian0, 30001)
    ForceAnimation(Characters.CLONE_Crystalian1, 30001)
    ForceAnimation(Characters.CLONE_Crystalian2, 30000)
    AND_2.Add(FlagEnabled(31112805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31112800))

    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Crystalian0)
    EnableAI(Characters.Crystalian1)
    EnableAI(Characters.Crystalian2)
    EnableAI(Characters.CLONE_Crystalian0)
    EnableAI(Characters.CLONE_Crystalian1)
    EnableAI(Characters.CLONE_Crystalian2)
    SetNetworkUpdateRate(Characters.Crystalian0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.Crystalian1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.Crystalian2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_Crystalian0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_Crystalian1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_Crystalian2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Crystalian0, name=903350313)
    EnableBossHealthBar(Characters.Crystalian1, name=903350312, bar_slot=1)
    EnableBossHealthBar(Characters.Crystalian2, name=903350314, bar_slot=2)
    EnableBossHealthBar(Characters.CLONE_Crystalian0, name=NameText.Crystalian0)
    EnableBossHealthBar(Characters.CLONE_Crystalian1, name=NameText.Crystalian1, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_Crystalian2, name=NameText.Crystalian2, bar_slot=2)
    ForceAnimation(Characters.Crystalian0, 20001)
    ForceAnimation(Characters.Crystalian1, 20001)
    ForceAnimation(Characters.Crystalian2, 20000)
    ForceAnimation(Characters.CLONE_Crystalian0, 20001)
    ForceAnimation(Characters.CLONE_Crystalian1, 20001)
    ForceAnimation(Characters.CLONE_Crystalian2, 20000)

    EnableFlag(31112812)  # allow bar swapping


@RestartOnRest(31112811)
def Event_31112811():
    """Event 31112811"""
    if FlagEnabled(31110800):
        return
    OR_15.Add(CharacterDead(Characters.Crystalian0))
    OR_15.Add(CharacterDead(Characters.Crystalian1))
    OR_15.Add(CharacterDead(Characters.Crystalian2))
    OR_15.Add(CharacterDead(Characters.CLONE_Crystalian0))
    OR_15.Add(CharacterDead(Characters.CLONE_Crystalian1))
    OR_15.Add(CharacterDead(Characters.CLONE_Crystalian2))

    MAIN.Await(OR_15)

    EnableFlag(31112842)


@RestartOnRest(31112812)
def SwapCrystalianHealthBar(_, original: uint, clone: uint, original_name: int, clone_name: int, bar_slot: short):
    """Swap health bar between Crystalian and its clone to last one hit."""
    if FlagEnabled(31110800):
        return  # dead

    OR_1.Add(FlagEnabled(31110800))
    AND_1.Add(FlagEnabled(31112812))  # battle started
    AND_1.Add(AttackedWithDamageType(clone))
    OR_1.Add(AND_1)
    MAIN.Await(OR_1)

    if FlagEnabled(31110800):
        return

    EnableBossHealthBar(clone, clone_name, bar_slot)

    OR_2.Add(FlagEnabled(31110800))
    AND_2.Add(FlagEnabled(31112812))  # battle started
    AND_2.Add(AttackedWithDamageType(original))
    OR_2.Add(AND_2)
    MAIN.Await(OR_2)

    if FlagEnabled(31110800):
        return

    EnableBossHealthBar(original, original_name, bar_slot)

    return RESTART


@RestartOnRest(31112849)
def Event_31112849():
    """Event 31112849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=31110800,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=31112800,
        host_entered_fog_flag=31112805,
        boss_characters=31115800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=31110800,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=31112800,
        host_entered_fog_flag=31112805,
        summon_entered_fog_flag=31112806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=31110800, fog_asset=Assets.AEG099_002_9000, model_point=5,
                              required_flag=0)
    CommonFunc_ControlBossMusic(0, 31110800, 931000, 31112805, 31112806, 0, 31112842, 0, 0)


@RestartOnRest(31113700)
def Event_31113700(_, character: uint):
    """Event 31113700"""
    if PlayerNotInOwnWorld():
        return
    DisableCharacter(character)
    DisableBackread(character)
    if FlagEnabled(400431):
        return
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    DisableHealthBar(character)
    OR_1.Add(FlagEnabled(1044369228))
    OR_1.Add(FlagEnabled(14009263))
    AND_1.Add(FlagEnabled(14009267))
    AND_1.Add(OR_1)
    AwaitConditionTrue(AND_1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableImmortality(character)
    End()
