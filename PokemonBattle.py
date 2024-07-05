import random
from move import Move
from weather import battle_weather, Sunny
from type import type_chart
from pokedex import *  # Import all Pokemon from pokedex module

# In pokemon.py or wherever calculate_damage is defined

def calculate_damage(attacker, defender, move):
    if move.category == 'Physical':
        attack_stat = attacker.attack
        defense_stat = defender.defense
    else:
        attack_stat = attacker.special_attack
        defense_stat = defender.special_defense

    modifier = calculate_modifier(attacker, defender, move)
    base_damage = (((2 * attacker.level / 5 + 2) * move.power * (attack_stat / defense_stat)) / 50 + 2)
    damage = int(base_damage * modifier)

    if move.recoil > 0:
        recoil_damage = int(move.recoil * damage)
        attacker.take_damage(recoil_damage)

    # Check if the defender has Levitate ability and the move is Ground-type
    if defender.ability and 'Levitate' in defender.ability.name and move.move_type == 'Ground':
        print(f"{defender.name} avoided the attack with Levitate!")
        damage = 0  # Defender avoids the attack, so no damage

    if random.random() < move.flinch_chance:
        print(f"{defender.name} flinched!")
        return damage, True  # Indicate that the opponent flinched
    else:
        return damage, False


def calculate_modifier(attacker, defender, move):
    target = 1
    weather = 1
    critical = 2 if random.random() < 0.0625 else 1
    stab = 1.5 if move.move_type in attacker.types else 1
    type_effectiveness = 1
    for defender_type in defender.types:
        type_effectiveness *= type_chart.get(move.move_type, {}).get(defender_type, 1)
    
    ability_modifier = 1.0
    if defender.ability and defender.ability.name == "Thick Fat":
        ability_modifier = defender.ability.effect(defender, move)
    
    random_factor = random.uniform(0.85, 1.0)
    modifier = target * weather * critical * stab * type_effectiveness * ability_modifier * random_factor

    return modifier

def select_best_move(attacker, defender):
    best_move = None
    best_score = -float('inf')

    for move in attacker.moves:
        if move.category == "Status":
            score = 0
            if move.status_effect and random.random() < move.status_chance:
                score = 50  # Arbitrary score for causing a status effect
        else:
            type_effectiveness = 1
            for defender_type in defender.types:
                type_effectiveness *= type_chart.get(move.move_type, {}).get(defender_type, 1)
            stab = 1.5 if move.move_type in attacker.types else 1
            score = move.power * type_effectiveness * stab
        
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move

def battle(pokemon1, pokemon2, weather=None):
    pokemon1.reset()
    pokemon2.reset()
    if weather:
        battle_weather.change_weather(weather)
        battle_weather.apply_weather_effects(pokemon1)
        battle_weather.apply_weather_effects(pokemon2)
    turn = 0
    while not pokemon1.is_fainted() and not pokemon2.is_fainted():
        turn += 1
        print(f"\n--- Turn {turn} ---")

        if not pokemon1.check_status_effect() or not pokemon2.check_status_effect():
            continue

        if pokemon1.speed > pokemon2.speed:
            first, second = pokemon1, pokemon2
        else:
            first, second = pokemon2, pokemon1

        # Apply abilities before attacking
        first.apply_ability(second)
        second.apply_ability(first)

        for attacker, defender in [(first, second), (second, first)]:
            if defender.is_fainted():
                break

            move = select_best_move(attacker, defender)


            if move.accuracy >= 1 or random.random() <= move.accuracy:
                print(f"{attacker.name} used {move.name}!")
                if move.category == "Status":
                    if move.status_effect and random.random() < move.status_chance:
                        defender.apply_status(move.status_effect)
                    else:
                        print(f"{attacker.name}'s {move.name} failed to cause any effect!")
                else:
                    damage, flinched = calculate_damage(attacker, defender, move)
                    defender.take_damage(damage)
            else:
                print(f"{attacker.name}'s {move.name} missed!")

            if defender.is_fainted():
                print(f"{defender.name} fainted!")
                attacker.wins += 1
                break

        continue  # Skip to the next turn if Protect succeeds

def round_robin_tournament(pokemon_list, num_battles_per_batch=10, num_battles=100):
    num_pokemon = len(pokemon_list)
    wins = {pokemon.name: 0 for pokemon in pokemon_list}

    for i in range(num_pokemon):
        for j in range(i + 1, num_pokemon):
            pokemon1 = pokemon_list[i]
            pokemon2 = pokemon_list[j]
            batch_count = 0
            while batch_count < num_battles:
                print(f"\nBatch {batch_count + 1} - Match {pokemon1.name} vs {pokemon2.name}:")
                for _ in range(num_battles_per_batch):
                    battle(pokemon1, pokemon2)
                    if pokemon1.is_fainted():
                        wins[pokemon2.name] += 1
                    elif pokemon2.is_fainted():
                        wins[pokemon1.name] += 1
                batch_count += num_battles_per_batch

    print("\nRound-Robin Tournament Results:")
    for pokemon, win_count in wins.items():
        print(f"{pokemon}: {win_count} wins")



# List of Pokémon participating in the tournament
pokemon_list = [gyarados, bulbasaur, charizard, blastoise, lucario, pikachu, torkoal, gengar, arcanine, dragonite]  # Add more Pokémon if needed

# Run the round-robin tournament with 100 battles per match-up
round_robin_tournament(pokemon_list, num_battles_per_batch=10, num_battles=20)
