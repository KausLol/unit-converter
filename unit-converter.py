"""a simple program that converts between various units"""

import time

# conversion values of various units
conversion_data = {
    "len": {
        "A": 10000000000,
        "nm": 1000000000,
        "um": 1000000,
        "mm": 1000,
        "cm": 100,
        "m": 1,
        "km": 0.001,
        "in": 39.37008,
        "ft": 3.28084,
        "yd": 1.093613,
        "mi": 0.000621,
        "nmi": 0.00054,
    },
    "area": {
        "mm2": 1000000,
        "cm2": 10000,
        "m2": 1,
        "ha": 0.0001,
        "km2": 0.000001,
        "in2": 1550.003,
        "ft2": 10.76391,
        "yd2": 1.19599,
        "ac": 0.000247,
        "mi2": 0.000000386102159,
    },
    "vol": {"ml": 1000, "cm3": 1000, "l": 1, "m3": 0.001},
    "weight": {
        "mg": 1000000,
        "g": 1000,
        "kg": 1,
        "mt": 0.001,
        "oz": 35.27396,
        "lb": 2.204623,
    },
    "speed": {
        "cmps": 100,
        "mps": 1,
        "kmph": 3.6,
        "ftps": 3.28084,
        "mph": 2.237136,
        "kn": 1.944012,
        "M": 0.002939,
    },
    "time": {
        "ms": 3600000,
        "sec": 3600,
        "min": 60,
        "hr": 1,
        "day": 1/24,
        "week": 1/168,
        "yr": 1/8766,
    }
}


# main code
def main():
    print(
        f"\nWelcome to the Unit-Calculator! This program is capable of converting between "
        f"a wide range of units."
    )
    time.sleep(1)

    print(f"\nPlease note that this program rounds results to two decimal values.\n"
          f"It is not suitable for extremely accurate calculations.")
    time.sleep(1)

    print(f"\nType 'help' to get information about all the valid commands!")
    time.sleep(1)

    # prompts user for a command
    while True:
        prompt = input(f"\nWhat would you like to do?: ")
        user_input(prompt)


# checks physical quantity
def user_input(prompt):
    while True:
        try:
            if prompt == "len":
                convert(conversion_data["len"])
                return
            elif prompt == "area":
                convert(conversion_data["area"])
                return
            elif prompt == "vol":
                convert(conversion_data["vol"])
                return
            elif prompt == "temp":
                temp()
                return
            elif prompt == "weight":
                convert(conversion_data["weight"])
                return
            elif prompt == "speed":
                convert(conversion_data["speed"])
                return
            elif prompt == "time":
                convert(conversion_data["time"])
                return
            elif prompt == "help":
                guide()
                return
            elif prompt == "unit_help":
                units()
                return
            elif prompt == "cancel":
                return
            elif prompt == "exit":
                exit()
            else:
                raise ValueError

        except ValueError:
            print(f"{prompt} is not recognised as a valid command!")
            return


# converts the amount to another unit
def convert(data_dict):
    while True:
        try:
            input_data = input(
                "\nEnter your amount and unit separated by space (eg. 25.56 cm): "
            )

            if input_data == "cancel":
                print("Cancelling the current command.")
                return

            val1, unit1 = input_data.split(" ")

            val1 = float(val1)

            unit1_val = data_dict[unit1]
            base = val1 / unit1_val

            unit2 = input("Enter the unit you want to convert to: ")
            if unit2 == "cancel":
                print("Cancelling the current command.")
                return

            unit2_val = data_dict[unit2]
            val2 = base * unit2_val

            print(f"\nConverted amount: {val2:,.2f} {unit2}")
            return

        # handles errors
        except ValueError:
            print(
                "Please type in correct format! Make sure you have entered the correct units."
            )
            return

        except KeyError:
            print(
                "Please type in correct format! Make sure you have entered the correct units."
            )


