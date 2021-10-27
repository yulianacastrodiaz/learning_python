demo_list = [1, 2, "hello", [3, 5, 4], True]
colors = ["red", "yellow", "green", "pink"]

numbers_list = list((1, 2, 3, 4))
print(numbers_list)

range_numbers = list(range(1, 10))
print(range_numbers)

print(dir(colors))

print(colors)
print(len(colors))
print("green" in colors)
colors[1] = "orange"
print(colors)
colors.append("violet")
print(colors)
colors.extend(["brown", "black"])
print(colors)

colors.insert(1, "white")
print(colors)

colors.pop()
print(colors)
colors.pop(1)
print(colors)

colors.remove("brown")
print(colors)

colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)

print(colors.index("pink"))
print(colors.count("pink"))

colors.clear()
print(colors)

demo_list += [4, 5, 6]
print(demo_list)

print(min(numbers_list))
print(max(numbers_list))

# help(numbers_list)

new_list = [1] * 10
print(new_list)

new_list2 = new_list  # pasaje por referencia
print(new_list2)

new_list2[7] = 3
print(new_list)
print(new_list2)

copy_of_list = new_list.copy()  # pasaje por valor
copy_of_list[3] = 4
print(new_list)
print(copy_of_list)

new_list = [1] * 10
list_slice = new_list[:]  # asigna todos los valores de new_list y es pasaje por valor
list_slice[2] = 34
print(new_list)
print(list_slice)

print(list_slice[3:])  # desde el índice 3 hasta el largo
print(list_slice[:5])  # desde el comienzo hasta el índice 5
print(list_slice[3:5])
print(list_slice[3:7:2])  # desde la posición 3 hasta la 7 de 2 en 2

list_with_for = [i for i in range(10)]
list_with_for2 = [i ** 2 for i in range(10)]
print(list_with_for)
print(list_with_for2)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)
print(matriz[0][2])
print(matriz[2][1])
