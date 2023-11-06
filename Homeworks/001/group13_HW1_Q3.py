# Firstly,I created variables to hold the starting values.
Time = 0
Bacteria_X = 10
Bacteria_Y = 10
Toxin_X = 0
Toxin_Y = 0

while Time <= 1000 and (
        (Bacteria_Y - Toxin_X * 0.005 > Bacteria_Y * 0.001) and (Bacteria_X - Toxin_Y * 0.01 > Bacteria_X * 0.001)):
    # I wrote the conditions of the homework which are iteration is less than or equal to 1000 and change in concentrations are less than 0.1%.

    # Incrase rate of bacteria X
    Bacteria_X *= 1.41
    # Incrase rate of bacteria Y)
    Bacteria_Y *= 1.55
    # Produced amount of toxin X
    Toxin_X += Bacteria_X * 0.5
    # Produced amount of toxin Y
    Toxin_Y += Bacteria_Y
    # Amount of bacteria Y killed by toxin X
    Bacteria_Y -= Toxin_X * 0.005 * Bacteria_Y
    # Amount of bacteria Y killed by toxin Y
    Bacteria_X -= Toxin_Y * 0.010 * Bacteria_X
    # Degradation amount of toxin Y
    Toxin_Y *= 0.95

    Time += 1

    print(f"\tHour {Time}")
    print(f"--------------")
    print(f"{Bacteria_X} moles of Bacteria X")
    print(f"{Bacteria_Y} molese of Bacteria Y")
    print(f"{Toxin_X} moles of Toxin X")
    print(f"{Toxin_Y} moles of Toxin Y")
