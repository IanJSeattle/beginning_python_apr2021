shopping_list = [('beans', 1.35),
                 ('lettuce', 2),
                 ('banana', 10),
                 ('bread', 5)]

total_price = 0
for item in shopping_list:
    name = item[0]
    price = item[1]
    print(name)
    total_price += price

print(f'total price: {total_price}')
