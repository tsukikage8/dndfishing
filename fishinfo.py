class Fish:
    def __init__(self, species, color, rarity):
        self._species = species
        self._color = color
        self._rarity = rarity

    def get_species(self):
        return self._species

    def get_color(self):
        return self._color

    def get_rarity(self):
        return self._rarity


def freshwater():
    pondie_common = Fish('pondie', 'charcoal', 'common')
    pondie_day = Fish('pondie', 'orchid', 'day')
    pondie_night = Fish('pondie', 'bronze', 'night')
    pondie_uncommon = Fish('pondie', 'bright', 'uncommon')
    pondie_rare = Fish('pondie', 'moonsky', 'rare')
    freshwater_list = [pondie_common, pondie_day, pondie_night, pondie_uncommon, pondie_rare]
    return freshwater_list


def saltwater():
    splash_common = Fish('splashtail', 'ruby', 'common')
    splash_day = Fish('splashtail', 'sunny', 'day')
    splash_night = Fish('splashtail', 'seafoam', 'night')
    splash_uncommon = Fish('splashtail', 'indigo', 'uncommon')
    splash_rare = Fish('splashtail', 'umber', 'rare')
    saltwater_list = [splash_common, splash_day, splash_night, splash_uncommon, splash_rare]
    return saltwater_list

