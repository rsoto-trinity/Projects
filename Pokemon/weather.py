# Define the Weather classes
class Weather:
    def __init__(self, name):
        self.name = name

class Sunny(Weather):
    def __init__(self):
        super().__init__("Sunny")

class WeatherManager:
    def __init__(self):
        self.current_weather = None

    def change_weather(self, weather):
        self.current_weather = weather

    def apply_weather_effects(self, pokemon):
        if self.current_weather and isinstance(self.current_weather, Sunny):
            # Apply effects of sunny weather to the Pokémon
            for move in pokemon.moves:
                if move.move_type == "Fire":
                    move.power *= 1.5  # Boost power of Fire-type moves during sunny weather
            print("The sun is shining brightly, boosting the power of Fire-type moves!")

    def is_sunny(self):
        return isinstance(self.current_weather, Sunny)

battle_weather = WeatherManager()
