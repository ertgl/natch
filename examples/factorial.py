import natch


@natch.lt(0)
def factorial(x):
    x = abs(x)
    x = factorial(x)
    x = -1 * x
    return x


@natch.eq(0)
def factorial(x):
    return 1


@natch.eq(1)
def factorial(x):
    return 1


@natch.gt(1)
def factorial(x):
    x = x * factorial(x - 1)
    return x


for i in [*range(-5, 0), *range(6)]:
    result = factorial(i)
    print(i, result)
