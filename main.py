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
            # get the car of given plate_number from our inventory of cars
            trip_car = None
            for plate_number, car in cars.items():
                if plate_number == words[1]:
                    trip_car = car

            # if trip car is not set to anything, means we don't have that car, we cannot make the trip
            # check the next trip in the case immediately (read the next input)
            if trip_car == None:
                print(f"Not enough fuel for {words[1]}")
                continue

            # otherwise we have found the car
            distance: int = int(words[2])

            # calculate the fuel consumtion for the trip
            fuel_consumption = \
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
