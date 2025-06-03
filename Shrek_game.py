# Text-Based Adventure Game
# Objective
# Create a text-based adventure game where players navigate through rooms, collect items, solve puzzles, and face challenges. The game will include:

# Room navigation
# Inventory management
# A combat system
# Random events
# A win/lose condition

# Text-Based Adventure Game
# Objective
# Create a text-based adventure game where players navigate through rooms, collect items, solve puzzles, and face challenges. The game will include:

# Room navigation
# Inventory management
# A combat system
# Random events
# A win/lose condition -->

# # Step 2: Define the player's inventory
# # Create an empty list to store items the player collects.

# # Step 3: Define the player's stats
# # Create a dictionary to store the player's health and attack power.

# # Step 4: Define enemies
# # Create a dictionary to represent enemies.
# # Each enemy should have:
# # - Health
# # - Attack power
# # Function 1: Display the player's inventory
# # Write a function to print the player's current inventory.
# # If the inventory is empty, display a message saying so.

# # Function 2: Pick up an item
# # Write a function to add an item to the player's inventory.
# # Print a message confirming the item was picked up.

# # Function 3: Use an item
# # Write a function to remove an item from the inventory and apply its effect.
# # If the item is not in the inventory, display an error message.

# # Function 4: Combat system
# # Write a function to handle combat between the player and an enemy.
# # - Display the enemy's health and attack power.
# # - Allow the player to choose between "attack" or "run".
# # - If the player attacks, reduce the enemy's health by the player's attack power.
# # - If the enemy is still alive, reduce the player's health by the enemy's attack power.
# # - If the player runs, end the combat.
# # - If the player's health reaches 0, display a "Game Over" message.
# # - If the enemy's health reaches 0, display a victory message.

# # Function: Trigger random events
# # Write a function to randomly trigger events during the game.
# # Examples of events:
# # - The player finds a health potion (+20 health).
# # - The player steps on a trap (-15 health).
# # - The player finds a shiny sword (+5 attack).
# # Use the `random` module to select an event at random.
# # Apply the effects of the event to the player's stats.
# # Function: Main game loop
# # Write the main function to run the game.
# # - Start in the "Entrance" room.
# # - Display the current room's description.
# # - Show the player's inventory and stats.
# # - Allow the player to choose an action (e.g., move, pick up item, fight).
# # - Handle the player's input:
# #   - If the player moves, update the current room.
# #   - If the player picks up an item, add it to the inventory.
# #   - If the player fights an enemy, call the combat function.
# #   - If the player triggers a random event, call the random event function.
# #   - If the player types "quit", end the game.
# # - Check for win/lose conditions:
# #   - If the player collects the treasure, display a victory message.
# #   - If the player's health reaches 0, display a "Game Over" message. -->

import random
from random import shuffle

import time

#SETTING UP THE GAME

