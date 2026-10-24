from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


# For our game to display correctly on the website, we need to define a WebWorld subclass.
class SunlessSeaWebWorld(WebWorld):
    # We need to override the "game" field of the WebWorld superclass.
    # This must be the same string as the regular World class.
    game = "SunlessSea"

    theme = "ocean"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Sunless Sea for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Curndle"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets