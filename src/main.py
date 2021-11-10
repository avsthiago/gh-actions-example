def hello_world(name="world"):
    hello = f"hello {name}"
    print(hello)
    return hello


if __name__ == "__main__":
    hello_world('user')