game_map = {"Forest": {"description": """You stand in the middle of a whimsical forest, where the trees are oddly shaped and whisper secrets when the wind blows.\nStrange mushrooms glow faintly near the roots, and somewhere in the distance, a suspiciously dramatic bird sings like it's auditioning for a musical.\nThe smell of swamp and pine mingle in the air.\nYou swear you saw a talking squirrel disappear behind a tree.""",
                       "actions": {"Inventory": 1, "Pick a glowing mushroom": 2, "Talk to a squirrel": 3, "Explore deeper": 4}},
            "The Dragon's Castle": {"description": "You stand inside a towering, ominous Castle surrounded by boiling lava and perched on a precarious cliff.\nThe crumbling stone walls are scorched with dragon fire, and the drawbridge is the only way in or out.\nThe air smells of sulfur and burnt knights.\nUp the never-ending stairs, Fiona awaits you.",
                                    "actions": {"Inventory": 1, "Grab a torch": 2, "Search for a weapon": 3, "Search for Fiona": 4}},
            "Shrek's Swamp": {"description": """You stand in Shrek’s peaceful swamp, where the air hangs heavy with the scent of damp earth and wild onions.\nThe thick mud squelches underfoot—a familiar, comforting sound in these parts.\nDragonflies dance lazily above the water, and the distant croak of frogs blends with the rustle of wind through gnarled trees.\nSunlight filters softly through the canopy, casting golden ripples across the bog.\nFor Shrek, this isn't just a swamp—it's home, a fortress, and a safe sanctuary all in one.""",
                              "actions": {"Inventory": 1, "Go snail collecting": 2, "Go to the outhouse": 3, "Go and scare some townpeople": 4}},
            "Fairy Tale Market": {"description": """You stand in the muddy heart of Duloc's makeshift market.\nWooden stalls line the area, piled high with sketchy potions, burnt dumplings, and magical trinkets.\nFairy tale creatures are being traded, scammed, and occasionally hexed.\nA suspicious-looking witch watches you from behind a bubbling cauldron, and Donkey is still talking non-stop nearby.""",
                                  "actions": {"Inventory": 1, "Ask the witch for a potion": 2, "Talk to Donkey": 3, "Leave the Market": 4}},
            "Duloc": {"description": """You enter a disgustingly pristine plaza paved in white stone, where identical Tudor-style buildings stretch in unnerving symmetry.\nA cheerful jingle plays on loop from hidden speakers.\nAnimatronic dolls in Duloc costumes dance on a stage, their smiles frozen in uncanny glee.\nA giant billboard reads: 'DULOC: A Perfect Town for Perfect People (No Ogres, Dragons, or Fun Allowed).'""",
                      "actions": {"Inventory": 1, "Read the Duloc rulebook": 2, "Listen to the Chorus of mechanical figures singing ‘Welcome to Duloc’": 3, "Mock the height of Lord Farquaad": 4}}}

player_stats = {"Health": 1000, "Attack Power": 300}

enemies = {"Lord Farquaad": {"Health": 100, "Attack Power": 50},
"Dragon": {"Health": 2000, "Attack Power": 250},
"Merrymen": {"Health": 1200, "Attack Power": 200},
"Townpeople": {"Health": 700, "Attack Power": 100}}

bad_events = [
    {"event": "You tripped over during the run! 😵 You lose 5 HP", "value": 5},
    {"event": "You ran away but they still caught you! 😬 You lose 15 HP", "value": 15},
    {"event": "You didn't notice an obstacle and you ran into it! 🤕 You get a bit dizzy and lose 10 HP", "value": 10}]

#INVENTORY FUNCTION

inventory = []
inventorydict = {}

pos_inv = {"A snail": {"A snail": {"Health": 10, "Attack Power": 0, "Description": "You eat a snail. (HP + 10)"}},
           "A glowing mushroom": {"A glowing mushroom": {"Health": 15, "Attack Power": 0, "Description" : "You eat a glowing mushroom. (HP + 15)"}},
            "A potion": {"A potion": {"Health": 20, "Attack Power": 15, "Description": "You drink the magic potion. (HP + 20, Attack + 15)"}},
           "A Duloc Rulebook": {"A Duloc Rulebook": {"Health": 0, "Attack Power": 10, "Description": "You read the Duloc Rulebook. It's mostly nonsense, but there is a chapter about fighting. (Attack + 10)"}},
           "A burning torch": {"A burning torch": {"Health": 0, "Attack Power": 5, "Description": "You use the torch. It helps you to see a little better. (Attack + 5)"}}}

def add_to_inventory(item):
  inventory.append(item)
  inventorydict.update(pos_inv[item])

def use_item(item):
    print(inventorydict[item]["Description"])
    for stat, value in inventorydict[item].items():
      if stat in player_stats:
        player_stats[stat] += value
    else:
      player_stats[stat] = value
    inventory.remove(item)
    inventorydict.pop(item)

def show_inventory(inventory):
  if not inventory:
    print("Your inventory is empty.")
  else:
    print("What would you like to do?")
    print("1 - Return")
    for num, item in enumerate(inventorydict.keys(), 2):
      print(f"{num} - Use {item}")
    inventory_choice = int(input())
    if inventory_choice != 1:
      item = inventory[inventory_choice - 2]
      use_item(item)

