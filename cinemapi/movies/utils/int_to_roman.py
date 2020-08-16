"Integer to roman conversion method."


roman_list = (
    (1000, "M"), (900, "CM"),
    (500, "D"), (400, "CD"), 
    (100, "C"), (90, "XC"),
    (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"),
    (5, "V"), (4, "IV"),
    (1, "I")
)

def int_to_roman(input_int):
    """
    Obtains a Roman numeral from an integer,
    The integer must be between 1 to 3999.
    This method is proper to represent years in Roman numeral.
    """

    if not isinstance(input_int, int):
        raise TypeError(
            'Expected integer, got {0}'.format(type(input_int))
        )
    if not 0 < input_int < 4000:
        raise ValueError(
            'Argument must be between 1 and 3999'
        )
    
    roman_result = ""
    for roman_tuple in roman_list:
        while input_int >= roman_tuple[0]:
            input_int -= roman_tuple[0]
            roman_result += roman_tuple[1]
    return roman_result
