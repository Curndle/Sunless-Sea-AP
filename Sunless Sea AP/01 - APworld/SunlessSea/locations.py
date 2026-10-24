from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import SunlessSeaWorld

LOCATION_NAME_TO_ID = {

    "Surveyed: Fallen London": 1,
    "Surveyed: Abbey Rock": 2,
    "Surveyed: Adam's Way": 3,
    "Surveyed: Aestival": 4,
    "Surveyed: Avid Horizon": 5,
    "Surveyed: Chapel of Lights": 6,
    "Surveyed: the Chelonate": 7,
    "Surveyed: Codex": 8,
    "Surveyed: Cumaean Canal": 9,
    "Surveyed: Demeaux Island": 10,
    "Surveyed: Empire of Hands": 11,
    "Surveyed: the Fathomking's Hold": 12,
    "Surveyed: Frostfound": 13,
    "Surveyed: Gaider's Mourn": 14,
    "Surveyed: Godfall": 15,
    "Surveyed: Grand Geode": 16,
    "Surveyed: Hunter's Keep": 17,
    "Surveyed: Irem": 18,
    "Surveyed: Iron Republic": 19,
    "Surveyed: Isle of Cats": 20,
    "Surveyed: Khan's Heart": 21,
    "Surveyed: Khan's Shadow": 22,
    "Surveyed: Kingeater's Castle": 23,
    "Surveyed: the Mangrove College": 24,
    "Surveyed: Mt Palmerston": 25,
    "Surveyed: Nuncio": 26,
    "Surveyed: Pigmote Isle": 27,
    "Surveyed: Polythreme": 28,
    "Surveyed: Port Carnelian": 29,
    "Surveyed: Port Cecil": 30,
    "Surveyed: Quaker's Haven": 31,
    "Surveyed: The Salt Lions": 32,
    "Surveyed: Saviour's Rocks": 33,
    "Surveyed: Shepherd Isles": 34,
    "Surveyed: Station III": 35,
    "Surveyed: the Uttershroom": 36,
    "Surveyed: Varchas": 37,
    "Surveyed: Venderbight": 38,
    "Surveyed: Visage": 39,
    "Surveyed: Whither": 40,
    "Surveyed: Wisdom": 41,

    "Port Report: Fallen London": 100,
    "Merchant Venturer: Seven Strange Catches": 101,
    "Merchant Venturer: Seven Hunting Trophies": 102,
    "Merchant Venturer: Seven Pieces of Scintillack": 103,
    "Merchant Venturer: Seven Volumes of Romantic literature": 104,
    "Merchant Venturer: Seven Bolts of Spider-Silk": 105,
    "Merchant Venturer: Seven Skins of Zzoup": 106,
    "Merchant Venturer: Seven Packages of Mutersalt": 107,
    "Merchant Venturer: Seven Devilbone Dice": 108,
    "Merchant Venturer: Seven Outlandish Artefacts": 109,
    "Merchant Venturer: Seven Bales of Parabola-Linen": 110,
    "Merchant Venturer: Seven Pieces of Stygian Ivory": 111,
    "Merchant Venturer: Seven Caskets of Sapphires": 112,
    "Merchant Venturer: One Lorn-Fluke Core": 113,
    "Merchant Venturer: Seven Lamentable Relics": 114,
    "Merchant Venturer: Seven Sacks of Darkdrop Coffee": 115,

    #Going to comment out these locations for now, not sure if they'll be useful
    #"Alarming Scholar: 7 Zee-Stories": 120,
    #"Alarming Scholar: 7 Memory of Distant Shores": 121,
    #"Alarming Scholar: 7 Tales of Terror": 122,
    #"Alarming Scholar: 7 Vision of the Surface": 123,
    #"Alarming Scholar: Judgements' Egg": 124,
    #"Alarming Scholar: Captivating Treasure": 125,
    #"Alarming Scholar: Live Specimen": 126,
    #"Alarming Scholar: Lump of Blue Scintillack": 127,
    #"Alarming Scholar: Ray-Drenched Cinder": 128,
    #"Alarming Scholar: Wakeful Idol": 129,
    #"Alarming Scholar: Element of Dawn": 130,
    #"Alarming Scholar: Extraordinary Implication": 131,
    #"Alarming Scholar: Searing Enigma": 132,

    "Recruit Officer: Genial Magician": 150,
    "Recruit Officer: Brisk Campaigner": 151,
    #For now, I'll just put the officers where you can recruit them.
    #Storylines will be checks later

    "A Port Report: Abbey Rock": 200,

    "A Port Report: Adam's Way": 300,
    "Recruit Officer: Presbyterate Adventuress": 350,

    "A Port Report: Aestival": 400,

    "A Port Report: Avid Horizon": 500,

    "A Port Report: Chapel of Lights": 600,

    "A Port Report: The Chelonate": 700,
    "Release Officer: Plausible Surgeon": 750,

    "A Port Report: Codex": 800,

    "A Port Report: Cumaean Canal": 900,

    "A Port Report: Demeaux Island": 1000,

    "A Port Report: Empire of Hands": 1100,
    "Recruit Officer: Monkey Foundling": 1150,

    "A Port Report: The Fathomking's Hold": 1200,

    "A Port Report: Frostfound": 1300,
    "Recruit Officer: Tireless Mechanic": 1350,
    "Release Officer: Sly Navigator": 1351,

    "A Port Report: Gaider's Mourn": 1400,

    "A Port Report: Godfall": 1500,
    "Recruit Officer: Eyeless Skull": 1550,
    #Does that make sense as a check? Doesn't hurt, I guess

    "A Port Report: Grand Geode": 1600,
    "Recruit Officer: Carnelian Exile": 1650,

    "A Port Report: Hunter's Keep": 1700,

    "A Port Report: Irem": 1800,

    "A Port Report: Iron Republic": 1900,
    "Recruit Officer: Irrepressible Cannoneer": 1950,

    "A Port Report: Isle of Cats": 2000,

    "A Port Report: Khan's Heart": 2100,
    "Purchase Nephrite Ring": 2190,

    "A Port Report: Khan's Shadow": 2200,
    "Release Officer: Longshanks Gunner": 2250,

    "A Port Report: Kingeater's Castle": 2300,
    "Release Officer: Gall-Eyed Engineer": 2350,

    "A Port Report: The Mangrove College": 2400,
    "Recruit Officer: Maybe's Daughter": 2450,
    "Recruit Officer: Elegiac Cockatoo": 2451,

    "A Port Report: Mt Palmerston": 2500,

    "A Port Report: Nuncio": 2600,

    "A Port Report: Pigmote Isle": 2700,
    "Recruit Officer: Albino Tinkerer": 2750,
    "Recruit Officer: Guinea Page": 2751,

    "A Port Report: Polythreme": 2800,

    "A Port Report: Port Carnelian": 2900,

    "A Port Report: Port Cecil": 3000,
    "Recruit Officer: Nacreous Outcast": 3050,
    "Recruit Officer: Vigilant Idol": 3051,

    "A Port Report: Quaker's Haven": 3100,
    "Recruit Officer: Wretched Mog": 3150,

    "A Port Report: The Salt Lion": 3200,

    "A Port Report: Saviour's Rocks": 3300,
    "Recruit Officer: Haunted Doctor": 3350,

    "A Port Report: Shepherd Isle": 3400,
    "Recruit Officer: Sigil-Ridden Navigator": 3450,

    "A Port Report: Station III": 3500,

    "A Port Report: The Uttershroom": 3600,

    "A Port Report: Varchas": 3700,

    "A Port Report: Venderbight": 3800,
    "Recruit Officer: Bandaged Poissonnier": 3850,

    "A Port Report: Visage": 3900,

    "A Port Report: Whither": 4000,

    "A Port Report: Wisdom": 4100,
    "Release Officer: Shady Cook": 4150

}

