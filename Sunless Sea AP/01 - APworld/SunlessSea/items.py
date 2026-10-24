from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import SunlessSeaWorld

ITEM_NAME_TO_ID = {
    "Abbey Rock: Port Access": 2,
    "Adam's Way: Port Access": 3,
    "Aestival: Port Access": 4,
    "Avid Horizon: Port Access": 5,
    "Chapel of Lights: Port Access": 6,
    "The Chelonate: Port Access": 7,
    "Codex: Port Access": 8,
    "Cumaean Canal: Port Access": 9,
    "Demeaux Island: Port Access": 10,
    "Empire of Hands: Port Access": 11,
    "The Fathomking's Hold: Port Access": 12,
    "Frostfound: Port Access": 13,
    "Gaider's Mourn: Port Access": 14,
    "Godfall: Port Access": 15,
    "Grand Geode: Port Access": 16,
    "Hunter's Keep: Port Access": 17,
    "Irem: Port Access": 18,
    "Iron Republic: Port Access": 19,
    "Isle of Cats: Port Access": 20,
    "Khan's Heart: Port Access": 21,
    "Khan's Shadow: Port Access": 22,
    "Kingeater's Castle: Port Access": 23,
    "Mangrove College: Port Access": 24,
    "Mt Palmerston: Port Access": 25,
    "Nuncio: Port Access": 26,
    "Pigmote Isle: Port Access": 27,
    "Polythreme: Port Access": 28,
    "Port Carnelian: Port Access": 29,
    "Port Cecil: Port Access": 30,
    "Quaker's Haven: Port Access": 31,
    "Salt Lions: Port Access": 32,
    "Saviour's Rocks: Port Access": 33,
    "Shepherd Isles: Port Access": 34,
    "Station III: Port Access": 35,
    "The Uttershroom: Port Access": 36,
    "Varchas: Port Access": 37,
    "Venderbight: Port Access": 38,
    "Visage: Port Access": 39,
    "Whither: Port Access": 40,
    "Wisdom: Port Access": 41,

    "Progressive Deck Gun Deed": 60,
    "Progressive Forward Gun Deed": 61,
    "Progressive Rear Gun Deed": 62,
    "Progressive Engine Deed": 63,
    "Progressive Lamp Deed": 64,
    "Progressive Ship Deed": 65,

    "Nephrite Ring": 70,

    "100 Echoes": 101,
    "1000 Echoes": 103,

    # forgot to add the crewmates
    "Officer: Genial Magician": 200,
    "Officer: Brisk Campaigner": 210,
    "Officer: Presbyterate Adventuress": 220,
    "Officer: Tireless Mechanic": 230,
    "Officer: Carnelian Exile": 240,
    "Officer: Irrepressible Cannoneer": 250,
    "Officer: Maybe's Daughter": 260,
    "Officer: Nacreous Outcast": 270,
    "Officer: Haunted Doctor": 280,
    "Officer: Sigil-Ridden Navigator": 290,
    "Officer: Bandaged Poissonnier": 300,

    "Officer: Monkey Foundling": 350,
    "Officer: Eyeless Skull": 351,
    "Officer: Elegiac Cockatoo": 352,
    "Officer: Albino Tinkerer": 353,
    "Officer: Guinea Page": 354,
    "Officer: Vigilant Idol": 355,
    "Officer: Wretched Mog": 356,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Abbey Rock: Port Access": ItemClassification.progression,
    "Adam's Way: Port Access": ItemClassification.progression,
    "Aestival: Port Access": ItemClassification.progression,
    "Avid Horizon: Port Access": ItemClassification.progression,
    "Chapel of Lights: Port Access": ItemClassification.progression,
    "The Chelonate: Port Access": ItemClassification.progression,
    "Codex: Port Access": ItemClassification.progression,
    "Cumaean Canal: Port Access": ItemClassification.progression,
    "Demeaux Island: Port Access": ItemClassification.progression,
    "Empire of Hands: Port Access": ItemClassification.progression,
    "The Fathomking's Hold: Port Access": ItemClassification.progression,
    "Frostfound: Port Access": ItemClassification.progression,
    "Gaider's Mourn: Port Access": ItemClassification.progression,
    "Godfall: Port Access": ItemClassification.progression,
    "Grand Geode: Port Access": ItemClassification.progression,
    "Hunter's Keep: Port Access": ItemClassification.progression,
    "Irem: Port Access": ItemClassification.progression,
    "Iron Republic: Port Access": ItemClassification.progression,
    "Isle of Cats: Port Access": ItemClassification.progression,
    "Khan's Heart: Port Access": ItemClassification.progression,
    "Khan's Shadow: Port Access": ItemClassification.progression,
    "Kingeater's Castle: Port Access": ItemClassification.progression,
    "Mangrove College: Port Access": ItemClassification.progression,
    "Mt Palmerston: Port Access": ItemClassification.progression,
    "Nuncio: Port Access": ItemClassification.progression,
    "Pigmote Isle: Port Access": ItemClassification.progression,
    "Polythreme: Port Access": ItemClassification.progression,
    "Port Carnelian: Port Access": ItemClassification.progression,
    "Port Cecil: Port Access": ItemClassification.progression,
    "Quaker's Haven: Port Access": ItemClassification.progression,
    "Salt Lions: Port Access": ItemClassification.progression,
    "Saviour's Rocks: Port Access": ItemClassification.progression,
    "Shepherd Isles: Port Access": ItemClassification.progression,
    "Station III: Port Access": ItemClassification.progression,
    "The Uttershroom: Port Access": ItemClassification.progression,
    "Varchas: Port Access": ItemClassification.progression,
    "Venderbight: Port Access": ItemClassification.progression,
    "Visage: Port Access": ItemClassification.progression,
    "Whither: Port Access": ItemClassification.progression,
    "Wisdom: Port Access": ItemClassification.progression,

    "Nephrite Ring": ItemClassification.progression,

    "Progressive Deck Gun Deed": ItemClassification.progression | ItemClassification.useful,
    "Progressive Forward Gun Deed": ItemClassification.useful,
    "Progressive Rear Gun Deed": ItemClassification.useful,
    "Progressive Engine Deed": ItemClassification.progression | ItemClassification.useful,
    "Progressive Lamp Deed": ItemClassification.useful,
    "Progressive Ship Deed": ItemClassification.progression | ItemClassification.useful,

    "100 Echoes": ItemClassification.filler,
    "1000 Echoes": ItemClassification.filler,

    "Officer: Genial Magician": ItemClassification.useful,
    "Officer: Brisk Campaigner": ItemClassification.useful,
    "Officer: Presbyterate Adventuress": ItemClassification.useful,
    "Officer: Tireless Mechanic": ItemClassification.useful,
    "Officer: Carnelian Exile": ItemClassification.useful,
    "Officer: Irrepressible Cannoneer": ItemClassification.useful,
    "Officer: Maybe's Daughter": ItemClassification.useful,
    "Officer: Nacreous Outcast": ItemClassification.useful,
    "Officer: Haunted Doctor": ItemClassification.useful,
    "Officer: Sigil-Ridden Navigator": ItemClassification.useful,
    "Officer: Bandaged Poissonnier": ItemClassification.useful,

    "Officer: Monkey Foundling": ItemClassification.useful,
    "Officer: Eyeless Skull": ItemClassification.useful,
    "Officer: Elegiac Cockatoo": ItemClassification.useful,
    "Officer: Albino Tinkerer": ItemClassification.useful,
    "Officer: Guinea Page": ItemClassification.useful,
    "Officer: Vigilant Idol": ItemClassification.useful,
    "Officer: Wretched Mog": ItemClassification.useful,

}

