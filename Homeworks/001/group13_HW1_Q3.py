import time

currentTime = 0
bacteria_X = 10  # mol
bacteria_Y = 10  # mol

amount_of_bacteria_produced_by_X = 0.41
amount_of_bacteria_produced_by_Y = 0.55

amount_of_toxin_produced_by_X = 0.50
amount_of_toxin_produced_by_Y = 1.00

toxin_X = 0
toxin_Y = 0


def produceBacteria():
    global bacteria_X
    global bacteria_Y

    bacteria_X += amount_of_bacteria_produced_by_X
    bacteria_Y += amount_of_bacteria_produced_by_Y


def produceToxin():
    global toxin_X
    global toxin_Y

    toxin_X += amount_of_toxin_produced_by_Y
    toxin_Y += amount_of_toxin_produced_by_X


def effectPoisions():
    global bacteria_Y
    global bacteria_X
    global  toxin_Y
    global  toxin_X

    bacteria_X -= (bacteria_X * 0.01) * toxin_Y
    bacteria_Y -= (bacteria_Y * 0.005) * toxin_X

def degradeToxinY():
    global  toxin_Y
    toxin_Y -= toxin_Y * 0.05

def TickTock():
    global currentTime
    global bacteria_X
    global bacteria_Y
    global amount_of_bacteria_produced_by_Y
    global amount_of_bacteria_produced_by_X
    global amount_of_toxin_produced_by_Y
    global amount_of_toxin_produced_by_X

    previousBacteriaX = 0
    previousBacteriaY = 0

    while currentTime < 1000:

        produceBacteria()
        produceToxin()
        effectPoisions()
        degradeToxinY()


        currentTime += 1

        print(f"\tHour {currentTime}")
        print(f"--------------")
        print(f"{bacteria_X} moles of Bacteria X")
        print(f"{bacteria_Y} molese of Bacteria Y")
        print(f"{toxin_X} moles of Toxin X")
        print(f"{toxin_Y} moles of Toxin Y")

        time.sleep(0.4)

        # if change in concentrations smaller than 0.1% we break here
        if(abs(bacteria_X - previousBacteriaX) <0.01 or abs(bacteria_Y - previousBacteriaY) <0.01  ):
            print("\nSteady state has been occured!")
            break

        previousBacteriaX = bacteria_X
        previousBacteriaY = bacteria_Y


TickTock()