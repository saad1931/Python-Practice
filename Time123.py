import time


def plus(a, b):
    return a + b
def lis():
    list = ["Saad", "Asad", "Ali", "Kamran"]
    for items in list:
        print(items,"," ,end="")


if __name__ == '__main__':
    initial_time = time.time()
    local_time = time.ctime()

    i = 0
    while (i < 100):
        print("loop1 is running")
        i += 1
    print(f"While loop takes {time.time() - initial_time} seconds")

    time.sleep(5)
    print("-------------------------------------------------")

    initial_time2 = time.time()
    for items in range(100):
        print("loop2 is running")
    print(f"For loop takes {time.time() - initial_time2} seconds")

    print(f"This code is running on {local_time}")

    def actualtime(str):
        print(f"{str} {local_time}")


    print(plus(2, 2))
    print(lis())

