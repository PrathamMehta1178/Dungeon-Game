import random as r
# statistics
Inventory = []
Coins = 0
Skip = 0
Magnet = 0
Teleport = 0
Sword = 0
zhealth = 25
round = 0
gapples = 0 
health = 100
iront = 0
diamondt = 0
quartzt = 0
rocks = 0
gold = 0
diamond = 0
iron = 0
rod = 0
bait = 0 
waterBreath = 0
hhead = 150
hwings = 100
hbody = 300 
hlegs = 75
def start():


    print('You wake up in the bedroom of a house what do you do?\n 1. Check surrondings\n2. Go back to sleep')
    startDecision = input('> ').casefold()

    if startDecision[0] == 'c':
        print(''' Looking around in the bedroom, you see the door is boarded up.
        Next to you is a lamp, and is the corner of the room you see a trapdoor that presumably goes down.
        What do you do?
        1. Head towards trapdoor
        2. Go back to sleep
        ''')
        choice = input('> ').lower()

        
        if choice[0] == 'h':
            print('You pop the trapdoor open and see a hole going down.\n Do you go in?\n1. Yes\n2. No\n3. YES')
            choice = input('> ').lower()

            if choice[0] == 'n':
                print('As you go to shut the trapdoor, you unfortunately trip and fall directly into the hole, falling tens of feet under ground.')
                Dungeon.dungeonStart()
            elif choice[0] == 'y': 
                print('You hop straight into this mysterious hole, ready to start your adventure.')
                Dungeon.dungeonStart()
        else:
            start()
    
    
    
    else:
        start()

