def funcThree():
    print("three")


def funcTwo():
    funcThree()
    print("two")


def funcOne():
    funcTwo()
    print("one")

funcOne()