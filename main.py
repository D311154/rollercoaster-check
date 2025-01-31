import lib_coasterimg as coasterimg
import time
import os

#Read check values
file1 = open("rules/age.txt", "r")
age_check = int(file1.read())
file1.close()

file2 = open("rules/height.txt", "r")
height_check = int(file2.read())
file1.close()

running = True
while running:

    #Get inputs
    os.system('cls')
    print("Rollercoaster-check™")
    age = input("Voer leeftijd in: ")
    height = input("Voer lengte in CM in: ")
    age = int(age)
    height = int(height)
    ageMissing = age_check - age
    heightMissing = height_check - height

    #Process checks
    if(age >= age_check and height >= height_check):
        os.system('cls')
        print("Stap maar in!")
        print(coasterimg.get())
        time.sleep(3)

    elif(age >= age_check and height < height_check):
        os.system('cls')
        print("je bent helaas te kort om in deze achtbaan te gaan...")
        print(coasterimg.sad())
        time.sleep(1)
        print(f"als je hier in wilt, moet je nog {heightMissing}cm groeien!")
        time.sleep(3)

    elif(age < age_check and height >= height_check):
        os.system('cls')
        print("je bent helaas te jong om in deze achtbaan te gaan...")
        print(coasterimg.sad())
        time.sleep(1)
        print(f"als je hier in wilt, moet je nog {ageMissing} jaar ouder worden!")
        time.sleep(3)

    else:
        os.system('cls')
        print("je bent te kort en te jong om in deze achtbaan te gaan...")
        print(coasterimg.sad())
        time.sleep(1)
        print(f"als je hier in wilt, moet je nog {heightMissing}cm groeien en {ageMissing} jaar ouder worden!")
        time.sleep(3)

    result = input("Druk op Enter om nog een keer te checken, of X om te stoppen\n\n")
    if(result.upper() == "X"):
        running = False
