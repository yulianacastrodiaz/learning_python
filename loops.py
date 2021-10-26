foods = ["apples", "bread", "cheese", "milk", "bananas", "grapes"]

for food in foods:
    if food == "milk":
        print("Debes comprar milk")
    print(food)

for food in foods:
    if food == "cheese":
        continue
    print(f"Debes comprar esta comida {food}")

for food in foods:
    if food == "cheese":
        break
    print(food)

for number in range(1, 8):
    print(number)

for letter in "Hello":
    print(letter)

count = 4

while count <= 10:
    print(count)
    count += 1
