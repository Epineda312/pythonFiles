from art import logo

bids = {}
bidding_finished = False

# function to find highest bidder
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} with a bid of ${highest_bid}")
    
# Show logo from Art.py
print(logo)

while not bidding_finished:
    # ask for name input
    name = input("What is your name?\n")
    # ask for bid price
    bid_price = int(input("What is your bid price? $\n"))
    # add new key value pair to dictionary
    bids[name] = bid_price
    # ask if there are other users who want to bid
    should_continue = input("Is there any other bidders? Please type 'Y' or 'N'\n").lower()
    # If there is no more new bidders, find current highest and display it while ending the loop.
    if should_continue == 'n':
        bidding_finished = True
        find_highest_bidder(bids)
    # if yes, clear the screen, ask for the next name (do not end loop)
    elif should_continue == 'y':
        clear()
