from math import log

def get_count_of_chars(file_path):
        with open(file_path, "r", encoding="utf-8") as inf:
            return sum([1 for char in inf.read().strip()])


def get_frequency_of_chars_dict(file_path):
        counts_dict = {}
        with open(file_path, "r", encoding="utf-8") as inf:
            all_text = inf.read().strip()
            for char in all_text:
                if char not in counts_dict.keys():
                    counts_dict[char] = 1
                else:
                    counts_dict[char] += 1
            return {char: counts_dict[char] / (get_count_of_chars(file_path)) for char in counts_dict.keys()}


def get_average_entropy(frequency_of_chars_dict):
    return sum([frequency * log(1 / frequency, 2) for frequency in frequency_of_chars_dict.values()])


def get_amount_of_information(average_entropy, count_of_chars):
    return count_of_chars * average_entropy / 8





