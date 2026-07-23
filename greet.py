def greet(name):
    return f"Hello, {name}!"


def shout(text):
    return text.upper() + "!"


if __name__ == "__main__":
    print(greet("world"))
    print(shout("this is a practice project"))
