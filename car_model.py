class CarModel:
    def __init__(self, model_name: str, fuel_efficiency: float, tank_capacity: float):
        self.set_model_name(model_name)
        self.set_fuel_efficiency(fuel_efficiency)
        self.set_tank_capacity(tank_capacity)

    def get_model_name(self) -> str:
        return self._model_name

    def get_fuel_efficiency(self) -> float:
        return self._fuel_efficiency

    def get_tank_capacity(self) -> float:
        return self._tank_capacity

    def set_model_name(self, model_name: str):
        self._model_name = model_name

    def set_fuel_efficiency(self, fuel_efficiency: float):
        self._fuel_efficiency = fuel_efficiency

    def set_tank_capacity(self, tank_capacity: float):
        self._tank_capacity = tank_capacity

    def __str__(self):
        result = f"CarModel Info:=\nModel: {self.get_model_name()}\n"
        result += f"Efficiency: {self.get_fuel_efficiency()}\nCapacity: {self.get_tank_capacity()}"
        return result
