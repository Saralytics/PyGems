import random

def deal(n, hand):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    for idx in range(n):
        idx = random.randint(0,len(cards)-1)
        hand.append(cards[idx])
    return hand

def show_one(hand):
    print(f"The dealer hand is {hand[0]} \n")

def show_all(role,hand):
    print(f"{role} hand is {hand} - total is {sum(hand)}\n")

def tally(hand):
    score = sum(hand)
    if (11 in hand) & (score > 21):
        score -= 10
    return score

def comparison(user_score, dealer_score):
    if user_score > 21:
        return "dealer"
    if user_score == 21 & user_score != dealer_score:
        return "user"
    if user_score == dealer_score:
        return "tie"
    if user_score - 21 > dealer_score - 21:
        return "user"
    else:
        return "dealer"
    
def hit(hand):
    """The user deal again 1 card"""
    hand = deal(1,hand)
    show_all("User",hand)

def stand():
    """Both hands are revealed. 
    If the dealer score < 17, the dealer will recursively deal 1 card
    until the score is >= 17"""

    print("====================\n  Now reveal \n====================== ")
    show_all("User", user_hand)
    show_all("Dealer", dealer_hand)

    while tally(dealer_hand) < 17:
        deal(1,dealer_hand)
        print("Dealer score small than 17, deal one more ")
    
    show_all("Dealer",dealer_hand)
    winner = comparison(sum(user_hand), sum(dealer_hand))
    print(f"Winner is {winner} ")
    return

# Deal
user_hand, dealer_hand = [],[]
user_hand = deal(2,user_hand)
dealer_hand = deal(2,dealer_hand)
show_all("User",user_hand)
show_one(dealer_hand)

# game begins
while True:
    user_score = tally(user_hand)
    dealer_score = tally(dealer_hand)

    if user_score > 21:
        print(f"Dealer hand is {dealer_hand}")
        print( "dealer wins! ")
        break

    if user_score == 21 & user_score != dealer_score:
        print(f"Dealer hand is {dealer_hand}")
        print("user wins!")
        break

    hit_or_stand = input("HIT or STAND? ").upper()
    if hit_or_stand == "HIT":
        hit(user_hand)
    else:
        stand()
        break

print("=========================\n         END GAME       \n==========================")

