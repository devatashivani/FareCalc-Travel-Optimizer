def calculate_fare(km, vehicle_type, hour):
    rates = {
        "economy": 10,
        "premium": 18,
        "suv": 25,
        "bike": 6,
        "auto": 8,
        "electric": 12
    }
    vehicle_type = vehicle_type.lower()
    if vehicle_type not in rates:
        return None
    base_fare = km * rates[vehicle_type]
    surge = 1.5 if 17 <= hour <= 21 else 1
    night_charge = 1.2 if (hour >= 22 or hour <= 5) else 1
    final_fare = base_fare * surge * night_charge
    return final_fare, surge, night_charge
try:
    print("\n   CityCab Fare Calculator   \n")
    km = float(input("Enter distance (in km): "))
    vehicle = input("Enter vehicle (Economy / Premium / SUV / Bike / Auto / Electric): ")
    hour = int(input("Enter hour (0-23): "))
    result = calculate_fare(km, vehicle, hour)
    if result is None:
        print("\nService Not Available for selected vehicle.")
    else:
        fare, surge, night = result
        print("\n    Ride Receipt    ")
        print(f"Distance : {km} km")
        print(f"Vehicle  : {vehicle.capitalize()}")
        print(f"Time     : {hour}:00 hrs")
        print("\nCharges Applied:")
        print(f"- Peak Surge  : {'Yes (1.5x)' if surge > 1 else 'No'}")
        print(f"- Night Charge: {'Yes (1.2x)' if night > 1 else 'No'}")
        print("\nTotal Fare: ₹{:.2f}".format(fare))
except ValueError:
    print("\nInvalid input! Please enter correct values.")
except Exception as e:
    print("\nUnexpected error:", e)