class SunlessSeaLocation(Location):
    game = "SunlessSea"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: SunlessSeaWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: SunlessSeaWorld) -> None:
    fallen_london = world.get_region("Fallen London")
    hunters_keep = world.get_region("Hunters Keep")
    mutton_island = world.get_region("Mutton Island")
    west_coast = world.get_region("Western Coastline")
    venderbight = world.get_region("Venderbight")
    whither = world.get_region("Whither")
    codex = world.get_region("Codex")
    cumaean_canal = world.get_region("Cumaean Canal")
    iron_republic = world.get_region("Iron Republic")
    grand_geode = world.get_region("Grand Geode")
    south_coast = world.get_region("Southern Coastline")
    port_carnelian = world.get_region("Port Carnelian")
    adams_way = world.get_region("Adam's Way")
    varchas = world.get_region("Varchas")
    new_home_waters = world.get_region("New Home Waters")
    gaiders_mourn = world.get_region("Gaider's Mourn")
    demeaux_island = world.get_region("Demeaux Island")
    pigmote_isle = world.get_region("Pigmote Isle")
    salt_lions = world.get_region("Salt Lions")
    abbey_rock = world.get_region("Abbey Rock")
    station_iii = world.get_region("Station III")
    shepherd_isles = world.get_region("Shepherd Isles")
    the_frozen_north = world.get_region("The Frozen North")
    chapel_of_lights = world.get_region("Chapel Of Lights")
    avid_horizon = world.get_region("Avid Horizon")
    frostfound = world.get_region("Frostfound")
    mount_palmerston = world.get_region("Mount Palmerston")
    the_north_east = world.get_region("The North East")
    port_cecil = world.get_region("Port Cecil")
    godfall = world.get_region("Godfall")
    polythreme = world.get_region("Polythreme")
    nuncio = world.get_region("Nuncio")
    wisdom = world.get_region("Wisdom")
    khans_heart = world.get_region("Khan's Heart")
    khans_glory = world.get_region("Khan's Glory")
    khans_shadow = world.get_region("Khan's Shadow")
    the_south_east = world.get_region("The South East")
    mangrove_college = world.get_region("Mangrove College")
    isle_of_cats = world.get_region("Isle Of Cats")
    visage = world.get_region("Visage")
    the_uttershroom = world.get_region("The Uttershroom")
    the_fathomkings_hold = world.get_region("The Fathomking's Hold")
    the_distant_east = world.get_region("The Distant East")
    irem = world.get_region("Irem")
    saviours_rocks = world.get_region("Saviour's Rocks")
    empire_of_hands = world.get_region("Empire Of Hands")
    aestival = world.get_region("Aestival")
    the_chelonate = world.get_region("The Chelonate")
    kingeaters_castle = world.get_region("Kingeater's Castle")

    fallen_london_locations = get_location_names_with_ids([])
    fallen_london.add_locations(fallen_london_locations, SunlessSeaLocation)
    #I'll put the Surveyed checks in the source locations, so when the location opens up they unlock immediately.
    #Location got emptied after I moved a bunch of stuff

    hunters_keep_locations = get_location_names_with_ids(["Surveyed: Hunter's Keep","A Port Report: Hunter's Keep"])
    hunters_keep.add_locations(hunters_keep_locations, SunlessSeaLocation)

    #This is going to be a lot, huh.
    #I think I'm also gonna need to do some AP Events? F-ck.

    mutton_island_locations = get_location_names_with_ids(["Surveyed: Quaker's Haven","A Port Report: Quaker's Haven"])
    mutton_island.add_locations(mutton_island_locations, SunlessSeaLocation)

    venderbight_locations = get_location_names_with_ids(["Surveyed: Venderbight""A Port Report: Venderbight"])
    venderbight.add_locations(venderbight_locations, SunlessSeaLocation)
    #Will add Curator as checks "eventually"

    whither_locations = get_location_names_with_ids(["Surveyed: Whither","A Port Report: Whither"])
    whither.add_locations(whither_locations, SunlessSeaLocation)

    codex_locations = get_location_names_with_ids(["Surveyed: Codex","A Port Report: Codex"])
    codex.add_locations(codex_locations, SunlessSeaLocation)

    cumaean_canal_locations = get_location_names_with_ids(["Surveyed: Cumaean Canal","A Port Report: Cumaean Canal"])
    cumaean_canal.add_locations(cumaean_canal_locations, SunlessSeaLocation)

    iron_republic_locations = get_location_names_with_ids(["Surveyed: Iron Republic","A Port Report: Iron Republic"])
    iron_republic.add_locations(iron_republic_locations, SunlessSeaLocation)

    grand_geode_locations = get_location_names_with_ids(["Surveyed: Grand Geode","A Port Report: Grand Geode"])
    grand_geode.add_locations(grand_geode_locations, SunlessSeaLocation)

    port_carnelian_locations = get_location_names_with_ids(["Surveyed: Port Carnelian","A Port Report: Port Carnelian"])
    port_carnelian.add_locations(port_carnelian_locations, SunlessSeaLocation)

    adams_way_locations = get_location_names_with_ids(["Surveyed: Adam's Way","A Port Report: Adam's Way"])
    adams_way.add_locations(adams_way_locations, SunlessSeaLocation)

    varchas_locations = get_location_names_with_ids(["Surveyed: Varchas","A Port Report: Varchas"])
    varchas.add_locations(varchas_locations, SunlessSeaLocation)

    gaiders_mourn_locations = get_location_names_with_ids(["Surveyed: Gaider's Mourn","A Port Report: Gaider's Mourn"])
    gaiders_mourn.add_locations(gaiders_mourn_locations, SunlessSeaLocation)

    salt_lions_locations = get_location_names_with_ids(["Surveyed: The Salt Lions","A Port Report: The Salt Lion"])
    salt_lions.add_locations(salt_lions_locations, SunlessSeaLocation)

    pigmote_isle_locations = get_location_names_with_ids(["Surveyed: Pigmote Isle","A Port Report: Pigmote Isle"])
    pigmote_isle.add_locations(pigmote_isle_locations, SunlessSeaLocation)

    shepherd_isles_locations = get_location_names_with_ids(["Surveyed: Shepherd Isles","A Port Report: Shepherd Isle"])
    shepherd_isles.add_locations(shepherd_isles_locations, SunlessSeaLocation)

    abbey_rock_locations = get_location_names_with_ids(["Surveyed: Abbey Rock","A Port Report: Abbey Rock"])
    abbey_rock.add_locations(abbey_rock_locations, SunlessSeaLocation)

    station_iii_locations = get_location_names_with_ids(["Surveyed: Station III","A Port Report: Station III"])
    station_iii.add_locations(station_iii_locations, SunlessSeaLocation)

    demeaux_island_locations = get_location_names_with_ids(["Surveyed: Demeaux Island","A Port Report: Demeaux Island"])
    demeaux_island.add_locations(demeaux_island_locations, SunlessSeaLocation)

    chapel_of_lights_locations = get_location_names_with_ids(["Surveyed: Chapel of Lights","A Port Report: Chapel of Lights"])
    chapel_of_lights.add_locations(chapel_of_lights_locations, SunlessSeaLocation)

    avid_horizon_locations = get_location_names_with_ids(["Surveyed: Avid Horizon","A Port Report: Avid Horizon"])
    avid_horizon.add_locations(avid_horizon_locations, SunlessSeaLocation)

    frostfound_locations = get_location_names_with_ids(["Surveyed: Frostfound","A Port Report: Frostfound"])
    frostfound.add_locations(frostfound_locations, SunlessSeaLocation)

    mount_palmerston_locations = get_location_names_with_ids(["Surveyed: Mt Palmerston","A Port Report: Mt Palmerston"])
    mount_palmerston.add_locations(mount_palmerston_locations, SunlessSeaLocation)

    port_cecil_locations = get_location_names_with_ids(["Surveyed: Port Cecil","A Port Report: Port Cecil"])
    port_cecil.add_locations(port_cecil_locations, SunlessSeaLocation)

    khans_glory_locations = get_location_names_with_ids([])
    khans_glory.add_locations(khans_glory_locations, SunlessSeaLocation)
    #this is empty for now, there's are no default locations here.

    khans_heart_locations = get_location_names_with_ids(["Surveyed: Khan's Heart","A Port Report: Khan's Heart"])
    khans_heart.add_locations(khans_heart_locations, SunlessSeaLocation)

    khans_shadow_locations = get_location_names_with_ids(["Surveyed: Khan's Shadow","A Port Report: Khan's Shadow"])
    khans_shadow.add_locations(khans_shadow_locations, SunlessSeaLocation)

    nuncio_locations = get_location_names_with_ids(["Surveyed: Nuncio","A Port Report: Nuncio"])
    nuncio.add_locations(nuncio_locations, SunlessSeaLocation)

    polythreme_locations = get_location_names_with_ids(["Surveyed: Polythreme","A Port Report: Polythreme"])
    polythreme.add_locations(polythreme_locations, SunlessSeaLocation)

    godfall_locations = get_location_names_with_ids(["Surveyed: Godfall","A Port Report: Godfall"])
    godfall.add_locations(godfall_locations, SunlessSeaLocation)

    wisdom_locations = get_location_names_with_ids(["Surveyed: Wisdom","A Port Report: Wisdom"])
    wisdom.add_locations(wisdom_locations, SunlessSeaLocation)

    mangrove_college_locations = get_location_names_with_ids(["Surveyed: the Mangrove College","A Port Report: The Mangrove College"])
    mangrove_college.add_locations(mangrove_college_locations, SunlessSeaLocation)

    isle_of_cats_locations = get_location_names_with_ids(["Surveyed: Isle of Cats","A Port Report: Isle of Cats"])
    isle_of_cats.add_locations(isle_of_cats_locations, SunlessSeaLocation)

    visage_locations = get_location_names_with_ids(["Surveyed: Visage","A Port Report: Visage"])
    visage.add_locations(visage_locations, SunlessSeaLocation)

    the_uttershroom_locations = get_location_names_with_ids(["Surveyed: the Uttershroom","A Port Report: The Uttershroom"])
    the_uttershroom.add_locations(the_uttershroom_locations, SunlessSeaLocation)

    the_fathomkings_hold_locations = get_location_names_with_ids(["Surveyed: Kingeater's Castle","A Port Report: The Fathomking's Hold"])
    the_fathomkings_hold.add_locations(the_fathomkings_hold_locations, SunlessSeaLocation)

    irem_locations = get_location_names_with_ids(["Surveyed: Irem","A Port Report: Irem"])
    irem.add_locations(irem_locations, SunlessSeaLocation)

    saviours_rocks_locations = get_location_names_with_ids(["Surveyed: Saviour's Rocks","A Port Report: Saviour's Rocks"])
    saviours_rocks.add_locations(saviours_rocks_locations, SunlessSeaLocation)

    empire_of_hands_locations = get_location_names_with_ids(["Surveyed: Empire of Hands","A Port Report: Empire of Hands"])
    empire_of_hands.add_locations(empire_of_hands_locations, SunlessSeaLocation)

    aestival_locations = get_location_names_with_ids(["Surveyed: Aestival","A Port Report: Aestival"])
    aestival.add_locations(aestival_locations, SunlessSeaLocation)

    the_chelonate_locations = get_location_names_with_ids(["Surveyed: the Chelonate","A Port Report: The Chelonate"])
    the_chelonate.add_locations(the_chelonate_locations, SunlessSeaLocation)

    kingeaters_castle_locations = get_location_names_with_ids(["Surveyed: Kingeater's Castle","A Port Report: Kingeater's Castle"])
    kingeaters_castle.add_locations(kingeaters_castle_locations, SunlessSeaLocation)

    if world.options.shuffle_nephrite_ring:
        #Realizing if I want an optional locations I have to set it up here, let's do this -_-
        nephrite_ring_location = get_location_names_with_ids(["Nephrite Ring"])
        khans_glory.add_locations(nephrite_ring_location, SunlessSeaLocation)

    if world.options.shuffle_officers:
        #I'm petty and won't include the latter added officers or the one from the kickstarter... for now. Also, no scarred sister and such, that's another thing entirely.
        recruit_empire_of_hands_locations = get_location_names_with_ids(["Recruit Officer: Monkey Foundling"])
        empire_of_hands.add_locations(recruit_empire_of_hands_locations, SunlessSeaLocation)

        recruit_saviours_rocks_locations = get_location_names_with_ids(["Recruit Officer: Haunted Doctor"])
        saviours_rocks.add_locations(recruit_saviours_rocks_locations, SunlessSeaLocation)

        recruit_mangrove_college_locations = get_location_names_with_ids(["Recruit Officer: Maybe's Daughter","Recruit Officer: Elegiac Cockatoo"])
        mangrove_college.add_locations(recruit_mangrove_college_locations, SunlessSeaLocation)

        recruit_godfall_locations = get_location_names_with_ids(["Recruit Officer: Eyeless Skull"])
        godfall.add_locations(recruit_godfall_locations, SunlessSeaLocation)

        recruit_port_cecil_locations = get_location_names_with_ids(["Recruit Officer: Nacreous Outcast", "Recruit Officer: Vigilant Idol"])
        port_cecil.add_locations(recruit_port_cecil_locations, SunlessSeaLocation)

        recruit_frostfound_locations = get_location_names_with_ids(["Recruit Officer: Tireless Mechanic"])
        frostfound.add_locations(recruit_frostfound_locations, SunlessSeaLocation)

        recruit_shepherd_isles_locations = get_location_names_with_ids(["Recruit Officer: Sigil-Ridden Navigator"])
        shepherd_isles.add_locations(recruit_shepherd_isles_locations, SunlessSeaLocation)

        recruit_pigmote_isle_locations = get_location_names_with_ids(["Recruit Officer: Albino Tinkerer","Recruit Officer: Guinea Page"])
        pigmote_isle.add_locations(recruit_pigmote_isle_locations, SunlessSeaLocation)

        recruit_adams_way_locations = get_location_names_with_ids(["Recruit Officer: Presbyterate Adventuress"])
        adams_way.add_locations(recruit_adams_way_locations, SunlessSeaLocation)

        recruit_grand_geode_locations = get_location_names_with_ids(["Recruit Officer: Carnelian Exile"])
        grand_geode.add_locations(recruit_grand_geode_locations, SunlessSeaLocation)

        recruit_iron_republic_locations = get_location_names_with_ids(["Recruit Officer: Irrepressible Cannoneer"])
        iron_republic.add_locations(recruit_iron_republic_locations, SunlessSeaLocation)

        recruit_venderbight_locations = get_location_names_with_ids(["Recruit Officer: Bandaged Poissonnier"])
        venderbight.add_locations(recruit_venderbight_locations, SunlessSeaLocation)

        recruit_mutton_island_locations = get_location_names_with_ids(["Recruit Officer: Wretched Mog"])
        mutton_island.add_locations(recruit_mutton_island_locations, SunlessSeaLocation)

        recruit_fallen_london_locations = get_location_names_with_ids(["Recruit Officer: Genial Magician", "Recruit Officer: Brisk Campaigner"])
        fallen_london.add_locations(recruit_fallen_london_locations, SunlessSeaLocation)

    if world.options.officer_quests:
        #Initial release will just do the Starter Officer quests as checks
        officer_kingeaters_castle_locations = get_location_names_with_ids(["Release Officer: Gall-Eyed Engineer"])
        kingeaters_castle.add_locations(officer_kingeaters_castle_locations, SunlessSeaLocation)

        officer_the_chelonate_locations = get_location_names_with_ids(["Release Officer: Plausible Surgeon"])
        the_chelonate.add_locations(officer_the_chelonate_locations, SunlessSeaLocation)

        officer_wisdom_locations = get_location_names_with_ids(["Release Officer: Shady Cook"])
        wisdom.add_locations(officer_wisdom_locations, SunlessSeaLocation)

        officer_khans_shadow_locations = get_location_names_with_ids(["Release Officer: Longshanks Gunner"])
        khans_shadow.add_locations(officer_khans_shadow_locations, SunlessSeaLocation)

        officer_frostfound_locations = get_location_names_with_ids(["Release Officer: Sly Navigator"])
        frostfound.add_locations(officer_frostfound_locations, SunlessSeaLocation)

    if world.options.trade_quest:
        #just Merchant Venture for now, may add other trade quests (First Curator or Principalities End for example) later
        merchant_venture_locations = get_location_names_with_ids(["Merchant Venturer: Seven Strange Catches", "Merchant Venturer: Seven Hunting Trophies","Merchant Venturer: Seven Pieces of Scintillack","Merchant Venturer: Seven Volumes of Romantic literature", "Merchant Venturer: Seven Bolts of Spider-Silk","Merchant Venturer: Seven Skins of Zzoup", "Merchant Venturer: Seven Packages of Mutersalt","Merchant Venturer: Seven Devilbone Dice", "Merchant Venturer: Seven Outlandish Artefacts","Merchant Venturer: Seven Bales of Parabola-Linen", "Merchant Venturer: Seven Pieces of Stygian Ivory","Merchant Venturer: Seven Caskets of Sapphires", "Merchant Venturer: One Lorn-Fluke Core","Merchant Venturer: Seven Lamentable Relics", "Merchant Venturer: Seven Sacks of Darkdrop Coffee"])
        fallen_london.add_locations(merchant_venture_locations, SunlessSeaLocation)

