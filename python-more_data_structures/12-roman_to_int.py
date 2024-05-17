#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        convert_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        convert_list = []

        for i in range(len(roman_string)):
            current_value = convert_dict.get(roman_string[i], 0)

            if (i > 0 and convert_dict.get(roman_string[i - 1], 0)
                    < current_value):
                convert_list[-1] *= -1
            convert_list.append(current_value)

        result = sum(convert_list)
        return result
    return 0