#RANDOM EVENTS

def trigger_random_event():
  events = [
	  {"event": "A group of fairy tale creatures gather around you and sing a cheerful song. It feels oddly uplifting! (+5 health)", "effect": "Health", "value": 5},
	  {"event": "You hear the sound of Puss in Boots’ boots slapping on the ground. He offers you a playful sword fight, but he’s too fast for you. (-5 health from embarrassment)", "effect": "Health", "value": -5},
	  {"event": "A fog rolls in from the swamp. Suddenly, a mysterious figure emerges from the mist... It’s Donkey, telling bad jokes. (-5 health from frustration)", "effect": "Health", "value": -5},
	  {"event": "You spot a group of ogre children playing with mud pies. They challenge you to a mud fight! You dominate them and feel empowered. (+5 attack)", "effect": "Attack Power", "value": 5},
	  {"event": "You overhear a conversation between Puss in Boots and Donkey about becoming a hero. Inspired, you feel your muscles grow. (+10 attack)", "effect": "Attack Power", "value": 10},
    {"event": "You tried to find a weapon nearby, but unfortunately there wasn't a single sharp tool in sight. Suddenly, you tripped over a pile of stones and thought, 'Hmm, I guess stones can be thrown too.' (+20 attack)", "effect": "Attack Power", "value": 20}]

  event = random.choice(events)
  stat = event["effect"]
  value = event["value"]
  player_stats[stat] += value

  if player_stats["Health"] < 0:
    player_stats["Health"] = 0

  print(event["event"])
  print(f"Current Stats ➜ Health: {player_stats['Health']} | Attack Power: {player_stats['Attack Power']}")

#FIGHTING SMALLER ENEMIES

def show_stats():
  return print("🛡️ Your stats are: Health:", player_stats["Health"], "and Attack Power:", player_stats["Attack Power"])


def show_en_stats(enemy):
  return print("🩸 The enemy's stats are: Health:", enemies[enemy]["Health"], "and Attack Power:", enemies[enemy]["Attack Power"])

def show_all_stats(enemy):
  print("=" * 40)
  show_stats()
  show_en_stats(enemy)
  print("=" * 40)
  return


def wrong_input():
  return print("‼️Enter the right word! Hurry up or they'll get you!")



def fight(enemy):
  fighting = True
  print(f"You are about to fight {enemy}!")
  while fighting:
    show_all_stats(enemy)
    fight_choice = input("What do you do?! 🏃 Run or 💥 Attack??? ")
    print()

    if fight_choice == "Run" or fight_choice == "run" or fight_choice == "RUN":
      random_bad_event = random.choice(bad_events)
      print(random_bad_event["event"])
      player_stats["Health"] -= random_bad_event["value"]
      print("Guess you shouldn't have ran away...")
      print()

    elif fight_choice == "Attack" or fight_choice == "attack" or fight_choice == "ATTACK":
    #walka
      print("💥 Time for a fight!")
      print("You swing your mighty fist and attack your enemy!")
      enemies[enemy]["Health"] -= player_stats["Attack Power"]
      show_all_stats(enemy)
      print()

      if enemies[enemy]["Health"] <= 0:
        print("🏆 Well done! You defeated", enemy)
        break

      else:
        while fighting:
          if player_stats["Health"] <= 0:
            print("You have 0 HP! GAME OVER 💀")
            print()
            fighting = False

          elif enemies[enemy]["Health"] <= 0:
            print("🏆 Well done! You defeated", enemy)
            fighting = False

          print("⚠️The enemy fights back! Where to go to avoid him?! ⬅️ Left or ➡️ Right?")
          avoid_choice = input()
          enemy_attack = ["Left", "Right"]
          shuffle(enemy_attack)
          print()

          if avoid_choice == enemy_attack[0] or avoid_choice == enemy_attack[0].capitalize() or avoid_choice == enemy_attack[0].lower():
            print("Oh no! Wrong side! The enemy punches you in the face and you lose", enemies[enemy]["Attack Power"], "HP! 💔")
            player_stats["Health"] -= enemies[enemy]["Attack Power"]
            print()
            if player_stats["Health"] <= 0:
              print("You have 0 HP! GAME OVER 💀")
              print()
              fighting = False
            break

          elif avoid_choice == enemy_attack[1] or avoid_choice == enemy_attack[1].capitalize() or avoid_choice == enemy_attack[1].lower():
            print("Phew.. Good choice! You avoided the attack! ❤️‍🩹")
            print()
            break

          else:
            wrong_input()
            print()
            continue
    else:
      wrong_input()
      print()
      continue

