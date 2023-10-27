# escape_by function
def escape_by(plan):
    # Determine which message to display
    if plan == "jumping over":
        return "We cannot escape that way! The boulder is too big"
    elif plan == "running around":
        return "We cannot escape that way! The boulder is moving too fast!"
    elif plan == "cross bridge ahead":
        return "That might just work! Let's go!"
    else:
        return "We cannot escape that way! The boulder is in the way!"


# Calls to the function
print(escape_by("jumping over"))
print(escape_by("running around"))
print(escape_by("cross bridge ahead"))


