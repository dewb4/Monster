import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Preliminary setup for journal, legacy mechanics, and gendered NPC interactions
journal = ["Find the secrets of the Fog."]
deaths = 0
victims = []
killers = []
killer_shields = []
genders = ["She", "He"]
health = 3

# Set up the window
WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button Clicker")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

background_image = pygame.image.load("FogMenu2.jpg")

# Set up fonts
font_path = "zig.ttf"
font_size = 20
font = pygame.font.Font(font_path,font_size)

# Function to display text
def draw_text(text, color, x, y):
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    rect.topleft = (x, y)
    WINDOW.blit(surface, rect)

def draw_border(rect, fill_color, border_color, border_width):
    pygame.draw.rect(WINDOW, fill_color, rect)
    border_rect = rect.inflate(border_width * 1, border_width * 1)
    pygame.draw.rect(WINDOW, border_color, border_rect, border_width)

def split_text(text, max_width):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + " " + word if current_line else word
        width, _ = font.size(test_line)
        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

# Function to display text wrapped within a rectangle
def draw_wrapped_text(text, color, rect):
    lines = split_text(text, rect.width)
    y = rect.top
    for line in lines:
        surface = font.render(line, True, color)
        WINDOW.blit(surface, (rect.left, y))
        y += surface.get_height()

def animate_text(text, color, x, y):
    for i in range(len(text)+1):
        draw_text(text[:i], color, x, y)
        pygame.display.flip()
        pygame.time.wait(50)  # Adjust the speed of text animation here

def text_wrapping(text):
    WINDOW.fill(WHITE)
    animate_text(text, WHITE)

def draw_input_field(x, y, width, height, color, text, active):
    pygame.draw.rect(WINDOW, color, (x, y, width, height))
    if active:
        pygame.draw.rect(WINDOW, RED, (x, y, width, height), 2)
    draw_text(text, BLACK, x, y)

# Function to create a button
def draw_button(x, y, width, height, color):
    pygame.draw.rect(WINDOW, color, (x, y, width, height))

# Main loop
def main_menu():
    pygame.mixer.music.load("Fogmusic.mp3")
    running = True
    button_clicked = False

    while running:
        WINDOW.blit(background_image, (0, 0))  # Blit the background image

        # Draw button
        button_rect = pygame.Rect(800, 100, 100, 50)
        draw_button(button_rect.x, button_rect.y, button_rect.width, button_rect.height, RED)

        # Draw text on the button
        draw_text("Click me!", BLACK, button_rect.x + 15, button_rect.y + 15)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    game_state = "charname"
                    return game_state

        pygame.display.flip()

def charname():
    running = True
    first_name = ""
    last_name = ""
    active_input = None

    while running:
        WINDOW.fill(BLACK)

        # Draw prompt and input fields
        draw_text("Enter your first name:", BLACK, 600, 100)
        draw_input_field(600, 150, 300, 30, WHITE, first_name, active_input == "first_name")

        draw_text("Enter your last name:", BLACK, 600, 200)
        draw_input_field(600, 250, 300, 30, WHITE, last_name, active_input == "last_name")

        button_rect = pygame.Rect(600, 50, 100, 50)
        firstname_box = pygame.Rect(600, 150, 300, 30)
        lastname_box = pygame.Rect(600, 250, 300, 30)
        draw_button(button_rect.x, button_rect.y, button_rect.width, button_rect.height, RED)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if firstname_box.collidepoint(event.pos):
                    active_input = "first_name"
                elif lastname_box.collidepoint(event.pos):
                    active_input = "last_name"
                elif button_rect.collidepoint(event.pos):
                    game_state = "game"
                    return game_state
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    # Handle backspace to remove characters from the active input field
                    if active_input == "last_name":
                        last_name = last_name[:-1]
                    elif active_input == "first_name":
                        first_name = first_name[:-1]
                else:
                    # Add characters to the active input field
                    if active_input == "first_name" and len(first_name) < 20:
                        first_name += event.unicode
                    elif active_input == "last_name" and len(last_name) < 20:
                        last_name += event.unicode
                
        pygame.display.flip() 

