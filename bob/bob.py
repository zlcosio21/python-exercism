def response(hey_bob):
    message = hey_bob.rstrip()

    if not message:
        return "Fine. Be that way!"

    if message.isupper() and "?" == message[-1]:
        return "Calm down, I know what I'm doing!"

    if "?" == message[-1]:
        return "Sure."

    if message.isupper() and "?" != message[-1]:
        return "Whoa, chill out!"

    return "Whatever."