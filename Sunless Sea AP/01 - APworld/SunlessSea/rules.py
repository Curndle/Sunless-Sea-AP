from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import SunlessSeaWorld


def set_all_rules(world: SunlessSeaWorld) -> None:

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: SunlessSeaWorld) -> None:

    fallen_london_to_hunters_keep = world.get_entrance("Fallen London to Hunters Keep")
    fallen_london_to_mutton_island = world.get_entrance("Fallen London to Mutton Island")
    fallen_london_to_cumaean_canal = world.get_entrance("Fallen London to Cumaean Canal")

    west_coast_to_venderbight = world.get_entrance("Western Coastline to Venderbight")
    west_coast_to_whither = world.get_entrance("Western Coastline to Whither")
    west_coast_to_codex = world.get_entrance("Western Coastline to Codex")
    west_coast_to_iron_republic = world.get_entrance("Western Coastline to Iron Republic")
    west_coast_to_grand_geode = world.get_entrance("Western Coastline to Grand Geode")

    venderbight_to_the_frozen_north = world.get_entrance("Venderbight to The Frozen North")
    whither_to_the_frozen_north = world.get_entrance("Whither to The Frozen North")
    codex_to_the_frozen_north = world.get_entrance("Codex to The Frozen North")

    iron_republic_to_south_coast = world.get_entrance("Iron Republic to Southern Coastline")
    iron_republic_to_the_south_east = world.get_entrance("Iron Republic to The South East")
    grand_geode_to_south_coast = world.get_entrance("Grand Geode to Southern Coastline")
    grand_geode_to_the_south_east = world.get_entrance("Grand Geode to The South East")

    new_home_waters_to_salt_lions = world.get_entrance("New Home Waters to Salt Lions")
    new_home_waters_to_abbey_rock = world.get_entrance("New Home Waters to Abbey Rock")
    new_home_waters_to_shepherd_isles = world.get_entrance("New Home Waters to Shepherd Isles")
    new_home_waters_to_station_iii = world.get_entrance("New Home Waters to Station III")
    new_home_waters_to_demeaux_island = world.get_entrance("New Home Waters to Demeaux island")
    new_home_waters_to_gaiders_mourn = world.get_entrance("New Home Waters to Gaider's Mourn")
    new_home_waters_to_pigmote_isle = world.get_entrance("New Home Waters to Pigmote Isle")

    salt_lions_to_the_frozen_north = world.get_entrance("Salt Lions to The Frozen North")
    salt_lions_to_the_north_east = world.get_entrance("Salt Lions to The North East")
    salt_lions_to_the_south_east = world.get_entrance("Salt Lions to The South East")
    abbey_rock_to_the_frozen_north = world.get_entrance("Abbey Rock to The Frozen North")
    abbey_rock_to_the_north_east = world.get_entrance("Abbey Rock to The North East")
    abbey_rock_to_the_south_east = world.get_entrance("Abbey Rock to The South East")
    shepherd_isles_to_the_frozen_north = world.get_entrance("Shepherd Isles to The Frozen North")
    shepherd_isles_to_the_north_east = world.get_entrance("Shepherd Isles to The North East")
    shepherd_isles_to_the_south_east = world.get_entrance("Shepherd Isles to The South East")
    station_iii_to_the_frozen_north = world.get_entrance("Station III to The Frozen North")
    station_iii_to_the_north_east = world.get_entrance("Station III to The North East")
    station_iii_to_the_south_east = world.get_entrance("Station III to The South East")
    demeaux_island_to_the_frozen_north = world.get_entrance("Demeaux island to The Frozen North")
    demeaux_island_to_the_north_east = world.get_entrance("Demeaux island to The North East")
    demeaux_island_to_the_south_east = world.get_entrance("Demeaux island to The South East")
    gaiders_mourn_to_the_frozen_north = world.get_entrance("Gaider's Mourn to The Frozen North")
    gaiders_mourn_to_the_north_east = world.get_entrance("Gaider's Mourn to The North East")
    gaiders_mourn_to_the_south_east = world.get_entrance("Gaider's Mourn to The South East")
    pigmote_isle_to_the_frozen_north = world.get_entrance("Pigmote Isle to The Frozen North")
    pigmote_isle_to_the_north_east = world.get_entrance("Pigmote Isle to The North East")
    pigmote_isle_to_the_south_east = world.get_entrance("Pigmote Isle to The South East")

    south_coast_to_adams_way = world.get_entrance("Southern Coastline to Adam's Way")
    south_coast_to_varchas = world.get_entrance("Southern Coastline to Varchas")
    south_coast_to_port_carnelian = world.get_entrance("Southern Coastline to Port Carnelian")

    adams_way_to_the_south_east = world.get_entrance("Adam's Way to The South East")
    adams_way_to_kingeaters_castle = world.get_entrance("Adam's Way to Kingeater's Castle")
    varchas_to_the_south_east = world.get_entrance("Varchas to the South East")
    varchas_to_kingeaters_castle = world.get_entrance("Varchas to Kingeater's Castle")
    port_carnelian_to_the_south_east = world.get_entrance("Port Carnelian to The South East")
    port_carnelian_to_kingeaters_castle = world.get_entrance("Port Carnelian to Kingeater's Castle")

    the_frozen_north_to_chapel_of_lights = world.get_entrance("The Frozen North to Chapel Of Lights")
    the_frozen_north_to_avid_horizon = world.get_entrance("The Frozen North to Avid Horizon")
    the_frozen_north_to_frostfound = world.get_entrance("The Frozen North to Frostfound")
    the_frozen_north_to_mount_palmerston = world.get_entrance("The Frozen North to Mount Palmerston")

    chapel_of_lights_to_the_north_east = world.get_entrance("Chapel Of Lights to The North East")
    chapel_of_lights_to_irem = world.get_entrance("Chapel Of Lights to Irem")
    avid_horizon_to_the_north_east = world.get_entrance("Avid Horizon to The North East")
    avid_horizon_to_irem = world.get_entrance("Avid Horizon to Irem")
    frostfound_to_the_north_east = world.get_entrance("Frostfound to The North East")
    frostfound_to_irem = world.get_entrance("Frostfound to Irem")
    mount_palmerston_to_the_north_east = world.get_entrance("Mount Palmerston to The North East")
    mount_palmerston_to_irem = world.get_entrance("Mount Palmerston to Irem")

    the_north_east_to_khans_heart = world.get_entrance("The North East to Khan's Heart")
    the_north_east_to_khans_glory = world.get_entrance("The North East to Khan's Glory")
    the_north_east_to_khans_shadow = world.get_entrance("The North East to Khan's Shadow")
    the_north_east_to_port_cecil = world.get_entrance("The North East to Port Cecil")
    the_north_east_to_nuncio = world.get_entrance("The North East to Nuncio")
    the_north_east_to_wisdom = world.get_entrance("The North East to Wisdom")
    the_north_east_to_polythreme = world.get_entrance("The North East to Polythreme")
    the_north_east_to_godfall = world.get_entrance("The North East to Godfall")

    khans_heart_to_the_distant_east = world.get_entrance("Khan's Heart to The Distant East")
    khans_heart_to_the_south_east = world.get_entrance("Khan's Heart to The South East")
    khans_glory_to_the_distant_east = world.get_entrance("Khan's Glory to The Distant East")
    khans_glory_to_the_south_east = world.get_entrance("Khan's Glory to The South East")
    khans_shadow_to_the_distant_east = world.get_entrance("Khan's Shadow to The Distant East")
    khans_shadow_to_the_south_east = world.get_entrance("Khan's Shadow to The South East")
    port_cecil_to_the_distant_east = world.get_entrance("Port Cecil to The Distant East")
    port_cecil_to_the_south_east = world.get_entrance("Port Cecil to The South East")
    nuncio_to_the_distant_east = world.get_entrance("Nuncio to The Distant East")
    nuncio_to_the_south_east = world.get_entrance("Nuncio to The South East")
    wisdom_to_the_distant_east = world.get_entrance("Wisdom to The Distant East")
    wisdom_to_the_south_east = world.get_entrance("Wisdom to The South East")
    polythreme_to_the_distant_east = world.get_entrance("Polythreme to The Distant East")
    polythreme_to_the_south_east = world.get_entrance("Polythreme to The South East")
    godfall_to_the_distant_east = world.get_entrance("Godfall to The Distant East")
    godfall_to_the_south_east = world.get_entrance("Godfall to The South East")

    the_south_east_to_isle_of_cats = world.get_entrance("The South East to Isle of Cats")
    the_south_east_to_visage = world.get_entrance("The South East to Visage")
    the_south_east_to_the_uttershroom = world.get_entrance("The South East to The Uttershroom")
    the_south_east_to_mangrove_college = world.get_entrance("The South East to Mangrove College")
    the_south_east_to_the_fathomkings_hold = world.get_entrance("The South East to The Fathomking's Hold")

    the_fathomkings_hold_to_the_distant_east = world.get_entrance("The Fathomking's Hold to The Distant East")
    visage_to_the_distant_east = world.get_entrance("Visage to The Distant East")
    the_uttershroom_to_the_distant_east = world.get_entrance("The Uttershroom to The Distant East")
    isle_of_cats_to_the_distant_east = world.get_entrance("Isle of Cats to The Distant East")
    mangrove_college_to_the_distant_east = world.get_entrance("Mangrove College to The Distant East")

    irem_to_the_distant_east = world.get_entrance("Irem to The Distant East")
    kingeaters_castle_to_the_distant_east = world.get_entrance("Kingeater's Castle to The Distant East")

    the_distant_east_to_empire_of_hands = world.get_entrance("The Distant East to Empire of Hands")
    the_distant_east_to_saviours_rocks = world.get_entrance("The Distant East to Saviours Rocks")
    the_distant_east_to_aestival = world.get_entrance("The Distant East to Aestival")
    the_distant_east_to_the_chelonate = world.get_entrance("The Distant East to The Chelonate")

    #I added trade regions, so I have to bring those up here, I think.
    #fuck
    strange_catches_regions_to_irem = world.get_entrance("Irem Strange Catches")
    hunting_trophies_regions_to_fallen_london = world.get_entrance("Hunting Trophies")
    scintillack_regions_to_pigmote_isle = world.get_entrance("Pigmote Isle Scintillack")
    scintillack_regions_to_port_cecil = world.get_entrance("Port Cecil Scintillack")
    romantic_literature_regions_to_khans_heart = world.get_entrance("Khans Heart Romantic Literature")
    spider_silk_regions_to_khans_heart = world.get_entrance("Khans Heart Spider Silk")
    spider_silk_regions_to_saviours_rocks = world.get_entrance("Saviour's Rocks Spider Silk")
    zzoup_regions_to_mount_palmerston = world.get_entrance("Mount Palmerston Zzoup")
    mutersalt_regions_to_whither = world.get_entrance("Whither Mutersalt")
    devilbone_dice_regions_to_mount_palmerston = world.get_entrance("Mount Palmerston Devilbone Dice")
    outlandish_artefacts_regions_to_khans_shadow = world.get_entrance("Khans Shadow Outlandish Artefacts")
    outlandish_artefacts_regions_to_mount_palmerston = world.get_entrance("Mount Palmerston Outlandish Artefacts")
    outlandish_artefacts_regions_to_varchas = world.get_entrance("Varchas Outlandish Artefacts")
    outlandish_artefacts_regions_to_whither = world.get_entrance("Whither Outlandish Artefacts")
    outlandish_artefacts_regions_to_codex = world.get_entrance("Codex Outlandish Artefacts")
    outlandish_artefacts_regions_to_frostfound = world.get_entrance("Frostfound Outlandish Artefacts")
    outlandish_artefacts_regions_to_chapel_of_lights = world.get_entrance("Chapel of Lights Outlandish Artefacts")
    outlandish_artefacts_regions_to_avid_horizon = world.get_entrance("Avid Horizon Outlandish Artefacts")
    parabola_linen_regions_to_irem = world.get_entrance("Irem Parabola Linen")
    stygian_ivory_regions_to_the_chelonate = world.get_entrance("The Chelonate Stygian Ivory")
    stygian_ivory_regions_to_khans_shadow = world.get_entrance("Khan's Shadow Stygian Ivory")
    sapphires_regions_to_port_carnelian = world.get_entrance("Port Carnelian Sapphires")
    fluke_core_regions_to_the_fathomkings_hold = world.get_entrance("The Fathomkings Hold Fluke Core")
    fluke_core_regions_to_aestival = world.get_entrance("Aestival Fluke Core")
    fluke_core_regions_to_empire_of_hands = world.get_entrance("Empire of Hands Fluke Core")
    fluke_core_regions_to_the_chelonate = world.get_entrance("The Chelonate Fluke Core")
    lamentable_relics_regions_to_mount_palmerston = world.get_entrance("Mount Palmerston Lamentable Relics")
    lamentable_relics_regions_to_adams_way = world.get_entrance("Adam's Way Lamentable Relics")
    darkdrop_coffee_regions_to_adams_way = world.get_entrance("Adam's Way Darkdrop Coffee")
    darkdrop_coffee_regions_to_port_carnelian = world.get_entrance("Port Carnelian Darkdrop Coffee")
    darkdrop_coffee_regions_to_khans_heart = world.get_entrance("Khan's Heart Darkdrop Coffee")

    if world.option.port_access_rules:

        set_rule(west_coast_to_venderbight, lambda state: state.has("Venderbight: Port Access", world.player))
        set_rule(venderbight_to_the_frozen_north, lambda state: state.has("Venderbight: Port Access", world.player))
        #Another long one... f_ck.
        #And I may have to go back and make trade events later... Double f_ck

        set_rule(west_coast_to_whither, lambda state: state.has("Whither: Port Access", world.player))
        set_rule(whither_to_the_frozen_north, lambda state: state.has("Whither: Port Access", world.player))

        set_rule(west_coast_to_codex, lambda state: state.has("Codex: Port Access", world.player))
        set_rule(codex_to_the_frozen_north, lambda state: state.has("Codex: Port Access", world.player))
        #ok, it's not as bad as I feared, I can do these in the batches I set up easily enough.
        #wish I could just lock regions tho

        set_rule(west_coast_to_iron_republic, lambda state: state.has("Iron Republic: Port Access", world.player))
        set_rule(iron_republic_to_south_coast, lambda state: state.has("Iron Republic: Port Access", world.player))
        set_rule(iron_republic_to_the_south_east, lambda state: state.has("Iron Republic: Port Access", world.player))

        set_rule(west_coast_to_grand_geode, lambda state: state.has("Grand Geode: Port Access", world.player))
        set_rule(grand_geode_to_south_coast, lambda state: state.has("Grand Geode: Port Access", world.player))
        set_rule(grand_geode_to_the_south_east, lambda state: state.has("Grand Geode: Port Access", world.player))
        #I say it's not that bad, but I think I have to do this 35ish more times? balls

        set_rule(fallen_london_to_cumaean_canal, lambda state: state.has("Cumaean Canal: Port Access", world.player))
        set_rule(fallen_london_to_hunters_keep, lambda state: state.has("Hunter's Keep: Port Access", world.player))
        set_rule(fallen_london_to_mutton_island, lambda state: state.has("Mutton Island: Port Access", world.player))

        set_rule(new_home_waters_to_station_iii, lambda state: state.has("Station III: Port Access", world.player))
        set_rule(station_iii_to_the_frozen_north, lambda state: state.has("Station III: Port Access", world.player))
        set_rule(station_iii_to_the_north_east, lambda state: state.has("Station III: Port Access", world.player))
        set_rule(station_iii_to_the_south_east, lambda state: state.has("Station III: Port Access", world.player))

        set_rule(new_home_waters_to_shepherd_isles, lambda state: state.has("Shepherd Isles: Port Access", world.player))
        set_rule(shepherd_isles_to_the_frozen_north, lambda state: state.has("Shepherd Isles: Port Access", world.player))
        set_rule(shepherd_isles_to_the_north_east, lambda state: state.has("Shepherd Isles: Port Access", world.player))
        set_rule(shepherd_isles_to_the_south_east, lambda state: state.has("Shepherd Isles: Port Access", world.player))

        set_rule(new_home_waters_to_abbey_rock, lambda state: state.has("Abbey Rock: Port Access", world.player))
        set_rule(abbey_rock_to_the_frozen_north, lambda state: state.has("Abbey Rock: Port Access", world.player))
        set_rule(abbey_rock_to_the_north_east, lambda state: state.has("Abbey Rock: Port Access", world.player))
        set_rule(abbey_rock_to_the_south_east, lambda state: state.has("Abbey Rock: Port Access", world.player))

        set_rule(new_home_waters_to_pigmote_isle, lambda state: state.has("Pigmote Isle: Port Access", world.player))
        set_rule(pigmote_isle_to_the_frozen_north, lambda state: state.has("Pigmote Isle: Port Access", world.player))
        set_rule(pigmote_isle_to_the_north_east, lambda state: state.has("Pigmote Isle: Port Access", world.player))
        set_rule(pigmote_isle_to_the_south_east, lambda state: state.has("Pigmote Isle: Port Access", world.player))

        set_rule(new_home_waters_to_salt_lions, lambda state: state.has("Salt Lions: Port Access", world.player))
        set_rule(salt_lions_to_the_frozen_north, lambda state: state.has("Salt Lions: Port Access", world.player))
        set_rule(salt_lions_to_the_north_east, lambda state: state.has("Salt Lions: Port Access", world.player))
        set_rule(salt_lions_to_the_south_east, lambda state: state.has("Salt Lions: Port Access", world.player))

        set_rule(new_home_waters_to_demeaux_island, lambda state: state.has("Demeaux Island: Port Access", world.player))
        set_rule(demeaux_island_to_the_frozen_north, lambda state: state.has("Demeaux Island: Port Access", world.player))
        set_rule(demeaux_island_to_the_north_east, lambda state: state.has("Demeaux Island: Port Access", world.player))
        set_rule(demeaux_island_to_the_south_east, lambda state: state.has("Demeaux Island: Port Access", world.player))

        set_rule(new_home_waters_to_gaiders_mourn, lambda state: state.has("Gaider's Mourn: Port Access", world.player))
        set_rule(gaiders_mourn_to_the_frozen_north, lambda state: state.has("Gaider's Mourn: Port Access", world.player))
        set_rule(gaiders_mourn_to_the_north_east, lambda state: state.has("Gaider's Mourn: Port Access", world.player))
        set_rule(gaiders_mourn_to_the_south_east, lambda state: state.has("Gaider's Mourn: Port Access", world.player))

        set_rule(the_frozen_north_to_chapel_of_lights, lambda state: state.has("Chapel of Lights: Port Access", world.player))
        set_rule(chapel_of_lights_to_irem, lambda state: state.has("Chapel of Lights: Port Access", world.player))
        set_rule(chapel_of_lights_to_the_north_east, lambda state: state.has("Chapel of Lights: Port Access", world.player))

        set_rule(the_frozen_north_to_avid_horizon, lambda state: state.has("Avid Horizon: Port Access", world.player))
        set_rule(avid_horizon_to_irem, lambda state: state.has("Avid Horizon: Port Access", world.player))
        set_rule(avid_horizon_to_the_north_east, lambda state: state.has("Avid Horizon: Port Access", world.player))

        set_rule(the_frozen_north_to_mount_palmerston, lambda state: state.has("Mount Palmerston: Port Access", world.player))
        set_rule(mount_palmerston_to_irem, lambda state: state.has("Mount Palmerston: Port Access", world.player))
        set_rule(mount_palmerston_to_the_north_east, lambda state: state.has("Mount Palmerston: Port Access", world.player))

        set_rule(the_frozen_north_to_frostfound, lambda state: state.has("Frostfound: Port Access", world.player))
        set_rule(frostfound_to_irem, lambda state: state.has("Frostfound: Port Access", world.player))
        set_rule(frostfound_to_the_north_east, lambda state: state.has("Frostfound: Port Access", world.player))

        set_rule(south_coast_to_varchas, lambda state: state.has("Varchas: Port Access", world.player))
        set_rule(varchas_to_kingeaters_castle, lambda state: state.has("Varchas: Port Access", world.player))
        set_rule(varchas_to_the_south_east, lambda state: state.has("Varchas: Port Access", world.player))

        set_rule(south_coast_to_adams_way, lambda state: state.has("Adam's Way: Port Access", world.player))
        set_rule(adams_way_to_kingeaters_castle, lambda state: state.has("Adam's Way: Port Access", world.player))
        set_rule(adams_way_to_the_south_east, lambda state: state.has("Adam's Way: Port Access", world.player))

        set_rule(south_coast_to_port_carnelian, lambda state: state.has("Port Carnelian: Port Access", world.player))
        set_rule(port_carnelian_to_kingeaters_castle, lambda state: state.has("Port Carnelian: Port Access", world.player))
        set_rule(port_carnelian_to_the_south_east, lambda state: state.has("Port Carnelian: Port Access", world.player))

        set_rule(the_north_east_to_khans_glory, lambda state: state.has("Khan's Glory: Port Access", world.player))
        set_rule(khans_glory_to_the_south_east, lambda state: state.has("Khan's Glory: Port Access", world.player))
        set_rule(khans_glory_to_the_distant_east, lambda state: state.has("Khan's Glory: Port Access", world.player))

        set_rule(the_north_east_to_khans_heart, lambda state: state.has("Khan's Heart: Port Access", world.player))
        set_rule(khans_heart_to_the_south_east, lambda state: state.has("Khan's Heart: Port Access", world.player))
        set_rule(khans_heart_to_the_distant_east, lambda state: state.has("Khan's Heart: Port Access", world.player))

        set_rule(the_north_east_to_khans_shadow, lambda state: state.has("Khan's Shadow: Port Access", world.player))
        set_rule(khans_shadow_to_the_south_east, lambda state: state.has("Khan's Shadow: Port Access", world.player))
        set_rule(khans_shadow_to_the_distant_east, lambda state: state.has("Khan's Shadow: Port Access", world.player))

        set_rule(the_north_east_to_nuncio, lambda state: state.has("Nuncio: Port Access", world.player))
        set_rule(nuncio_to_the_south_east, lambda state: state.has("Nuncio: Port Access", world.player))
        set_rule(nuncio_to_the_distant_east, lambda state: state.has("Nuncio: Port Access", world.player))

        set_rule(the_north_east_to_godfall, lambda state: state.has("Godfall: Port Access", world.player))
        set_rule(godfall_to_the_south_east, lambda state: state.has("Godfall: Port Access", world.player))
        set_rule(godfall_to_the_distant_east, lambda state: state.has("Godfall: Port Access", world.player))

        set_rule(the_north_east_to_polythreme, lambda state: state.has("Polythreme: Port Access", world.player))
        set_rule(polythreme_to_the_south_east, lambda state: state.has("Polythreme: Port Access", world.player))
        set_rule(polythreme_to_the_distant_east, lambda state: state.has("Polythreme: Port Access", world.player))

        set_rule(the_north_east_to_wisdom, lambda state: state.has("Wisdom: Port Access", world.player))
        set_rule(wisdom_to_the_south_east, lambda state: state.has("Wisdom: Port Access", world.player))
        set_rule(wisdom_to_the_distant_east, lambda state: state.has("Wisdom: Port Access", world.player))

        set_rule(the_north_east_to_port_cecil, lambda state: state.has("Port Cecil: Port Access", world.player))
        set_rule(port_cecil_to_the_south_east, lambda state: state.has("Port Cecil: Port Access", world.player))
        set_rule(port_cecil_to_the_distant_east, lambda state: state.has("Port Cecil: Port Access", world.player))

        set_rule(the_south_east_to_visage,lambda state: state.has("Visage: Port Access", world.player))
        set_rule(visage_to_the_distant_east, lambda state: state.has("Visage: Port Access", world.player))

        set_rule(the_south_east_to_isle_of_cats,lambda state: state.has("Isle of Cats: Port Access", world.player))
        set_rule(isle_of_cats_to_the_distant_east, lambda state: state.has("Isle of Cats: Port Access", world.player))

        set_rule(the_south_east_to_mangrove_college,lambda state: state.has("Mangrove College: Port Access", world.player))
        set_rule(mangrove_college_to_the_distant_east, lambda state: state.has("Mangrove College: Port Access", world.player))

        set_rule(the_south_east_to_the_uttershroom,lambda state: state.has("The Uttershroom: Port Access", world.player))
        set_rule(the_uttershroom_to_the_distant_east, lambda state: state.has("The Uttershroom: Port Access", world.player))

        set_rule(the_south_east_to_the_fathomkings_hold,lambda state: state.has("The Fathomkings Hold: Port Access", world.player))
        set_rule(the_fathomkings_hold_to_the_distant_east, lambda state: state.has("The Fathomkings Hold: Port Access", world.player))

        set_rule(frostfound_to_irem, lambda state: state.has("Irem: Port Access", world.player))
        set_rule(avid_horizon_to_irem, lambda state: state.has("Irem: Port Access", world.player))
        set_rule(chapel_of_lights_to_irem, lambda state: state.has("Irem: Port Access", world.player))
        set_rule(mount_palmerston_to_irem, lambda state: state.has("Irem: Port Access", world.player))
        set_rule(irem_to_the_distant_east, lambda state: state.has("Irem: Port Access", world.player))

        set_rule(port_carnelian_to_kingeaters_castle, lambda state: state.has("Kingeater's Castle: Port Access", world.player))
        set_rule(adams_way_to_kingeaters_castle, lambda state: state.has("Kingeater's Castle: Port Access", world.player))
        set_rule(varchas_to_kingeaters_castle, lambda state: state.has("Kingeater's Castle: Port Access", world.player))
        set_rule(kingeaters_castle_to_the_distant_east, lambda state: state.has("Kingeater's Castle: Port Access", world.player))

        set_rule(the_distant_east_to_aestival, lambda state: state.has("Aestival: Port Access", world.player))
        set_rule(the_distant_east_to_saviours_rocks, lambda state: state.has("Saviour's Rocks: Port Access", world.player))
        set_rule(the_distant_east_to_the_chelonate, lambda state: state.has("The Chelonate: Port Access", world.player))
        set_rule(the_distant_east_to_empire_of_hands, lambda state: state.has("Empire Of Hands: Port Access", world.player))
        #phew. Do I do this again with Sea Regions? Not now.
        #I'm doing it all again for trade logic though. Not a lot of it, but enough

        set_rule(darkdrop_coffee_regions_to_khans_heart, lambda state: state.has("Nephrite Ring", world.player))
        set_rule(spider_silk_regions_to_khans_heart, lambda state: state.has("Nephrite Ring", world.player))
        set_rule(romantic_literature_regions_to_khans_heart, lambda state: state.has("Nephrite Ring", world.player))

        #Were those the only 3? There's 1 I can find, but I'm not sure about any others. darn

        set_rule(outlandish_artefacts_regions_to_varchas, lambda state: state.has("Source of Scintillack", world.player))

        if world.options.equipment_required:

            set_rule(outlandish_artefacts_regions_to_codex ,lambda state: state.has_all(("Progressive Deck Gun Deed", "Progressive Engine Deed", "Progressive Ship Deed"), world.player))
            set_rule(outlandish_artefacts_regions_to_whither ,lambda state: state.has_all(("Progressive Deck Gun Deed", "Progressive Engine Deed", "Progressive Ship Deed"), world.player))
            set_rule(outlandish_artefacts_regions_to_frostfound ,lambda state: state.has_all(("Progressive Deck Gun Deed", "Progressive Engine Deed", "Progressive Ship Deed"), world.player))
            set_rule(outlandish_artefacts_regions_to_avid_horizon ,lambda state: state.has_all(("Progressive Deck Gun Deed", "Progressive Engine Deed", "Progressive Ship Deed"), world.player))
            set_rule(outlandish_artefacts_regions_to_chapel_of_lights ,lambda state: state.has_all(("Progressive Deck Gun Deed", "Progressive Engine Deed", "Progressive Ship Deed"), world.player))

