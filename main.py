from api import fetcher


def main_wrapper():
    print(f"This is the start of our python project. This function's name is {main_wrapper.__name__}")

    fetcher.states_accessor()

    print("This is the end of out python project.")


if __name__ == "__main__":
    main_wrapper()
