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

help(numbers_list)
