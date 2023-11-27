EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016

def water_column_height(tower_height, tank_height):
    """Calculate and return the height of a column of water from a
       tower height and a tank wall height.".

    Parameters
        tower_height: height of the tower
        tank_height: height of the walls of the tank that is on top of the tower
    Return: a float
    """
    
    # Compute and return water column height
    water_column = tower_height + (3 * tank_height / 4)
    return water_column

def pressure_gain_from_water_height(height):
    """Calculate and return the pressure caused by Earth's gravity pulling on 
       the water stored in an elevated tank.".

    Parameters
        height: height of the water column in meter
    Return: a float
    """
    
    # Compute and return pressure gain from water height
    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate and return the water pressure lost because of the friction between
    the water and the walls of a pipe that it flows through.".

    Parameters
        pipe_diameter: diameter of the pipe in meters
        pipe_length: length of the pipe in meters
        friction_factor: pipe¿s friction factor
        fluid_velocity: velocity of the water flowing through the pipe in meters / second
    Return: a float
    """
    
    # Compute and return pressure loss from pipe
    lost_pressure = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return lost_pressure

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculate and return the water pressure lost because of fittings such as 45° 
       and 90° bends that are in a pipeline.".

    Parameters
        fluid_velocity: velocity of the water flowing through the pipe in meters / second
        quantity_fittings: quantity of fittings
    """
    
    # Compute and return pressure loss from fittings
    lost_pressure = (-0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings) / 2000
    return lost_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate and return the Reynolds number for a pipe with water flowing through it.".

    Parameters
        hydraulic_diameter: hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
        fluid_velocity: velocity of the water flowing through the pipe in meters / second
    """
    
    # Compute and return reynolds number
    reynolds = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculate and return the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter.".

    Parameters
        larger_diameter: diameter of the larger pipe in meters
        fluid_velocity: velocity of the water flowing through the pipe in meters / second
        reynolds_number: the Reynolds number that corresponds to the pipe with the larger diameter
        smaller_diameter: diameter of the smaller pipe in meters
    """
    
    # Compute and return pressure loss from pipe reduction
    k = (0.1 + (50 / reynolds_number)) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    
    lost_pressure = (-k * WATER_DENSITY * fluid_velocity ** 2) / 2000
    return lost_pressure

def convert_kpa_to_psi(kpa):
    """Calculate and return psi.".

    Parameters
        kpa: kilopascal value
        """
    # Compute and return psi
    psi = kpa * 0.145038
    return psi

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    
    
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    
    psi_pressure = convert_kpa_to_psi(pressure)
    
    print(f"Pressure at house: {psi_pressure:.1f} psi")

if __name__ == "__main__":
    main()