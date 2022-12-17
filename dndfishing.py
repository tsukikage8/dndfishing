# abstract:
# series of questions
# are you in freshwater?
# what is your location (input island name)
# near a shipwreck?
# in a battle?
# in a storm?
# what time of day?
# create table of options (species, color, rarity)
# base variant, day/night, uncommon, rare
# output what fish is caught

from random import randint
import FishInfo


def roll_d20():
    roll = randint(1, 20)
    return roll


class Fishing:

    print("So, your players decided to go fishing AGAIN?")

    def __init__(self):
        self._fish_list = None
        self._freshwater = None
        self._time = None
        self._common = []
        self._day = []
        self._night = []
        self._uncommon = []
        self._rare = []

    def build_list(self):
        freshwater = input("Are you currently in freshwater? Type yes or no: ")
        if freshwater.lower() == 'yes':
            self._fish_list = FishInfo.freshwater()
            self._freshwater = 'Y'
        if freshwater.lower() == 'no':
            self._fish_list = FishInfo.saltwater()
            print(self._fish_list)
        current_time = input("Is it day or night? ")
        if current_time.lower() == 'day':
            self._time = 'D'
        if current_time.lower() == 'night':
            self._time = 'N'
        for fish in self._fish_list:
            rarity = fish.get_rarity()
            if rarity == 'common':
                self._common.append(fish)
            elif rarity == 'day':
                self._day.append(fish)
            elif rarity == 'night':
                self._night.append(fish)
            elif rarity == 'uncommon':
                self._uncommon.append(fish)
            elif rarity == 'rare':
                self._rare.append(fish)

    def go_fishing(self):
        print("Time to go fishing!")
        num_fish = int(input("How many fish are you rolling for? "))
        caught_fish = []
        for i in range(num_fish + 1):  # for each roll
            rarity_roll = roll_d20()  # rolls for rarity
            if rarity_roll >= 18:
                fish = len(self._rare)
                roll = randint(1, fish)
                what_was_caught = self._rare[roll]
                caught_fish.append(what_was_caught)
            elif rarity_roll >= 13:
                fish = len(self._uncommon)
                roll = randint(1, fish)
                what_was_caught = self._uncommon[roll]
                caught_fish.append(what_was_caught)
            elif rarity_roll >= 7:
                if self._time == 'D':
                    fish = len(self._day)
                    roll = randint(1, fish)
                    what_was_caught = self._day[roll]
                    caught_fish.append(what_was_caught)
                if self._time == 'N':
                    fish = len(self._night)
                    roll = randint(1, fish)
                    what_was_caught = self._night[roll]
                    caught_fish.append(what_was_caught)
            else:
                fish = len(self._common)
                roll = randint(1, fish)
                what_was_caught = self._common[roll]
                caught_fish.append(what_was_caught)
        print(caught_fish)
        return caught_fish


newgame = Fishing()
newgame.build_list()
newgame.go_fishing()
