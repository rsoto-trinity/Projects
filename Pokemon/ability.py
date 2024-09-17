import random
from natures import Nature, natures
from weather import Weather,WeatherManager,Sunny,battle_weather
from pokemon import Pokemon
from move import Move
class Ability:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply(self, pokemon, opponent):
        self.effect(pokemon, opponent)

def overgrow_effect(pokemon, opponent):
    if any(move.move_type == "Grass" for move in pokemon.moves) and pokemon.hp <= pokemon.max_hp * 0.3:
        for move in pokemon.moves:
            if move.move_type == "Grass":
                move.power *= 1.5
        print(f"{pokemon.name}'s Overgrow ability boosted the power of its Grass-type moves!")

def blaze_effect(pokemon, opponent):
    if any(move.move_type == "Fire" for move in pokemon.moves) and pokemon.hp <= pokemon.max_hp * 0.3:
        for move in pokemon.moves:
            if move.move_type == "Fire":
                move.power *= 1.5
        print(f"{pokemon.name}'s Fire ability boosted the power of its Fire-type moves!")

def torrent_effect(pokemon, opponent):
    if any(move.move_type == "Water" for move in pokemon.moves) and pokemon.hp <= pokemon.max_hp * 0.3:
        for move in pokemon.moves:
            if move.move_type == "Water":
                move.power *= 1.5
        print(f"{pokemon.name}'s Water ability boosted the power of its Water-type moves!")

def intimidate_effect(user, opponent):
    if opponent.ability is not None and opponent.ability.name == "Clear Body":
        print(f"{opponent.name}'s Clear Body prevents Intimidate from taking effect!")
    else:
        print(f"{user.name} intimidates {opponent.name}!")
        opponent.reduce_stat('attack', 1)  # Reduce opponent's Attack stat by 1 point


def multiscale_effect(self, opponent):
    if self.ability and self.ability.name == 'Multiscale' and self.hp == self.max_hp:
        print(f"{self.name}'s Multiscale ability reduced the damage taken!")
        opponent.max_hp //= 2
        
def drought_effect(pokemon, opponent):
    print(f"{pokemon.name} brought intense sunlight by its Drought ability!")
    battle_weather.change_weather(Sunny())

def inner_focus_effect(pokemon, opponent):
    print(f"{pokemon.name}'s Inner Focus ability prevents flinching!")

def levitate_effect(pokemon, opponent):
    if 'Ground' in opponent.types:
        print(f"{pokemon.name}'s Levitate ability prevents it from being affected by Ground-type moves!")
        return 0  # Return 0 damage if the move is Ground-type
    else:
        return 1  # Return default damage multiplier if the move is not Ground-type

def static_effect(pokemon, opponent):
    if random.random() < 0.3:  # Adjust the probability as needed
        print(f"{opponent.name} made contact with {pokemon.name} and got paralyzed!")
        opponent.apply_status("Paralyzed")