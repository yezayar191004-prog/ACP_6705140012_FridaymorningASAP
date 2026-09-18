class AirConditioner:
    """A room air-conditioner. Reported buggy by the QA team - fix it!"""
    VALID_MODES = ("cool", "fan", "dry", "auto")
    MIN_TEMP = 16
    MAX_TEMP = 30

    def __init__(self, brand, room_name, temperature=25, mode="cool", fan_speed=1):
        self.brand = brand
        self.room_name = room_name
        self.is_on = False
        
        # FIX 1: Assign to self.temperature instead of self._temperature 
        # so that constructor arguments are validated through the setter.
        self.temperature = temperature
        
        self.mode = mode
        self.fan_speed = fan_speed

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        # FIX 2a: Changed 'and' to 'or'. A number cannot be simultaneously < 16 AND > 30.
        if value < self.MIN_TEMP or value > self.MAX_TEMP:
            raise ValueError(f"Temperature must be {self.MIN_TEMP}-{self.MAX_TEMP} C.")...
