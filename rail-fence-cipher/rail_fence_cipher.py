def encode(message, rails):
    letter_rails = {i: [] for i in range(1, rails + 1)}
    act_rail = rails
    down = lambda x: x - 1
    up = lambda x: x + 1
    act_mov = down
    for letter in message:
        letter_rails[act_rail].append(letter)
        if act_mov == down and act_rail == 1:
            act_mov = up
        if act_mov == up and act_rail == rails:
            act_mov = down
        act_rail = act_mov(act_rail)
    return "".join(("".join(letter_rails[rail]) for rail in range(rails, 0, -1)))


def decode(encoded_message: str, rails: int) -> str:
    L = len(encoded_message)
    N = 2 * (rails - 1)
    if L % N == 0:
        K = int(L / N)
        first, medium, last = (
            encoded_message[:K],
            encoded_message[K : L - K],
            encoded_message[L - K :],
        )
        print(first, medium, last)
    return ""


decode("abcdefghqwerhyjuujki", 3)
