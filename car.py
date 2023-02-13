from car_model import CarModel


class Car(CarModel):
    def __init__(self, plate_number: str, model: CarModel):
        self.set_car_model(model)
        self.set_plate_number(plate_number)
        self.set_remaining_fuel(self.get_car_model().get_tank_capacity())

    def get_car_model(self) -> CarModel:
        return self._car_model

    def get_plate_number(self) -> str:
        return self._plate_number

    def get_remaining_fuel(self) -> float:
        return self._remaining_fuel

    def set_car_model(self, model: CarModel):
        self._car_model = model

    def set_plate_number(self, plate_number: str):
        self._plate_number = plate_number

    def set_remaining_fuel(self, amount):
        self._remaining_fuel = amount

    def __str__(self):
        result = f"Car Info:=\nModel: {self.get_car_model().get_model_name()}\n"
        result += f"Efficiency: {self.get_car_model().get_fuel_efficiency()}\n"
        result += f"Capacity: {self.get_car_model().get_tank_capacity()}\n"
        result += f"Plate Number: {self.get_plate_number()}"
        return result
