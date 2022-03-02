# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random
Dndraces_set = {"warforged", "human", "Dwarf", "Halfling", "Tiefling", "Owlin", "Dragonborn", "Genasi", "Kobold", "Kenku"}
DnDclass_set = {"Cleric", "Wizard", "Fighter", "Paladin", "Rouge", "Bard", "Barbarian", "Druid", "Warlock", "Sorcerer", "Artificer"}

class DnDRace:
    Race = random.choice(tuple(Dndraces_set))
    print(Race)

class DndClass:
    Class = random.choice(tuple(DnDclass_set))
    print(Class)

class DndStats:
    stat1 = random.randint(1,20)
    print(stat1)
    stat2 = random.randint(1, 20)
    print(stat2)
    stat3 = random.randint(1, 20)
    print(stat3)
    stat4 = random.randint(1, 20)
    print(stat4)
    stat5 = random.randint(1, 20)
    print(stat5)
    stat6 = random.randint(1, 20)
    print(stat6)
