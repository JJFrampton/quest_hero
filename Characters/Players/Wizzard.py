class Wizzard(Player):
    def __init__(self, name):
        self.stats_attack = 1
        self.stats_defend = 2
        self.stats_body = 4
        self.stats_mind = 6
        self.stats_move = 2
        self.stats_weapon = "daggar"
        self.stats_armour = None
        self.stats_name = name
        print("initialized")
