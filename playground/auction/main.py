import art.gavel

print(art.gavel.gavel)
print("Welcome to the silent bid! ")

bids = {}
more_bidder = True

while more_bidder: 
    name = input("Your name please: ")
    amount = float(input("Your bid: "))

    bids[name] = amount
    add_another = input("Is there another bidder? Enter Yes or No ")
    if add_another == "No":
        more_bidder = False

## find out who the highest bidder is 
highest_amount = 0 
winner = ""
for bidder in bids:
    if bids[bidder] > highest_amount:
        highest_amount = bids[bidder]
        winner = bidder

print(f"The winner is {winner} with bid amount {highest_amount}")