#FIGHTING THE DRAGON
def fight_dragon():
  fight = True
  print("You are about to fight the Dragon!")
  print("Their stats are: Health:", enemies["Dragon"]["Health"], "and Attack Power:", enemies["Dragon"]["Attack Power"])

  while fight:
    show_all_stats("Dragon")
    fight_choice = input("What do you do?! 🏃 Run or 💥 Attack??? ")
    print()

    if player_stats["Health"] <= 0:
          print("You have 0 HP! GAME OVER 💀")
          print()
          fight = False

    elif fight_choice == "Run" or fight_choice == "run" or fight_choice == "RUN":
      print("Don't be a coward and fight for Fiona!!!")
      print()
      continue

    elif fight_choice == "Attack" or fight_choice == "attack" or fight_choice == "ATTACK":
      #walka
      print("💥 Time for a fight!")
      print("You swing your mighty fist and attack the dragon!")
      enemies["Dragon"]["Health"] -= player_stats["Attack Power"]
      show_all_stats("Dragon")
      print()

      if player_stats["Health"] <= 0:
        print("You have 0 HP! GAME OVER 💀")
        print()
        fight = False

      elif enemies["Dragon"]["Health"] <= 0:
        print("🏆 Well done! You defeated the Dragon!")
        print("You have finished the game! GG!")
        fight = False

      else:
        while fight:
          if player_stats["Health"] <= 0:
            print("You have 0 HP! GAME OVER 💀")
            print()
            fight = False

          elif enemies["Dragon"]["Health"] <= 0:
            print("🏆 Well done! You defeated the Dragon!")
            print("You have finished the game! GG!")
            fight = False

          print("⚠️The dragon fights back! Where to go to avoid him?! ⬅️ Left or ➡️ Right?")
          avoid_choice = input()
          enemy_attack = ["Left", "Right"]
          shuffle(enemy_attack)
          print()

          if avoid_choice == enemy_attack[0] or avoid_choice == enemy_attack[0].capitalize() or avoid_choice == enemy_attack[0].lower():
            print("Oh no! Wrong side! The enemy punches you in the face and you lose", enemies["Dragon"]["Attack Power"], "HP! 💔")
            player_stats["Health"] -= enemies["Dragon"]["Attack Power"]
            print()
            if player_stats["Health"] <= 0:
              print("You have 0 HP! GAME OVER 💀")
              print()
              fight = False
            break

          elif avoid_choice == enemy_attack[1] or avoid_choice == enemy_attack[1].capitalize() or avoid_choice == enemy_attack[1].lower():
            print("Phew.. Good choice! You avoided the attack! ❤️‍🩹")
            print()
            break

          else:
            wrong_input()
            print()
            continue
    else:
      wrong_input()
      print()
      continue

#STARTING THE GAME FUNCTION

