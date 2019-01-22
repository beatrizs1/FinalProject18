#importing the time and system modules
import time
import sys

#creating a function that prints out a string one character at a time with 0.1 seconds between each character. to be used for printing the title and the end messages
def titleprint(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

#creating a function that prints out a string one character at a time with 0.03 seconds between each character. to be used throughout the game
def extra(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.03)

#creating a list of valid options so that invalid inputs can be detected
valid_options=['1','2','3','4']
yesorno=['yes', 'y', 'no', 'n']

#printing the title of the game
print(f"-"*20)
titleprint("𝕖𝕤𝕔𝕒𝕡𝕖 𝕥𝕙𝕖 𝕛𝕒𝕚𝕝 𝕔𝕖𝕝𝕝\n")
print(f"-"*20)
time.sleep(2)

#user enters their name
name=input(f"\nEnter your name.\n☛  ").title()

response=input(f"Hello, {name}... Have you played this before?\n☛  ").lower()

while response==response:
    #if user does not enter yes or no, they are prompted to do so in order to continue
    while response not in yesorno:
        response=input(f"Please enter yes or no.\n☛  ").lower()

    #if user has played before, they are assigned "hard mode"
    if response=="yes" or response=="y":
        easyhard='hard'
        extra(f"Great! Welcome back! So you know the gist of it. \n")
        time.sleep(3)
        break

    #if user has not played before, the game is described to them and they are assigned "easy mode"
    elif response=="no" or response=="n":
        easyhard='easy'
        extra(f"That's fine. Here's the basic idea:")
        time.sleep(1)
        extra(f"\nThroughout this game you will observe your surroundings and make decisions in order to successfully escape and win the game. Making the wrong decision will cause you to lose health. If you run out of health, you lose! (But don't worry, this is a video game, so real-life-you will be fine).\n")
        time.sleep(2)
        break

#printing the rules of the game
extra(f"Here are the basic rules for this game:\n")
extra(f"""1. Read the descriptions carefully.
2. Type in one of the options when prompted to (be careful with typos!) It will usually prompt you to enter a number.
3. Think carefully about the decisions you make; doing the wrong thing can make you lose health or even end your adventure!
4. Once your physical health or mental health reach zero, you lose!\n""")
time.sleep(2)

extra(f"Ready? Here we go!\n")

print(f"-"*50)
time.sleep(2)

#this function prints the same character three times on the same line, with a second of delay between prints. to be used for "...", hence the name "dots"
def dots(string):
  for x in range(3):
    sys.stdout.write(string)
    sys.stdout.flush()
    time.sleep(1)

#creating a class of two modes with unique hp and mentality points
class mode:
  def __init__(self, hp, mentality):
    self.hp = hp
    self.mental = mentality

  #this function within the class will subtract any amount of points from either category and then print the player's statistics
  def hurt(self, health, mentality):
    self.hp -= health
    self.mental -= mentality
    print(f"""\nYour stats:
    - HP: {self.hp}
    - Mentality: {self.mental}\n""")

#assigning the starting hp and mentality points for easy and hard mode, respectively
easy = mode(100, 100)
hard = mode(70, 70)

#the die function checks if either the hp or mentality of the player is less than or equal to zero. if so, it will end the game.
def die():
    if easyhard=='easy':
        if easy.hp <= 0:
            extra("You died!\n")
            time.sleep(1)
            titleprint("GAME OVER\n\n")
            time.sleep(2)
            sys.exit()
        elif easy.mental<=0:
            extra("You have finally reached the point of a mental breakdown. You cannot possibly go on. Your life is over, and you know it. You rot in your cell forever, with only the voices in your head to comfort you.\n")
            time.sleep(1)
            titleprint("GAME OVER\n\n")
            time.sleep(2)
            sys.exit()
    if easyhard=='hard':
        if hard.hp <= 0:
            extra("You died!\n")
            time.sleep(1)
            titleprint("GAME OVER\n\n")
            time.sleep(2)
            sys.exit()
        elif hard.mental<=0:
            extra("You have finally reached the point of a mental breakdown. You cannot possibly go on. Your life is over, and you know it. You rot in your cell forever, with only the voices in your head to comfort you.\n")
            time.sleep(1)
            titleprint("GAME OVER\n\n")
            time.sleep(2)
            sys.exit()

#the dig function displays the optional scenario of the player digging with the spoon
def dig():
  extra("\nYou pick up the spoon. You settle in the corner and start digging at the cement.\n")
  dots('.')
  extra("You dig.\n")
  dots('.')
  extra("You keep digging.\n")
  dots('.')
  extra("You realize this is hopeless and start to cry.\n")
  extra("You lost 10 mental health points!\n")

  #this setup is used whenever points are subtracted/added. it checks which mode is used and subtracts using the hurt function within the class. the die function at the end checks if the player has died after that subtraction.
  if easyhard=='hard':
      hard.hurt(0, 10)
      die()
  elif easyhard=='easy':
      easy.hurt(0, 10)
      die()

#the soap function displays the optional scenario of the player using soap to escape and failing, thus ending the game
def soap():
  extra("\nYou pick up the soap. You have the genius plan of lathering yourself in soap to slip through the bars. However all does not go as expected. The soapy mixture gets all over the cement cell floor and you slip and bang your head on the cell bars. You get brain damage and die before the guards can even catch you escaping. What a disappointment you are!\n")
  time.sleep(1)
  titleprint("GAME OVER\n\n")
  time.sleep(2)
  sys.exit()

#the inmates fucntion displays the optional scenario with the other prisoner and subtracts 10 mentality points
def inmates():
  extra("\nYou ask your next door cell neighbor to help you and instead of being a kind, loyal neighbor they spit all the way from across the room and hit you straight in the eye.\n This made you very sad. You lost 10 mental health points.\n")
  if easyhard=='hard':
      hard.hurt(0, 10)
      die()
  elif easyhard=='easy':
      easy.hurt(0, 10)
      die()

#the cane function displays the scenario of using the cane to escape
def cane():
  extra("""\nYou take the cane lying against your cell and you use it to knock the coat off of its hook. As the coat drops you hear keys jingling inside the coat pocket. You decide to use the cane to fish out the keys.

  "Hey!" It's your next door neighbor. "If you get me out of here, we can both escape together. If not, I'll just tell the guards one of their prisoners got out!\n""")

  #asking the player if they would like to help
  help=input("\nDo you help the guy?\n☛  ").lower()

  #if they player does not enter yes or no, they are prompted to do so
  while help not in yesorno:
      help = input("Please enter yes or no.\n☛  ")

  #if the player enters yes, they gain 20 mentality points
  if help == 'yes' or help=='y':
    extra("\nYou unlock your cell and the guy thanks you but promptly runs the other direction. You are filled with happiness as you watch him run off into freedom!\nYou gain 20 mental health points.\n")
    if easyhard=='hard':
      hard.hurt(0, -20)
      die()
    elif easyhard=='easy':
      easy.hurt(0, -20)
      die()

  #if the player enters no, they lose 20 mentality points
  elif help =='no' or help == 'n':
    extra("\nAs you run past the other guy's cell, the guy begins to scream: 'You are never going to leave now! The moment the guard comes back I am gonna let them know you left!'\nYou become scared of getting caught and lose 20 mental health points.\n")
    if easyhard=='hard':
      hard.hurt(0, 20)
      die()
  elif easyhard=='easy':
      easy.hurt(0, 20)
      die()

#the papers function displays a piece of paper graphic
def papers():
  extra("\nYou pick up a piece of paper.\n")
  print("""
   ____________________________________
  | Sheriffs at Magnet Jail           |
  |   Officer Richard - ext.333       |
  |   Officer Wilson - ext.343        |
  | ♥ Officer Richard II - ext. 660 ♥ |
  |   Officer Santos - ext. 314       |
  |   Officer Zajac - ext. 702        |
  |   Officer Tears - ext. 123        |
  |                                   |
  |   code: 2020                      |
  |___________________________________|

  """)

#the donuts function displays the scenario of encountering a pack of donuts in the office
def donuts():
  extra("\nOn the desk you find a pack of Duck Donuts. The smell is quite strong and you become very hungry. You open the donut box and find there is one half eaten donut. It still looks delicious, though.\n")

  #asking the player if they wish to eat the donut
  donutdecision = input("\nDo you wish to take a bite into the half-eaten donut?\n☛  ").lower()

  #if they do not enter yes or no, they are prompted to do so
  while donutdecision not in yesorno:
      donutdecision = input("Please enter yes or no.\n☛  ").lower()

  #if they enter yes, they lose 50 hp from getting sick
  if donutdecision == 'yes' or donutdecision =='y':
    extra("\nYou bit into a donut that was infested with bacteria from a sick officer. You now have the flu.\nYour hp points have gone down by 50!\n")
    if easyhard=='hard':
      hard.hurt(50, 0)
      die()
    elif easyhard=='easy':
      easy.hurt(50, 0)
      die()

  #if they say no, they lose 10 mentality points from disappointment
  if donutdecision == 'no' or donutdecision=='n':
    extra("\nYou close the box with disappointment.\nYour mentality points have decreased by 10! :( \n")
    if easyhard=='hard':
      hard.hurt(0, 10)
      die()
    elif easyhard=='easy':
      easy.hurt(0, 10)
      die()

#the photos function displays a description of the photos on the office wall and subtracts 50 mentality points from sadness
def photos():
  extra("\nOn the walls you see a wide range of photos all of the same family over and over. There is a wife with two twin girls and a boy. All five of them have huge smiles and appear to be genuinely laughing. Looking at this happy family you find yourself reminiscing to your own family. Because you are upset, you lose 50 mental health points.\n")
  if easyhard=='hard':
      hard.hurt(0, 50)
      die()
  elif easyhard=='easy':
      easy.hurt(0, 50)
      die()

#the hallway function that occurs if the player successfully leaves the office
def hallway():
  extra("""\nYou leave the office and realize that you quickly need to make a run for it. You're seconds away from freedom!!! You can choose to go straight(1), left(2) or right(3)...""")

  #asking the player which direction they want to go
  halldecision = input("\nWhich direction do you want to go?\n☛  ")

  #if they do not choose 1, 2, or 3, they are prompted to do so
  while halldecision not in valid_options:
    halldecision = input("Please type 1, 2, or 3.\n☛  ")

  #if they choose to go right, they get caught and the game ends
  if halldecision == '3':
    extra("You sprint at top speed to the right. You run and you run until you arrive at another corner. You think you hear something, but you keep running. A guard catches up to you. He grabs you by the arm and throws you back into the jail cell. You failed.\n")
    time.sleep(1)
    titleprint("GAME OVER\n\n")
    time.sleep(2)
    sys.exit()

  #if they choose to go left
  elif halldecision == '2':

    #they trip and lose 20 hp and 10 mentality points
    extra("You sprint at top speed to the left. You trip and scrape your knee, which is more painful than you'd imagine it to be. It's also a little embarassing.\n")
    extra("You lose 20 hp and 10 mental health points!\n")
    if easyhard=='hard':
      hard.hurt(20, 10)
      die()
    elif easyhard=='easy':
      easy.hurt(20, 10)
      die()
    extra("You come to a corner and you do not hear anyone behind you so you take a moment to breathe.")

    #they are asked to choose another direction to go
    halldecision2 = input("You think you hear something on your left but you aren't sure. Maybe it's from your right side? Where do you go? Left(1)? Or right(2)?\n☛  ")

    #if they do not type in 1 or 2, they are prompted to do so
    while halldecision2 not in valid_options:
        halldecision2 = input("Please type 1 or 2. \n☛  ")

    #if they choose to go left, they get caught and the game ends
    if halldecision2 == '1':
      extra("Unfortunately your hearing is horrible and you run straight into the guard. He grabs you by the arm and throws you back into the jail cell. You failed.\n")
      time.sleep(1)
      titleprint("GAME OVER\n\n")
      time.sleep(2)
      sys.exit()

    #if they choose to go right...
    elif halldecision2 == '2':
      extra("You run and the noise you heard before is becoming more faint as you keep running down the hall. You see the exit but there's a lock that requires a four number code.\n")

      #they can guess the code
      code_attempt = input("\nThink back to all the clues you looked at in previous rooms. What do you think is the code?\n☛  ")

      #if the code is correct, they win! game ends
      if code_attempt == '2020':
        extra("\nThe light on the lock turns green and you hear a click as the door unlocks. CONGRATS! You run outside, finally making your escape.\n")
        time.sleep(2)
        titleprint("""THE END ✩\n\n""")
        time.sleep(3)
        sys.exit()

      #if the code is incorrect, they lose and the game ends
      else:
        extra("\nBoo hoo! Judging by the loud buzzing noise, looks like you were wrong! The guards caught up to you and threw you back in the jail cell.\n")
        time.sleep(1)
        titleprint("GAME OVER\n\n")
        time.sleep(2)
        sys.exit()

  #if they chose to go straight, they trip and lose 20 hp and 10 mentality points but encounter a lock
  elif halldecision == '1':
      extra("You decide to continue straight and start sprinting. You trip and scrape your knee, which is more painful than you'd imagine it to be. It's also a little embarassing.\n")
      extra("You lose 20 hp and 10 mental health points!\n")
      if easyhard=='hard':
        hard.hurt(20, 10)
        die()
      elif easyhard=='easy':
        easy.hurt(20, 10)
        die()
      extra("\nYou continue on and see the exit! But there's a lock that requires a four number code.\n")

      #they are asked to enter the code
      code_attempt = input("\nThink back to all the clues you looked at in previous rooms. What do you think is the code?\n☛  ")

      #if the code is correct, they win! game ends
      if code_attempt == '2020':
        extra("\nThe light on the lock turns green and you hear a click as the door unlocks. CONGRATS! You run outside, finally making your escape.\n")
        time.sleep(1)
        titleprint("THE END ✩\n\n")
        time.sleep(3)
        sys.exit()

      #if code is incorrect, they lose and game ends
      else:
        extra("\nBoo hoo! Judging by the loud buzzing noise, looks like you were wrong! The guards caught up to you and threw you back in the jail cell.\n")
        time.sleep(1)
        titleprint("GAME OVER\n\n")
        time.sleep(2)
        sys.exit()

#the office function that occurs after the player used the cane to escape
def office():
  extra("""\nYou make a run for the office door at the end of the hallway. You don't hear anyone so you unlock the door and enter, closing it behind you again.

 You look around the room and you see an old rotary phone in the corner right above a desk. There are photos on the wall and a box of donuts on the desk on top of some papers.\n""")

  #player is asked to choose what to do
  observation = input("\nWhat do you want to check out? The papers (1), the donuts (2), or the photos (3)? Or do you want to leave?(4)\n☛  ")

  #if player does not enter 1, 2, 3, or 4 then they are prompted to do so
  while observation not in valid_options:
    observation=int(input("Please type 1, 2, 3, or 4.\n☛  "))

  #this loop makes it so that the player can keep choosing until they choose to leave
  while observation!='4':
    if observation=='1':
      papers()
    elif observation=='2':
      donuts()
    elif observation=='3':
      photos()
    observation = input("\nWhat do you want to check out? The papers (1), the donuts (2), or the photos (3)? Or do you want to leave?(4)\n☛  ")

  #when they finally choose to leave, the phone rings
  extra("""\nAs you begin to leave, the phone from the corner of the room starts to ring loudly.\n""")

  #player is asked if they want to answer the phone
  phone_ring = input("\nDo you wish to answer the phone call? ☎ \n☛  ").lower()

  #if they do not enter yes or no, they are prompted to do so
  while phone_ring not in yesorno:
      phone_ring = input("Please enter yes or no.\n☛  ").lower()

  #if they do not answer, then they lose the game and game ends
  if phone_ring =='no' or phone_ring=='n':
    extra("\nUnfortunately since you did not answer the phone, Officer Richard II suspected suspicious activity since Officer Tears always picks up his phone.\n")
    time.sleep(1)
    titleprint("GAME OVER\n\n")
    time.sleep(2)
    sys.exit()

  #if they choose to answer, a conversation is displayed
  elif phone_ring == 'yes' or phone_ring == 'y':
    extra("""\nYou answer the phone and the voice on the other end of the line speaks:

        "Officer Tears, Officer Tears! I think a prisoner has escaped his cell!"

        Panicking, you respond:
        "Oh, that's unfortunate... Well...What do we do now?"

        The other officer seems to suspect something.
        "Do you not remember protocol?"

        You reply:
        "Uh, of course. I guess I'm just a little tired."

        He then questions:
        "Say, Officer Tears, can you answer a question for me?"

        You hesitantly respond:
        "Uh, sure Officer."\n""")

    #they are asked a question over the phone
    question_1input = input("""\n'What is my name? You should know this since we are best buds!'
    You try to think of any names you might have seen...
    With which name do you wish to respond with?
      A) Officer Wilson
      B) Officer Richard II
      C) Officer Santos
      D) Officer Zajac\n☛  """).upper()

    #if they answer correctly, a second question is asked
    if question_1input == 'B' or question_1input == 'B)':
      extra("""\n"Hm, alright Officer Tears. I have another question..."\n""")
      question_2input = input("""
    'How many kids do you have?'
    A) two kids
    B) one kid
    C) five kids
    D) three kids\n☛  """).upper()

      #if they answer the second question correctly, they may move on to the hallway scene
      if question_2input == 'D' or question_2input == 'D)':
        extra("\n'Okay, sorry about that Officer, I just thought you were the person trying to escape. I will talk to you later, bye!'\n")
        hallway()

      #if they answer incorrectly, the game ends
      else:
        extra("""Suddenly, the person hangs up. Within a few seconds, Officer Richard II comes into the office and catches you, shaking his head.
      'It's like you didn't even try...'\n""")
        time.sleep(1)
        titleprint("GAME OVER\n\n")
        time.sleep(2)
        sys.exit()

    #if they answer incorrectly, the game ends
    else:
      extra("""Suddenly, the person hangs up. Within a few seconds, Officer Richard II comes into the office and catches you, shaking his head.
    "It's like you didn't even try..."\n""")
      time.sleep(1)
      titleprint("GAME OVER\n\n")
      time.sleep(2)
      sys.exit()

#the scene that plays if the player chooses to wait
def night():
  extra("""\nIt is now dark outside. ☾
 The guards at the end of each hallway have left their assigned location to switch shifts with the next officers. The officer that just left appears to have left behind a coat on a hook and a cane resting against your bars.\n""")
  extra("\nYou look around. You find a spoon under your bed and a bar of soap on the sink. To the left and right of your cell are other inmates that you think may be able to help in your escape.\n""")

  #they are asked what they want to do
  choice1=input("\nDo you want to dig your way out?(1) Do you want to use the soap to slide through the bars?(2) Or do you want to recruit the other prisoners in your escape?(3) Do you want to use the cane?(4)\n☛  ")

  #if they do not enter 1, 2, 3, or 4, they are prompted to do so
  while choice1 not in valid_options:
    choice1=int(input("Please type 1, 2, 3, or 4.\n☛  "))

  #this loop makes it so that the player may keep choosing what to do until they choose the cane
  while choice1!='4':
    if choice1=='1':
      dig()
    elif choice1=='2':
      soap()
      die()
    elif choice1=='3':
      inmates()
    choice1=input("\nDo you want to dig your way out?(1) Do you want to use the soap to slide through the bars?(2) Or do you want to recruit the other prisoners in your escape?(3) Do you want to use the cane?(4)\n☛  ")

  #if they choose the cane, that scene occurs and then they move on to the office scene
  if choice1=='4':
    cane()
    office()


#THIS IS WHERE THE STORYLINE BEGINS AFTER THE INTRO, NO MORE DEFINITIONS!

#setting the scene
extra("\nYou find yourself in a dark cold jail cell after being wrongly accused of murder. In your cell you find a bed with a pillow and sheets, a sink, and a broken down toilet. Surrounding your cell there are other mean looking inmates. You walk forward toward the bars and look into the hallway. There is a guard on each side of the hallway, blocking your only way of escape.\n")

#player is asked if they want to start now or wait
daynight = input("\nWill you start your escape now or wait until night time?\n☛  ").lower()

#if they do not enter now or wait, they are promopted to do so
while daynight != 'now' and daynight!= 'wait':
    daynight=input("Please type in 'now' or 'wait'.\n☛  ").lower()

#if they choose now...
if daynight == "now":
  extra("\nYou look around. You find a spoon under your bed and a bar of soap on the sink. To the left and right of your cell are other inmates that you think may be able to help in your escape.\n")

  #player is asked what they would like to do
  choice1=input("\nDo you want to dig your way out?(1) Do you want to use the soap to slide through the bars?(2) Or do you want to recruit the other prisoners in your escape?(3)\n☛  ")

  #if they do not enter 1, 2, or 3, they are prompted to do so
  while choice1 not in valid_options:
    choice1=int(input("Please type 1, 2, or 3.\n☛  "))

  #if they choose 1, they get the digging scene
  if choice1=='1':
    dig()
  #if they choose 2, they get the soap scene
  elif choice1=='2':
    soap()
  #if they choose 3, they get the inmate scene
  elif choice1=='3':
     inmates()

  #since the player did not choose to wait, the guards catch them and the game ends
  extra("\nOne of the guards noticed you were trying to escape and caught you!\n")
  time.sleep(1)
  titleprint("GAME OVER\n\n")
  time.sleep(2)
  sys.exit()

#if the player chooses to wait, the night function is used
elif daynight == "wait":
  night()