# separate function to convert temperature
def temp():
    while True:
        try:
            input_data = input(
                "\nEnter your amount and unit separated by space (eg. 25.56 F): "
            )

            if input_data == "cancel":
                print("Cancelling the current command.")
                return

            val1, unit1 = input_data.split(" ")

            val1 = float(val1)

            unit2 = input("Enter the unit you want to convert to: ")

            if unit2 == "cancel":
                print("Cancelling the current command.")
                return

            # to convert from C to other
            elif unit1 == "C":
                if unit2 == "F":
                    val2 = val1 * 1.8
                    val3 = val2 + 32
                    print(f"\nConverted amount: {val3:,.2f} {unit2}\n")
                    return

                elif unit2 == "K":
                    val2 = val1 + 273.15
                    print(f"\nConverted amount: {val2:,.2f} {unit2}\n")
                    return

            # to convert from F to other
            elif unit1 == "F":
                if unit2 == "C":
                    val2 = val1 - 32
                    val3 = val2 * 5 / 9
                    print(f"\nConverted amount: {val3:,.2f} {unit2}\n")
                    return

                elif unit2 == "K":
                    val2 = val1 - 32
                    val3 = val2 * 5 / 9
                    val4 = val3 + 273.15
                    print(f"\nConverted amount: {val4:,.2f} {unit2}\n")
                    return

            # to convert from K to other
            elif unit1 == "K":
                if unit2 == "C":
                    val2 = val1 - 273.15
                    print(f"\nConverted amount: {val2:,.2f} {unit2}\n")
                    return

                elif unit2 == "F":
                    val2 = val1 - 273.15
                    val3 = val2 * 1.8
                    val4 = val3 + 32
                    print(f"\nConverted amount: {val4:,.2f} {unit2}\n")
                    return

            else:
                raise ValueError

        except ValueError:
            print(
                "Please type in correct format! Make sure you have entered the correct units."
            )


# displays all valid commands to the user
def guide():
    print(
        "\nAvailable Commands: \n"
        "\nhelp: Display a list of all commands\n"
        "unit_help: Display a list of compatible units (eg: len.help)\n"
        "len: Convert between length units\n"
        "area: Convert between areas units\n"
        "vol: Convert between volumes units\n"
        "temp: Convert between temperature units\n"
        "weight: Convert between weight units\n"
        "speed: Convert between speed units\n"
        "time: Convert between time units\n"
        "cancel: Cancel a command"
        "exit: Exit the program"
    )


# gives info about each unit to the user
def units():
    len_units = (
        "\nCompatible length units: \n"
        "\nA: Angstrom\n"
        "nm: Nanometer\n"
        "um: Micrometer\n"
        "mm: Millimeter\n"
        "cm: Centimeter\n"
        "m: Meter\n"
        "km: Kilometer\n"
        "in: Inch\n"
        "ft: Feet\n"
        "yd: Yard\n"
        "mi: Mile\n"
        "nmi: Nautical Mile"
    )

    area_units = (
        "\nCompatible Area units: \n"
        "\nmm2: Square millimeter\n"
        "cm2: Square centimeter\n"
        "m2: Square meter\n"
        "km2: Square kilometer\n"
        "in2: Square Inch\n"
        "ft2: Square feet\n"
        "yd2: Square yard\n"
        "mi2: Square mile\n"
        "ha: Hectare\n"
        "ac: Acre"
    )

    weight_units = (
        "\nCompatible Weight units: \n"
        "\nmg: Milligram\n"
        "g: Gram\n"
        "kg: Kilogram\n"
        "mt: Metric tonne\n"
        "oz: Ounce\n"
        "lb: Pound"
    )

    speed_units = (
        "\nCompatible Speed units: \n"
        "\ncmps: Centimeter per second\n"
        "ms: Meter per second\n"
        "kmph: Kilometer per hour\n"
        "ftps: Feet per second\n"
        "mph: Miles per hour\n"
        "kn: Knots\n"
        "M: Mach"
    )

    time_units = (
        "\nCompatible Time units: \n"
        "\nms: Millisecond\n"
        "sec: Second\n"
        "min: Minute\n"
        "hr: Hour\n"
        "yr: year\n"
        "day\n"
        "week"
    )

    temp_units = (
        "\nCompatible temperature units: \n"
        "\nC: Celsius\n"
        "F: Fahrenheit\n"
        "K: Kelvin"
    )

    # checks for the physical quantity that the user wants to know about
    while True:
        try:
            unit = input("Enter a physical quantity: ")

            if unit == "cancel":
                print("Cancelling the current command.")
                return
            elif unit == "len":
                print(len_units)
                return
            elif unit == "area":
                print(area_units)
                return
            elif unit == "weight":
                print(weight_units)
                return
            elif unit == "speed":
                print(speed_units)
                return
            elif unit == "time":
                print(time_units)
                return
            elif unit == "temp":
                print(temp_units)
                return
            else:
                raise ValueError

        except ValueError:
            print("Please enter a valid physical quantity! ")


if __name__ == "__main__":
    main()
