# import keyword
# print(keyword.kwlist)

# Assignment 1
def calc_change(paid, price):
    change = paid - price
    return change

print("Change:", change)

snack_price = 25
print("Snack vending machine")
print("Accepted coins: 1, 5, 10, 25")
total_inserted = 0.0
coins_inserted = 0

while True:
    coin = int(input("Insert coin (1, 5, 10, 25) or 0 to finish: "))
    if coin != 1 and coin != 5 and coin != 10 and coin!= 25:
        print("Invalid coin: Try again")
        continue
    total_inserted += coin
    coins_inserted += 1
    print("Total inserted:", total_inserted)

    if total_inserted >= snack_price:
        print("Enough money inserted. Dispensing snack...")
        break

    change_due = calc_change(total_inserted, snack_price)
    