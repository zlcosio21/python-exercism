EXPECTED_BAKE_TIME = 40
bake_of_layers = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param elapsed_bake_time: akes the actual minutes the lasagna has been in the oven as an argument
    :return: EXPECTED_BAKE_TIME - elapsed_bake_time how many minutes the lasagna still needs to bake based on the 

    This function the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the total elapsed minutes spent cooking the
       lasagna.

    :param number_of_layers: the number of layers in the lasagna.
    :return: the sum of its preparation time and the time the lasagna has already been baked in the oven.

    This function should return the total number of minutes it has been cooking, or the sum of its preparation time and the time the lasagna has already been baked in the oven.
    """
    return number_of_layers * bake_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time