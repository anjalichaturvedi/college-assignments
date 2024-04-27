while True:
    action = input("Enter 'add' to add color, 'remove' to remove color, or 'done' to stop: ")
    if action.lower() == 'done':
        break
    elif action.lower() == 'add':
        color = input("Enter color to add: ")
        favorite_colors.add(color)
    elif action.lower() == 'remove':
        color = input("Enter color to remove: ")
        favorite_colors.discard(color)
    else:
        print("Invalid action.")

print("Updated favorite colors set:", favorite_colors)
