painting_members = {'Alice', 'Bob', 'Charlie', 'David'}
chess_members = {'Alice', 'Eve', 'Frank', 'David'}
dance_members = {'Alice', 'Bob', 'Grace', 'David'}
yoga_members = {'Eve', 'Frank', 'Grace', 'Harry'}

all_members = painting_members.union(chess_members, dance_members, yoga_members)
print("All unique members:", all_members)

all_courses_members = painting_members.intersection(chess_members, dance_members, yoga_members)
print("Members enrolled for all four courses:", all_courses_members)

dance_not_yoga_members = dance_members.difference(yoga_members)
print("Members enrolled for dance but not yoga:", dance_not_yoga_members)

either_painting_or_chess_members = painting_members.symmetric_difference(chess_members)
print("Members enrolled for either painting or chess but not both:", either_painting_or_chess_members)

if dance_members.isdisjoint(yoga_members):
    print("Dance and yoga have no common participants.")
else:
    print("Dance and yoga have common participants.")
