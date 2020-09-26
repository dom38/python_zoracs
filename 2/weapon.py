class weapon:
    def __init__(self, attack, attack_range):
        print('Class init.')
        self.attack = attack
        self.attack_range = attack_range
        print('Finished class init.')

    def print_stats(self):
        print(f"Attack: {self.attack}" )
        print(f"Range: {self.attack_range}")