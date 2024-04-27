favorite_colors = set()

while True:
    color = input("Enter favorite color (enter 'done' to stop): ")
    if color.lower() == 'done':
        break
    else:
        favorite_colors.add(color)

print("Favorite colors set:", favorite_colors)
