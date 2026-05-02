#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return None

    values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 100, 'D': 500, 'M': 1000
    }

    result = 0
    for i in range (len(roman_string)):
        current = values.get(roman_string[i], 0)
        next_val = values.get(roman_string[i + 1], 0) if i + 1 < len(roman_string) else 0

        if current < next_val:
            result -= current
        else:
            result += current

    return result
