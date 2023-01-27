from string import ascii_letters, punctuation


class PhoneNumber:
    NUMBERS = {"0": "zero", "1": "one"}
    PUNCTUATION = set(punctuation).difference("().-+")

    def __init__(self, number):
        self.number = PhoneNumber.clean_number(number)

    @staticmethod
    def clean_number(number: str):
        clean_number = []
        for digit in number:
            if digit in ascii_letters:
                raise ValueError("letters not permitted")
            if digit in PhoneNumber.PUNCTUATION:
                raise ValueError("punctuations not permitted")
            if digit.isdigit():
                clean_number.append(digit)
        clean_number = "".join(clean_number)
        if len(clean_number) < 10:
            raise ValueError("incorrect number of digits")
        if len(clean_number) > 11:
            raise ValueError("more than 11 digits")
        if len(clean_number) == 11:
            if clean_number[0] != "1":
                raise ValueError("11 digits must start with 1")
            clean_number = clean_number[1:]
        if clean_number[0] in ("0", "1"):
            raise ValueError(
                f"area code cannot start with {PhoneNumber.NUMBERS[clean_number[0]]}"
            )
        if clean_number[3] in ("0", "1"):
            raise ValueError(
                f"exchange code cannot start with {PhoneNumber.NUMBERS[clean_number[3]]}"
            )
        return clean_number

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"

    @property
    def area_code(self):
        return self.number[:3]
