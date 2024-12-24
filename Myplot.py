import random
import matplotlib
import matplotlib.pyplot as plt


def rollDice():
    roll = random.randint(1, 100)
    if roll == 100:
       # print("The roll was 100, you lose. What are the odds? Play Again!")
        return False
    elif roll <= 50:
         # print (roll, "roll was 1 - 50 you lose!")
        return False

    elif 100 > roll >  50:
        # print (roll, " Roll was between 51 - 99. You win!!! Play more!")
        return True


def simple_bettor (funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    curent_wager = 1

    while curent_wager <= wager_count:
        if rollDice():
            value += wager
            wX.append(curent_wager)
            vY.append(value)
        else:
            value -= wager
            wX.append(curent_wager)
            vY.append(value)


        curent_wager +=1


    if value < 0:
        value = 'broke'
    # print ('Funds: ', value)

    plt.plot(wX,vY)
x = 0
while x < 1000:
    simple_bettor(10000, 100, 100000)
    x+=1

plt.ylabel('Account Value')
plt.xlabel("Wager Count")
plt.show()