instructions = ["💚 You start at Shrek's swamp, which is a save zone.", "💚 Your goal is to get to the castle and save Fiona.", "💚 Before making it to the castle, you will have to face several enemies.", "💚 Throughout the game, you will be asked to decide on different things by inputting 1, 2, 3, and 4, for the most part.", "💚 Sometimes, you will be asked to input specific words, especially during the fights, e.g. 'left' or 'attack'. ", "💚 You can also input 'quit', and you will leave the game immediately.", "💚 However, this won't be possible when checking the inventory and during fights.", "💚 So, once you start fighting, you have to finish it one way or another.", "💚 And when you pick up an item, you can use it later to your advantage by entering the inventory again.", "Now you know everything. Good luck!", ".", "."]
swamp_description = ["You stand in Shrek’s peaceful swamp, where the air hangs heavy with the scent of damp earth and wild onions.🧅", "The thick mud squelches underfoot—a familiar, comforting sound in these parts.🦶💦", "Dragonflies dance lazily above the water, and the distant croak of frogs blends with the rustle of wind through gnarled trees.🐸", "Sunlight filters softly through the canopy, casting golden ripples across the bog.☀️✨", "For Shrek, this isn't just a swamp—it's home, a fortress, and a safe sanctuary all in one.🏠", ".", "."]

def start_game():
  print("""Hello! Welcome to the Kingdom of Far Away in Shrek's universe. Before starting, please read the following instructions:""")
  for sentence in instructions:
    time.sleep(2)
    print(sentence)
  for sentence in swamp_description:
    time.sleep(3)
    print(sentence)
  print("Here's what you can do at the Swamp. What do you choose?")
  for action, number in game_map["Shrek's Swamp"]["actions"].items():
    print(f"{action} ➔ {number}")
  handle_room_swamp()

#HANDLING THE ROOM FUNCTION: SWAMP

def handle_room_swamp():
  item = "A snail"
  first_choice = input()
  while first_choice:
    if first_choice.lower() == "quit":
      break
    elif first_choice not in ("1", "2", "3", "4"):
      print("Wrong input, please provide the right number: ")
      first_choice = input()
    elif first_choice == "1":
      show_inventory(inventory)
      print()
      print("What do you want to do next?")
      for action, number in game_map["Shrek's Swamp"]["actions"].items():
        print(f"{action} ➔ {number}")
      first_choice = input()
      print()
    elif first_choice == "2":
      print("You rummage through the muck, looking for sluggish snails perfect for soup, and you actually find one! It's now added to your inventory.🐌")
      add_to_inventory(item)
      print()
      game_map["Shrek's Swamp"]["actions"].pop("Go snail collecting")
      print("What do you want to do next?")
      for action, number in game_map["Shrek's Swamp"]["actions"].items():
        print(f"{action} ➔ {number}")
      first_choice = input()
      print()
    elif first_choice == "3":
      trigger_random_event()
      print()
      game_map["Shrek's Swamp"]["actions"].pop("Go to the outhouse")
      print("What do you want to do next?")
      for action, number in game_map["Shrek's Swamp"]["actions"].items():
        print(f"{action} ➔ {number}")
      first_choice = input()
    elif first_choice == "4":
      handle_room_market()
      break

#HANDLING THE ROOM FUNCTION: MARKET

loading_effect = [".", "."]

market_description = ["You stand in the muddy heart of Duloc's makeshift market.🏚️", "Wooden stalls line the area, piled high with sketchy potions, burnt dumplings, and magical trinkets.🥟", "Fairy tale creatures are being traded, scammed, and occasionally hexed.🧚", "A suspicious-looking witch watches you from behind a bubbling cauldron, and Donkey is still talking non-stop nearby.👀", ".", "."]

