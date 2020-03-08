import string

replacements = {
    "%A": list(string.ascii_uppercase),
    "%a": list(string.ascii_lowercase),
    "%n": list(string.digits)
}
template = "V%A"


def count_list_appearances_in_string(keys: list, car_plate_template: str) -> int:
    appearances = 0

    for key in keys:
        appearances += car_plate_template.count(key)

    return appearances


def combinations_from_template(car_plate_template: str, options: dict) -> int:
    total_combinations = 0
    for current_key in options.keys():
        times_found = car_plate_template.count(current_key)
        if times_found:
            for x in range(times_found):
                if not total_combinations:
                    total_combinations = len(options[current_key])
                    continue

                total_combinations = total_combinations * len(options[current_key])

    return total_combinations


def find_next_placeholder(car_plate_template: str, keys: list) -> str:
    next_placeholder = ''
    last_found = -1

    for key in keys:
        current_match = car_plate_template.find(key)
        if last_found < 0 or current_match < last_found and current_match != -1:
            next_placeholder = key
            last_found = current_match

    return next_placeholder


def form_car_plate(car_plate_template: str, options: dict) -> str:
    plate = car_plate_template
    keys = options.keys()

    i = 0
    for x in range(count_list_appearances_in_string(car_plate_template=car_plate_template, keys=keys)):
        next_key = find_next_placeholder(car_plate_template=car_plate_template, keys=keys)
        key_options = options[next_key]
        plate = plate.replace(next_key, key_options[i], 1)

    return plate


def create_strings(car_plate_template: str, options: dict):
    i = 0
    while i < combinations_from_template(car_plate_template=car_plate_template, options=options):
        print(
            form_car_plate(car_plate_template=car_plate_template, options=options)
        )

        i += 1


create_strings(car_plate_template=template, options=replacements)