def set_all_location_rules(world: SunlessSeaWorld) -> None:

    venture_strange_catches = world.get_location("Merchant Venturer: Seven Strange Catches")
    venture_hunting_trophies = world.get_location("Merchant Venturer: Seven Hunting Trophies")
    venture_scintillack = world.get_location("Merchant Venturer: Seven Pieces of Scintillack")
    venture_romantic_literature = world.get_location("Merchant Venturer: Seven Volumes of Romantic literature")
    venture_spider_silk = world.get_location("Merchant Venturer: Seven Bolts of Spider-Silk")
    venture_zzoup = world.get_location("Merchant Venturer: Seven Skins of Zzoup")
    venture_mutersalt = world.get_location("Merchant Venturer: Seven Packages of Mutersalt")
    venture_devilbone_dice = world.get_location("Merchant Venturer: Seven Devilbone Dice")
    venture_outlandish_artefacts = world.get_location("Merchant Venturer: Seven Outlandish Artefacts")
    venture_parabola_linen = world.get_location("Merchant Venturer: Seven Bales of Parabola-Linen")
    venture_stygian_ivory = world.get_location("Merchant Venturer: Seven Pieces of Stygian Ivory")
    venture_sapphires = world.get_location("Merchant Venturer: Seven Caskets of Sapphires")
    venture_lorn_fluke = world.get_location("Merchant Venturer: One Lorn-Fluke Core")
    venture_lamentable_relics = world.get_location("Merchant Venturer: Seven Lamentable Relics")
    venture_darkdrop_coffee = world.get_location("Merchant Venturer: Seven Sacks of Darkdrop Coffee")

    #I'm realsing a lot of these could be general rules, which are then brought up to signal if something can be obtained.
    #It would be more work now, for less work later? Maybe. let me get those set up.

    strange_catches_source = world.get_location("Strange Catches Location")
    hunting_trophies_source = world.get_location("Hunting Trophies Location")
    scintillack_source = world.get_location("Scintillack Location")
    romantic_literature_source = world.get_location("Romantic Literature Location")
    spider_silk_source = world.get_location("Spider-Silk Location")
    zzoup_source = world.get_location("Zzoup Location")
    mutersalt_source = world.get_location("Mutersalt Location")
    devilbone_dice_source = world.get_location("Devilbone Dice Location")
    outlandish_artefacts_source = world.get_location("Outlandish Artefacts Location")
    parabola_linen_source = world.get_location("Parabola-Linen Location")
    stygian_ivory_source = world.get_location("Stygian Ivory Location")
    sapphires_source = world.get_location("Sapphires Location")
    fluke_core_source = world.get_location("Fluke-Core Location")
    lamentable_relics_source = world.get_location("Lamentable Relics Location")
    darkdrop_coffee_source = world.get_location("Darkdrop Coffee Location")

    #I've ended up bypassing the need for these here, but I'll keep them around for now

    #late addition but nephrite ring needs location stuff. Probably. was just going to let it be but if we have 12 more locations for it then sure.
    nephrite_ring_location = world.get_location("Purchase Nephrite Ring")

    if world.options.equipment_required:
    #decided this could be an option, and would eleviate any problems involved with it.

        set_rule(fluke_core_source, lambda state: (state.has_all(("Progressive Deck Gun Deed", "Progressive Engine Deed", "Progressive Ship Deed"),world.player)))

        set_rule(hunting_trophies_source, lambda state: (state.has_all(("Progressive Deck Gun Deed", "Progressive Engine Deed", "Progressive Ship Deed"),world.player)))

    #And now for the Merchant Venture Checks
    set_rule(venture_strange_catches, lambda state: (state.has("Source of Strange Catches", world.player)))

    set_rule(venture_hunting_trophies, lambda state: (state.has("Source of Hunting Trophies", world.player)))

    set_rule(venture_scintillack, lambda state: (state.has("Source of Scintillack", world.player)))

    set_rule(venture_romantic_literature, lambda state: (state.has("Source of Romantic Literature", world.player)))

    set_rule(venture_spider_silk, lambda state: (state.has("Source of Spider-Silk", world.player)))

    set_rule(venture_zzoup, lambda state: (state.has("Source of Zzoup", world.player)))

    set_rule(venture_mutersalt, lambda state: (state.has("Source of Mutersalt", world.player)))

    set_rule(venture_devilbone_dice, lambda state: (state.has("Source of Devilbone Dice", world.player)))

    set_rule(venture_outlandish_artefacts, lambda state: (state.has("Source of Outlandish Artefacts", world.player)))

    set_rule(venture_parabola_linen, lambda state: (state.has("Source of Parabola-Linen", world.player)))

    set_rule(venture_stygian_ivory, lambda state: (state.has("Source of Stygian Ivory", world.player)))

    set_rule(venture_sapphires, lambda state: (state.has("Source of Sapphires", world.player)))

    set_rule(venture_lorn_fluke, lambda state: (state.has("Source of Fluke-Core", world.player)))

    set_rule(venture_lamentable_relics, lambda state: (state.has("Source of Lamentable Relics", world.player)))

    set_rule(venture_darkdrop_coffee, lambda state: (state.has("Source of Darkdrop Coffee", world.player)))
    #Will this work? We'll find out

    set_rule(nephrite_ring_location, lambda state: (state.has("Source of Darkdrop Coffee", world.player)))
    #also this. not going to bother with Drowning-Pearl logic. yet.

def set_completion_condition(world: SunlessSeaWorld) -> None:

        world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)