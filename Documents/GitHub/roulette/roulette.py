import random

def choosePick():
   pick = input('Pick Red or Black: ').lower()
   if pick != 'red' and pick != 'black':
        print('Invalid Pick')
        choosePick()
   return pick

def startGame():   
    balance = 0
    while balance <= 0:
        try:
            balance = int(input('Please enter the amount to use: '))
            if balance <= 0:
                print('Please enter a positive amount.')
        except ValueError:
            print('This is not a number.')
    newRound(balance)

def newRound(balance):
    stake = 0
    while stake > balance or stake <= 0:
        try: 
            stake = int(input('Please enter your stake: '))
            if stake > balance:
                print('You do not have enough balance to stake that amount.')
            elif stake <= 0:
                print('Please enter a positive amount.')
        except ValueError:
            print('This is not a number.')
    pick = choosePick()
    spin = game(pick)
    result = calculateWinner(pick, spin)
    calculateBalance(balance, stake, result)

def game(pick):
    spin = random.randrange(1,33)
    if spin in range(1,16):
        spin = 'red'
    elif spin in range(17,32):
        spin = 'black'
    else:
        spin = 'green'
    print('The spin was: ' + spin)
    return spin

def calculateWinner(pick, spin):
    result = ''
    if spin == pick:
        print('Win')
        result = 'win'
    else:
        print('Lose')
        result = 'lose'
    return result

def calculateBalance(balance, stake, result):
    balance -= stake
    if result == 'win':
        balance += stake * 2
    print('Your balance is: ' + str(balance))
    if balance > 0:
        playAgain = input('Do you want to play again?:  ').lower()
        if playAgain == 'y' or playAgain == 'yes':
            newRound(balance)
    else:
        print('Your wallet is empty, game over.')
    
def main():
    startGame()


if __name__ == '__main__':
    main()
    
