import time
import sys

def titleprint(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

def extra(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.03)

valid_options=['1','2','3','4']
yesorno=['yes', 'y', 'no', 'n']

print(f"-"*20)
titleprint("𝕖𝕤𝕔𝕒𝕡𝕖 𝕥𝕙𝕖 𝕛𝕒𝕚𝕝 𝕔𝕖𝕝𝕝\n")
print(f"-"*20)
time.sleep(2)
name=input(f"\nEnter your name.\n☛  ").title()

response=input(f"Hello, {name}... Have you played this before?\n☛  ").lower()

while response==response:
    while response not in yesorno:
        response=input(f"Please enter yes or no.\n☛  ").lower()
    if response=="yes" or response=="y":
        easyhard='hard'
        extra(f"Great! Welcome back! So you know the gist of it. \n")
        time.sleep(3)
        break
    elif response=="no" or response=="n":
        easyhard='easy'
        extra(f"That's fine. Here's the basic idea:")
        time.sleep(1)
        extra(f"\nThroughout this game you will observe your surroundings and make decisions in order to successfully escape and win the game. Making the wrong decision will cause you to lose health. If you run out of health, you lose! (But don't worry, this is a video game, so real-life-you will be fine).\n")
        time.sleep(2)
        break


extra(f"Here are the basic rules for this game:\n")
extra(f"""1. Read the descriptions carefully.
2. Type in one of the options when prompted to (be careful with typos!) It will usually prompt you to enter a number.
3. Think carefully about the decisions you make; doing the wrong thing can make you lose health or even end your adventure!
4. Once your physical health or mental health reach zero, you lose!\n""")
time.sleep(3)
extra(f"Ready? Here we go!\n")

print(f"-"*50)
time.sleep(2)

def dots(string):
  for x in range(3):
    sys.stdout.write(string)
    sys.stdout.flush()
    time.sleep(1)


class mode:
  def __init__(self, hp, mentality):
    self.hp = hp
    self.mental = mentality
  def hurt(self, health, mentality):
    self.hp -= health
    self.mental -= mentality
    print(f"""Your stats:
    - HP: {self.hp}
    - Mentality: {self.mental}\n""")

easy = mode(100, 100)
hard = mode(70, 70)



#statistics= {
#	'hp': 100,
#	'mentality': 100
#}

def die():
    if easyhard=='easy':
        if easy.hp <= 0:
            extra("""You died!
            GAME OVER\n\n""")
            sys.exit()
        elif easy.mental<=0:
            extra("""You have finally reached the point of a mental breakdown. You cannot possibly go on. Your life is over, and you know it. You rot in your cell forever, with only the voices in your head to comfort you.
            GAME OVER\n\n""")
            sys.exit()
    if easyhard=='hard':
        if hard.hp <= 0:
            extra("""You died!
            GAME OVER\n\n""")
            sys.exit()
        elif hard.mental<=0:
            extra("""You have finally reached the point of a mental breakdown. You cannot possibly go on. Your life is over, and you know it. You rot in your cell forever, with only the voices in your head to comfort you.
            GAME OVER\n\n""")
            sys.exit()


def dig():
  extra("\nYou pick up the spoon. You settle in the corner and start digging at the cement.\n")
  dots('.')
  extra("You dig.\n")
  dots('.')
  extra("You keep digging.\n")
  dots('.')
  extra("You realize this is hopeless and start to cry.\n")
  extra("You lost 10 mental health points!\n")
  if easyhard=='hard':
      hard.hurt(0, 10)
      die()
  elif easyhard=='easy':
      easy.hurt(0, 10)
      die()


def soap():
  extra("\nYou pick up the soap. You have the genius plan of lathering yourself in soap to slip through the bars. However all does not go as expected. The soapy mixture gets all over the cement cell floor and you slip and bang your head on the cell bars. You get brain damage and die before the guards can even catch you escaping. What a disappointment you are!\n")
  extra("GAME OVER\n\n")
  sys.exit()


def inmates():
  extra("\nYou ask your next door cell neighbor to help you and instead of being a kind, loyal neighbor they spit all the way from across the room and hit you straight in the eye.\n This made you very sad. You lost 10 mental health points.\n")
  if easyhard=='hard':
      hard.hurt(0, 10)
      die()
  elif easyhard=='easy':
      easy.hurt(0, 10)
      die()


def cane():
  extra("""\nYou take the cane lying against your cell and you use it to knock the coat off of it's hook. As the coat drops you hear keys jingling inside the coat pocket. You decide to use the cane to fish out the keys.

  "Hey!" It's your next door neighbor. "If you get me out of here, we can both escape together. If not, I'll just tell the guards one of their prisoners got out!\n""")

  help=input("\nDo you help the guy?\n☛  ").lower()

  while help not in yesorno:
      help = input("Please enter yes or no.\n☛  ")

  if help == 'yes' or help=='y':
    extra("\nYou unlock your cell and the guy thanks you but promptly runs the other direction. You are filled with happiness as you watch him run off into freedom!\nYou gain 20 mental health points.\n")
    if easyhard=='hard':
      hard.hurt(0, -20)
      die()
    elif easyhard=='easy':
      easy.hurt(0, -20)
      die()

  elif help =='no' or help == 'n':
    extra("\nAs you run past the other guy's cell, the guy begins to scream: 'You are never going to leave now! The moment the guard comes back I am gonna let them know you left!'\nYou become scared of getting caught and lose 20 mental health points.\n")
    if easyhard=='hard':
      hard.hurt(0, 20)
      die()
  elif easyhard=='easy':
      easy.hurt(0, 20)
      die()



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

def donuts():
  extra("\nOn the desk you find a pack of Duck Donuts. The smell is quite strong and you become very hungry. You open the donut box and find there is one half eaten donut. It still looks delicious, though.\n")

  donutdecision = input("\nDo you wish to take a bite into the half-eaten donut?\n☛  ").lower()

  while donutdecision not in yesorno:
      donutdecision = input("Please enter yes or no.\n☛  ").lower()

  if donutdecision == 'yes' or donutdecision =='y':
    extra("\nYou bit into a donut that was infested with bacteria from a sick officer. You now have the flu.\nYour hp points have gone down by 50!\n")
    if easyhard=='hard':
      hard.hurt(50, 0)
      die()
    elif easyhard=='easy':
      easy.hurt(50, 0)
      die()
  if donutdecision == 'no' or donutdecision=='n':
    extra("\nYou close the box with disappointment.\nYour mentality points have decreased by 10! :( \n")
    if easyhard=='hard':
      hard.hurt(0, 10)
      die()
    elif easyhard=='easy':
      easy.hurt(0, 10)
      die()


def photos():
  extra("\nOn the walls you see a wide range of photos all of the same family over and over. There is a wife with two twin girls and a boy. All five of them have huge smiles and appear to be genuinely laughing. Looking at this happy family you find yourself reminiscing to your own family. Because you are upset, you lose 50 mental health points.\n")
  if easyhard=='hard':
      hard.hurt(0, 50)
      die()
  elif easyhard=='easy':
      easy.hurt(0, 50)
      die()


def hallway():
  extra("""\nYou leave the office and realize that you quickly need to make a run for it. You're seconds away from freedom!!! You can choose to go straight(1), left(2) or right(3)...""")
  halldecision = input("\nWhich direction do you want to go?\n☛  ")
  while halldecision not in valid_options:
    halldecision = input("Please type 1, 2, 3, or 4.\n☛  ")
  if halldecision == '3':
    extra("You sprint at top speed to the right. You run and you run until you arrive at another corner. You think you hear something, but you keep running. A guard catches up to you. He grabs you by the arm and throws you back into the jail cell. You failed.")
    extra("GAME OVER\n\n")
    sys.exit()
  elif halldecision == '2':
    extra("You sprint at top speed to the left. You trip and scrape your knee, which is more painful than you'd imagine it to be. It's also a little embarassing.\n")
    extra("You lose 20 hp and 10 mental health points!\n")
    if easyhard=='hard':
      hard.hurt(20, 10)
      die()
    elif easyhard=='easy':
      easy.hurt(20, 10)
      die()
    extra("You come to a corner and you do not hear anyone behind you so you take a moment to breathe.")
    halldecision2 = input("You think you hear something on your left but you aren't sure. Maybe it's from your right side? Where do you go? Left(1)? Or right(2)?\n☛  ")
    while halldecision2 not in valid_options:
        halldecision2 = input("Please type 1 or 2. \n☛  ")
    if halldecision2 == '1':
      extra("Unfortunately your hearing is horrible and you run straight into the guard. He grabs you by the arm and throws you back into the jail cell. You failed.")
      extra("GAME OVER\n\n")
      sys.exit()
    elif halldecision2 == '2':
      extra("You run and the noise you heard before is becoming more faint as you keep running down the hall. You see the exit but there's a lock that requires a four number code.\n")
      code_attempt = input("Think back to all the clues you looked at in previous rooms. What do you think is the code?\n☛  ")
      if code_attempt == '2020':
        extra("The light on the lock turns green and you hear a click as the door unlocks. CONGRATS! You run outside, finally making your escape.")
        extra("""THE END ✩""")
        sys.exit()
      else:
        extra("Boo hoo! Judging by the loud buzzing noise, looks like you were wrong! The guards caught up to you and threw you back in the jail cell.")
        extra("GAME OVER\n\n")
        sys.exit()
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
      code_attempt = input("Think back to all the clues you looked at in previous rooms. What do you think is the code?\n☛  ")
      if code_attempt == '2020':
        extra("The light on the lock turns green and you hear a click as the door unlocks. CONGRATS! You run outside, finally making your escape.")
        extra("""THE END ✩""")
        sys.exit()
      else:
        extra("Boo hoo! Judging by the loud buzzing noise, looks like you were wrong! The guards caught up to you and threw you back in the jail cell.")
        extra("GAME OVER\n\n")
        sys.exit()

def office():
  extra("""\nYou make a run for the office door at the end of the hallway. You don't hear anyone so you unlock the door and enter, closing it behind you again.

  You look around the room and you see an old rotary phone in the corner right above a desk. There are photos on the wall and a box of donuts on the desk on top of some papers.\n""")

  observation = input("\nWhat do you want to check out? The papers (1), the donuts (2), or the photos (3)? Or do you want to leave?(4)\n☛  ")

  while observation not in valid_options:
    observation=int(input("Please type 1, 2, 3, or 4.\n☛  "))
  while observation!='4':
    if observation=='1':
      papers()
    elif observation=='2':
      donuts()
    elif observation=='3':
      photos()
    observation = input("\nWhat do you want to check out? The papers (1), the donuts (2), or the photos (3)? Or do you want to leave?(4)\n☛  ")


  extra("""\nAs you begin to leave, the phone from the corner of the room starts to ring loudly.\n""")
  phone_ring = input("Do you wish to answer the phone call? ☎ \n☛  ").lower()

  while phone_ring not in yesorno:
      phone_ring = input("Please enter yes or no.\n☛  ").lower()

  if phone_ring =='no' or phone_ring=='n':
    extra("\nUnfortunately since you did not answer the phone, Officer Richard II suspected suspicious activity since Officer Tears always picks up his phone.\n")
    extra("GAME OVER\n\n")
    sys.exit()

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
    question_1input = input("""\n'What is my name? You should know this since we are best buds!'
    You try to think of any names you might have seen...
     With which name do you wish to respond with?
      A) Officer Wilson
      B) Officer Richard II
      C) Officer Santos
      D) Officer Zajac\n☛  """).upper()

  if question_1input == 'B' or question_1input == 'B)':
    extra("""\n"Hm, alright Officer Tears. I have another question..."\n""")
    question_2input = input("""
    'How many kids do you have?'
    A) two kids
    B) one kid
    C) five kids
    D) three kids\n☛  """).upper()

    if question_2input == 'D' or question_2input == 'D)':
      extra("\n'Okay, sorry about that Officer, I just thought you were the person trying to escape. I will talk to you later, bye!'\n")
      hallway()
    else:
      extra("""Suddenly, the person hangs up. Within a few seconds, Officer Richard II comes into the office and catches you, shaking his head.
      'It's like you didn't even try...'\n""")
      extra("GAME OVER\n\n")
      sys.exit()

  else:
    extra("""Suddenly, the person hangs up. Within a few seconds, Officer Richard II comes into the office and catches you, shaking his head.
    "It's like you didn't even try..."\n""")
    extra("GAME OVER\n\n")
    sys.exit()



def night():
  extra("""\nIt is now dark outside. ☾
  The guards at the end of each hallway have left their assigned location to switch shifts with the next officers. The officer that just left appears to have left behind a coat on a hook and a cane resting against your bars.\n""")
  extra("\nYou look around. You find a spoon under your bed and a bar of soap on the sink. To the left and right of your cell are other inmates that you think may be able to help in your escape.\n""")
  choice1=input("\nDo you want to dig your way out?(1) Do you want to use the soap to slide through the bars?(2) Or do you want to recruit the other prisoners in your escape?(3) Do you want to use the cane?(4)\n☛  ")
  while choice1 not in valid_options:
    choice1=int(input("Please type 1, 2, 3, or 4.\n☛  "))
  while choice1!='4':
    if choice1=='1':
      dig()
    elif choice1=='2':
      soap()
      die()
    elif choice1=='3':
      inmates()
    choice1=input("\nDo you want to dig your way out?(1) Do you want to use the soap to slide through the bars?(2) Or do you want to recruit the other prisoners in your escape?(3) Do you want to use the cane?(4)\n☛  ")
  if choice1=='4':
    cane()
    office()

extra("You find yourself in a dark cold jail cell after being wrongly accused of murder. In your cell you find a bed with a pillow and sheets, a sink, and a broken down toilet. Surrounding your cell there are other mean looking inmates. You walk forward toward the bars and look into the hallway. There is a guard on each side of the hallway, blocking your only way of escape.\n")

daynight = input("\nWill you start your escape now or wait until night time?\n☛  ").lower()

while daynight != 'now' and daynight!= 'wait':
    daynight=input("Please type in 'now' or 'wait'.\n☛  ").lower()

if daynight == "now":
  extra("\nYou look around. You find a spoon under your bed and a bar of soap on the sink. To the left and right of your cell are other inmates that you think may be able to help in your escape.\n")
  choice1=input("\nDo you want to dig your way out?(1) Do you want to use the soap to slide through the bars?(2) Or do you want to recruit the other prisoners in your escape?(3)\n☛  ")
  while choice1 not in valid_options:
    choice1=int(input("Please type 1, 2, or 3.\n☛  "))
  if choice1=='1':
    dig()
  elif choice1=='2':
    soap()
  elif choice1=='3':
     inmates()
  extra("""
    One of the guards noticed you were trying to escape and caught you!

    GAME OVER

    """)
  sys.exit()
if daynight == "wait":
  night()