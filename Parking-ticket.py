# Parking Ticket Payment Helper
def calculate_change(paid, price):
    change = paid - price
    return change
 
ticket_price = 30
print(f"This parking ticket costs {ticket_price} units.")
print("Accepted coins: 1, 5, 10, 25\n")
 
total_inserted = 0
coins_inserted = 0
 
while True:
    coin = int(input("Insert a coin (1, 5, 10, or 25): "))

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin, try again!")
        continue
 
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")
 
    if total_inserted >= ticket_price:
        print("Enough money inserted!")
        break

change_due = calculate_change(total_inserted, ticket_price)
 
print("Printing your parking ticket...")

if change_due == 0:
    print("No change due. Thank you for your payment!")
else:
    print(f"Here is your change: {change_due} units")
 