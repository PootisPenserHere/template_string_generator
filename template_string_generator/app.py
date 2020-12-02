"""
Contains the logic for the package, the methods to generate the strings
based on a template are declared here
"""

import string


class StringGenerator:
    """
    Helper class to generate a all posible combinations of a string
    based on wildcards

    :param string_template: String containing wildcards to be used as
    template for all combinations
    :type string_template: str
    :param placeholders: Dic containing the placeholders contained in the
    template and their respective list of possible values defaults
    to self.default_place_holders()
    :type placeholders: dict
    """

    def __init__(self, string_template: str, placeholders: dict = None):
        """
        :param string_template: String containing wildcards to be used as
        template for all combinations
        :type string_template: str
        :param placeholders: Dic containing the placeholders contained in the
        template and their respective list of possible values defaults
        to self.default_place_holders()
        :type placeholders: dict
        """
        self.template = string_template
        self.placeholders = placeholders if placeholders else self.default_place_holders()

        self.previous_replace = {}

    @staticmethod
    def default_place_holders() -> dict:
        """
        Returns the default wildcards for replacement

        :return: A dictionary containing the default wildcards for
        replacements and their characters list
        :rtype: dict
        """
        return {
            "%A": list(string.ascii_uppercase),
            "%a": list(string.ascii_lowercase),
            "%n": list(string.digits),
            "%s": ['A', 'B'] + list(string.digits)
        }

    def _count_placeholders_in_template(self) -> int:
        """
        Counts the cumulative amount of times that each wildcard appears inside the template

        :return: The amount of placeholders found
        :rtype: int
        """
        appearances = 0

        for key in self.placeholders:
            appearances += self.template.count(key)

        return appearances

    def _total_combinations_from_template(self) -> int:
        """
        Calculates the total number of strings that will be generated based on
        the given template and placeholder values
        :return: Total amount of combinations for the template
        :rtype int
        """
        total_combinations = 0
        for current_key in self.placeholders:
            times_found = self.template.count(current_key)
            if times_found:
                for _ in range(times_found):
                    if not total_combinations:
                        total_combinations = len(
                            self.placeholders[current_key]
                        )
                        continue

                    total_combinations = total_combinations * len(
                        self.placeholders[current_key]
                    )

        return total_combinations

    def find_next_placeholder(self, haystack: str) -> [str, int]:
        next_placeholder = ''
        last_found = -1

        for key in self.placeholders.keys():
            current_match = haystack.rfind(key)
            if last_found < 0 or current_match > last_found \
                    and current_match != -1:
                next_placeholder = key
                last_found = current_match

        return next_placeholder, last_found

    def form_string(self):
        new_string = self.template

        # Initially set to True as the function will always increase the
        # iteration by one
        increment = True
        for _ in range(self._count_placeholders_in_template()):
            next_key, next_key_index = self.find_next_placeholder(new_string)
            key_options = self.placeholders[next_key]
            previous_index = self.previous_replace.get(next_key_index) \
                if self.previous_replace.get(next_key_index) \
                else 0

            # TODO when iterating for th first time the previous_index is
            #  set to 0 as it doesnt yet exists but it's later increased
            #  by one skipping the first value and pushing it back to the end
            new_index = previous_index + 1 if increment else previous_index
            increment = False  # Increment done
            if new_index >= len(key_options):
                new_index = 0
                increment = True  # Carry over to the next iteration

            # Preserve the state for the next string
            self.previous_replace[next_key_index] = new_index

            new_string = key_options[new_index].join(
                new_string.rsplit(next_key, 1)
            )

        return new_string

    def create_strings(self) -> list:
        items = []
        i = 0
        while i < self._total_combinations_from_template():
            items.append(self.form_string())

            i += 1

        return items