def text_animation(text):
    pygame.display.flip()
    talking = True
    animate_text(text, WHITE, 5, 520)
    draw_text(text, WHITE, 5, 520)
    talking = False

def text_animation2(text):
    pygame.display.flip()
    animate_text(text, WHITE, 5, 550)
    draw_text(text, WHITE, 5, 550)

def clear_text():
    draw_button(0, 512, 1000, 200, BLACK)

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            img = pygame.image.load(os.path.join(folder, filename))
            images.append(img)
    return images

def load_image_filenames_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        images.append(filename)
    return images

def display_random_image(images):
    random_image = random.choice(images)
    WINDOW.blit(random_image, (0, 0))
    pygame.display.flip()
    return random_image
    

def game():
    running = True
    talking = True
    journal = ["Find the secrets of the Fog."]
    deaths = 0
    victims = []
    killers = []
    killer_shields = []
    genders = ["She", "He"]
    health = 3
    just_attacked = False
    pygame.mixer.music.load("Monsternear.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0)
    with open('journals.txt', 'r') as file:
        journals = file.read().splitlines()
    with open('areas/creatures.txt', 'r') as file:
        creatures = file.read().splitlines()
    with open('creature_names.txt', 'r') as file:
        creature_names = file.read().splitlines()
    with open('areas/forests.txt', 'r') as file:
        forests = file.read().splitlines()
    with open('areas/swamps.txt', 'r') as file:
        swamps = file.read().splitlines()
    with open('areas/meadows.txt', 'r') as file:
        meadows = file.read().splitlines()
    with open('areas/lakes.txt', 'r') as file:
        lakes = file.read().splitlines()
    with open('areas/valleys.txt', 'r') as file:
        valleys = file.read().splitlines()
    with open('areas/camps.txt', 'r') as file:
        camps = file.read().splitlines()
    with open('areas/towers.txt', 'r') as file:
        towers = file.read().splitlines()
    with open('areas/crypts.txt', 'r') as file:
        crypts = file.read().splitlines()
    with open('areas/caves.txt', 'r') as file:
        caves = file.read().splitlines()
    with open('areas/chapels.txt', 'r') as file:
        chapels = file.read().splitlines()
    with open('areas/treehouses.txt', 'r') as file:
        treehouses = file.read().splitlines()
    with open('areas/gardens.txt', 'r') as file:
        gardens = file.read().splitlines()
    with open('warnings.txt', 'r') as file:
        warnings = file.read().splitlines()
    with open('asks.txt', 'r') as file:
        asks = file.read().splitlines()
    with open('lore.txt', 'r') as file:
        lore = file.read().splitlines()
    cmd = []
    moves = 100
    old_man = 0
    health_image = pygame.image.load("Heart.png")
    health_image = pygame.transform.scale(health_image, (50,50))
    WINDOW.fill(BLACK)
    folder = "abs"
    images = load_images_from_folder(folder)
    display_random_image(images)
    WINDOW.blit(health_image, (840, 10))  # Blit the background image
    WINDOW.blit(health_image, (890, 10))  # Blit the background image
    WINDOW.blit(health_image, (940, 10))  # Blit the background image

    text_animation(f"You find yourself in a strange land shrouded by fog.")
    text_animation2("It is nearly silent.")
    
    defending = False
    luring = False
    attacking = False
    chance_of_finding_tool = 0.25
    chance_of_meeting_npc = 0.15
    chance_of_meeting_man = 0.01
    actions = 3
    biomes = ["forest", "lake", "meadow", "valley", "swamp"]
    points = ["treehouse", "garden", "chapel", "crypt", "radio tower", "camp", "cave"]
    items = ["cursed blood", "snakeskin boots", "blanket", "music box",
             "poison mushroom", "rancid vegetable", "mirror", "salt", "silver sword",
             "wooden stake", "ancient tome", "water bottle", "torch", "cigarette",
             "crucifix"]
    tools = ["torn journal", "medkit", "binoculars", "trap", "sensor"]
    forest_items = ["wood", "berry", "mushroom", "herb", "stone", "sap", "feather"]
    meadow_items = ["flower", "grass", "honey", "clay", "wild onion", "wild garlic", "reed"]
    swamp_items = ["mud", "swamp grass", "moss", "bog iron", "leech", "swamp ash"]
    lake_items = ["cattail", "fish", "clam", "algae", "water lily"]
    valley_items = ["stone", "gemstone", "granite", "gold dust", "lily of the valley"]

    monsters_items = [
        {"name": "Cherub", "weapon": "cursed blood", "shield": "snakeskin boots", "lure": "blanket"},
        {"name": "Fairy Queen", "weapon": "music box", "shield": "cursed blood", "lure": "poison mushroom"},
        {"name": "Dark Vampire", "weapon": "rancid vegetable", "shield": "mirror", "lure": "cursed blood"},
        {"name": "Fallen Crusader", "weapon": "cursed blood", "shield": "salt", "lure": "silver sword"},
        {"name": "Father Rathburn", "weapon": "wooden stake", "shield": "ancient tome", "lure": "mirror"},
        {"name": "Fire Devil", "weapon": "water bottle", "shield": "cursed blood", "lure": "torch"},
        {"name": "Frost Serpent", "weapon": "cigarette", "shield": "torch", "lure": "snakeskin boots"},
        {"name": "Fungal Beast", "weapon": "crucifix", "shield": "blanket", "lure": "poison mushroom"},
        {"name": "Gargoyle", "weapon": "gargoyle", "shield": "music box", "lure": "crucifix"},
        {"name": "Giant Serpent", "weapon": "poison mushroom", "shield": "wooden stake", "lure": "snakeskin boots"},
        {"name": "Giant Slug Man", "weapon": "salt", "shield": "snakeskin boots", "lure": "rancid vegetable"},
        {"name": "Giant Termite", "weapon": "rancid vegetable", "shield": "cigarette", "lure": "wooden stake"},
        {"name": "Gorgon", "weapon": "silver sword", "shield": "mirror", "lure": "snakeskin boots"},
        {"name": "The Loner", "weapon": "music box", "shield": "silver sword", "lure": "cigarette"},
        {"name": "Hellhound", "weapon": "blanket", "shield": "silver sword", "lure": "rancid vegetable"},
        {"name": "Glowing Specter", "weapon": "mirror", "shield": "salt", "lure": "blanket"},
        {"name": "Lava Slime", "weapon": "salt", "shield": "wooden stake", "lure": "torch"},
        {"name": "Little Deerpire", "weapon": "wooden stake", "shield": "blanket", "lure": "music box"},
        {"name": "Living Vines", "weapon": "music box", "shield": "rancid vegetable", "lure": "water bottle"},
        {"name": "Lost Baby", "weapon": "blanket", "shield": "cigarette", "lure": "water bottle"},
        {"name": "Lot", "weapon": "water bottle", "shield": "crucifix", "lure": "salt"},
        {"name": "Magic Carpet", "weapon": "snakeskin boots", "shield": "water bottle", "lure": "ancient tome"},
        {"name": "Phoenix", "weapon": "blanket", "shield": "ancient tome", "lure": "torch"},
        {"name": "Rabid Cat", "weapon": "poison mushroom", "shield": "mirror", "lure": "water bottle"},
        {"name": "Shadow Demon", "weapon": "crucifix", "shield": "torch", "lure": "silver sword"},
        {"name": "The Prospector", "weapon": "poison mushroom", "shield": "cigarette", "lure": "salt"},
        {"name": "The Wise Man", "weapon": "cigarette", "shield": "cursed blood", "lure": "ancient tome"},
        {"name": "Treant", "weapon": "torch", "shield": "rancid vegetable", "lure": "poison mushroom"},
        {"name": "Vampire Lord", "weapon": "wooden stake", "shield": "crucifix", "lure": "cursed blood"},
        {"name": "Weeping Widow", "weapon": "mirror", "shield": "crucifix", "lure": "cigarette"},
        {"name": "Were-Beaver", "weapon": "silver sword", "shield": "water bottle", "lure": "wooden stake"},
        {"name": "Werewolf", "weapon": "silver sword", "shield": "poison mushroom", "lure": "ancient tome"},
        {"name": "Witch", "weapon": "torch", "shield": "music box", "lure": "mirror"},
        {"name": "Youthful Spirit", "weapon": "ancient tome", "shield": "salt", "lure": "music box"},
        {"name": "Zack the Zealot", "weapon": "ancient tome", "shield": "rancid vegetable", "lure": "crucifix"}
    ]

    monsters_lairs = {
        "Cherub": "chapel",
        "Fairy Queen": "garden",
        "Dark Vampire": "crypt",
        "Fallen Crusader": "chapel",
        "Father Rathburn": "chapel",
        "Fire Devil": "crypt",
        "Frost Serpent": "treehouse",
        "Fungal Beast": "garden",
        "Gargoyle": "chapel",
        "Giant Serpent": "garden",
        "Giant Slug Man": "cave",
        "Giant Termite": "treehouse",
        "Gorgon": "cave",
        "The Loner": "radio tower",
        "Hellhound": "cave",
        "Glowing Specter": "radio tower",
        "Lava Slime": "camp",
        "Little Deerpire": "treehouse",
        "Living Vines": "garden",
        "Lost Baby": "treehouse",
        "Lot": "chapel",
        "Magic Carpet": "radio tower",
        "Phoenix": "radio tower",
        "Rabid Cat": "camp",
        "Shadow Demon": "crypt",
        "The Prospector": "cave",
        "The Wise Man": "radio tower",
        "Treant": "garden",
        "Vampire Lord": "crypt",
        "Weeping Widow": "cave",
        "Were-Beaver": "treehouse",
        "Werewolf": "camp",
        "Witch": "camp",
        "Youthful Spirit": "crypt",
        "Zack the Zealot": "camp"
    }

    chosen_monster = random.choice(list(monsters_lairs.keys()))
    monster_lair = monsters_lairs[chosen_monster]
    lair_row = 0
    lair_col = 0

    for monster in monsters_items:
        if monster["name"] == chosen_monster:
            chosen_weapon = monster["weapon"]
            items.remove(monster["weapon"])
            chosen_shield = monster["shield"]
            items.remove(monster["shield"])
            chosen_lure = monster["lure"]
            items.remove(monster["lure"])
            break

    # guarantees one of the randomly placed special locations is the monster's lair
    if monsters_lairs[chosen_monster] in points:
        points.remove(monsters_lairs[chosen_monster])

    random_points = random.sample(points, 5)
    random_points.append(monsters_lairs[chosen_monster])

    # guarantees the monster's required items are in the random item selection

    random_items = random.sample(items, 2)
    random_items.append(str(chosen_weapon))
    random_items.append(str(chosen_shield))
    random_items.append(str(chosen_lure))

    # mark all points on the grid as unexplored
    grid_size = 6
    equipload = 0
    inventory = []

    searched = [
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False]
    ]
    examined = [
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False]
    ]

    # populate the grid with biomes
    grid = []
    for i in range(6):
        row = []
        for j in range(6):
            biome = random.choice(biomes)
            row.append(biome)
        grid.append(row)


    
    # put random special locations on random points in the grid
    for location in random_points:
        row = random.randint(0, grid_size-1)
        col = random.randint(0, grid_size-1)
        grid[row][col] = location

    for location in grid:
        if location == monster_lair:
            lair_row = location[row]
            lair_col = location[col]

    # place the player in a random square
    user_row = None
    user_col = None
    monster_row = None
    monster_col = None
    distance = 0
    while user_row is None or grid[user_row][user_col] in points:
        user_row = random.randint(0, grid_size-1)
        user_col = random.randint(0, grid_size-1)
    while monster_row is None or monster_row == user_row or distance <= 2:
        monster_row = random.randint(0, grid_size-1)
        monster_col = random.randint(0, grid_size-1)
        distance = abs(user_row - monster_row) + abs(user_col - monster_col)
    user_biome = grid[user_row][user_col]
    button_width, button_height = 100, 50
    west_button_rect = pygame.Rect(600, 200, button_width, button_height)
    draw_button(west_button_rect.x, west_button_rect.y, west_button_rect.width, west_button_rect.height, RED)
    
    while running:
        pygame.mixer.music.set_volume((distance*-0.2)+1)
        if health == 0:
            game_state = "charname"
            deaths += 1
            victims.append("Guy")
            killers.append(str(chosen_monster))
            killer_shields.append(str(chosen_shield))
            journal.append(f"Find guy's killer.")
            return game_state
        if moves == 0:
            game_state = "charname"
            deaths += 1
            victims.append("Guy")
            killers.append(str(chosen_monster))
            killer_shields.append(str(chosen_shield))
            journal.append(f"Find guy's killer.")
            return game_state
        if actions == 0:
            w = monster_col - user_col
            e = user_col - monster_col
            n = monster_row - user_row
            s = user_row - monster_row
            if w >= e and w >= n and w >= s:
                direction = w
            elif e >= w and e >= n and e >= s:
                direction = e
            elif n >= w and n >= e and n >= s:
                direction = n
            else:
                direction = s
            if direction == n:
                monster_row -= 1
            elif direction == s:
                monster_row += 1
            elif direction == e:
                monster_col += 1
            else:
                monster_col -= 1
            actions = 3
        distance = abs(user_row - monster_row) + abs(user_col - monster_col)
        if 1.1 <= distance <= 2:
            text_animation2("You hear the sound of movement in the distance.")
        if distance == 1:
            text_animation2("Something is close...")
        if distance == 0:
            print("What's that sound?")
            if defending:
                print(f"You feel a force attempt to attack you, but something deflects the blow. "
                    f"Maybe it was the {use_item}?")
                journal.append(f"{chosen_shield} is an effective shield against whatever is chasing me.")
            elif luring:
                print(f"You feel something approach, but it seems distracted by something."
                    f"Maybe it was the {use_item}?")
                journal.append(f"{chosen_lure} is an effective distraction against whatever is chasing me.")
            elif attacking:
                monster_col = lair_col
                monster_row = lair_row
                print("The unseen monster quickly flees.")
                journal.append(f"{chosen_weapon} is an effective weapon against whatever is chasing me.")
                attacking = False
            else:
                print("You feel a searing pain as you are attacked by an unseen entity.")
                health = health - 1
                actions  = actions - 1
                user_row = random.randint(0, grid_size-1)
                user_col = random.randint(0, grid_size-1)
                folder = "abs"
                images = load_images_from_folder(folder)
                display_random_image(images)
                clear_text()
                text_animation("You find yourself disoriented...")
                if attacking or defending or luring:
                    print(f"{use_item} has no effect against whatever is chasing me.")
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    clear_text()
                    just_attacked = False
                    attacking = False
                    defending = False
                    luring = False
                    if user_col > 0:
                        user_col -= 1
                        user_biome = grid[user_row][user_col]
                        if not examined[user_row][user_col]:
                            folder = "abs"
                            images = load_images_from_folder(folder)
                            display_random_image(images)
                            text_animation("You move westward through the fog.")
                        else:
                            text_animation(f"You move westward and enter a {user_biome}.")
                        actions = actions - 1
                        moves -= 1
                    else:
                        text_animation("An unknown force prevents you from moving further.")
                elif event.key == pygame.K_w:
                    clear_text()
                    just_attacked = False
                    attacking = False
                    defending = False
                    luring = False
                    if user_row > 0:
                        user_row -= 1
                        user_biome = grid[user_row][user_col]
                        if not examined[user_row][user_col]:
                            folder = "abs"
                            images = load_images_from_folder(folder)
                            display_random_image(images)
                            text_animation("You move northward through the fog.")
                        else:
                            text_animation(f"You move northward and enter a {user_biome}.")
                        actions = actions-1
                        moves -= 1
                    else:
                        text_animation("An unknown force prevents you from moving further.")
                elif event.key == pygame.K_s:
                    clear_text()
                    just_attacked = False
                    attacking = False
                    defending = False
                    luring = False
                    if user_row < 5:
                        user_row += 1
                        user_biome = grid[user_row][user_col]
                        if not examined[user_row][user_col]:
                            folder = "abs"
                            images = load_images_from_folder(folder)
                            display_random_image(images)
                            text_animation("You move southward through the fog.")
                        else:
                            text_animation(f"You move southward and enter a {user_biome}.")
                        actions = actions - 1
                        moves -= 1
                    else:
                        text_animation("An unknown force prevents you from moving further.")
                elif event.key == pygame.K_d:
                    clear_text()
                    just_attacked = False
                    attacking = False
                    defending = False
                    luring = False
                    if user_col < 5:
                        user_col += 1
                        user_biome = grid[user_row][user_col]
                        if not examined[user_row][user_col]:
                            folder = "abs"
                            images = load_images_from_folder(folder)
                            display_random_image(images)
                            text_animation("You move eastward through the fog.")
                        else:
                            text_animation(f"You move eastward through the {user_biome}.")
                        actions = actions - 1
                        moves -= 1
                    else:
                        text_animation("An unknown force prevents you from moving further.")
                elif event.key == pygame.K_l:
                    clear_text()
                    if not examined[user_row][user_col]:
                        examined[user_row][user_col] = True
                        letter_to_add = "s"
                        folder = "{}{}".format(str(user_biome), letter_to_add)
                        images = load_images_from_folder(folder)
                        display_random_image(images)
                        pygame.display.flip()
                        if user_biome == "forest":
                            desc = random.choice(forests)
                            text_animation(desc)
                        elif user_biome == "swamp":
                            desc = random.choice(swamps)
                            text_animation(desc)
                        elif user_biome == "meadow":
                            desc = random.choice(meadows)
                            text_animation(desc)
                        elif user_biome == "valley":
                            desc = random.choice(valleys)
                            text_animation(desc)
                        elif user_biome == "lake":
                            desc = random.choice(lakes)
                            text_animation(desc)
                        elif user_biome == "camp":
                            desc = random.choice(camps)
                            text_animation(desc)
                        elif user_biome == "radio tower":
                            desc = random.choice(towers)
                            text_animation(desc)
                        elif user_biome == "crypt":
                            desc = random.choice(crypts)
                            text_animation(desc)
                        elif user_biome == "cave":
                            desc = random.choice(caves)
                            text_animation(desc)
                        elif user_biome == "treehouse":
                            desc = random.choice(treehouses)
                            text_animation(desc)
                        elif user_biome == "garden":
                            desc = random.choice(gardens)
                            text_animation(desc)
                        elif user_biome == "chapel":
                            desc = random.choice(chapels)
                            text_animation(desc)
                        actions = actions - 1
                        moves -= 1
                    else:
                        text_animation(f"You've been to this {user_biome} before... right?")
                elif event.key == pygame.K_x:
                    clear_text()
                    if examined[user_row][user_col]:
                        if not searched[user_row][user_col]:
                            just_attacked = False
                            searched[user_row][user_col] = True
                            if grid[user_row][user_col] in random_points:
                                item = random.choice(random_items)
                                text_animation(f"While searching the {user_biome}, you find a {item}.")
                                inventory.append(item)
                                journal.append(f"I found {item} near the {user_biome}.")
                                random_items.remove(item)
                                icon = pygame.image.load("coin.png")
                                icon = pygame.transform.scale(icon, (50, 50))
                                x = (equipload*55) + 535
                                WINDOW.blit(icon, (x, 447))
                                equipload += 1
                                pygame.display.flip()
                                actions = actions - 1
                                moves -= 1
                            elif grid[user_row][user_col] in biomes:
                                rand = random.random()
                                if rand < chance_of_finding_tool:
                                    item = random.choice(tools)
                                    text_animation(f"While searching the {user_biome}, you find a {item}.")
                                    inventory.append(item)
                                    icon = pygame.image.load("coin.png")
                                    icon = pygame.transform.scale(icon, (50, 50))
                                    x = (equipload*55) + 535
                                    WINDOW.blit(icon, (x, 447))
                                    equipload += 1
                                    pygame.display.flip()
                                    actions = actions - 1
                                    moves -= 1
                                elif rand < chance_of_finding_tool + chance_of_meeting_npc + chance_of_meeting_man:
                                    if old_man == 0:
                                        warning = random.choice(warnings)
                                        ask = random.choice(asks)
                                        lorebit = random.choice(lore)
                                        text_animation(f"Old man")
                                        actions = actions - 1
                                        moves -= 1
                                        old_man += 1
                                        chance_of_meeting_man += 0.15
                                    elif old_man == 1:
                                        warning = random.choice(warnings)
                                        ask = random.choice(asks)
                                        lorebit = random.choice(lore)
                                        text_animation("Old man 2")
                                        actions = actions - 1
                                        moves -= 1
                                        old_man += 1
                                        chance_of_meeting_man += 0.15
                                    elif old_man == 2:
                                        text_animation(f"As you continue to explore the {user_biome}, you once more find the old man's cabin.")
                                        journal.append(f"The monster's lair is in the {monster_lair}.")
                                        actions = actions - 1
                                        moves -= 1
                                        old_man += 1
                                        chance_of_meeting_man += 0.15
                                    else:
                                        text_animation(f"While exploring the {user_biome}, you find an old empty cabin.")
                                        journal.append(f"I am being hunted by {chosen_monster}.")
                                        actions = actions - 1
                                        moves -= 1
                                        old_man += 1
                                elif rand > 0.99:
                                    other_monster = random.choice(list(monsters_lairs.keys()))
                                    other_lair = monsters_lairs[other_monster]
                                    gender = random.choice(genders)
                                    if gender == "He":
                                        gen_disc = "man"
                                        gen_poss = "his"
                                    elif gender == "She":
                                        gen_disc = "woman"
                                        gen_poss = "her"
                                    text_animation(f"You find a {gen_disc} lying in a pool of blood in the {user_biome}, barely clinging on to life.")
                                    text_animation(f"You rush over to help, but the wounds are too severe for you to treat. {gender} looks up at you ")
                                    text_animation(f"and says with {gen_poss} last breath: 'Don't go to the {other_lair}... ")
                                    text_animation(f"There was... it was... {other_monster}...")
                                    text_animation(f"The {gen_disc} goes limp, and {gen_poss} eyes go dark.")
                                    journal.append(f"I found {gen_disc} killed by {other_monster}.")
                                    journal.append(f"{other_monster}'s lair is in the {other_lair}.")
                                    actions = actions - 1
                                    moves -= 1
                                else:
                                    text_animation("You don't find anything interesting here.")
                                    actions = actions - 1
                                    moves -= 1
                        else:
                            text_animation("You have already searched this area.")
                    else:
                        text_animation("You must know where you are before searching the area.")
                    pygame.display.flip()
        pygame.display.flip()

    pygame.quit()
    sys.exit()
        
   



def main():
    game_state = "menu"  # Initial game state is the main menu

    while True:
        if game_state == "menu":
            game_state = main_menu()
        elif game_state == "charname":
            game_state = charname()
        elif game_state == "game":
            game_state = game()

if __name__ == "__main__":
    main()