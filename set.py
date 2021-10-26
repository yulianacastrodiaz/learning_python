colors = {"Red", "White", "Pink", "Violet"}

print(type(colors))
print(dir(colors))

print(colors)
print("Red" in colors)

colors.add("Blue")
print(colors)

colors.remove("Red")
print(colors)


colors.clear()
print(colors)

del colors  # esto elimina la variable
