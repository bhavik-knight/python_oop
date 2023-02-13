from car_model import CarModel
from car import Car
from sys import stdin


def main():
    models = dict()
    cars = dict()

    for line in stdin:
        if line.strip() == "FINISH":
            break

        words = line.strip().split()
        # check input for different starting words
        # MODEL: Create the object of CarModel class, and add to models
        if words[0] == "MODEL":
            models[words[1]] = CarModel(
                words[1], float(words[2]), float(words[3])
            )
        # CAR: Create the object of Car class, and add to cars
        elif words[0] == "CAR":
            model = models[words[1]]
            cars[words[2]] = Car(words[2], model)
        # REFUEL: Refuel the car tank to the full capacity
        elif words[0] == "REFILL":
            trip_car = cars[words[1]]
            trip_car.set_remaining_fuel(
                trip_car.get_car_model().get_tank_capacity()
            )
        # TRIP: Calculate and check if car is able to make a trip of not
        else:
            # let's fetch the car for our trip from the car inventory
            trip_car = None

            # try to check if we have this plate_number in our cars inventory
            try:
                trip_car = cars[words[1]]

            # if we don't have this car, we cannto make this trip
            except KeyError:
                print(f"Not enough fuel for {words[1]}")

            # if we have the car, then only we can make the trip
            else:
                distance: int = int(words[2])

                fuel_consumption: float = \
                    (trip_car.get_car_model().get_fuel_efficiency() * distance) / 100

                # if not enough fuel, we cannot make a trip
                if trip_car.get_remaining_fuel() < fuel_consumption:
                    print(f"Not enough fuel for {words[1]}")
                else:
                    # trip success, calculate the remaining fuel
                    trip_car.set_remaining_fuel(
                        trip_car.get_remaining_fuel() - fuel_consumption
                    )
                    print(
                        f"Trip completed successfulluy for {trip_car.get_plate_number()}"
                        f", Remaining Fuel: {trip_car.get_remaining_fuel()}"
                    )


if __name__ == "__main__":
    main()
