import amount_of_information
from os import path
from sys import argv

try:
    read_file_path = argv[1]
    count_of_chars = amount_of_information.get_count_of_chars(read_file_path)
    frequency_of_chars_dict = amount_of_information.get_frequency_of_chars_dict(read_file_path)
    print("Count of chars:", count_of_chars)
    print()
    print("Frequency for each character:")
    print("\n".join([r'"{}":{}'.format(key, frequency_of_chars_dict[key]) for key in frequency_of_chars_dict.keys()]))
    print()
    print("Entropy for all text: ", amount_of_information.get_average_entropy(frequency_of_chars_dict))
    print()
    print("Amount of information in the text:", amount_of_information.get_amount_of_information
                            (amount_of_information.get_average_entropy(frequency_of_chars_dict), count_of_chars), "bytes")
    print()
    print("Amount of information/File size:", amount_of_information.get_amount_of_information
        (amount_of_information.get_average_entropy(frequency_of_chars_dict), count_of_chars) / path.getsize(read_file_path))
except Exception as e:
    print(e)