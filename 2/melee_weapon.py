import weapon
class melee_weapon(weapon.weapon):
    def __init__(self, attack, defence, attack_range):
        super().__init__(attack, attack_range)
        self.defence=defence

    def print_stats(self):
        print(f"Attack: {self.attack}" )
        print(f"Defence: {self.defence}")
        print(f"Range: {self.attack_range}")