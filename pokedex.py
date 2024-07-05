import random
from natures import Nature, natures
from weather import Weather,WeatherManager,Sunny,battle_weather
from pokemon import Pokemon
from move import Move
from ability import *
from type import type_chart

bulbasaur = Pokemon(
    name="Bulbasaur", level=50,
    base_stats=(45, 49, 49, 45, 65, 65),
    moves=[
        Move("Solar Beam", "Grass", 120, 1.0, "Special"),
        Move("Razor Leaf", "Grass", 55, 0.95, "Physical"),
        Move("Vine Whip", "Grass", 45, 1.0, "Physical"),
        Move("Poison Powder", "Poison", 0, 0.75, "Status", status_effect="Poisoned", status_chance=1.0)
    ],
    types=["Grass", "Poison"],
    ability=Ability("Overgrow", overgrow_effect)
)

charizard = Pokemon(
    name="Charizard", level=50,
    base_stats=(78, 84, 78, 100, 109, 85),
    moves=[
        Move("Flamethrower", "Fire", 90, 1.0, "Special", status_effect="Burned", status_chance=0.1, flinch_chance=0.0),
        Move("Dragon Claw", "Dragon", 80, 1.0, "Physical"),
        Move("Flare Blitz", "Fire", 120, 1.0, "Physical",status_chance= 0.1, recoil=0.33),  # 33% recoil damage
        Move("Fire Blast", "Fire", 110, 0.85, "Special", status_effect="Burned", status_chance=0.1)
    ],
    types=["Fire", "Flying"],
    ability=Ability("Blaze", blaze_effect)
)

blastoise = Pokemon(
    name="Blastoise", level=50,
    base_stats=(79, 83, 100, 78, 85, 105),
    moves=[
        Move("Hydro Pump", "Water", 110, 0.8, "Special"),
        Move("Ice Beam", "Ice", 90, 1.0, "Special", status_effect="Frozen", status_chance=0.1),
        Move("Bite", "Dark", 60, 1.0, "Physical"),
        Move("Surf", "Water", 90, 1.0, "Special")
    ],
    types=["Water"],
    ability=Ability("Torrent", torrent_effect)
)

gyarados = Pokemon(
    name="Gyarados", level=50,
    base_stats=(95, 125, 79, 81, 60, 100),
    moves=[
        Move("Waterfall", "Water", 80, 1.0, "Physical", flinch_chance=0.2),
        Move("Dragon Dance", "Dragon", 0.0, 1.0, "Status"),
        Move("Ice Fang", "Ice", 65, 0.95, "Physical", status_effect="Frozen", status_chance=0.1),
        Move("Earthquake", "Ground", 100, 1.0, "Physical")
    ],
    types=["Water", "Flying"],
    ability=Ability("Intimidate", intimidate_effect)
)

lucario = Pokemon(
    name="Lucario", level=50,
    base_stats=(70, 110, 70, 90, 115, 70),
    moves=[
        Move("Aura Sphere", "Fighting", 90, 1.0, "Special"),
        Move("Close Combat", "Fighting", 120, 1.0, "Physical"),
        Move("Dark Pulse", "Dark", 80, 1.0, "Special", flinch_chance=0.2),
        Move("Extreme Speed", "Normal", 80, 1.0, "Physical")
    ],
    types=["Fighting", "Steel"],
    ability=Ability("Inner Focus", inner_focus_effect)
)

arcanine = Pokemon(
    name="Arcanine", level=50,
    base_stats=(90, 110, 80, 95, 100, 80),
    moves=[
        Move("Flare Blitz", "Fire", 120, 1.0, "Physical", status_chance= 0.1, recoil=0.33),  # 33% recoil damage
        Move("Extreme Speed", "Normal", 80, 1.0, "Physical"),
        Move("Wild Charge", "Electric", 90, 1.0, "Physical"),
        Move("Close Combat", "Fighting", 120, 1.0, "Physical")
    ],
    types=["Fire"],
    ability=Ability("Intimidate", intimidate_effect)
)

dragonite = Pokemon(
    name="Dragonite", level=50,
    base_stats=(91, 134, 95, 80, 100, 100),
    moves=[
        Move("Dragon Dance", "Dragon", 0, 1.0, "Status"),
        Move("Outrage", "Dragon", 120, 1.0, "Physical"),
        Move("Earthquake", "Ground", 100, 1.0, "Physical"),
        Move("Fire Punch", "Fire", 75, 1.0, "Physical", status_effect="Burned", status_chance=0.1)
    ],
    types=["Dragon", "Flying"],
    ability=Ability("Multiscale", multiscale_effect)
)

gengar = Pokemon(
    name="Gengar", level=50,
    base_stats=(60, 65, 60, 110, 130, 75),
    moves=[
        Move("Shadow Ball", "Ghost", 80, 1.0, "Special"),
        Move("Sludge Bomb", "Poison", 90, 1.0, "Special"),
        Move("Focus Blast", "Fighting", 120, 0.7, "Special"),
        Move("Thunderbolt", "Electric", 90, 1.0, "Special", status_effect="Paralyzed", status_chance=0.1)
    ],
    types=["Ghost", "Poison"],
    ability=Ability("Levitate", levitate_effect)
)

pikachu = Pokemon(
    name="Pikachu", level=50,
    base_stats=(35, 55, 40, 90, 50, 50),
    moves=[
        Move("Thunderbolt", "Electric", 90, 1.0, "Special", status_effect="Paralyzed", status_chance=0.1),
        Move("Quick Attack", "Normal", 40, 1.0, "Physical"),
        Move("Iron Tail", "Steel", 100, 0.75, "Physical", flinch_chance=0.3),
        Move("Thunder Wave", "Electric", 0, 0.9, "Status", status_effect="Paralyzed", status_chance=1.0)
    ],
    types=["Electric"],
    ability=Ability("Static", static_effect)
)

torkoal = Pokemon(
    name="Torkoal", level=50,
    base_stats=(70, 85, 140, 20, 85, 70),  # Adjust base stats as needed
    moves=[
        Move("Eruption", "Fire", 150, 1.0, "Special"),
        Move("Earth Power", "Ground", 90, 1.0, "Special"),
        Move("Flamethrower", "Fire", 90, 1.0, "Special"),
        Move("Rock Slide", "Rock", 75, 0.9, "Physical")
    ],
    types=["Fire"],
    ability=Ability("Drought", drought_effect)  # Implement the Drought ability effect
)

