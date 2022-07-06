import numpy as np
def draw_card(s):
    card = np.random.randint(2, 11)
    if card == 11:
        if s + card > 21: return 1
        else: return 11
    else: return card
player= []
dealer = []
print("Welcome to a game of Balckjack")
print("You will start of with $100")
money = 100
def main():
    global money
    while True:
        bet = input("How much are you willing to bet: ")
        try: 
            if money >= int(bet) > 0:
                print("Thank You")
                bet = int(bet)
                break
            else:
                print("Please enter a number that is less than {}, and greater than 0".format(money))
        except: print("Please Enter a number")
    player.append(draw_card(sum(player)))
    player.append(draw_card(sum(player)))
    print("Your Hand: {}".format(player))
    dealer.append(draw_card(sum(dealer)))
    print("The Dealer is showing a {}".format(dealer[0]))
    dealer.append(draw_card(sum(dealer)))
    while True:
        act = input("Stay or Hit: ")
        try:
            act = act.upper()
            if act == 'STAY': 
                break
            if act == 'HIT':
                player.append(draw_card(sum(player)))
                print("You got a {}, total is {}" .format(player[-1], sum(player)))
                if sum(player) > 21:
                    money = money - int(bet)
                    print("You went over 21")
                    print("You have {} dollars".format(money))
                    return
                elif sum(player) == 21:
                    money = money + int(bet)
                    print("You got 21 \nYou win")
                    print("You have {} dollars".format(money))
                    return
            else: print("Please Stay or Hit")
        except:
            print("Please Stay or Hit")
    while True:
        print("The deal has {}".format(sum(dealer)))
        if sum(dealer) == 21:
            print("Dealer has 21 \nThe house wins")
            money = money - int(bet)
            print("You have {} dollars".format(money))
            return
        elif 21 > sum(dealer) > sum(player): 
            print("The Dealer has more \nThe house wins")
            money = money - int(bet)
            print("You have {} dollars".format(money))
            return
        elif sum(dealer) > 21:
            print("The dealer is over 21")
            money = money + int(bet)
            print("You have {} dollars".format(money))
            return
        else:
            dealer.append(draw_card(sum(dealer)))
def game():
    global money
    while True:
        main()
        dealer.clear()
        player.clear()
        if money <= 0:
            print("You have no more money, you fool!")
            return
        while True:
            stop = input("Play again? ")
            try:
                stop = stop.upper()
                if stop == 'NO':
                    print('You came out with {} more than what you started out with'.format(money - 100))
                    print("Thank you for playing")
                    return
                if stop != 'NO' and stop != 'YES':
                    print("Yes or NO:")
                else:
                    break
            except:print("Yes or No")
game()