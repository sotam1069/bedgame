def Project2():
  #Pedro Matos 802213189
  #Ivanier Bellido 802214690
  
  cmd_bed = 'b'
  cmd_close = 'c'
  cmd_east = 'e'
  cmd_feed = 'f'
  cmd_get = 'g'
  cmd_lock = 'l'
  cmd_north = 'n'
  cmd_open = 'o'
  cmd_put = 'p'
  cmd_quit = 'q'
  cmd_south = 's'
  cmd_tv = 't'
  cmd_unlock = 'u'
  cmd_west = 'w'

  room_front = 0
  room_living = 1
  room_kitchen = 2
  room_office = 3
  room_bed = 4

  room_names = ("front door", "living room", "kitchen", "office", "bedroom")

  me_awake = True
  tv_on = False
  dog_fed = False
  pantry_unlocked = False
  pantry_open = False
  key = False
  safe_open = False
  treat = False

  room = 0
  turn = 0
  
  #Welcome Message
  print("Welcome to CIIC 3015 Project 2. Your goal is to climb in bed and go to sleep after a long day, but first you must complete a few tasks... Good Luck!\n")
  print("Objectives: Feed your dog Stella and go to sleep.\n")
  
  #Main Loop
  while me_awake:
    print("\nLocation: ", room_names[room])
    cmd = input("\n> ")
    turn += 1

    #Quit Game
    if cmd == cmd_quit:
      print("Thanks for playing, better luck next time!")
      print("\u0332".join("STATISTICS"))
      print("Turns played: ", turn)
      print("Ps. The fastest score is 24 turns ;)")

      return False

    #Enter House
    if room == room_front:
      if cmd == cmd_east:
        print("\nYou have entered your house.")
        room = room_living
      else:
        print("Invalid command, input 'e' to enter the house.")
      continue

    #Living Room
    if room == room_living:

      #TV
      if cmd == cmd_tv:
        if tv_on:
          print("\nYou turn off the tv.")
        else:
          print("\nYou turn on the tv.")
        tv_on = not tv_on
        continue
    
      #Trying to leave the house
      if cmd == cmd_west:
        print("\nYou are way too tired to face the world again just now. Best to remain indoors.")
        continue

      #ToBedroom
      if cmd == cmd_north:
        if not dog_fed:
          print("\nStella is blocking your entrance, she must be fed.")
          print("\nHint: There is a tasty treat in the pantry of the kitchen.")
          continue
        else:
          room = room_bed
          print("\nYou have entered your bedroom.")
          continue
        
      #ToKitchen
      if cmd == cmd_south:
        print("\nYou have entered the Kitchen.")
        room = room_kitchen 
        continue
              
      #ToOffice
      if cmd == cmd_east:
        print("\nYou have entered the office.")
        room = room_office
        continue

      #Feeding Stella
      if cmd == cmd_feed:
        if dog_fed:
          print("\nStella already ate.")
        else:
          if not treat:
            print("\nYou must have the treats to feed Stella.")
          elif tv_on:
            dog_fed = True
            print("\nStella is enjoying her treat.")
          else:
            print("\nPlease turn on the tv for stella to begin eating.")
        continue

    #KitchenRoom
    if room == room_kitchen:

      #To Living Room
      if cmd == cmd_north:
        print("\nYou have gone back to the living room.")
        room = room_living
        continue

      #Unlocking the Pantry
      if cmd == cmd_unlock:
        if pantry_unlocked:
          print("\nPantry is already unlocked.")
        elif key:
          pantry_unlocked = True
          print("\nYou have unlocked the pantry door.")
        else:
          print("\nYou must look for the key that is inside the office vault.")
        continue

      #Opening the pantry
      if cmd == cmd_open:
        if pantry_open:
          print("\nPantry is already opened.")
        elif pantry_unlocked:
          pantry_open = True
          print("\nPantry door is now opened.")
        else:
          print("\nPantry door must be unlocked first.")
        continue

      #Getting the treat
      if cmd == cmd_get:
        if treat:
          print("\nYou already have the treat.")
        elif pantry_open:
          treat = True
          print("\nYou have grabbed the treat.")
        else:
          print("\nPantry must be opened before grabbing the treat.")
        continue

      #Closing the Pantry
      if cmd == cmd_close:
        if not pantry_open:
          print("\nPantry is already closed.")
        else:
          pantry_open = False
          print("\nPantry is closed.")
        continue

      #Putting away the treats
      if cmd == cmd_put:
        if pantry_open and pantry_unlocked and treat:
          treat = False
          print("\nYou have stored the treats.")
        elif not treat:
          print("\nYou must have the treat first before storing it.")
        elif not pantry_open:
          print("\nPantry must be opened to store the treat.")
        elif not pantry_unlocked:
          print("\nPantry must be unlocked before storing treats.")
        continue

      #Locking the Pantry
      if cmd == cmd_lock:
        if not key:
          print("\nYou need the key to lock the pantry.")
        elif not pantry_unlocked:
          print("\nPantry already locked.")
        elif pantry_open:
          print("\nPantry must be closed.")
        else:
          pantry_unlocked = False
          print("\nPantry was locked.")
        continue
           
    #OfficeRoom
    if room == room_office:

      #ToLivingRoom
      if cmd == cmd_west:
        print("\nYou have gone back to the living room.")
        room = room_living
        continue

      #Unlocking the safe
      if (cmd == cmd_open or cmd == cmd_unlock):
        if not safe_open:
          print("Please enter the safe's combination to unlock it, one number at a time.\n")
          comb1 = input("First combination > ")
          comb2 = input("Second combination > ")
          comb3 = input("Third combination > ")
          if comb1 == "21" and comb2 == "64" and comb3 == "32":
            safe_open = True
            print("\nSafe is now opened.")
          else:
            print("\nInvalid combination. Please try again.")
          continue
        else:
          print("\nSafe is already opened.")
          continue

      #Closing the safe
      if cmd == cmd_close or cmd == cmd_lock:
        if safe_open:
          safe_open = False
          print("\nSafe has been closed.")
        else:
          print("\nSafe is already closed.")
        continue
      
      #Putting Away The Key
      if cmd == cmd_put:
        if not key:
          print("\nYou need the key before storing the key.")
        elif not safe_open:
          print("\nYou need to open the safe before storing it.")
        else:
          key = False
          print("\nYou have stored the key.")
        continue

      #Getting the Key
      if cmd == cmd_get:
        if key:
          print("\nYou already have the key.")
        elif safe_open:
          key = True
          print("\nYou have grabbed the key.")
        else:
          print("\nYou must first open the safe.")
        continue

       

    #BedRoom  
    if room == room_bed:

      #To Living Room
      if cmd == cmd_south:
        print("\nYou have gone back to the living room.")
        room = room_living
        continue

      #Requirements to sleep  
      if cmd == cmd_bed:
        if not dog_fed:
          print("\nStella must be fed before sleeping.")
        elif tv_on:
          print("\nTV must be turned off before sleeping.")
        elif treat:
          print("\nTreats must be returned to the pantry.")
        elif key:
          print("\nKey must be returned to the safe.")
        elif safe_open:
          print("\nSafe must be closed.")
        elif pantry_open:
          print("\nPantry must be closed and locked.")
        elif pantry_unlocked:
          print("\nPantry must be locked.")
        else:
          break
        continue
  print("---------------------------------------------------------")
  print("You have succesfully gone to sleep. \nCongratulations on finishing Project 2 of the CIIC 3015 course made by Ivanier and Pedro :)")
  print("--------------------------------------------------------") 
  print("\u0332".join("STATISTICS"))
  print("Turns played:", turn)
  print("Ps. The fastest score is 24 turns ;)")
  return True





print(Project2())

