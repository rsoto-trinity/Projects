import random
class Nature:
    def __init__(self, name, increased_stat, decreased_stat):
        self.name = name
        self.increased_stat = increased_stat
        self.decreased_stat = decreased_stat

natures = [
    Nature('Hardy', None, None), Nature('Lonely', 'attack', 'defense'),
    Nature('Brave', 'attack', 'speed'), Nature('Adamant', 'attack', 'special_attack'),
    Nature('Naughty', 'attack', 'special_defense'), Nature('Bold', 'defense', 'attack'),
    Nature('Docile', None, None), Nature('Relaxed', 'defense', 'speed'),
    Nature('Impish', 'defense', 'special_attack'), Nature('Lax', 'defense', 'special_defense'),
    Nature('Timid', 'speed', 'attack'), Nature('Hasty', 'speed', 'defense'),
    Nature('Serious', None, None), Nature('Jolly', 'speed', 'special_attack'),
    Nature('Naive', 'speed', 'special_defense'), Nature('Modest', 'special_attack', 'attack'),
    Nature('Mild', 'special_attack', 'defense'), Nature('Quiet', 'special_attack', 'speed'),
    Nature('Bashful', None, None), Nature('Rash', 'special_attack', 'special_defense'),
    Nature('Calm', 'special_defense', 'attack'), Nature('Gentle', 'special_defense', 'defense'),
    Nature('Sassy', 'special_defense', 'speed'), Nature('Careful', 'special_defense', 'special_attack'),
    Nature('Quirky', None, None)
]

