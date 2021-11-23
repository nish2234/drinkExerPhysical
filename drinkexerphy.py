import time
import pygame

def paanipaani():
    print("You should drink water , drink water ")
    pygame.mixer.init()
    pygame.mixer.music.load("paana.mp3")  # any mp3 file
    pygame.mixer.music.play()
    if input("enter E if you have drank water ") == 'E':
        pygame.mixer.music.stop()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()

def aankhon():
    print("You should do some eye exercise ")
    pygame.mixer.init()
    pygame.mixer.music.load("aankho.mp3")  # any mp3 file
    pygame.mixer.music.play()
    if input("enter E if you have done exercise ") == 'E':
        pygame.mixer.music.stop()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()
def sultan():
    print("You should do some physical activities ")
    pygame.mixer.init()
    pygame.mixer.music.load("maidan.mp3")  # any mp3 file
    pygame.mixer.music.play()
    if input("enter E if you have done physical activities ") == 'E':
        pygame.mixer.music.stop()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()




name = input("Enter the name: ")
print(f"HI {name} HOW ARE YOU HOPE YOU ARE DOING GOOD")
print("SO PRESS 1 TO START YOUR DAY: ")
start = int(input())
if start == 1:
    while(True):


        time.sleep(45*60)
        paanipaani()


        time.sleep(45*60)
        aankhon()


        time.sleep(45*60)
        sultan()
        print("IF YOUR OFFICE TIME IS OVER THAN PRESS Y")
        if input() == 'Y':
            break
