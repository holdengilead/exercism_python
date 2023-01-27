class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num

    def valid(self):
        aux_num = "".join(digit for digit in self.card_num if digit != " ")
        if len(aux_num) < 2:
            return False
        accum = 0
        try:
            for pos, digit in enumerate(reversed(aux_num), start=1):
                if pos % 2 != 0:
                    accum += int(digit)
                else:
                    if int(digit) < 5:
                        accum += int(digit) * 2
                    else:
                        accum += int(digit) * 2 - 9
        except ValueError:
            return False
        return accum % 10 == 0


print(Luhn("59").valid())
