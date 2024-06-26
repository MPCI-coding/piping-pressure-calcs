import math

def calculate_air_released(valve_size, blowing_time):
    # Define the discharge coefficient and air density
    Cd = 0.65  # Discharge coefficient
    density_air = 1.225  # kg/m³ (density of air at standard conditions)

    # Define a dictionary for valve diameters in meters
    valve_diameters = {
        "1/2 inch": 0.0127,
        "3/4 inch": 0.01905,
        "1 inch": 0.0254,
        "2 inch": 0.0508
    }

    # Convert initial pressure from psi to Pascals
    pressure_psi = 60  # psi (initial pressure)
    pressure_pa = pressure_psi * 6894.76  # Convert to Pascals

    # Get the diameter of the specified valve size
    diameter = valve_diameters.get(valve_size)
    if diameter is None:
        raise ValueError(f"Invalid valve size: {valve_size}")

    # Calculate the cross-sectional area of the orifice
    A = math.pi * (diameter / 2)**2

    # Calculate the flow rate through the orifice
    Q = Cd * A * math.sqrt((2 * pressure_pa) / density_air)

    # Calculate the total volume of air released
    air_released = Q * blowing_time

    return air_released

# Example usage:
valve_size = "3/4 inch"
blowing_time = 60  # seconds
released_volume = calculate_air_released(valve_size, blowing_time)
print(f"Volume of air released through {valve_size} valve in {blowing_time} seconds: {released_volume:.4f} cubic meters")

