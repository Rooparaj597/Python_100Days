# Access from anywhere
game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    # Access inside the function
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