class Pokemon:
    def __init__(self, name, level, hp, attack, defense, speed, special_attack, special_defense, moves, types, ability=None, nature = None ,evs=None, ivs=None):
        self.name = name
        self.level = level
        self.base_hp = hp
        self.base_attack = attack
        self.base_defense = defense
        self.base_speed = speed
        self.base_special_attack = special_attack
        self.base_special_defense = special_defense
        self.moves = moves
        self.types = types
        self.ability = ability
        self.status = None
        self.sleep_turns = 0  # Add this attribute to track sleep turns
        self.wins = 0

        # Initialize EVs and IVs
        self.evs = evs if evs else {'hp': 0, 'attack': 0, 'defense': 0, 'speed': 0, 'special_attack': 0, 'special_defense': 0}
        self.ivs = ivs if ivs else {'hp': random.randint(0, 31), 'attack': random.randint(0, 31), 'defense': random.randint(0, 31), 'speed': random.randint(0, 31), 'special_attack': random.randint(0, 31), 'special_defense': random.randint(0, 31)}

        # Calculate stats based on level, base stats, EVs, and IVs
        self.calculate_stats()

    def calculate_stats(self):
        # HP calculation is different from other stats
        self.max_hp = int(((2 * self.base_hp + self.ivs['hp'] + self.evs['hp'] / 4) * self.level) / 100 + self.level + 10)

        # Other stats formula
        self.attack = int(((2 * self.base_attack + self.ivs['attack'] + self.evs['attack'] / 4) * self.level) / 100 + 5)
        self.defense = int(((2 * self.base_defense + self.ivs['defense'] + self.evs['defense'] / 4) * self.level) / 100 + 5)
        self.speed = int(((2 * self.base_speed + self.ivs['speed'] + self.evs['speed'] / 4) * self.level) / 100 + 5)
        self.special_attack = int(((2 * self.base_special_attack + self.ivs['special_attack'] + self.evs['special_attack'] / 4) * self.level) / 100 + 5)
        self.special_defense = int(((2 * self.base_special_defense + self.ivs['special_defense'] + self.evs['special_defense'] / 4) * self.level) / 100 + 5)

    # Methods for modifying EVs and IVs could be added here
    def generate_random_evs(self):
        evs = {}
        for stat in ['hp', 'attack', 'defense', 'speed', 'special_attack', 'special_defense']:
            evs[stat] = random.randint(0, 255)  # Each stat can have up to 255 EVs
        return evs

    def generate_random_ivs(self):
        ivs = {}
        for stat in ['hp', 'attack', 'defense', 'speed', 'special_attack', 'special_defense']:
            ivs[stat] = random.randint(0, 31)  # Each IV can be from 0 to 31
        return ivs

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
        self.status = None  # Reset status condition

    def apply_ability(self, opponent):
        if self.ability:
            self.ability.apply(self, opponent)

    def apply_status(self, status):
        if self.status is None:  # Can only have one status condition at a time
            self.status = status
            if status == 'Asleep':
                self.sleep_turns = random.randint(1, 3)  # Sleep lasts 1-3 turns
            print(f"{self.name} is now {status}!")

    def check_status_effect(self):
        if self.status == 'Paralyzed':
            self.current_speed = self.speed // 2
            if random.random() < 0.25:  # 25% chance to be fully paralyzed
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
             print(f"{self.name} is hurt by the poison")
             return False
        elif self.status == 'Badly Poisoned':
            poison_damage = (self.max_hp // 16) * self.poison_turns
            self.take_damage(poison_damage)
            print(f"{self.name} is hurt by its poison!")
            self.poison_turns += 1
        elif self.status == 'Frozen':
              self.current_speed = self.speed // 2
              if random.random() < 0.80:  # 80% chance to be frozen
                print(f"{self.name} is Frozem and can't move!")
                return False
        return True

    def modify_attack(self, modifier):
        self.attack *= modifier

    def modify_defense(self, modifier):
        self.defense *= modifier

    def modify_speed(self, modifier):
        self.speed *= modifier

    def modify_special_attack(self, modifier):
        self.special_attack *= modifier

    def modify_special_defense(self, modifier):
        self.special_defense *= modifier

class Move:
    def __init__(self, name, move_type, power, accuracy, category, status_effect=None, status_chance=0.0):
        self.name = name
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.status_effect = status_effect
        self.status_chance = status_chance

class Ability:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply(self, pokemon, opponent):
        self.effect(pokemon, opponent)

type_chart = {
    'Normal': {'Fighting': 1.0, 'Ghost': 0.0},
    'Fighting': {'Normal': 2.0, 'Flying': 0.5, 'Poison': 0.5, 'Rock': 2.0, 'Bug': 0.5, 'Ghost': 0.0, 'Psychic': 0.5, 'Ice': 2.0, 'Dragon': 1.0, 'Dark': 2.0, 'Fairy': 0.5},
    'Flying': {'Fighting': 2.0, 'Rock': 2.0, 'Bug': 0.5, 'Grass': 0.5, 'Electric': 2.0},
    'Poison': {'Grass': 2.0, 'Poison': 0.5, 'Ground': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Steel': 0.0, 'Fairy': 2.0},
    'Ground': {'Flying': 0.0, 'Poison': 2.0, 'Rock': 2.0, 'Bug': 0.5, 'Fire': 2.0, 'Grass': 0.5, 'Electric': 2.0},
    'Rock': {'Fighting': 0.5, 'Flying': 0.5, 'Ground': 2.0, 'Bug': 2.0, 'Fire': 2.0, 'Ice': 2.0},
    'Bug': {'Fighting': 0.5, 'Flying': 2.0, 'Poison': 2.0, 'Ghost': 0.5, 'Steel': 0.5, 'Fire': 0.5, 'Grass': 2.0, 'Psychic': 2.0, 'Dark': 2.0, 'Fairy': 0.5},
    'Ghost': {'Normal': 0.0, 'Ghost': 2.0, 'Psychic': 2.0, 'Dark': 0.5},
    'Steel': {'Rock': 0.5, 'Steel': 0.5, 'Fire': 2.0, 'Water': 0.5, 'Electric': 0.5, 'Ice': 2.0, 'Fairy': 0.5},
    'Fire': {'Bug': 2.0, 'Steel': 0.5, 'Fire': 0.5, 'Water': 0.5, 'Rock': 2.0, 'Ground': 2.0, 'Grass': 2.0, 'Ice': 2.0, 'Fairy': 0.5},
    'Water': {'Steel': 0.5, 'Fire': 2.0, 'Water': 0.5, 'Grass': 0.5, 'Electric': 2.0, 'Ice': 0.5},
    'Grass': {'Flying': 2.0, 'Poison': 0.5, 'Ground': 2.0, 'Rock': 2.0, 'Bug': 0.5, 'Fire': 0.5, 'Water': 2.0, 'Grass': 0.5, 'Electric': 0.5},
    'Electric': {'Flying': 0.5, 'Ground': 0.0, 'Water': 2.0, 'Grass': 2.0, 'Electric': 0.5, 'Dragon': 0.5},
    'Psychic': {'Fighting': 2.0, 'Poison': 2.0, 'Psychic': 0.5, 'Dark': 0.0},
    'Ice': {'Flying': 2.0, 'Ground': 2.0, 'Grass': 2.0, 'Fire': 0.5, 'Water': 0.5, 'Ice': 0.5, 'Steel': 0.5},
    'Dragon': {'Dragon': 2.0, 'Steel': 0.5, 'Fairy': 0.0},
    'Dark': {'Fighting': 0.5, 'Ghost': 2.0, 'Psychic': 2.0, 'Dark': 0.5, 'Fairy': 0.5},
    'Fairy': {'Fighting': 2.0, 'Poison': 0.5, 'Steel': 2.0, 'Fire': 0.5, 'Dragon': 2.0, 'Dark': 2.0}
}

def type_effectiveness(move_type, defender_types):
    effectiveness = 1.0
    for defender_type in defender_types:
        if defender_type in type_chart.get(move_type, {}):
            effectiveness *= type_chart[move_type][defender_type]
    return effectiveness

def calculate_damage(attacker, defender, move):
    effectiveness = type_effectiveness(move.move_type, defender.types)
    modifier = random.uniform(0.85, 1.0) * effectiveness

    # Factor in STAB (Same Type Attack Bonus)
    stab_bonus = 1.5 if move.move_type in attacker.types else 1.0

    if move.category == 'Physical':
        attack_stat = attacker.attack
        defense_stat = defender.defense
    elif move.category == 'Special':
        attack_stat = attacker.special_attack
        defense_stat = defender.special_defense
    elif move.category == 'Status':
        return 0;
    else:
        raise ValueError("Invalid move category")

    damage = (((2 * attacker.level / 5 + 2) * move.power * (attack_stat / defense_stat)) / 50 + 2) * modifier * stab_bonus
    return int(damage)



def perform_move(attacker, defender, move):
    print(f"{attacker.name} used {move.name}!")

    # Check if the defender already has a status condition and if the move is a status move
    if defender.status and move.category == 'Status':
        print(f"{defender.name} already has a status condition and cannot be affected by another status move!")
        # Choose a different move from the attacker's moveset
        move = random.choice([m for m in attacker.moves if m.category != 'Status'])
        print(f"{attacker.name} chose {move.name} instead.")

    if random.random() <= move.accuracy:
        if attacker.check_status_effect():
            damage = calculate_damage(attacker, defender, move)
            defender.take_damage(damage)
            # Check if move has a chance to inflict a status condition
            if move.status_effect and random.random() < move.status_chance:
                defender.apply_status(move.status_effect)
            # Check for abilities that activate on contact (e.g., Static)
            if move.category in ['Physical']:
                defender.apply_ability(attacker)
    else:
        print(f"{attacker.name}'s attack missed!")

def battle(pokemon1, pokemon2):
    pokemon1.reset()
    pokemon2.reset()
    print(f"A wild {pokemon2.name} appeared!")
    print(f"Go! {pokemon1.name}!")

    while not pokemon1.is_fainted() and not pokemon2.is_fainted():
        pokemon1.apply_ability(pokemon2)
        pokemon2.apply_ability(pokemon1)

        # Determine the order of moves based on speed
        if pokemon1.speed > pokemon2.speed:
            first, second = pokemon1, pokemon2
        elif pokemon2.speed > pokemon1.speed:
            first, second = pokemon2, pokemon1
        else:  # Handle speed tie
            if random.choice([True, False]):
                first, second = pokemon1, pokemon2
            else:
                first, second = pokemon2, pokemon1

        if not first.is_fainted():
            perform_move(first, second, random.choice(first.moves))
        if not second.is_fainted():
            perform_move(second, first, random.choice(second.moves))

    if pokemon1.is_fainted():
        print(f"{pokemon1.name} fainted! {pokemon2.name} wins!")
        pokemon2.wins += 1
    elif pokemon2.is_fainted():
        print(f"{pokemon2.name} fainted! {pokemon1.name} wins!")
        pokemon1.wins += 1

class BattleSimulator:
    def __init__(self, pokemon_list):
        self.pokemon_list = pokemon_list

    def run_round_robin_tournament(self):
        for i in range(len(self.pokemon_list)):
            for j in range(i + 1, len(self.pokemon_list)):
                battle(self.pokemon_list[i], self.pokemon_list[j])

    def display_rankings(self):
        rankings = sorted(self.pokemon_list, key=lambda p: p.wins, reverse=True)
        print("\nRankings:")
        for rank, pokemon in enumerate(rankings, start=1):
            print(f"{rank}. {pokemon.name} - {pokemon.wins} wins")

# Define ability effects
def blaze_effect(pokemon, opponent):
    if pokemon.hp <= pokemon.max_hp * 0.3:
    #    print(f"{pokemon.name}'s Blaze ability boosts its Fire-type moves!")
        for move in pokemon.moves:
            if move.move_type == 'Fire':
                move.power *= 1.5

def overgrow_effect(pokemon, opponent):
    if pokemon.hp <= pokemon.max_hp * 0.3:
     #   print(f"{pokemon.name}'s Overgrow ability boosts its Grass-type moves!")
        for move in pokemon.moves:
            if move.move_type == 'Grass':
                move.power *= 1.5

def torrent_effect(pokemon, opponent):
    if pokemon.hp <= pokemon.max_hp * 0.3:
     #   print(f"{pokemon.name}'s Torrent ability boosts its Water-type moves!")
        for move in pokemon.moves:
            if move.move_type == 'Water':
                move.power *= 1.5

def static_effect(pokemon, opponent):
    if random.random() < 0.3 and opponent.status != 'Paralyzed':  # 30% chance to paralyze
        opponent.apply_status('Paralyzed')
        print(f"{opponent.name} was paralyzed by {pokemon.name}'s Static ability!")
# Example moves
tackle = Move('Tackle', 'Normal', 40, 1.0, 'Physical')
water_gun = Move('Water Gun', 'Water', 40, 1.0, 'Special')
ember = Move('Ember', 'Fire', 40, 1.0, 'Special', status_effect='Burned', status_chance=0.1)  # 10% chance to burn
vine_whip = Move('Vine Whip', 'Grass', 45, 1.0, 'Physical')
thunder_wave = Move('Thunder Wave', 'Electric', 0, 0.9, 'Status', status_effect='Paralyzed', status_chance=1.0)  # 100% chance to paralyze
thunder_shock = Move('Thundershock', 'Electric', 40, 1.0, 'Special', status_effect='Paralyzed', status_chance=0.1)

# Example abilities
blaze = Ability('Blaze', blaze_effect)
overgrow = Ability('Overgrow', overgrow_effect)
torrent = Ability('Torrent', torrent_effect)
static = Ability('Static', static_effect)

# Example Pokémon
bulbasaur = Pokemon('Bulbasaur', 5, 45, 49, 49, 65, 65, 45, [tackle, vine_whip], ['Grass', 'Poison'], overgrow)
charmander = Pokemon('Charmander', 5, 39, 52, 43, 60, 50, 65, [tackle, ember], ['Fire'], blaze)
squirtle = Pokemon('Squirtle', 5, 44, 48, 65, 50, 64, 43, [tackle, water_gun], ['Water'], torrent)
pikachu = Pokemon('Pikachu', 5, 35, 55, 40, 50, 50, 90, [tackle, thunder_shock], ['Electric'], static)

# Example Pokémon list (Add more Pokémon to reach 1089)
pokemon_list = [bulbasaur, charmander, squirtle, pikachu]  # Add 1086 more Pokémon

# Run round-robin tournament
simulator = BattleSimulator(pokemon_list)
simulator.run_round_robin_tournament()
simulator.display_rankings()