def handle_room_market():
  item = "A potion"
  for sentence in loading_effect:
    time.sleep(2)
    print(sentence)
  for sentence in market_description:
    time.sleep(3)
    print(sentence)
  print("Here's what you can do at the Fairy Tale Market. What do you choose?")
  for action, number in game_map["Fairy Tale Market"]["actions"].items():
    print(f"{action} ➔ {number}")
  second_choice = input()
  while second_choice:
    if second_choice.lower() == "quit":
      break
    elif second_choice not in ("1", "2", "3", "4"):
      print("Wrong input, please provide the right number: ")
      second_choice = input()
    elif second_choice == "1":
      show_inventory(inventory)
      print()
      print("What do you want to do next?")
      for action, number in game_map["Fairy Tale Market"]["actions"].items():
        print(f"{action} ➔ {number}")
      second_choice = input()
      print()
    elif second_choice == "2":
      print("The cacklin’, grining witch hands you a bubbling, neon-green potion that smells like swamp gas and bad decisions. It's now added to your inventory. Bottoms up!🧪")
      add_to_inventory(item)
      print()
      game_map["Fairy Tale Market"]["actions"].pop("Ask the witch for a potion")
      print("What do you want to do next?")
      for action, number in game_map["Fairy Tale Market"]["actions"].items():
        print(f"{action} ➔ {number}")
      second_choice = input()
      print()
    elif second_choice == "3":
      trigger_random_event()
      print()
      game_map["Fairy Tale Market"]["actions"].pop("Talk to Donkey")
      print("What do you want to do next?")
      for action, number in game_map["Fairy Tale Market"]["actions"].items():
        print(f"{action} ➔ {number}")
      second_choice = input()
      print()
    elif second_choice == "4":
        fight("Townpeople")
        handle_room_duloc()
        break

#HANDLING THE ROOM FUNCTION: DULOC

duloc_description = ["You enter a disgustingly pristine plaza paved in white stone, where identical Tudor-style buildings stretch in unnerving symmetry.🏰", "A cheerful jingle plays on loop from hidden speakers.🎶", "Animatronic dolls in Duloc costumes dance on a stage, their smiles frozen in uncanny glee.🤖", "A giant billboard reads: 'DULOC: A Perfect Town for Perfect People (No Ogres, Dragons, or Fun Allowed).'🚫", ".", "."]

def handle_room_duloc():
  item = "A Duloc Rulebook"
  for sentence in loading_effect:
    time.sleep(2)
    print(sentence)
  for sentence in duloc_description:
    time.sleep(3)
    print(sentence)
  print("Here's what you can do in Duloc. What do you choose?")
  for action, number in game_map["Duloc"]["actions"].items():
    print(f"{action} ➔ {number}")
  third_choice = input()
  print()
  while third_choice:
    if third_choice.lower() == "quit":
      break
    elif third_choice not in ("1", "2", "3", "4"):
      print("Wrong input, please provide the right number: ")
      third_choice = input()
    elif third_choice == "1":
      show_inventory(inventory)
      print()
      print("What do you want to do next?")
      for action, number in game_map["Duloc"]["actions"].items():
        print(f"{action} ➔ {number}")
      third_choice = input()
      print()
    elif third_choice == "2":
      print("You grab the joyless Duloc Rulebook full of nonsense like ‘No fun allowed’ or ‘Stay in line, peasant!’. It's now added to your inventory.📕")
      add_to_inventory(item)
      print()
      game_map["Duloc"]["actions"].pop("Read the Duloc rulebook")
      print("What do you want to do next?")
      for action, number in game_map["Duloc"]["actions"].items():
        print(f"{action} ➔ {number}")
      third_choice = input()
      print()
    elif third_choice == "3":
      trigger_random_event()
      print()
      game_map["Duloc"]["actions"].pop("Listen to the Chorus of mechanical figures singing ‘Welcome to Duloc’")
      print("What do you want to do next?")
      for action, number in game_map["Duloc"]["actions"].items():
        print(f"{action} ➔ {number}")
      third_choice = input()
      print()
    elif third_choice == "4":
      fight("Lord Farquaad")
      handle_room_forest()
      break

#HANDLING THE ROOM FUNCTION: FOREST

forest_description = ["You stand in the middle of a whimsical forest, where the trees are oddly shaped and whisper secrets when the wind blows.🌳💬", "Strange mushrooms glow faintly near the roots, and somewhere in the distance, a suspiciously dramatic bird sings like it's auditioning for a musical.🎤", "The smell of swamp and pine mingle in the air.🌫️", "You swear you saw a talking squirrel disappear behind a tree.🐿️", ".", "."]

