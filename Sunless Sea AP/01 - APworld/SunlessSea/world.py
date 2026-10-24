from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as sunlesssea_options

class SunlessSeaWorld(World):
    """
    Sunless Sea is part text based narrative, part boat exploration and resource management
    Wrapped in a gothic horror setting where Victorian London was dragged into the underground.
    """

    Game = "SunlessSea"

    web = web_world.SunlessSeaWebWorld()

    options_dataclass = sunlesssea_options.SunlessSeaOptions
    options: sunlesssea_options.SunlessSeaOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Fallen London"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.SunlessSeaItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "port_access_rules", "shuffle_nephrite_ring", "shuffle_officers", "officer_quests", "trade_quest"
        )