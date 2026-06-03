def response(hey_bob):
    if hey_bob is None or hey_bob.strip() == "":
        return "Fine. Be that way!"
    elif (
        hey_bob == hey_bob.upper() and hey_bob != hey_bob.lower() and hey_bob[-1] == "?"
    ):
        return "Calm down, I know what I'm doing!"
    elif hey_bob == hey_bob.upper() and hey_bob != hey_bob.lower():
        return "Whoa, chill out!"
    elif hey_bob.strip()[-1] == "?":
        return "Sure."
    return "Whatever."
