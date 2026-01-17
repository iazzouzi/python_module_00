x = int(input("Days until harvest: "))
y = x


def ft_count_harvest_recursive(x):
    if (x > 1):
        ft_count_harvest_recursive(x - 1)
    print("Day", x)
    if (y == x):
        print("Harvest time!")
