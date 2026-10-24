from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle



class PortAccessRules(Choice):
    """
    How to unlock access to ports.
    Currently only one option
    Port Access: locks each individual port. Will require you to have an appropriate "Port Access" item to unlock it.
    *future*
    Sea Zone Access: locks ports by what sea zone they are in, e.g. "Sea Zone Access: Frozen North"
    Sea Zone and Port Access: require both to unlock any port.
    """
    #writing that made me realize the current system won't work for Sea Zone access, I'll need to make outgoing sea zones for it to work.

    display_name = "Port Access Rules"

    port_access = 0

    default = port_access

class EquipmentRequired(Toggle):
    """
    Most monsters can be defeated with the basic gun and ship with a bit of caution and a lot of patients.
    However, that's not a fair thing to ask, so here's a toggle for that.
    """

    display_name = "Equipment Required"

class ShuffleNephriteRing(Toggle):
    """
    Determines whether to shuffle nephrite ring or not.
    If not shuffled, you will start with it to help me with logic
    """

    display_name = "Shuffle Nephrite Ring"

class ShuffleOfficers(Toggle):
    """
    Determines whether to officers or not.
    """
    #Maybe I should have worried about this later? fuck

    display_name = "Shuffle Officers"

class OfficerQuests(Toggle):
    """
    Determines whether officer quests are locations or not.
    *just the starter officers for now (from the backgrounds) to keep it simple*
    """

    display_name = "Officer Quests"

class TradeQuests(Toggle):
    """
    Determines whether "Trade Quests" are locations or not.
    Just merchant venturer for now, and if I do add more I'll probably separate them into different options.
    """

    display_name = "Trade Quests"

#That's all the option's I believe
@dataclass
class SunlessSeaOptions(PerGameCommonOptions):
    port_access_rules: PortAccessRules
    equipment_required: EquipmentRequired
    shuffle_nephrite_ring: ShuffleNephriteRing
    shuffle_officers: ShuffleOfficers
    officer_quests: OfficerQuests
    trade_quest: TradeQuests

option_groups = [
    OptionGroup(
        "Access Rules",
        [PortAccessRules, EquipmentRequired],
    ),
    OptionGroup(
        "Additional locations",
        [ShuffleNephriteRing, ShuffleOfficers, OfficerQuests, TradeQuests],
    ),
]

option_presets = {
    "Basic": {
        "port_access_rules": 0,
        "equipment_required": True,
        "shuffle_nephrite_ring": True,
        "shuffle_officers": True,
        "officer_quests": True,
        "trade_quest": True,
    },
}