def handle_room_forest():
  item = "A glowing mushroom"
  for sentence in loading_effect:
    time.sleep(2)
    print(sentence)
  for sentence in forest_description:
    time.sleep(3)
    print(sentence)
  print("Here's what you can do in the Forest. What do you choose?")
  for action, number in game_map["Forest"]["actions"].items():
    print(f"{action} ➔ {number}")
  fourth_choice = input()
  print()
  while fourth_choice:
    if fourth_choice.lower() == "quit":
      break
    elif fourth_choice not in ("1", "2", "3", "4"):
      print("Wrong input, please provide the right number: ")
      fourth_choice = input()
    elif fourth_choice == "1":
      show_inventory(inventory)
      print()
      print("What do you want to do next?")
      for action, number in game_map["Forest"]["actions"].items():
        print(f"{action} ➔ {number}")
      fourth_choice = input()
      print()
    elif fourth_choice == "2":
      print("The mushroom comes loose with a wet pop. Its glow intensifies, humming like a trapped fairy. The mushroom is now added to your inventory.🍄")
      add_to_inventory(item)
      print()
      game_map["Forest"]["actions"].pop("Pick a glowing mushroom")
      print("What do you want to do next?")
      for action, number in game_map["Forest"]["actions"].items():
        print(f"{action} ➔ {number}")
      fourth_choice = input()
      print()
    elif fourth_choice == "3":
      trigger_random_event()
      print()
      game_map["Forest"]["actions"].pop("Talk to a squirrel")
      print("What do you want to do next?")
      for action, number in game_map["Forest"]["actions"].items():
        print(f"{action} ➔ {number}")
      fourth_choice = input()
      print()
    elif fourth_choice == "4":
      fight("Merrymen")
      handle_room_castle()
      break

#HANDLING THE ROOM FUNCTION: CASTLE

castle_description = ["You stand inside a towering, ominous Castle surrounded by boiling lava and perched on a precarious cliff.🌋", "The crumbling stone walls are scorched with dragon fire, and the drawbridge is the only way in or out.🔥", "The air smells of sulfur and burnt knights.☠️", "Up the never-ending stairs, Fiona awaits you.👑", ".", "."]

def handle_room_castle():
  item = "A burning torch"
  for sentence in loading_effect:
    time.sleep(2)
    print(sentence)
  for sentence in castle_description:
    time.sleep(3)
    print(sentence)
  print("Here's what you can do in the The Dragon's Castle. What do you choose?")
  for action, number in game_map["The Dragon's Castle"]["actions"].items():
    print(f"{action} ➔ {number}")
  fifth_choice = input()
  print()
  while fifth_choice:
    if fifth_choice.lower() == "quit":
      break
    elif fifth_choice not in ("1", "2", "3", "4"):
      print("Wrong input, please provide the right number: ")
      fifth_choice = input()
    elif fifth_choice == "1":
      show_inventory(inventory)
      print()
      print("What do you want to do next?")
      for action, number in game_map["The Dragon's Castle"]["actions"].items():
        print(f"{action} ➔ {number}")
      fifth_choice = input()
      print()
    elif fifth_choice == "2":
      print("You pick up a torch, which is sputtering omniously and casting shadows that look suspiciously like Lord Farquaad's tiny silhouette. The torch is now added to your inventory.🔥")
      add_to_inventory(item)
      print()
      game_map["The Dragon's Castle"]["actions"].pop("Grab a torch")
      print("What do you want to do next?")
      for action, number in game_map["The Dragon's Castle"]["actions"].items():
        print(f"{action} ➔ {number}")
      fifth_choice = input()
      print()
    elif fifth_choice == "3":
      trigger_random_event()
      print()
      game_map["The Dragon's Castle"]["actions"].pop("Search for a weapon")
      print("What do you want to do next?")
      for action, number in game_map["The Dragon's Castle"]["actions"].items():
        print(f"{action} ➔ {number}")
      fifth_choice = input()
      print()
    elif fifth_choice == "4":
      fight_dragon()
      break

start_game()