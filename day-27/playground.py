def add(*args):
    answer = 0
    for n in args:
        answer += n

    return answer


print(add(2, 3, 5, 21))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # Does not work if there's no argument
        # self.make = kw["make"]
        # self.model = kw["model"]

        # Works even without argument
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car()
print(my_car)
print(my_car.make)
