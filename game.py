import time
import sys

def extra(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

print(f"-"*20)
extra("𝕖𝕤𝕔𝕒𝕡𝕖 𝕥𝕙𝕖 𝕛𝕒𝕚𝕝 𝕔𝕖𝕝𝕝\n")
print(f"-"*20)
time.sleep(2)
name=input(f"\nEnter your name.\n☛  ").title()

response=input(f"Hello, {name}... Have you played this before?\n").lower()

while response==response:
    if response != "yes" and response!="y" and response!="no" and response!="n":
        response=input(f"Please enter yes or no.\n").lower()
    elif response=="yes" or response=="y":
        print(f"Great! So you know the gist of it. \n")
        time.sleep(3)
        break
    elif response=="no" or response=="n":
      print(f"That's fine. Here's the basic idea:")
      time.sleep(1)
      print(f"Throughout this game you will observe your surroundings and make decisions in order to successfully escape and win the game. Making the wrong decision will cause you to lose health. If you run out of health, you lose! (But don't worry, this is a video game, so real-life-you will be fine).\n")
      time.sleep(6)
      break


print(f"Here are the basic rules for this game:")
print(f"""1. Read the descriptions carefully.
2. Type in one of the options when prompted to (be careful with typos!) It will usually prompt you to enter a number.
4. Think carefully about the decisions you make; doing the wrong thing can make you lose health or even end your adventure!
5. Once your physical health or mental health reach zero, you lose!""")
time.sleep(5)
print(f"Ready? Here we go!")

print(f"-"*50)
time.sleep(2)

def dots(string):
  for x in range(3):
    sys.stdout.write(string)
    sys.stdout.flush()
    time.sleep(1)


statistics= {
	'hp': 100,
	'mentality': 100
}

def die():
  if statistics['hp']==0:
    print("""You died!
    GAME OVER""")
  elif statistics['mentality']==0:
    print("""You have finally reached the point of a mental breakdown. You cannot possibly go on. Your life is over, and you know it. You rot in your cell forever, with only the voices in your head to comfort you.
    GAME OVER""")
    sys.exit()

valid_options=['1','2','3','4']

def dig():
  print("\nYou pick up the spoon. You settle in the corner and start digging at the cement.\n")
  dots('.')
  print("You dig.\n")
  dots('.')
  print("You keep digging.\n")
  dots('.')
  print("You realize this is hopeless and start to cry.")
  print("You lost 10 mental health points!")
  statistics['mentality']-=10
  print(statistics)
  die()


def soap():
  print("\nYou pick up the soap. You have the genius plan of lathering yourself in soap to slip through the bars. However all does not go as expected. The soapy mixture gets all over the cement cell floor and you slip and bang your head on the cell bars. You get brain damage and die before the guards can even catch you escaping. What a disappointment you are!")
  statistics['hp'] -=100
  print(statistics)
  die()


def inmates():
  print("\nYou ask your next door cell neighbor to help you and instead of being a kind, loyal neighbor they spit all the way from across the room and hit you straight in the eye.\n This made you very sad. You lost 10 mental health points.")
  statistics['mentality']-=10
  print(statistics)
  die()


def cane():
  help=input("""\nYou take the cane lying against your cell and you use it to knock the coat off of it's hook. As the coat drops you hear keys jingling inside the coat pocket. You decide to use the cane to fish out the keys.

  "Hey!" It's your next door neighbor. "If you get me out of here, we can both escape together. If not, I'll just tell the guards one of their prisoners got out!"

  Do you help the guy?
  ☛  """)
  if help == 'yes' or help=='y':
    print("\nYou unlock your cell and the guy thanks you but promptly runs the other direction. You are filled with happiness as you watch him run off into freedom!\nYou gain 20 mental health points.")
    statistics['mentality']+=20
    print(statistics)
  elif help =='no' or help == 'n':
    print("\nAs you run past the other guy's cell, the guy begins to scream: 'You are never going to leave now! The moment the guard comes back I am gonna let them know you left!'\nYou become scared of getting caught and lose 20 mental health points.")
    statistics['mentality']-=20
    print(statistics)
    die()


def cell():
  print("You look around. You find a spoon under your bed and a bar of soap on the sink. To the left and right of your cell are other inmates that you think may be able to help in your escape.")
  choice1=input("\nDo you want to dig your way out?(1) Do you want to use the soap to slide through the bars?(2) Or do you want to recruit the other prisoners in your escape?(3)\n")
  while choice1 not in valid_options:
    choice1=int(input("Please type 1, 2, or 3."))
  if choice1=='1':
    dig()
  elif choice1=='2':
    soap()
  elif choice1=='3':
    inmates()

def papers():
  print("""\nYou pick up a piece of paper.
   ____________________________________
  | Sheriffs at Magnet Jail           |
  |   Officer Richard - ext.333       |
  |   Officer Wilson - ext.343        |
  | ♥ Officer Richard II - ext. 660 ♥ |
  |   Officer Santos - ext. 314       |
  |   Officer Zajac - ext. 702        |
  |   Officer Tears - ext. 123        |
  |___________________________________|

  """)

def donuts():
  print("\nOn the desk you find a pack of duck donuts. The smell is so strong and you become very hungry. You open the donut box and find there is one half eaten donut. It still looks delicious though.")

  donutdecision = input("\nDo you wish to take a bite into the half-eaten donut? Yes or no?\n☛  ")

  if donutdecision == 'yes' or donutdecision =='y':
    print("\nYou bit into a donut that was infested with bacteria from a sick officer. You now have the flu.\nYour hp points have gone down by half!")
    statistics['hp'] = statistics['hp']/2
    print(statistics)
    die()
  if donutdecision == 'no' or donutdecision=='n':
    print("\nYou close the box with disappointment.\nYour mentality points have decreased by 10! :( ")
    statistics['mentality'] -= 10
    print(statistics)
    die()


def photos():
  print("\nOn the walls you see a wide range of photos all of the same family over and over. There is a wife with two girls and a boy. The girls appear to be twins and the boy seems to look younger than the twins. You glance over to one specific photo of the whole family. All five of them have huge smiles and appear to be genuinely laughing. Looking at this happy family you find yourself reminiscing to your own family. Because you are upset, you lose 50 mental health points.")
  statistics['mentality']-=50
  print(statistics)
  die()


def office():
  print(""""\nYou make a run for the office door at the end of the hallway. You don't hear anyone so you unlock the door and enter, closing it behind you again.

  You look around the room and you see an old rotary phone in the corner right above a desk. There are photos on the wall and a box of donuts on the desk on top of some papers.
  """)

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


  print("""\nAs you begin to leave, the phone from the corner of the room starts to ring loudly.
  """)
  phone_ring = input("Do you wish to answer the phone call? ☎ Hmmm... it seems rather important.\n☛  ")

  if phone_ring =='no' or phone_ring=='n':
    print("\nUnfortunately since you did not answer the phone, Officer Richard II suspected suspicious activity since Officer Tears always picks up his phone.")
    print("GAME OVER")
    sys.exit()

  elif phone_ring == 'yes' or phone_ring == 'y':
    print("""\nYou answer the phone and the voice on the other end of the line speaks:

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
        "Uh, sure Officer." """)
    question_1input = input("""\n'What is my name? You should know this since we are best buds!'
    You try to think of any names you might have seen...
     With which name do you wish to respond with?
      A) Officer Wilson
      B) Officer Richard II
      C) Officer Santos
      D) Officer Zajac\n☛  """).upper()

  if question_1input == 'B' or question_1input == 'B)':
    print("""\n"Hm, alright Officer Tears. I have another question..." """)
    question_2input = input("""
    'How many kids do you have?'
    A) two kids
    B) one kid
    C) five kids
    D) three kids\n☛  """).upper()

    if question_2input == 'D' or question_1input == 'D)':
      print("\nOkay, sorry about that Officer, I just thought you were the person trying to escape. I will talk to you later, bye!")
    else:
      print("""Suddenly, the person hangs up. Within a few seconds, Officer Richard II comes into the office and catches you, shaking his head.
      'It's like you didn't even try...' """)
      print("GAME OVER")
      sys.exit()

  else:
    print("""Suddenly, the person hangs up. Within a few seconds, Officer Richard II comes into the office and catches you, shaking his head.
    "It's like you didn't even try..." """)
    print("GAME OVER")
    sys.exit()


def night():
  print("""\nIt is now dark outside. ☾
  The guards at the end of each hallway have left their assigned location to switch shifts with the next officers. The officer that just left appears to have left behind a coat on a hook and a cane resting against your bars.\n""")
  print("You look around. You find a spoon under your bed and a bar of soap on the sink. To the left and right of your cell are other inmates that you think may be able to help in your escape.""")
  choice1=input("\nDo you want to dig your way out?(1) Do you want to use the soap to slide through the bars?(2) Or do you want to recruit the other prisoners in your escape?(3) Do you want to use the cane?(4)\n☛  ")
  while choice1 not in valid_options:
    choice1=int(input("Please type 1, 2, 3, or 4."))
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

print("You find yourself in a dark cold jail cell after being wrongly accused of murder. In your cell you find a bed with a pillow and sheets, a sink, and a broken down toilet. Surrounding your cell there are other mean looking inmates. You walk forward toward the bars and look into the hallway. There is a guard on each side of the hallway, blocking your only way of escape.")

daynight = input("\nWill you start your escape now or wait until night time?\n☛  ").lower()

if daynight == "now":
  print("\nYou look around. You find a spoon under your bed and a bar of soap on the sink. To the left and right of your cell are other inmates that you think may be able to help in your escape.")
  choice1=input("\nDo you want to dig your way out?(1) Do you want to use the soap to slide through the bars?(2) Or do you want to recruit the other prisoners in your escape?(3)\n☛  ")
  while choice1 not in valid_options:
    choice1=int(input("Please type 1, 2, or 3.\n☛  "))
  if choice1=='1':
    dig()
  elif choice1=='2':
    soap()
  elif choice1=='3':
     inmates()
  else:
    print("""
    One of the guards noticed you were trying to escape and caught you!

    GAME OVER""")
    sys.exit()
if daynight == "wait":
  night()