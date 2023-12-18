import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(script_dir)

data_dir = os.path.join(parent_dir, 'data')

csv_file_path = os.path.join(data_dir, 'Wincons.csv')

win_cons = pd.read_csv(csv_file_path)["card_name"][0:24].to_list()



defenders = ['Bowler', 'Giant Skeleton', 'Inferno Dragon', 'Barbarians', 'Sparky', 'Ice Wizard', 'Ice Golem', 'Guards']

attackers = ["Mini P.E.K.K.A", 'Hog Rider', 'Prince', 'Balloon', 'Miner', 'Minions', 'Elite Barbarians', 'Royal Giant', 'Three Musketeers', 'Goblins']

skirmishers = ['Lumberjack', 'Knight', 'Valkyrie', 'Electro Wizard', 'Dark Prince', 'Dart Goblin', 'Minion Horde', 'Goblin Gang', 'Skeletons', 'Skeleton Army', 'Fire Spirit', 'Bandit', 'Night Witch', 'Ice Spirit', 'Bats', 'Princess', 'Fire Spirit', 'Electro Spirit', 'Heal Spirit']

tanks = ["P.E.K.K.A.", 'Giant', 'Lavahound', 'Golem']

spell_names = [
    "Arrows", "Barbarian Barrel", "Earthquake", "Fireball",
    "Freeze", "Giant Snowball", "Lightning", "Poison",
    "Rage", "Rocket", "Royal Delivery", "The Log",
    "Tornado", "Zap", "Mirror", "Graveyard", "Clone"]

building_names = [
    "Bomb Tower", "Cannon", "Cannon Cart", "Inferno Tower",
    "Mortar", "Tesla", "X-Bow", "Barbarian Hut", "Elixir Collector",
    "Furnace", "Goblin Cage", "Goblin Hut",
    "Tombstone"]

troop_names = [
    "Archers", "Baby Dragon", "Balloon", "Bandit",
    "Barbarians", "Bats", "Battle Healer", "Battle Ram", "Bomber",
    "Bowler", "Dark Prince", "Dart Goblin",
    "Electro Dragon", "Electro Giant", "Electro Spirit", "Electro Wizard",
    "Elite Barbarians", "Elixir Golem",
    "Executioner", "Firecracker", "Fire Spirits", "Fisherman", "Flying Machine",
    "Giant", "Giant Skeleton", "Goblin Gang", "Goblin Giant",
    "Goblins", "Golem", "Guards", "Goblin Barrel", "Hog Rider",
    "Hunter", "Heal Spirit", "Ice Golem", "Ice Spirit", "Ice Wizard",
    "Inferno Dragon", "Knight", "Lava Hound", "Lumberjack",
    "Magic Archer", "Mega Knight", "Mega Minion", "Miner",
    "Mini P.E.K.K.A", "Minions", "Mother Witch", "Musketeer",
    "Night Witch", "P.E.K.K.A", "Prince", "Minion Horde",
    "Princess", "Ram Rider", "Rascals", "Royal Ghost",
    "Royal Giant", "Royal Hogs", "Royal Recruits", "Skeletons", "Skeleton Barrel",
    "Skeleton Dragons", "Sparky", "Spear Goblins", "Three Musketeers",
    "Valkyrie", "Wall Breakers", "Witch", "Wizard", 'Skeleton Army', "Zappies"]

troops = [troop for troop in troop_names if troop not in win_cons]

spells = [spell for spell in spell_names if spell not in win_cons]

buildings = [building for building in building_names if building not in win_cons]


aerial_troops = ['Bats', 'Electro Dragon', 'Flying Machine','Inferno Dragon', 'Minions', 'Minion Horde', 'Mega Minion','Skeleton Dragons',]

ground_troops = [troop for troop in troop_names if troop not in aerial_troops]

projectile_troops = ['Archers', 'Dart Goblin', 'Electro Wizard', 'Executioner',
 'Firecracker', 'Hunter', 'Ice Wizard', 'Magic Archer', 'Mother Witch', 'Princess',
 'Rascals', 'Spear Goblins', 'Witch','Wizard', 'Zappies']

melee_troops = [troop for troop in ground_troops if troop not in projectile_troops]