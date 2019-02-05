# package used for user-input numerical value check.
import re

# Constants for Light
LIGHT_GREEN = "Green"
LIGHT_RED = "Red"
LIGHT_AMBER = "Amber"


# Constants for Pressure
PRESSURE_HIGH = "High"
PRESSURE_NORMAL = "Normal"
PRESSURE_LOW = "low"

# Constants for Velocity
VELOCITY_HIGH = "High"
VELOCITY_NORMAL = "Normal"
VELOCITY_LOW = "low"


''' 
    fn: get_user_input(message)
    Gets the user input.
    
    Parameters
    ----------
    arg1 : string
        message for the console
    
    Returns
    ---------
    string
        returns the input of the user
    
'''


def get_user_input(message):
    return input(message)


''' 
    fn: validate_input(message)
    Validate the user input basic case. Checks for the blank input.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    string
        returns the input of the user after validation.

'''


def validate_input(message):

    # Runs until the user inputs a non-blank value.
    while True:
        user_input = get_user_input(message)
        if user_input == '':
            print("Please do not leave the input blank")
        else:
            break
    return user_input


''' 
    fn: validate_input_status_lights(message)
    Extends the user input basic validation. Checks for the light status.

    Parameters
    ----------
    arg1 : string
        message for the console.

    Returns
    ---------
    string
        returns the input of the user after validation.

'''


def validate_input_status_lights(message):

    # Runs until the user inputs a non-blank value within constants LIGHT_GREEN, LIGHT_AMBER or LIGHT_RED.
    while True:
        user_input = validate_input(message)
        print(user_input)
        if user_input == LIGHT_GREEN or user_input == LIGHT_RED or user_input == LIGHT_AMBER:
            break
        else:
            print("Please choose one of the colors(%s, %s, %s)" % (LIGHT_GREEN, LIGHT_AMBER, LIGHT_RED))
    return user_input


''' 
    fn: validate_input_meter(message)
    Extends the user input basic validation. Checks for the meter status.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    float
        returns the input of the user after validation

'''


def validate_input_meter(message):

    # Runs until the user inputs a non-blank numerical value.
    while True:
        user_input = validate_input(message)
        num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
        is_number = re.match(num_format, user_input)
        if not is_number:
            print("Please enter a digit")
        else:
            break
    return float(user_input)


''' 
    fn: validate_input_pressure(message)
    Extends the user input basic validation. Checks for the pressure status.

    Parameters
    ----------
    arg1 : string
        message for the console.

    Returns
    ---------
    string
        returns the input of the user after validation.

'''


def validate_input_pressure(message):
    # Runs until the user inputs a non-blank value within constants PRESSURE_NORMAL, PRESSURE_HIGH or PRESSURE_LOW.
    while True:
        user_input = validate_input(message)
        if user_input == PRESSURE_NORMAL or user_input == PRESSURE_HIGH or user_input == PRESSURE_LOW:
            break
        else:
            print("Please choose one of the pressures(%s, %s, %s)" % (PRESSURE_NORMAL, PRESSURE_HIGH, PRESSURE_LOW))
    return user_input


''' 
    fn: validate_input_flow_velocity(message)
    Extends the user input basic validation. Checks for the velocity status.

    Parameters
    ----------
    arg1 : string
        message for the console.

    Returns
    ---------
    string
        returns the input of the user after validation.

'''


def validate_input_flow_velocity(message):
    # Runs until the user inputs a non-blank value within constants VELOCITY_NORMAL, VELOCITY_HIGH or VELOCITY_LOW.
    while True:
        user_input = validate_input(message)
        if user_input == VELOCITY_NORMAL or user_input == VELOCITY_HIGH or user_input == VELOCITY_LOW:
            break
        else:
            print("Please choose one of the statuses(%s, %s, %s)" % (VELOCITY_NORMAL, VELOCITY_HIGH, VELOCITY_LOW))
    return user_input


print("Check status lights")
status_lights = validate_input_status_lights("Enter Light Status(Green, Amber, Red): ")

if status_lights == LIGHT_GREEN:
    print("Do restart procedure")
elif status_lights == LIGHT_AMBER:
    print("Check fuel line service routine")
else:
    print("Shut-off all input lines")
    print("Check meter")
    meter = validate_input_meter("Enter meter: ")
    if meter < 50:
        print("Check main line for test pressure")
        pressure = validate_input_pressure("Enter pressure(Normal, High, low): ")
        if pressure == PRESSURE_NORMAL:
            print("Refer to motor service manual")
        elif pressure == PRESSURE_HIGH or pressure == PRESSURE_LOW:
            print("Refer to main line manual")
    else:
        print("Measure flow velocity at inlet 2-B")
        flow_velocity = validate_input_flow_velocity("Enter flow velocity:")
        if flow_velocity == VELOCITY_HIGH or flow_velocity == VELOCITY_LOW:
            print("Refer unit for factory service")
        else:
            print("Refer to inlet service manual")



