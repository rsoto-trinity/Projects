import random
from natures import Nature, natures
from weather import Weather,WeatherManager,Sunny,battle_weather
class Pokemon:
    def __init__(self, name, level, base_stats, moves, types, ability=None, nature=None, evs=None, ivs=None):
        self.name = name
        self.level = level
        self.base_hp, self.base_attack, self.base_defense, self.base_speed, self.base_special_attack, self.base_special_defense = base_stats
        self.moves = moves
        self.types = types
        self.nature = nature if nature else random.choice(natures)
        self.ability = ability
        self.status = None
        self.sleep_turns = 0
        self.wins = 0

        self.evs = evs if evs else self.generate_random_evs()
        self.ivs = ivs if ivs else self.generate_random_ivs()

        self.calculate_stats()
        
    def reduce_stat(self, stat_name, amount):
        if stat_name == 'attack':
            self.attack -= amount
            print(f"{self.name}'s Attack stat decreased by {amount}!")
        elif stat_name == 'defense':
            self.defense -= amount
            print(f"{self.name}'s Defense stat decreased by {amount}!")
        elif stat_name == 'speed':
            self.speed -= amount
            print(f"{self.name}'s Speed stat decreased by {amount}!")
        elif stat_name == 'special_attack':
            self.special_attack -= amount
            print(f"{self.name}'s Special Attack stat decreased by {amount}!")
        elif stat_name == 'special_defense':
            self.special_defense -= amount
            print(f"{self.name}'s Special Defense stat decreased by {amount}!")
        else:
            print(f"Invalid stat name: {stat_name}")
    def calculate_stats(self):
        self.max_hp = int(((2 * self.base_hp + self.ivs['hp'] + self.evs['hp'] / 4) * self.level) / 100 + self.level + 10)
        self.hp = self.max_hp

        self.attack = self.apply_nature_effect('attack', int(((2 * self.base_attack + self.ivs['attack'] + self.evs['attack'] / 4) * self.level) / 100 + 5))
        self.defense = self.apply_nature_effect('defense', int(((2 * self.base_defense + self.ivs['defense'] + self.evs['defense'] / 4) * self.level) / 100 + 5))
        self.speed = self.apply_nature_effect('speed', int(((2 * self.base_speed + self.ivs['speed'] + self.evs['speed'] / 4) * self.level) / 100 + 5))
        self.special_attack = self.apply_nature_effect('special_attack', int(((2 * self.base_special_attack + self.ivs['special_attack'] + self.evs['special_attack'] / 4) * self.level) / 100 + 5))
        self.special_defense = self.apply_nature_effect('special_defense', int(((2 * self.base_special_defense + self.ivs['special_defense'] + self.evs['special_defense'] / 4) * self.level) / 100 + 5))

    def apply_nature_effect(self, stat_name, stat_value):
        if self.nature.increased_stat == stat_name:
            return int(stat_value * 1.1)
        elif self.nature.decreased_stat == stat_name:
            return int(stat_value * 0.9)
        else:
            return stat_value
    
    def generate_random_evs(self):
        return {stat: random.randint(0, 255) for stat in ['hp', 'attack', 'defense', 'speed', 'special_attack', 'special_defense']}
    
    def generate_random_ivs(self):
        return {stat: random.randint(0, 31) for stat in ['hp', 'attack', 'defense', 'speed', 'special_attack', 'special_defense']}

    def is_fainted(self):
        return self.hp <= 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        print(f"{self.name} took {damage} damage and has {self.hp} HP left.")

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} healed for {amount} HP and has {self.hp} HP now.")

    def reset(self):
        self.hp = self.max_hp
        self.status = None

    def apply_ability(self, opponent, move=None):
        if self.ability:
            if self.ability.name == "Thick Fat" and move is not None:
                self.ability.apply(self, move)
            else:
                self.ability.apply(self, opponent)

    def apply_status(self, status):
        if self.status is None:
            self.status = status
            if status == 'Asleep':
                self.sleep_turns = random.randint(1, 3)
            print(f"{self.name} is now {status}!")

    def check_status_effect(self):
        if self.status == 'Paralyzed':
            self.current_speed = self.speed // 2
            if random.random() < 0.25:
                print(f"{self.name} is paralyzed and can't move!")
                return False
        elif self.status == 'Burned':
            self.current_attack = self.attack // 2
            burn_damage = self.max_hp // 16
            self.take_damage(burn_damage)
            print(f"{self.name} is hurt by its burn!")
        elif self.status == 'Asleep':
            if self.sleep_turns > 0:
                print(f"{self.name} is asleep and can't move!")
                self.sleep_turns -= 1
                return False
            else:
                self.status = None
                print(f"{self.name} woke up!")
        elif self.status == 'Poisoned':
            poison_damage = self.max_hp // 8
            self.take_damage(poison_damage)
            print(f"{self.name} is hurt by the poison!")
        elif self.status == 'Badly Poisoned':
            poison_damage = (self.max_hp // 16) * self.poison_turns
            self.take_damage(poison_damage)
            print(f"{self.name} is hurt by its poison!")
            self.poison_turns += 1
        elif self.status == 'Frozen':
            if random.random() < 0.2:
                print(f"{self.name} is frozen and can't move!")
                return False
        return True