class SunlessSeaItem(Item):
    game = "SunlessSea"

def get_filler_item_name(world: SunlessSeaWorld) -> str:

    return "1000 Echoes"

def create_item_with_correct_classification(world: SunlessSeaWorld, name: str) -> SunlessSeaItem:

    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    if name == "Progressive Deck Gun Deed" and world.options.equipment_required:
        classification = ItemClassification.progression | ItemClassification.useful

    if name == "Progressive Engine Deed" and world.options.equipment_required:
        classification = ItemClassification.progression | ItemClassification.useful

    if name == "Progressive Ship Deed" and world.options.equipment_required:
        classification = ItemClassification.progression | ItemClassification.useful

    return SunlessSeaItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: SunlessSeaWorld) -> None:
    #More to do here, but I'm not trying to go crazy anymore. Hopefully.
    itempool: list[Item] = [
        world.create_item("Progressive Deck Gun Deed"),
        world.create_item("Progressive Forward Gun Deed"),
        world.create_item("Progressive Rear Gun Deed"),
        world.create_item("Progressive Engine Deed"),
        world.create_item("Progressive Lamp Deed"),
        world.create_item("Progressive Ship Deed"),

        world.create_item("Nephrite Ring"),
    ]

    if world.options.port_access_rules.port_access:

        itempool.append(world.create_item("Abbey Rock: Port Access")),
        itempool.append(world.create_item("Adam's Way: Port Access")),
        itempool.append(world.create_item("Aestival: Port Access")),
        itempool.append(world.create_item("Avid Horizon: Port Access")),
        itempool.append(world.create_item("Chapel of Lights: Port Access")),
        itempool.append(world.create_item("The Chelonate: Port Access")),
        itempool.append(world.create_item("Codex: Port Access")),
        itempool.append(world.create_item("Cumaean Canal: Port Access")),
        itempool.append(world.create_item("Demeaux Island: Port Access")),
        itempool.append(world.create_item("Empire of Hands: Port Access")),
        itempool.append(world.create_item("The Fathomking's Hold: Port Access")),
        itempool.append(world.create_item("Frostfound: Port Access")),
        itempool.append(world.create_item("Gaider's Mourn: Port Access")),
        itempool.append(world.create_item("Godfall: Port Access")),
        itempool.append(world.create_item("Grand Geode: Port Access")),
        itempool.append(world.create_item("Hunter's Keep: Port Access")),
        itempool.append(world.create_item("Irem: Port Access")),
        itempool.append(world.create_item("Iron Republic: Port Access")),
        itempool.append(world.create_item("Isle of Cats: Port Access")),
        itempool.append(world.create_item("Khan's Heart: Port Access")),
        itempool.append(world.create_item("Khan's Shadow: Port Access")),
        itempool.append(world.create_item("Kingeater's Castle: Port Access")),
        itempool.append(world.create_item("Mangrove College: Port Access")),
        itempool.append(world.create_item("Mt Palmerston: Port Access")),
        itempool.append(world.create_item("Nuncio: Port Access")),
        itempool.append(world.create_item("Pigmote Isle: Port Access")),
        itempool.append(world.create_item("Polythreme: Port Access")),
        itempool.append(world.create_item("Port Carnelian: Port Access")),
        itempool.append(world.create_item("Port Cecil: Port Access")),
        itempool.append(world.create_item("Quaker's Haven: Port Access")),
        itempool.append(world.create_item("Salt Lions: Port Access")),
        itempool.append(world.create_item("Saviour's Rocks: Port Access")),
        itempool.append(world.create_item("Shepherd Isles: Port Access")),
        itempool.append(world.create_item("Station III: Port Access")),
        itempool.append(world.create_item("The Uttershroom: Port Access")),
        itempool.append(world.create_item("Varchas: Port Access")),
        itempool.append(world.create_item("Venderbight: Port Access")),
        itempool.append(world.create_item("Visage: Port Access")),
        itempool.append(world.create_item("Whither: Port Access")),
        itempool.append(world.create_item("Wisdom: Port Access")),

    if world.options.shuffle_officers:

        itempool.append(world.create_item("Officer: Genial Magician")),
        itempool.append(world.create_item("Officer: Brisk Campaigner")),
        itempool.append(world.create_item("Officer: Presbyterate Adventuress")),
        itempool.append(world.create_item("Officer: Tireless Mechanic")),
        itempool.append(world.create_item("Officer: Carnelian Exile")),
        itempool.append(world.create_item("Officer: Irrepressible Cannoneer")),
        itempool.append(world.create_item("Officer: Maybe's Daughter")),
        itempool.append(world.create_item("Officer: Nacreous Outcast")),
        itempool.append(world.create_item("Officer: Haunted Doctor")),
        itempool.append(world.create_item("Officer: Sigil-Ridden Navigator")),
        itempool.append(world.create_item("Officer: Bandaged Poissonnier")),

        itempool.append(world.create_item("Officer: Monkey Foundling")),
        itempool.append(world.create_item("Officer: Eyeless Skull")),
        itempool.append(world.create_item("Officer: Elegiac Cockatoo")),
        itempool.append(world.create_item("Officer: Albino Tinkerer")),
        itempool.append(world.create_item("Officer: Guinea Page")),
        itempool.append(world.create_item("Officer: Vigilant Idol")),
        itempool.append(world.create_item("Officer: Wretched Mog"))

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    if world.options.shuffle_nephrite_ring:
        starting_hunters_keep = world.create_item("Hunter's Keep: Port Access")
        world.push_precollected(starting_hunters_keep)

        starting_mutton_island = world.create_item("Quaker's Haven: Port Access")
        world.push_precollected(starting_mutton_island)

        starting_cumaean_canal = world.create_item("Cumaean Canal: Port Access")
        world.push_precollected(starting_cumaean_canal)
    else:
        starting_hunters_keep = world.create_item("Hunter's Keep: Port Access")
        world.push_precollected(starting_hunters_keep)

        starting_mutton_island = world.create_item("Quaker's Haven: Port Access")
        world.push_precollected(starting_mutton_island)

        starting_cumaean_canal = world.create_item("Cumaean Canal: Port Access")
        world.push_precollected(starting_cumaean_canal)

        starting_nephrite_ring = world.create_item("Nephrite Ring")
        world.push_precollected(starting_nephrite_ring)