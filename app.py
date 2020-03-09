import string


class StringGenerator:
    def __init__(self, string_template: str, placeholders: dict):
        self.template = string_template
        self.placeholders = placeholders
        self.previous_replace = []

    def count_list_appearances_in_string(self) -> int:
        appearances = 0

        for key in self.placeholders.keys():
            appearances += self.template.count(key)

        return appearances

    def combinations_from_template(self) -> int:
        total_combinations = 0
        for current_key in self.placeholders.keys():
            times_found = self.template.count(current_key)
            if times_found:
                for x in range(times_found):
                    if not total_combinations:
                        total_combinations = len(self.placeholders[current_key])
                        continue

                    total_combinations = total_combinations * len(self.template[current_key])

        return total_combinations

    def find_next_placeholder(self) -> str:
        next_placeholder = ''
        last_found = -1

        for key in self.placeholders.keys():
            current_match = self.template.find(key)
            if last_found < 0 or current_match < last_found and current_match != -1:
                next_placeholder = key
                last_found = current_match

        return next_placeholder

    def form_string(self):
        new_string = self.template

        i = 0
        for x in range(self.count_list_appearances_in_string()):
            next_key = self.find_next_placeholder()
            key_options = self.placeholders[next_key]
            new_string = new_string.replace(next_key, key_options[i], 1)

        return new_string

    def create_strings(self):
        i = 0
        while i < self.combinations_from_template():
            print(
                self.form_string()
            )

            i += 1


replacements = {
    "%A": list(string.ascii_uppercase),
    "%a": list(string.ascii_lowercase),
    "%n": list(string.digits)
}
template = "V%A"

string_generator = StringGenerator(template, replacements)
string_generator.create_strings()
