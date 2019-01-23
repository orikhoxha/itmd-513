import re

# Validate user input function
def get_user_input(message):


    while True:
        userinput = input(message)
        num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
        is_number = re.match(num_format, userinput)
        if userinput == '':
            print("Please do not leave the input blank")
        elif not is_number:
            print("Please enter a digit")
        elif float(userinput) <= 0:
            print("Please enter a non-negative number greater than 0")
        else:
            break
    return float(userinput)


# Validate the number of shares to be sold
def get_num_shares_sold(message):
    while True:
        shares_sold = get_user_input(message)
        if shares_sold > num_shares_purchased:
            print("You cannot sell more shares than you have purchased. Please try again.")
            continue
        break
    return shares_sold


# Validate the commission percentage
def get_commission_percentage(message):
    while True:
        commission_charge = get_user_input(message)
        if commission_charge > 100:
            print("The commission must be less than 100%. Please try again")
            continue
        break
    return commission_charge / 100


# Purchase calculations
num_shares_purchased = get_user_input("Number of shares to be purchased: ")
price_per_share_purchased = get_user_input("Enter the price per share purchased($): ")
commission_charge_percentage_purchased = get_commission_percentage("Enter the commission percentage(%) for purchasing shares: ")
price_per_stock_purchased = num_shares_purchased * price_per_share_purchased
commission_charge_purchased = price_per_stock_purchased * commission_charge_percentage_purchased

# Sold calculations
num_shares_sold = get_num_shares_sold("Number of shares to be sold: ")
price_per_share_sold = get_user_input("Enter the price per share sold($): ")
commission_charge_percentage_sold = get_commission_percentage("Enter the commission percentage(%) for selling shares: ")
price_per_stock_sold = num_shares_sold * price_per_share_sold
commission_charge_sold = num_shares_sold * price_per_share_sold * commission_charge_percentage_sold

# profit calculation
stock_profit = price_per_stock_sold - (commission_charge_sold + commission_charge_purchased + price_per_stock_purchased)

print("Joe paid for the stock %.2f $ " % price_per_stock_purchased)
print("The amount of commission Joe paid his broker when he bought the stock was %.2f $" % commission_charge_purchased)
print("Joe sold the stock for %.2f $ " % price_per_stock_sold)
print("The amount of commission Joe paid his broker when he sold the stock was %.2f $" % commission_charge_sold)
print("The amount of the money Joe had left %.2f $" % stock_profit)

