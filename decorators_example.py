import datetime


def func_name(func):

    def stat():
        print("-" * 100)
        print(f"Executing function - {func.__name__}")
        func()
        print("-" * 100)

    return stat


def func_time(func):

    def stat():
        print("-" * 100)
        print(f"Function executed at - {datetime.datetime.now()}")
        func()

    return stat


@func_time
@func_name
def test_function(): print("I am a printer !! ")


if __name__ == '__main__':
    test_function()