class Dungeon(object):
    global Skip, Coins, Magnet, Sword, Teleport, Inventory

    def dungeonStart():
        print('''
        Somehow after falling from all those feet in the air, you manage to survive.
        You see that you are in a stone corridor that leads to a big oak door.
        You decide to go through it.''')
        Dungeon.starterRoom()
    
    def death():
        global Coins
        print('YOU DIED\n Unfortunately you lost half your Coins :(')
        Coins = Coins // 2

    def starterRoom():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory
        print('''You find yourself in a room full of various crops.
        The three sides of the room all have doors that seem to lead to more places.
        But, you decide to stay in this room for now and explore it.
        Where do you go?
        1. Crop fields
        2. Barnhouse
        3. Exit''')

        choice = input('> ').lower()
        if choice[0] == 'c':
            print(49*'=-=')
            print('''
            You run up to the fields and look at the crops. 
            You decide to pocket some carrots for later
            + 5 carrots''')
            print(49*'=-=')

            Inventory.append('Carrot Bundle')
            Dungeon.starterRoom()

        elif choice[0] == 'b':
            global Coins
            print(49*'=-=')
            print('You walk into the barn and find some livestock.\nYou see some Coins in a corner and decide to grab them and head out.\n + 5 Coins')
            print(49*'=-=')

            Coins += 5
            Dungeon.starterRoom()

        else:
            Dungeon.exitRoom()
    
    def exitRoom():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory
        exitMsg = r.randint(1,3)

        if exitMsg == 1:
            print('You decide to leave this room and explore a new one.')
        if exitMsg == 2:
            print('You decide to move on from this room and explore others')
        if exitMsg == 3:
            print('You leave the room searching for new ones')

        print('What direction do you decide to go in?\nex: left, forward, right')
        direction = input('> ').capitalize()
        print('You decide to go '+direction+'.')
        Dungeon.generateRooms()

    def generateRooms():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory
        room = r.randint(1,10)

        if room == 1:
            Dungeon.trap_room_one()
        elif room == 2:
            Dungeon.trap_room_two()
        elif room == 3:
            Dungeon.trap_room_three()
        elif room == 4:
            Dungeon.shop()
        elif room == 5:
            Dungeon.zombieQuest()
        elif room == 6:
            Dungeon.casinoRoom()
        elif room == 7:
            Dungeon.swampRoom()
        elif room == 8:
            Dungeon.fishRoom()
        elif room == 9:
            Dungeon.themines()
        elif room == 10:
            Dungeon.battleRoom()


       
    
    def trap_room_one():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory
        Dungeon.ShopTeleport()
        Dungeon.health()
        Dungeon.skip()
        print("You enter a room that doesn\'t seem safe.\nIn front of you lies a golden chest. However, it is surrounded by skulls and skeletons.\nDo you open the chest?\n1. Yes\n2. No")
        choice = input('> ').lower()
        
        ifTrap = r.randint(1,2)
        
        if choice[0] == 'y':
            if ifTrap == 1 and choice[0] == 'y':
                print('You try to open the chest, but it doesn\'t budge.\nYou try to take your hands off the chest, but they stick to the chest.\nYour body begins to shrivel and burn up to a skeleton.\nYou have failed the trap room.')
                Dungeon.death()
                Dungeon.generateRooms()
            elif ifTrap == 2 and choice[0] == 'y':
                print('You somehow open the chest and recieve a total of 30 Coins. Nice!')
                Coins += 30
                Dungeon.exitRoom()
        if choice[0] == 'n':
            print('You decide not to take the risk and move on to the next room')
            Dungeon.exitRoom()


    def trap_room_two():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory
        Dungeon.ShopTeleport()
        Dungeon.health()
        Dungeon.skip()
        print('Before you stands a wizard.\n"Guess the number I am thinking of and I let you pass," he says.\n"A number between 1-20 it is."')
        answer = r.randint(1,20)
        guessAmt = 0
        while True:

            print('Take a guess')
            guess = int(input('> '))
            if guess > answer:
                print('too high')
                guessAmt += 1
            if guess < answer:
                print('too low')
                guessAmt += 1
    
            if guess == answer:
                print("You got it!")
                print('The wizard spares you and lets you pass.\nHe tosses you a couple of Coins as you exit\n + 20 Coins')
                Coins += 20
                Dungeon.exitRoom()
    
            if guess != answer and guessAmt == 5:
                print(f'You failed. The correct answer was {answer}')
                print('You fail the challenge, and the wizard using his magical properties turns you into a parrot.')
                Dungeon.death()
                Dungeon.exitRoom()
                break
    def trap_room_three():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory
        Dungeon.ShopTeleport()
        Dungeon.health()
        Dungeon.skip()
        print("""
        In the room ahead of you lies an obstacle course. 
        There is a pit full of spikes and pieces of wood are on top of the spikes. 
        You will need to jump from plank to plank to escape this room. 
        However, the some of the planks seem fragile. You will need to make the correct choice. 
        What plank do you jump to? ex. left, right""")

        choice = input('> ').lower()

        if choice[0] == 'l':
            print('You jump to the plank of wood to your left.\nAt first it stays stable, but the collapses with you being impaled to death.\n You have failed the trap room.')
            Dungeon.death()
            Dungeon.generateRooms()
        else:
            print('The plank you jump on shakes a little at first, but remains stable.\nWhich plank do you jump to next?')
            choice = input('> ').lower()
            if choice[0] == 'l':
                print('You decide to jump to the left-ward plank.\nHowever, as you land on it, it breaks apart sending you to your untimely demise.')
                Dungeon.death()
                Dungeon.generateRooms()
            else:
                print('Deciding to stay on the right lane, you jump to the next plank.\nYou land perfectly on the wooden board.')
                print('Standing between you and the exit is one last choice, which direction do you take? Left or Right?')
                choice = input('> ').lower()
                if choice[0] == 'l':
                    print('Thinking the right lane 3 times in a row surely won\'t be be the answer, you jump left.\nAt first the board remains stable. Suddenly, it shreds in front of your eyes as you tumble to your death.')
                    Dungeon.death()
                    Dungeon.generateRooms()
                else:
                    print('Trusting the right plank, you lunge at it, and make it.\nAnother jump later you finish the trap room.\n + 20 Coins')
                    Coins += 20
                    Dungeon.exitRoom()
    
    def shop():
        global Skip, Coins, Magnet, Sword, Teleport
        
        print('You are in the dungeon shop. \nThere are plants and greenery everywhere, and in the middle is the actaul shop.\n You walk up to it and can see what the shop has to offer.')
        print('\n\n[SKIP-KEY]: 15 Coins\n[COIN-MAGNET-V3]: 30 Coins\n[TELEPORTER-TO-SHOP]: 10 Coins\n[IRON-SWORD]: 20 Coins\n\nType the item\'s name in order to buy it.\nType \'Balance\' to check your coin balance.\nType \'Exit\' to leave the room.')            
        choice = input('> ').lower()
        if choice[0] == 's' and Coins > 15:
            print('Buying Skip-Key\nThis allows you to skip a room.')            
            Skip += 1
            Coins -= 15
            Dungeon.shop()
        
        if choice[0] == 'c' and Coins >= 30:
            print('Buying Coin Magnet V3\nThis brings the total amount of coins in a room to your Coin Balance')
            Magnet += 1
            Coins -= 30
            Dungeon.shop()

        
        if choice[0] == 't' and Coins >= 10:
            print('Buying Teleporter to Shop\nBrings you to the shop. Can be used at the start of a room.')
            Teleport += 1
            Coins -=10
            Dungeon.shop()
        
        if choice[0] == 'i' and Coins >=20:
            print('Buying Iron Sword.\nCan be used on hostile things.')
            Sword += 1
            Coins -= 20
            Dungeon.shop()
        if choice[0] == 'b':
            print(Coins)
            Dungeon.shop()
        
        if choice[0] == 'e':
            Dungeon.exitRoom()

        else:
            print('You cannot afford this item.')

                    
    
    
    def ShopTeleport():
        global Teleport
        if Teleport > 0:
            print('Would you like to teleport to the shop?\n1. Yes\n2. No')
            choice = input('> ').lower()
            if choice[0] == 'y':
                Teleport -= 1
                print('[TELEPORTER:]Taking you to the shop.')
                print(f'Amount of Teleporters in your Inventory: {Teleport}')
                Dungeon.shop()

            else:
                print('[GAME:] Contine your adventure.')

        else:
            pass
    def skip():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory
        if Skip > 0:
            print('Would you like to skip this room?\n1. Yes\n2. No')
            choice = input('> ').lower()
            if choice[0] == 'y':
                Skip -= 1
                print(f'You have used your skip key.\nYou now have {Skip} key(s)')
                Dungeon.exitRoom()
            else:
                print('[GAME:] Continue your adventure')
        else:
            pass

    def MagnetItem():
            global Skip, Coins, Magnet, Sword, Teleport, Inventory
            if Magnet >= 1:
                print('Would you like to use the Magnet?\n1. Yes\n2. No')
                choice = input('> ').lower()
                if choice[0] == 'y':
                    print('Using Magnet...')
                    Magnet -= 1
                    coinsFound = r.randint(20,55)
                    print(f'You found {coinsFound} coins!')
                    Coins += coinsFound
                else:
                    print('[GAME:] Continue your adventure.')
    def casinoRoom():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory
        Dungeon.ShopTeleport()
        Dungeon.skip()
        Dungeon.health()
        
        print('You are enter a room that appears to be a casino. The walls are themed with red and black.\nAt the center is the main attraction where you can bet your coins.\nWhat do you do?')
        print('1. Go to Center\n2. Explore More\n Leave the room')
        choice = input('> ').lower()

        if choice[0] == 'g':
            Dungeon.gambleTable()

        if choice[0] == 'e':
            print('Seeing more of the room, you see some slot machines. You head towards them.')
            Dungeon.slots
    
        else:
            Dungeon.exitRoom()
    
    
    def gambleTable():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory
        print('You are at the gambling table.\nYou can bet an amount of coins on a coinflip.\nIf it lands, you get double your bet, if it doesn\'t you lose all.')
        print('How many coins do you bet? ex 10, 20, 30')
        coinbet = input('> ')

        if int(coinbet) > Coins: # check if player is abusing
            print('You cannot bet more than your balance.')
    
        else:
            print('What number? 1 or 2?')
            bet = input('> ')
            win = r.randint(1,2) # making the odds 
            winnings = int(coinbet) * 2

            if int(bet) == win:
    
                print(f'YOU WON! {winnings} coins have been added to your balance.')
                Coins = winnings + Coins
                Dungeon.casinoRoom()
            elif int(bet) != win:
                print(f'YOU LOST! {bet} coins have been subtracted from your balance.')
                Coins = Coins - int(coinbet)
                print(Coins)
                Dungeon.casinoRoom()

    def slots():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory

        print('You arrive at the slot machine.\nIn order to win here, you need to get 3 symbols in a row.\nDo you play? [5 coins to play]')
        choice = input('> ').lower()

        if choice[0] == 'y' and Coins > 0:
            Coins -= 5
    
            slots = ['$','$','$','#','#','#','!','!','!']

            x = r.randint(0,8)
            y = r.randint(0,8)
            z = r.randint(0,8)

            firstNum = slots[x]
            secondNum = slots[y]
            thirdNum = slots[z]
            print('Balance: '+Coins)

            print(f"[SLOT-MACHINE:] {slots[x]} {slots[y]} {slots[z]}")

            if firstNum == thirdNum and thirdNum == secondNum:
                print('YOU WON! 50 Coins added to balance.')
                Coins += 50
                Dungeon.slots()
            
            else:
                print('You...LOST')
                Dungeon.slots()
        
        elif choice[0] == 'y' and Coins < 0:
            print('INSUFFICENT FUNDS')
            Dungeon.casinoRoom()        
        else:
            Dungeon.casinoRoom()
    
    def zombieQuest():
        global Skip, Coins, Magnet, Sword, Teleport, Inventory, gapples
        Dungeon.ShopTeleport()
        Dungeon.skip()
        Dungeon.health()
        print('You have entered a quest room.\nYou will need to complete a task in order to leave.\n[QUEST:] Kill all zombies in the room. ')
        if Sword >= 1:
            print('You start to attack the zombies with your sword.')

        else:
            print('You start to fight the zombies with your bare-fists.')

        if Sword >= 1:
            Dungeon.swordpvp()
        else:
            Dungeon.handpvp()

        print('After clearing all the zombies out, you see the exit of the room.\nAs you get closer to the exit, you a treasure chest.\nYou decide to open it.')
        Dungeon.chest()
        Dungeon.exitRoom()

    def zombiepvp():
        global health
        
        chance = r.randint(1,3)
        if chance == 3:
            zdmg = r.randint(5,10)
            print(f'A zombie attacked you for {zdmg} damage!')
            health -= zdmg
    
    def swordpvp():
        global zhealth, round, Coins
        
        for i in range(3):
            dmg = r.randint(7,15)
            print(f'You did {dmg} damage.')
            Dungeon.zombiepvp()
            zhealth -= dmg

            if zhealth > 0:
                Dungeon.swordpvp()

            elif zhealth < 0:
                print('Zombie slain!')
                zhealth = 25
                round += 1
                Dungeon.coinPvp()
                print('')
            
            elif zhealth == 0:
                zhealth = 25
                print('Zombie slain!')
                Dungeon.coinPvp()
                print('')
                round += 1
            
            if round == 6:
                break
            
    def coinPvp():
        global Coins
        reward = r.randint(5,15)
        print(f'+ {reward} coins!')
        Coins += reward

    def handpvp():
        global zhealth, round, Coins
        
        for i in range(1):
            dmg = r.randint(5,10)
            print(f'You did {dmg} damage.')
            zhealth -= dmg
            Dungeon.zombiepvp()
            if zhealth > 0:
                Dungeon.handpvp()

            elif zhealth < 0:
                print('Zombie slain!')
                zhealth = 25
                round += 1
                Dungeon.coinPvp()
                print('')
            
            elif zhealth == 0:
                zhealth = 25
                print('Zombie slain!')
                Dungeon.coinPvp()
                print('')
                round += 1
            
            if round == 6:
                break
    def chest():
        global Coins, gapples, Skip, Magnet, Teleport, Sword, Inventory
        print('[GAME:] You found a treasure chest!')
        reward = r.randint(20,35)
        print(f'You got + {reward} coins!')
        Coins += reward
        
        reward = r.randint(1,3)
        print(f'You got {reward} golden apples!')
        gapples += reward
        
        reward = r.randint(1,3)

        if reward == 1:
            print('You got a skip key!')
            Skip += 1
        if reward == 2:
            print('You got a Coin Magnet!')
            Magnet += 1

        else:
            print('You got a Shop Teleporter!')
            Teleport += 1
    
    def health():
        global health, Inventory
        if health != 100 and Inventory:
            print('Would you like to eat something to revive your health?\n1. Yes\n2. No')
            choice = input('> ').lower()

            if choice[0] == 'y':
                print('Taking some food out of your bag, you slowly revive your health back to 100.')
                Inventory.pop()
                health = 100

            else:
                print('[GAME:] Continue your adventure.')

    def fish():
        global Coins
        treasure = r.randint(1,3)
        if treasure == 3:
            camt = r.randint(5,15)
            print(f'You cast the rod and find {camt} coins.')
            print('Fish Again?\n1. Yes\n2. No')
            Coins += camt
            choice = input('> ').lower()
            if choice[0] == 'y':
                Dungeon.fish()
            else:
                Dungeon.swampRoom()
        else:
            print('You feel the bobber hook on, but you fish up nothing.')
            print('Fish Again?\n1. Yes\n2. No')
            choice = input('> ').lower()
            if choice[0] == 'y':
                Dungeon.fish()
            else:
                Dungeon.swampRoom()
    def roomfish():
        global Coins
        treasure = r.randint(1,3)
        if treasure == 3:
            camt = r.randint(5,15)
            print(f'You cast the rod and find {camt} coins.')
            print('Fish Again?\n1. Yes\n2. No')
            Coins += camt
            choice = input('> ').lower()
            if choice[0] == 'y':
                Dungeon.fish()
            else:
                Dungeon.fishRoom()
        else:
            print('You feel the bobber hook on, but you fish up nothing.')
            print('Fish Again?\n1. Yes\n2. No')
            choice = input('> ').lower()
            if choice[0] == 'y':
                Dungeon.fish()
            else:
                Dungeon.fishRoom()
    def swampRoom():
        global Coins, gapples, Skip, Magnet, Teleport, Sword, Inventory
        Dungeon.ShopTeleport()
        Dungeon.skip()
        Dungeon.health()
        Dungeon.MagnetItem()

        print('A musty smell is in the air. You see that you are in the swamp room\nLooking around you see a pond surronded by mushrooms.\nYou also see a hut in the corner.\n Where do you go?') 
        print('1. Pond\n2. Hut\n3. Exit')

        choice = input('> ').lower()

        if choice[0] == 'p':
            print('You walk over to the pond.\nAs you walk past the mushrooms, you take some for later.\nAt the pond you see a fishing rod.\n Do you go fishing?')
            choice = input('> ').lower()
            if choice[0] == 'y':
                Dungeon.fish()
            else:
                Dungeon.swampRoom()

        if choice[0] == 'h':
            print('You go to the hut. Inside, there are pots.\nYou break them, finding 20 coins in total.\n + 20 Coins')
            Coins += 20
            print('You leave the hut after taking the coins.')
            Dungeon.swampRoom()
            Dungeon.swampRoom()
        if choice[0] == 'e':
            Dungeon.exitRoom()
        else: # if user inputs none of above
            Dungeon.exitRoom()

    def quartzMines():
        global rocks, gold, Coins, diamond, iron
        mineRes  = r.randint(1,5)
        
        if mineRes == 1:
            print('You dig up some rock.\nWorth 1 coins per')
            rocks += 3 
            Dungeon.qkeepDrill()

        if mineRes == 2:
            print('You drilled some iron!\nWorth 4 coins per')
            iron += 6
            Dungeon.qkeepDrill()
        if mineRes == 3:
            print('You found some gold!\nWorth 8 coins per')
            gold += 9
            Dungeon.qkeepDrill()

        if mineRes == 4:
            print('You found some diamonds!\n Worth 12 coins per')
            diamond += 16   
            Dungeon.qkeepDrill()

        if mineRes == 5:
            reward = r.randint(5,15)
            print(f'You found {reward} Coins!')
            Coins += reward
            Dungeon.qkeepDrill()

    def diamondMines():
        global rocks, gold, Coins, diamond, iron
        mineRes  = r.randint(1,5)
        
        if mineRes == 1:
            print('You dig up some rock.\nWorth 1 coins per')
            rocks += 1
            Dungeon.dkeepDrill()

        if mineRes == 2:
            print('You drilled some iron!\nWorth 4 coins per')
            iron += 4
            Dungeon.dkeepDrill()
        if mineRes == 3:
            print('You found some gold!\nWorth 8 coins per')
            gold += 6
            Dungeon.dkeepDrill()

        if mineRes == 4:
            print('You found some diamonds!\n Worth 12 coins per')
            diamond += 8
            Dungeon.dkeepDrill()

        if mineRes == 5:
            reward = r.randint(5,15)
            print(f'You found {reward} Coins!')
            Coins += reward
            Dungeon.dkeepDrill()

    def ironMines():
        global rocks, gold, Coins, diamond, iron
        mineRes  = r.randint(1,5)
        
        if mineRes == 1:
            print('You dig up some rock.\nWorth 1 coins per')
            rocks += 1
            Dungeon.ikeepDrill()

        if mineRes == 2:
            print('You drilled some iron!\nWorth 4 coins per')
            iron += 2
            Dungeon.ikeepDrill()
        if mineRes == 3:
            print('You found some gold!\nWorth 8 coins per')
            gold += 3
            Dungeon.ikeepDrill()

        if mineRes == 4:
            print('You found some diamonds!\n Worth 12 coins per')
            diamond += 4   
            Dungeon.ikeepDrill()

        if mineRes == 5:
            reward = r.randint(5,15)
            print(f'You found {reward} Coins!')
            Coins += reward
            Dungeon.ikeepDrill()


    def qkeepDrill():
        print('Keep drilling?')
        choice = input('> ').lower()
        if choice[0] == 'y':
            Dungeon.quartzMines()
        else:
            Dungeon.themines
    def dkeepDrill():
        print('Keep drilling?')
        choice = input('> ').lower()
        if choice[0] == 'y':
            Dungeon.diamondMines()
        else:
            Dungeon.themines
    def ikeepDrill():
        print('Keep drilling?')
        choice = input('> ').lower()
        if choice[0] == 'y':
            Dungeon.ironMines()
        else:
            Dungeon.themines

    def themines():
        global Coins, Inventory, iront, quartzt, diamondt, rocks, gold, diamond, iron
        print('You have entered the mines.\nIn front of you is a cavern in which lie many minerals.\nNext to you is a Miner Shop\nWhere do yo go?\n1. Miner Shop 2. Exit')
        choice = input('> ').lower()
        if choice[0] == 'm':
            print('You arrive to see the shop.\nYou see that this shop is special. It exclusively sells pickaxes.')
            print('IRON-PICKAXE | Decent Pickaxe for Casual Mining | 10 Coins')
            print('DIAMOND-PICKAXE | Good Pickaxe for Serious Spelunking | 15 Coins')
            print('QUARTZ-DRILL | Professional Drill for Mining the Underground | 25 Coins')
            print('Type the name of the tool to buy, or type exit.\n[Exiting the room will delete your pickaxe\\drill.]')
            print('You can also type \'Sell\' to sell the resources you have gathered from the mines.')

            choice = input('> ').lower()

            if choice[0] == 'i' and Coins >= 10:
                print('You succesfully bought the Iron Pickaxe!')
                iront += 1
                Dungeon.ironMines()
            
            if choice[0] =='d' and Coins >=15:
                print('You successfully bought a Diamond Pickaxe!')
                diamondt += 1
                Dungeon.diamondMines()
            
            if choice[0] == 'q' and Coins >= 25:
                print('You succesfully bought a Quartz Drill!')
                quartzt += 1
                Dungeon.quartzMines()

            if choice[0] == 's':
                print('Selling Items...')
                crocks = rocks * 1
                cgold = gold * 8
                ciron = iron * 4
                cdiamond = diamond * 12
                totalMin = crocks + cgold + ciron + cdiamond
                Coins += totalMin
                print(f'You earned a total of {totalMin} coins!\nAfter all this mining you decide to leave.')
                iront = 0
                diamondt = 0
                quartzt = 0
                Dungeon.exitRoom()
            else:
                Dungeon.exitRoom()
                iront = 0
                diamondt = 0
                quartzt = 0
        else:
            Dungeon.exitRoom()

    def fishRoom():
        global Coins, rod, bait, waterBreath
        print('You enter the room and are greeted by a salty air.\nYou are in the fishing room.\nIn the center is a shop, and surronding it are pools.\nWhere do you go?\n1. Shop\n2. Jump into pool\n3. Fish in pond.\n4. Exit')
        choice = input().lower()

        if choice[0] == 's':
            print('You head towards the shop.')    
            print('[FISHING ROD:] 10 Coins\n[BAIT x 60:] Better Catches | FREE\n[Water-Breathing-Potion:] Allows Under Water Breathing | 15 Coins')

            choice = input('> ').lower()

            if choice[0] == 'f' and Coins >= 10:
                print('Successfully bought Fishing Rod.')
                rod += 1 
                Coins -= 10
                Dungeon.fishRoom()

            if choice[0] == 'b' and Coins >= 30:
                print('Successfully bought Bait x 60.')
                Coins -= 0
                bait += 60
                Dungeon.fishRoom()

            if choice[0] ==  'w' and Coins >= 15:
                print('Successfully bought Water-Breath Potion.')
                Coins -= 15
                waterBreath += 1
                Dungeon.fishRoom()

            else:
                print('You can\'t afford this item!')
                Dungeon.fishRoom()
        
        if choice[0] == 'j' and waterBreath <= 0:
            print('You jump into the pool.\nYou go farther downward, but your air runs out and you drown.')
            Dungeon.death()        
            Dungeon.fishRoom()

        if choice[0] == 'j' and waterBreath >= 0:
            print('Drinking the potion, you go into the pool, exploring downwards.\nYou come across a golden chest and open it.')
            Dungeon.chest
            print('After getting all the loot you head back up.')
            Dungeon.fishRoom()

        if choice[0] == 'f' and rod >= 1 and bait >=1:
            Dungeon.roomfish()

        else:
            Dungeon.exitRoom()

    def battleRoom():
        global hlegs, hbody, hhead, hwings
        if int(hlegs + hbody + hhead + hwings) == 0:
            Dungeon.finalStroke()
        else:
            print('What part of the dragon do you aim for?\n1. Head\n2. Body\n3. Legs\n4. Wings')
        
            choice = input('> ').lower()


            if choice[0] == 'h' and hhead > 0:
                Dungeon.headFight()

            if choice[0] == 'h' and hhead <= 0:
                print('You have already destroyed the head armor!')
                Dungeon.battleRoom()
        
            if choice[0] == 'w' and hwings > 0:
                Dungeon.wingFight()

            if choice[0] == 'w' and hwings <= 0:
                print('You have already destroyed the wings\' armor!')
                Dungeon.battleRoom()
    
            if choice[0] == 'b' and hbody > 0:
                Dungeon.bodyFight()

            if choice[0] == 'b' and hbody <= 0:
                print('You have already destroyed the body\'s armor!')
                Dungeon.battleRoom()

            if choice[0] == 'l' and hlegs > 0:
                Dungeon.legsFight()

            if choice[0] == 'l' and hlegs <= 0:
                print('You have already destroyed the legs\' armor!')
                Dungeon.battleRoom()

            else:
                print('Thats not an available command.')
                Dungeon.battleRoom()

    def headFight():
        global hhead, Inventory, health
        print('You go for the dragon\'s head.')

        while hhead > 0:
            print('Do you attack or heal?')
            choice = input('> ').lower()

            if choice[0] == 'a':
                dmg = r.randint(15,30)
                hhead -= dmg
                hhead = max(0, hhead)
                print(f'You do {dmg} damage to the dragon.\n{hhead} health remains!')
                if hhead <= 0:
                    print('You have have destroyed the head armor on the dragon!')
                    Dungeon.battleRoom()
            if choice[0] == 'h':
                if Inventory:  
                    print('Taking some food out of your bag, you slowly revive your health back to 100.')
                    Inventory.pop()
                    health = 100
                else:
                    print('You don\'t have any food!')
                    Dungeon.headFight()
    def wingFight():
        global hwings, Inventory, health
        print('You go for the dragon\'s wings.')

        while hwings > 0:
            print('Do you attack or heal?')
            choice = input('> ').lower()

            if choice[0] == 'a':
                dmg = r.randint(15,30)
                hwings -= dmg
                hwings = max(0, hwings)
                print(f'You do {dmg} damage to the dragon.\n{hwings} health remains!')
                if hwings <= 0:
                    print('You have have destroyed the wing armor on the dragon!')
                    Dungeon.battleRoom()
            if choice[0] == 'h':
                if Inventory:  
                    print('Taking some food out of your bag, you slowly revive your health back to 100.')
                    Inventory.pop()
                    health = 100
                else:
                    print('You don\'t have any food!')
                    Dungeon.wingFight()



    def bodyFight():
        global hbody, Inventory, health
        print('You go for the dragon\'s body.')

        while hbody > 0:
            print('Do you attack or heal?')
            choice = input('> ').lower()

            if choice[0] == 'a':
                dmg = r.randint(15,30)
                hbody -= dmg
                hbody = max(0, hbody)
                print(f'You do {dmg} damage to the dragon.\n{hbody} health remains!')
                if hbody <= 0:
                    print('You have have destroyed the body armor on the dragon!')
                    Dungeon.battleRoom()
            if choice[0] == 'h':
                if Inventory:  
                    print('Taking some food out of your bag, you slowly revive your health back to 100.')
                    Inventory.pop()
                    health = 100
                else:
                    print('You don\'t have any food!')
                    Dungeon.bodyFight()

    def legsFight():
        global hlegs, Inventory, health
        print('You go for the dragon\'s legs')

        while hlegs > 0:
            print('Do you attack or heal?')
            choice = input('> ').lower()

            if choice[0] == 'a':
                dmg = r.randint(15,30)
                hlegs -= dmg
                hlegs = max(0, hlegs)
                print(f'You do {dmg} damage to the dragon.\n{hlegs} health remains!')
                if hlegs <= 0:
                    print('You have have destroyed the leg armor on the dragon!')
                    Dungeon.battleRoom()
            if choice[0] == 'h':
                if Inventory:  
                    print('Taking some food out of your bag, you slowly revive your health back to 100.')
                    Inventory.pop()
                    health = 100
                else:
                    print('You don\'t have any food!')
                    Dungeon.legsFight()
    def finalStroke():
        global hlegs, hbody, hhead, hwings

        print('You weakened all the armor!\nYou prepare the final stroke of the sword.\nAttack?')
        choice = input('> ')

        if choice:
            print('You bring down the sword, and finish off the dragon.\nThe gates behind it magically open, ready for you to leave.\nYou walk past the gates and into the free world.')
            Dungeon.credits()
    def credits():
        print('\n\n\nThe End')
        
            





start()