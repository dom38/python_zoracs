import weapon
class ranged_weapon(weapon.weapon):
    def __init__(self, attack, attack_range, quiver_capacity):
        super().__init__(attack, attack_range)
        self.quiver_capacity=quiver_capacity

    def print_stats(self):
        print(f"Attack: {self.attack}" )
        print(f"Range: {self.attack_range}")
        print(f"Shots: {self.quiver_capacity}")
        