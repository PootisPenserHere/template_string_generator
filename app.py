import string

replacements = {
    "%A": list(string.ascii_uppercase),
    "%a": list(string.ascii_lowercase),
    "%n": list(string.digits)
}
template = "V%A%A%n%n%nA"


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


print(
    combinations_from_template(
        car_plate_template=template,
        options=replacements
    )
)
