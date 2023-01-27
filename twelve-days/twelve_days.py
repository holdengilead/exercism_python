lyrics = [
    ("first", "a Partridge in a Pear Tree."),
    ("second", "two Turtle Doves"),
    ("third", "three French Hens"),
    ("fourth", "four Calling Birds"),
    ("fifth", "five Gold Rings"),
    ("sixth", "six Geese-a-Laying"),
    ("seventh", "seven Swans-a-Swimming"),
    ("eighth", "eight Maids-a-Milking"),
    ("ninth", "nine Ladies Dancing"),
    ("tenth", "ten Lords-a-Leaping"),
    ("eleventh", "eleven Pipers Piping"),
    ("twelfth", "twelve Drummers Drumming"),
]


def recite(start_verse, end_verse):
    result = []
    for day in range(start_verse, end_verse + 1):
        song = "On the {} day of Christmas my true love gave to me: ".format(
            lyrics[day - 1][0]
        )
        gifts = [lyrics[i][1] for i in range(day - 1, -1, -1)]
        if len(gifts) > 1:
            gifts[-1] = f"and {gifts[-1]}"
        result.append(song + ", ".join(gifts))
    return result
