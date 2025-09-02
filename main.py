from waggle.plugin import Plugin


def main():
    with Plugin() as plugin:
        print("This is the start of an amazing app!")
        plugin.publish("Hellow World")


if __name__ == "__main__":
    main()
