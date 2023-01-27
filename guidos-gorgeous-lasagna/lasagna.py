EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_time


def preparation_time_in_minutes(layers):
    """Calculate the preparation time for the layers

    :param layers: int layers of the lasagna.
    :return: int time taken to prepare all the layers, derived from 'PREPARATION_TIME'

    Function that takes the actual number of layers of the lasagna, and returns how
    many minutes it takes to prepare all the layers based on the 'PREPARATION_TIME'
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate total elapsed cooking time (prep + bake) in minutes.

    :param layers: int layers of the lasagna.
    :param elapsed_bake_time: int minutes has been baking.
    :return: int time elapsed, prep time, and bake time.

    Function that returns the total number of minutes you've been cooking, the sum
    of your preparation time and the time the lasagna has already spent baking in the oven.
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
