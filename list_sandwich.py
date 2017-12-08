# print each item in sandwich_orders then remove and append to finished_sandwiches
# remove pastrami from sandwich_orders

sandwich_orders = ["clam roll","tuna","pastrami","hamburger","pastrami","club","bologna roll","pastrami","gyro","torta","falafel"]
finished_sandwiches = []

print("The deli has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    for order in sandwich_orders:
        print("I have made your", order, "sandwich")
        finished_sandwiches.append(order)
        sandwich_orders.remove(order)

print(sandwich_orders)
print(finished_sandwiches)
