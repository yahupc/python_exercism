"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.


    Example: A, B, C, D

    """
    letters = ["A", "B", "C", "D"]
    for count in range(number):
        yield letters[count % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    letters = ["A", "B", "C", "D"]
    row = 1
    seat_count = 0
    while seat_count < number:
        if row == 13:
            row += 1
            continue
        for letter in letters:
            if seat_count >= number:
                return
            yield f"{row}{letter}"
