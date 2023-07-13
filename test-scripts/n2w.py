#! /usr/bin/env python3
"""n2w: number to words conversion module: contains function
   num2words. Can also be run as a script
usage as a script: n2w num
           (Convert a number to its English word description)
           num: whole integer from 0 and 999,999,999,999,999 (commas are
           optional)
example: n2w 10,003,103
           for 10,003,103 say: ten million three thousand one hundred three
"""
import argparse

dict_1_to_9 = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
dict_10_to_90 = {
    "1": "ten",
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}
dict_100_to_900 = {
    "1": "one hundred",
    "2": "two hundred",
    "3": "three hundred",
    "4": "four hundred",
    "5": "five hundred",
    "6": "six hundred",
    "7": "seven hundred",
    "8": "eight hundred",
    "9": "nine hundred",
}
# magnitude = {
#     0: "",
#     3: "thousand",
#     6: "million",
#     9: "billion",
#     12: "trillion",
# }


def num2words(num_string):
    """Convert a number to its English word description"""
    if num_string == "0":
        return "zero"
    elif len(num_string) == 1:
        res = handle_1_to_9(num_string[0])
    elif len(num_string) == 2:
        res = handle_10_to_99(num_string[0], num_string[1])
    elif len(num_string) == 3:
        res = handle_100_to_999(num_string[0], num_string[1], num_string[2])
    else:
        raise ValueError("num_string must be between 0 and 999")
    return res


def handle_1_to_9(ones):
    if ones == "0":
        return ""
    return dict_1_to_9[ones]


def handle_10_to_99(tens, ones):
    if tens == "0":
        return handle_1_to_9(ones)
    return dict_10_to_90[tens] + " " + handle_1_to_9(ones)


def handle_100_to_999(hundreds, tens, ones):
    if hundreds == "0":
        return handle_10_to_99(tens, ones)
    return dict_100_to_900[hundreds] + " " + handle_10_to_99(tens, ones)


def test():
    pass


def main():
    parser = argparse.ArgumentParser(
        description="Convert a number to its \
                                     English word description"
    )
    parser.add_argument(
        "num",
        type=int,
        help="whole integer from 0 and \
                        999,999,999,999,999 (dont include commas)",
    )
    args = parser.parse_args()
    print(num2words(str(args.num)))


if __name__ == "__main__":
    main()
else:
    print("n2w  loaded as a module")
