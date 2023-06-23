import itertools
import random
import os
import time
import os
os.add_dll_directory(os.getcwd())
import vlc
ladderSound = vlc.MediaPlayer("https://cdn.discordapp.com/attachments/1034986606702112818/1064651638431821954/Victory_Sound_Effect.mp3")
snakeSound  = vlc.MediaPlayer("https://cdn.discordapp.com/attachments/1034986606702112818/1064651638431821954/Victory_Sound_Effect.mp3")
                                                             
def GetDimensions():
    while True:
        getRow = input("Tedad Satr Haye Zamin Bazi Ra Moshakhas Konid: ")
        getCol = input("Tedad Sotun Haye Zamin Bazi Ra Moshakhas Konid: ")
        if getCol.isnumeric() and getRow.isnumeric() and (int(getRow)*int(getCol)) >= 1:
            break
        else:
            os.system("cls")
            print("Value Eshtebah Vared Kardid")
            print("===========================")
    return int(getRow), int(getCol)

def setSnakes():
    os.system("cls")
    while True:
        getSnakes = input("Tedad Snake Ha Ra Moshakhas Konid: ")
        if getSnakes.isnumeric():
            os.system("cls")
            for i in range(int(getSnakes)):
                while True:
                    index = input("Mabdaa Snake Shomare "+str(i+1)+" : ")
                    value = input("Maghsad Snake Shomare "+str(i+1)+": ")
                    if index.isnumeric() and value.isnumeric() and int(index) > int(value):
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        print("Vorudi Ha Bayad Adad Bashand Va Voroudi Aval Az Dovomi Koochik Tar Bashad")
                        print("============================================")
                SNAKESANDLADDERS[index] = value
            break
    return int(getSnakes) 

def setLadders():
    os.system("cls")
    while True:
        getLadders = input("Tedad Ladder Ha Ra Moshakhas Konid: ")
        if getLadders.isnumeric():
            os.system("cls")
            for i in range(int(getLadders)):
                while True:
                    index = input("Mabdaa Ladder Shomare "+str(i+1)+" : ")
                    value = input("Maghsad Ladder Shomare "+str(i+1)+": ")
                    if index.isnumeric() and value.isnumeric() and int(index) < int(value):
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        print("Vorudi Ha Bayad Adad Bashand Va Voroudi Aval Az Dovomi Koochik Tar Bashad")
                        print("============================================")
                SNAKESANDLADDERS[index] = value
            break
    return int(getLadders)

def GetNumPlayers():
    os.system("cls")
    return int(input("Tedad Player Ha Ra Moshakhas Konid: "))

def setNames():
    os.system("cls")
    player_names = []
    for i in range(Players + 1):
        if i == 0:
            continue
        player_names.append(input("Esm Player "+str(i)+" Ra Vared Konid: "))
    return player_names

def setupPlayers():
    os.system("cls")
    Queue = {}
    for name in player_names:
        Queue[name] = {"canPlay" : False, "Position" : "Not in Game", "Turn": True}
    return Queue

def HasGameEnded():
    result = True
    for name in (player_names):
        if Queue[name]["Position"] == "Not in Game" or Queue[name]["Position"] < Row*Col:
            result = False
            break
    return result

def selectPlayer():
    result = False
    while True:
        for name in (player_names):
            if Queue[name]["Turn"]:
                result = name
        if result:
            break
        else:
            for name in (player_names):
                Queue[name]["Turn"] = True
    return result

if __name__ == "__main__":
    while True:
        os.system("cls")
        SNAKESANDLADDERS = {}
        LeaderBoard = []
        Row, Col = GetDimensions()
        Ladders = setLadders()
        Snakes = setSnakes()
        Players = GetNumPlayers()
        player_names = setNames()
        Queue = setupPlayers()
        lastPlayer = False

        while not HasGameEnded():
            os.system("cls")
            if Ladders > 0:
                print("Ladders:", end = " ")
                for x in SNAKESANDLADDERS:
                    if int(x) < int(SNAKESANDLADDERS[x]):
                        print(str(x)+" - "+str(SNAKESANDLADDERS[x])+",", end = "")
                print("")
                print("---------------------------") 
            if Snakes > 0:
                print("Snakes:", end = " ")
                for x in SNAKESANDLADDERS:
                    if int(x) > int(SNAKESANDLADDERS[x]):
                        print(str(x)+" - "+str(SNAKESANDLADDERS[x])+",", end = "")
                print("")
                print("---------------------------")        
            for name in (player_names):
                print("["+name+"] ==> "+str(Queue[name]["Position"])+" / "+str(Row*Col))
            print("======================================================") 
            currentPlayer = lastPlayer or selectPlayer()
            while True:
                if Queue[currentPlayer]["Position"] != "Not in Game" and Queue[currentPlayer]["Position"] == Row*Col:
                    Queue[currentPlayer]["Turn"] = False
                    break
                print("Nobat Be "+currentPlayer+" Reside "+(lastPlayer and "(Jayeze 6)" or ""))
                lastPlayer = False
                input("Dokme [Enter] Baraye Endakhtan Taas: ")
                Queue[currentPlayer]["Turn"] = False
                diceVal = random.randint(1, 6)
                print("Adad Taas: "+str(diceVal))
                time.sleep(1.5)
                if Players > 1 and not Queue[currentPlayer]["canPlay"]:
                    if diceVal == 6:
                        Queue[currentPlayer]["Position"] = 0
                        Queue[currentPlayer]["canPlay"] = True
                        lastPlayer = currentPlayer
                    break
                else:
                    if Players == 1:
                        if Queue[currentPlayer]["Position"] == "Not in Game":
                            Queue[currentPlayer]["Position"] = 0
                            Queue[currentPlayer]["canPlay"] = True
                    if Queue[currentPlayer]["Position"] + diceVal <= Row*Col:
                        Queue[currentPlayer]["Position"] = Queue[currentPlayer]["Position"] + diceVal
                        for x in SNAKESANDLADDERS:
                            if int(x) == int(Queue[currentPlayer]["Position"]):
                                Queue[currentPlayer]["Position"] = int(SNAKESANDLADDERS[x])
                                if int(x) < int(SNAKESANDLADDERS[x]):
                                    ladderSound.play()
                                else:
                                    snakeSound.play()
                                break
                        if Queue[currentPlayer]["Position"] == Row*Col:
                            LeaderBoard.append(currentPlayer)
                            break
                        if diceVal != 6:
                            break
                        else:
                            lastPlayer = currentPlayer
                            break
                    elif diceVal != 6:
                        break
                    else:
                        lastPlayer = currentPlayer
                        break
        os.system("cls")
        print("=====LeaderBoard=====")
        for i in range(len(LeaderBoard)):
            print("Nafare "+str(i+1)+": "+LeaderBoard[i])
        time.sleep(5)