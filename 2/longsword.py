class longsword:
    def __init__(self, attack, defence, attack_range):
        self.attack = attack
        self.defence = defence
        self.attack_range = attack_range

    def print_stats(self):
        print(f"Attack: {self.attack}" )
        print(f"Defence: {self.defence}")
        print(f"Range: ${self.attack_range}")
