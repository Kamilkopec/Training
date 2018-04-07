# create a function that calculates acceleration given initial velocity v1
# final velocity v2, start time t1, and end time t2.
# formula for acceleration is:
# a = (V2 - V1)/(t2-t1)


def acceleration(V1, V2, T1, T2):
    a = (V2 - V1) / (T2 - T1)
    print(a)


def user_input():
    V1 = int(input("What is your initial velocity?: "))
    V2 = int(input("What is your final velocity?:"))
    T1 = int(input("What is your starting time?: "))
    T2 = int(input("What is your end time?: "))
    return V1, V2, T1, T2


def main():
    x = user_input()
    V1, V2, T1, T2 = x
    acceleration(V1, V2, T1, T2)


main()


