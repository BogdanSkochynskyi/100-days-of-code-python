from art import logo

print(logo)
user_name = input("Please enter your name: ")
user_price = input("Please enter the price: ")
auction_data = {user_name: user_price}
new_bid = input("Yes or no for new bid?: ")
is_new_bid = new_bid.lower() == "yes"
while is_new_bid:
    print("\n" * 20)
    user_name = input("Please enter your name: ")
    user_price = input("Please enter the price: ")
    auction_data[user_name] = user_price
    new_bid = input("Yes or no for new bid?: ")
    is_new_bid = new_bid.lower() == "yes"
max_bidder_name = ""
max_bidder_value = 0
for key, value in auction_data.items():
    if int(value) > int(max_bidder_value):
        max_bidder_name = key
        max_bidder_value = value

print(f"Best bid of {max_bidder_name} is ${max_bidder_value}")