def create_events(world: SunlessSeaWorld) -> None:
    #Not sure if I'll need many events but let's at least make a victory thingy
    fallen_london = world.get_region("Fallen London")

    #I think I may need to put these trade events into new regions, so I can then lock their location until any source unlocking can occur.
    strange_catches_regions = world.get_region("Strange Catches Region")
    hunting_trophies_regions = world.get_region("Hunting Trophies Region")
    scintillack_regions = world.get_region("Scintillack Region")
    romantic_literature_regions = world.get_region("Romantic Literature Region")
    spider_silk_regions = world.get_region("Spider-Silk Region")
    zzoup_regions = world.get_region("Zzoup Region")
    mutersalt_regions = world.get_region("Mutersalt Region")
    devilbone_dice_regions = world.get_region("Devilbone Dice Region")
    outlandish_artefacts_regions = world.get_region("Outlandish Artefacts Region")
    parabola_linen_regions = world.get_region("Parabola-Linen Region")
    stygian_ivory_regions = world.get_region("Stygian Ivory Region")
    sapphires_regions = world.get_region("Sapphires Region")
    fluke_core_regions = world.get_region("Fluke-Core Region")
    lamentable_relics_regions = world.get_region("Lamentable Relics Region")
    darkdrop_coffee_regions = world.get_region("Darkdrop Coffee Region")

    fallen_london.add_event(
        "Retired Successfully", "Victory", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    #figured I could make some events to call upon for all the trade goods currently being used. Hoping it's less annoying later because of this.

    #I think I may need to put these events into new regions, so I can then lock their location until any source unlocking can occur.

    strange_catches_regions.add_event(
        "Strange Catches Location", "Source of Strange Catches", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    hunting_trophies_regions.add_event(
        "Hunting Trophies Location", "Source of Hunting Trophies", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )
    #not sure if this will ever get used, you can get Hunting Trophies from just about any enemy.

    scintillack_regions.add_event(
        "Scintillack Location", "Source of Scintillack", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    romantic_literature_regions.add_event(
        "Romantic Literature Location", "Source of Romantic Literature", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    spider_silk_regions.add_event(
        "Spider-Silk Location", "Source of Spider-Silk", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    zzoup_regions.add_event(
        "Zzoup Location", "Source of Zzoup", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    mutersalt_regions.add_event(
        "Mutersalt Location", "Source of Mutersalt", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    devilbone_dice_regions.add_event(
        "Devilbone Dice Location", "Source of Devilbone Dice", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    outlandish_artefacts_regions.add_event(
        "Outlandish Artefacts Location", "Source of Outlandish Artefacts", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    parabola_linen_regions.add_event(
        "Parabola-Linen Location", "Source of Parabola-Linen", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    stygian_ivory_regions.add_event(
        "Stygian Ivory Location", "Source of Stygian Ivory", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    sapphires_regions.add_event(
        "Sapphires Location", "Source of Sapphires", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    fluke_core_regions.add_event(
        "Fluke-Core Location", "Source of Fluke-Core", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    lamentable_relics_regions.add_event(
        "Lamentable Relics Location", "Source of Lamentable Relics", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

    darkdrop_coffee_regions.add_event(
        "Darkdrop Coffee Location", "Source of Darkdrop Coffee", location_type=SunlessSeaLocation, item_type=items.SunlessSeaItem
    )

#that's it for now, I think there's enough locations in there.
#may have to make 2000 events thought, we'll see.