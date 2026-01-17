def ft_plant_age():
    x = int(input("Enter plant age in days: "))
    if (x > 60):
        print("Plant is ready to harvest!")
    elif (x <= 60):
        print("Plant need more time to grow.")
