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