import pyttsx3
import pyperclip as pc
import random
import speech_recognition as sr
import datetime
import wikipedia
import math
from PIL import Image
import webbrowser
import os
import pyjokes
import pygame 
import sys
import pywhatkit
from pygame.locals import *
import time
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print("you said: ",query,"\n")
    except Exception as e: 
        print("You were not audible. Please try by typing")
        speak("You were not audible. Please try by typing")
        r.pause_threshold = 1
        query=input("")
        return query
    return query

def wikipedia_search(name):
    try:
        results = wikipedia.summary(name, sentences = 2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except:
        messuif="We were unable to find "+name+"in wikipedia please retry"
        print(messuif)
        speak(messuif)

def message():
    print("Please Enter The Number to which you want to send the message")
    speak("Please Enter The Number to which you want to send the message")
    num=(input(""))
    clear()
    print("Contact No.",num)
    print('Please speak the message you want to send')
    speak('Please speak the message you want to send')
    mes=takeCommand()
    clear()
    print("Contact No.",num)
    print("message is-",mes)
    print("Please enter the hour on which you want to send the message")
    speak("Please enter the hour on which you want to send the message")
    hour=int(input(""))
    print("Please enter the minute on which you want to send the message")
    speak("Please enter the minute on which you want to send the message")
    min=int(input(""))
    clear()
    print("Contact No.",num)
    print("message",mes)
    print("The set Time",hour,":",min)
    print("Please enter the wait time")
    speak("Please enter the wait time")
    wait=int(input())
    clear()
    print("Contact No.",num)
    print("message",mes)
    print("The set Time",hour,":",min)
    print("Wait time",wait)
    sp1="Your Whatsapp Web will open according to the time set and then the message will be sent after",wait,"seconds"
    speak(sp1)
    pywhatkit.sendwhatmsg(num,mes,hour,min,wait,)
    clear()

def calculator():
    clear = lambda: os.system('cls')
    clear()
    zz=0
    while zz!=1:   
        print("1-Sum")
        print("2-difference")
        print("3-product")
        print("4-quotient")
        print("5-table teller")
        print("6-Square")
        print("7-power")
        print("8-square root")
        print("9-cube root")
        print("10-Factorial")
        print("11-Fibonacci series")
        a=int(input("please select one of them \n",))
        if(a==1):
            b=int(input("enter the first no."))
            c=int(input("enter the second no."))
            d=b+c
            print(b,"+",c,"=",d)
        elif(a==2):
            e=int(input("enter the first no."))
            f=int(input("enter the second no."))
            g=e-f
            print(e ,"-",f,"=",g)
        elif(a==3):
            h=int(input("enter the first no."))
            i=int(input("enter the second no."))
            j=h*i
            print(h,"*",i,"=",j)
        elif(a==4):
            k=int(input("enter the first no."))
            l=int(input("enter the second no."))
            m=k/l
            print(k,"/",l,"=",m)
        elif(a==5):
            n=int(input("enter the number of which you want the table"))
            o=int(input("enter the number till where do you want the table"))
            p=1
            while p<=o:
                print(str(n) + ' * ' + str(p) + ' = '+str(n*p))
                p=p+1
        elif(a==6):
            q=int(input("enter the number you want to know the square"))
            r=q*q
            print('the square of',q,'is =',r)
        elif(a==7):
            s=int(input("enter the no. you want to know the square of"))
            t=int(input("enter the the no. of power"))
            u=t*(s*s)
            print("the answer is",u)
        elif(a==8):
            w=int(input("Enter the no. of which you want the square root"))
            x=0
            while x**2 < w:
                x=x+1
                print("the square root of " + str(w) + " is equal to: " + str(x))
        elif(a==9):
            y=int(input("Enter the no. of which you want the cube root"))
            z=0
            while z**3 < y:
                z=z+1
            print("the cube root of " + str(y) + " is equal to: " + str(z))
        elif(a==10):
            za=int(input("Enter the number"))
            zb=1
            for i in range(1,za+1):
                zb=zb*i
            print("the factorial of a number is= ", zb)
        elif(a==11):
            fg=int(input("Enter the level upto which you want to know the fibonacci series"))
            zd=0
            ze=1
            for zf in range(1,fg+1):
                zg=zd+ze
                print(zg)
                zd=ze
                ze=zg
        else:
            print("please select a valid choise")
        Var1=input("To re run press ENTER to exit Type-E")
        if Var1=="":
            zz=0
            clear()
        if Var1!="":
            zz=1
            clear()

def voicenoter():
    clear()
    print("Speak what you want to type")
    speak("Speak What you want to type")
    stra=takeCommand().capitalize()
    sp="Your note is "+stra
    print(sp)
    speak(sp)
    print("Your text has been copied to your clipboard")
    speak("Your text has been copied to your clipboard")
    pc.copy(sp)

def wishMe(name):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        wishm="good morning"+name
        print(wishm)
        speak(wishm)
    elif hour>=12 and hour<18:
        wisha="good afternoon"+name
        print(wisha)
        speak(wisha)
    else:
        wishe="Good evening"+name
        print(wishe)
        speak(wishe)
    print("I am Your Assistant sir. Please tell me how may I help you.")
    speak("I am Your Assistant sir. Please tell me how may I help you.")

def boredome(choise):
    if choise==1:
        print('You can talk with me to remove your boredom')
        speak('You can talk with me to remove your boredom')
        print("Let's start with a joke")
        speak("Let's start with a joke")
        joke1=(pyjokes.get_joke())
        print(joke1)
        speak(joke1)
        time.sleep(1)
        print("How was the joke")
        speak("How was the joke")
        joke_feed=takeCommand()
        if "good" in joke_feed or "excellent" in joke_feed or "outstanding" in joke_feed or "nice" in joke_feed:
            print("Thanks for your compliment")
            speak("Thanks for your compliment")
            print("do you want to listen one more joke?")
            speak("do you want to listen one more joke?")
            aaaa=takeCommand()
            if aaaa=="yes":
                joke2=(pyjokes.get_joke())
                print(joke2)
                speak(joke2)
                time.sleep(1)
            else:
                print("No probelem")
                speak("No probelem")
                time.sleep(1)
        else :
            print("Sorry for the thing wrong. Next time I will take care of this")
            speak("Sorry for the thing wrong. Next time I will take care of this")
            time.sleep(1)
        print("I want to tell you one thing")
        speak("I want to tell you one thing")
        time.sleep(1)
        print("You are very handsome and beautifull. I have not seen you but I can tell this by your Voice and style of speaking")
        speak("You are very handsome and beautifull. I have not seen you but I can tell this by your Voice and style of speaking")
        time.sleep(1)
        print("and because you are so good so I can show you my face today. That means a face reveal")
        speak("and because you are so good so I can show you my face today. That means a face reveal")
        image = Image.open('Python/Assistant/download.jfif')
        image.show()
        time.sleep(2)
        print("How was I. was I good ")
        speak("How was I. was I good ")
        face_feed=takeCommand()
        if "good" in face_feed or "excellent" in face_feed or "outstanding" in face_feed or "nice" in face_feed or "handsome" in query or "beautifull" in query or "smart" in query:
            print("Thanks for your compliment. i think now I should leave. we will meet soon. Till that time you can do something another to remove your boredome")
            speak("Thanks for your compliment. i think now I should leave. we will meet soon. Till that time you can do something another to remove your boredome")
            
        else:
            print("Next time I will try to be more smarter. I think I should leave. we will meet soon. Till that time you can do something another to remove your boredome")
            speak("Next time I will try to be more smarter. I think I should leave. we will meet soon. Till that time you can do something another to remove your boredome")
    elif choise==2:
        webbrowser.open('https://chromedino.com/')
        exit()
    elif choise==3:
        FPS=32
        scorechange=1
        SCREENWIDTH=289
        SCREENHEIGHT=511
        SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        GROUNDY=SCREENHEIGHT*0.8
        GAME_SPRITES={}
        GAME_SOUNDS={}
        PLAYER='Python/Flappy bird game/gallery/sprites/bird.png'
        BACKGROUND='Python/Flappy bird game/gallery/sprites/background.png'
        PIPE='Python/Flappy bird game/gallery/sprites/pipe.png'

        def welcomeScreen():
            playerx = int(SCREENWIDTH/5)
            playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
            messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
            messagey = int(SCREENHEIGHT*0.13)
            basex = 0
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                        pygame.quit()
                        os.system('cls')
                        sys.exit()
                    elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                        return
                    else:
                        SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                        SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                        pygame.display.update()
                        FPSCLOCK.tick(FPS)
        def mainGame():
            score = 0
            playerx = int(SCREENWIDTH/5)
            playery = int(SCREENWIDTH/2)
            basex = 0
            newPipe1 = getRandomPipe()
            newPipe2 = getRandomPipe()
            upperPipes = [
                {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
                {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
            ]
            lowerPipes = [
                {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
                {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
            ]

            pipeVelX = -4

            playerVelY = -9
            playerMaxVelY = 10
            playerMinVelY = -8
            playerAccY = 1

            playerFlapAccv = -8
            playerFlapped = False


            while True:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                        if playery > 0:
                            playerVelY = playerFlapAccv
                            playerFlapped = True
                            GAME_SOUNDS['wing'].play()
                crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) 
                if crashTest:
                    return     
                playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
                for pipe in upperPipes:
                    pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2

                    if pipeMidPos<= playerMidPos < pipeMidPos +4:
                        score += scorechange
                        print(f"Your score is {score}") 
                        GAME_SOUNDS['point'].play()



                if playerVelY <playerMaxVelY and not playerFlapped:
                    playerVelY += playerAccY

                if playerFlapped:
                    playerFlapped = False            
                playerHeight = GAME_SPRITES['player'].get_height()
                playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

                for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                    upperPipe['x'] += pipeVelX
                    lowerPipe['x'] += pipeVelX
                if 0<upperPipes[0]['x']<5:
                    newpipe = getRandomPipe()
                    upperPipes.append(newpipe[0])
                    lowerPipes.append(newpipe[1])
                if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                    upperPipes.pop(0)
                    lowerPipes.pop(0)
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                    SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                    SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                myDigits = [int(x) for x in list(str(score))]
                width = 0
                for digit in myDigits:
                    width += GAME_SPRITES['numbers'][digit].get_width()
                Xoffset = (SCREENWIDTH - width)/2

                for digit in myDigits:
                    SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                    Xoffset += GAME_SPRITES['numbers'][digit].get_width()
                pygame.display.update()
                FPSCLOCK.tick(FPS)

        def isCollide(playerx, playery, upperPipes, lowerPipes):
            if playery> GROUNDY - 25  or playery<0:
                GAME_SOUNDS['hit'].play()
                return True

            for pipe in upperPipes:
                pipeHeight = GAME_SPRITES['pipe'][0].get_height()
                if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
                    GAME_SOUNDS['hit'].play()
                    return True

            for pipe in lowerPipes:
                if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                    GAME_SOUNDS['hit'].play()
                    return True

            return False

        def getRandomPipe():
            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            offset = SCREENHEIGHT/3
            y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
            pipeX = SCREENWIDTH + 10
            y1 = pipeHeight - y2 + offset
            pipe = [
                {'x': pipeX, 'y': -y1},
                {'x': pipeX, 'y': y2}
            ]
            return pipe

        if __name__ == '__main__':
            pygame.init()
            FPSCLOCK=pygame.time.Clock()
            pygame.display.set_caption('Flappy bird by Aayansh')
            GAME_SPRITES['numbers']=(
                pygame.image.load('Python/Flappy bird game/gallery/sprites/0.png').convert_alpha(),
                pygame.image.load('Python/Flappy bird game/gallery/sprites/1.png').convert_alpha(),
                pygame.image.load('Python/Flappy bird game/gallery/sprites/2.png').convert_alpha(),
                pygame.image.load('Python/Flappy bird game/gallery/sprites/3.png').convert_alpha(),
                pygame.image.load('Python/Flappy bird game/gallery/sprites/4.png').convert_alpha(),
                pygame.image.load('Python/Flappy bird game/gallery/sprites/5.png').convert_alpha(),
                pygame.image.load('Python/Flappy bird game/gallery/sprites/6.png').convert_alpha(),
                pygame.image.load('Python/Flappy bird game/gallery/sprites/7.png').convert_alpha(),
                pygame.image.load('Python/Flappy bird game/gallery/sprites/8.png').convert_alpha(),
                pygame.image.load('Python/Flappy bird game/gallery/sprites/9.png').convert_alpha(),
            )
            GAME_SPRITES['message']=pygame.image.load('Python/Flappy bird game/gallery/sprites/message.png').convert_alpha()
            GAME_SPRITES['base']=pygame.image.load('Python/Flappy bird game/gallery/sprites/base.png').convert_alpha()
            GAME_SPRITES['pipe']=(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
            pygame.image.load(PIPE).convert_alpha()
            )

            GAME_SOUNDS['die']=pygame.mixer.Sound('Python/Flappy bird game/gallery/audio/die.wav')
            GAME_SOUNDS['hit']=pygame.mixer.Sound('Python/Flappy bird game/gallery/audio/hit.wav')
            GAME_SOUNDS['point']=pygame.mixer.Sound('Python/Flappy bird game/gallery/audio/point.wav')
            GAME_SOUNDS['swoosh']=pygame.mixer.Sound('Python/Flappy bird game/gallery/audio/swoosh.wav')
            GAME_SOUNDS['wing']=pygame.mixer.Sound('Python/Flappy bird game/gallery/audio/wing.wav')

            GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert_alpha()
            GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()
            while True:
                welcomeScreen()
                mainGame()
    elif choise==4:
        pygame.init()
        screen = pygame.display.set_mode((798,600))
        pygame.mixer.init()
        pygame.display.set_caption('Racing Game by Aayansh')
        logo = pygame.image.load('Python\Car racing\logo.jpeg')
        pygame.display.set_icon(logo)
        IntroFont = pygame.font.Font("freesansbold.ttf", 38)
        def introImg(x,y):
            intro = pygame.image.load("Python\Car racing\intro.png")

            screen.blit(intro,(x,y))
        def instructionIMG(x,y):
            instruct = pygame.image.load("Python\Car racing\instruction.png")
            run = True
            while run:
                screen.blit(instruct,(x,y))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

        def aboutIMG(x,y):
            aboutimg = pygame.image.load("Python\Car racing\About new.jpg")
            run = True
            while run:
                screen.blit(aboutimg,(x,y))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
        def play(x,y):
            playtext = IntroFont.render("PLAY",True,(255,0,0))
            screen.blit (playtext,(x,y))
        def ABOUT(x,y):
            aboutText = IntroFont.render("ABOUT",True,(255,0,0))
            screen.blit (aboutText,(x,y))
        def Instruction(x,y):
            instructionText = IntroFont.render("INSTRUCTION",True,(255,0,0))
            screen.blit(instructionText,(x,y))


        def introscreen():
            run = True
            pygame.mixer.music.load('Python\Car racing\On and On_320(PaglaSongs) (1).mp3')
            pygame.mixer.music.play()
            while run :
                screen.fill((0,0,0))
                introImg(0,0)
                play(100,450)
                Instruction(280,450)
                ABOUT(615,450)
                x,y = pygame.mouse.get_pos()
                button1 = pygame.Rect(60,440,175,50)
                button2 = pygame.Rect(265,440,300,50)
                button3 = pygame.Rect(600,440,165,50)
                pygame.draw.rect(screen, (255,255,255), button1,6)
                pygame.draw.rect(screen, (255,255,255), button2,6)
                pygame.draw.rect(screen,(255,255,255),button3,6)
                if button1.collidepoint(x,y): 
                    pygame.draw.rect(screen, (155,0,0), button1,6)
                    if click:
                        countdown()
                if button2.collidepoint(x,y):
                    pygame.draw.rect(screen, (155,0,0), button2,6)
                    if click:
                        instructionIMG(0,0)
                if button3.collidepoint(x,y):
                    pygame.draw.rect(screen,(155,0,0),button3,6)
                    if click:
                        aboutIMG(0,0)
                click = False
                for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    run = False
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     if event.button == 1:
                         click = True
                pygame.display.update()
        def countdown():
            font2 = pygame.font.Font('freesansbold.ttf', 85)
            countdownBacground = pygame.image.load('Python\Car racing\\bg.png')
            three = font2.render('3',True, (187,30,16))
            two =   font2.render('2',True, (255,255,0))
            one =   font2.render('1',True, (51,165,50))
            go =    font2.render('GO!!!',True, (0,255,0))
            screen.blit(countdownBacground, (0,0))
            pygame.display.update()
            screen.blit(three,(350,250))
            pygame.display.update()
            time.sleep(0.5)
            screen.blit(countdownBacground, (0,0))
            pygame.display.update()
            time.sleep(0.5)
            screen.blit(two,(350,250))
            pygame.display.update()
            time.sleep(0.5)
            screen.blit(countdownBacground, (0,0))
            pygame.display.update()
            time.sleep(0.5)
            screen.blit(one,(350,250))
            pygame.display.update()
            time.sleep(0.5)
            screen.blit(countdownBacground, (0,0))
            pygame.display.update()
            time.sleep(0.5)
            screen.blit(go,(300,250))
            pygame.display.update()
            time.sleep(0.5)
            gameloop()
            pygame.display.update()
        def gameloop():
            pygame.mixer.music.load('Python\Car racing\BackgroundMusic.mp3')
            pygame.mixer.music.play()
            crash_sound = pygame.mixer.Sound('Python\Car racing\car_crash.wav')
            score_value = 0
            font1= pygame.font.Font("freesansbold.ttf",25)

            def show_score(x,y):
                score = font1.render("SCORE: "+ str(score_value), True, (255,0,0))
                screen.blit(score, (x,y))

            with open ("Python\Car racing\highscore.txt","r") as f:
                    highscore = f.read()
            def show_highscore(x,y):
                Hiscore_text = font1.render('HISCORE :' + str(highscore),True,(255,0,0))
                screen.blit (Hiscore_text,(x,y))
                pygame.display.update()
            def gameover():
                gameoverImg = pygame.image.load("Python\Car racing\gameover.png")
                run = True
                while run:
                
                    screen.blit(gameoverImg,(0,0))
                    time.sleep(0.5)
                    show_score(330,400)
                    time.sleep(0.5)
                    show_highscore(330,450)
                    pygame.display.update()

                    for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()
                     if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            countdown()
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()

            bg = pygame.image.load('Python\Car racing\\bg.png')
            maincar = pygame.image.load('Python\Car racing\car.png')
            maincarX = 350
            maincarY = 495
            maincarX_change = 0
            maincarY_change = 0
            car1 = pygame.image.load('Python\Car racing\car1.jpeg')
            car1X = random.randint(178,490)
            car1Y = 100
            car1Ychange = 5
            car2 = pygame.image.load('Python\Car racing\car2.png')
            car2X = random.randint(178,490)
            car2Y = 100
            car2Ychange = 5

            car3 = pygame.image.load('Python\Car racing\car3.png')
            car3X = random.randint(178,490)
            car3Y = 100
            car3Ychange = 5  
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN: 
                        if event.key == pygame.K_RIGHT:
                            maincarX_change += 5

                        if event.key == pygame.K_LEFT:
                            maincarX_change -= 5

                        if event.key == pygame.K_UP:
                            maincarY_change -= 5

                        if event.key == pygame.K_DOWN:
                            maincarY_change += 5
                    if event.type == pygame.KEYUP: 
                        if event.key == pygame.K_RIGHT:
                            maincarX_change = 0

                        if event.key == pygame.K_LEFT:
                            maincarX_change = 0

                        if event.key == pygame.K_UP:
                            maincarY_change = 0

                        if event.key == pygame.K_DOWN:
                            maincarY_change = 0            

                if maincarX < 178:
                    maincarX = 178
                if maincarX > 490:
                    maincarX = 490

                if maincarY < 0:
                    maincarY = 0
                if maincarY > 495:
                    maincarY = 495
                screen.fill((0,0,0))
                screen.blit(bg,(0,0))
                screen.blit(maincar,(maincarX,maincarY))
                screen.blit(car1,(car1X,car1Y))
                screen.blit(car2,(car2X,car2Y))
                screen.blit(car3,(car3X,car3Y))
                show_score(570,280)
                show_highscore(0,0)
                maincarX += maincarX_change
                maincarY += maincarY_change
                car1Y += car1Ychange
                car2Y += car2Ychange
                car3Y += car3Ychange
                if car1Y > 670:
                    car1Y = -100
                    car1X = random.randint(178,490)
                    score_value += 1
                if car2Y > 670:
                    car2Y = -150
                    car2X = random.randint(178,490)
                    score_value += 1
                if car3Y > 670:
                    car3Y = -200
                    car3X = random.randint(178,490)
                    score_value += 1
                if score_value > int(highscore):
                    highscore = score_value
                def iscollision(car1X,car1Y,maincarX,maincarY):
                    distance = math.sqrt(math.pow(car1X-maincarX,2) + math.pow(car1Y - maincarY,2)) 
                    if distance < 50: 
                        return True
                    else:
                        return False
                def iscollision(car2X,car2Y,maincarX,maincarY):
                    distance = math.sqrt(math.pow(car2X-maincarX,2) + math.pow(car2Y - maincarY,2))
                    if distance < 50:
                        return True
                    else:
                        return False
                def iscollision(car3X,car3Y,maincarX,maincarY):
                    distance = math.sqrt(math.pow(car3X-maincarX,2) + math.pow(car3Y - maincarY,2))
                    if distance < 50:
                        return True
                    else:
                        return False
                coll1 = iscollision(car1X,car1Y,maincarX,maincarY) 
                coll2 = iscollision(car2X,car2Y,maincarX,maincarY) 
                coll3 = iscollision(car3X,car3Y,maincarX,maincarY) 
                if coll1: 


                    car1Ychange = 0
                    car2Ychange = 0
                    car3Ychange = 0
                    car1Y = 0
                    car2Y = 0
                    car3Y = 0
                    maincarX_change = 0
                    maincarY_change = 0
                    pygame.mixer.music.stop()
                    crash_sound.play()
                    time.sleep(1)
                    gameover()
                if coll2:
                

                    car1Ychange = 0
                    car2Ychange = 0
                    car3Ychange = 0
                    car1Y = 0
                    car2Y = 0
                    car3Y = 0
                    maincarX_change = 0
                    maincarY_change = 0
                    pygame.mixer.music.stop()
                    crash_sound.play()
                    time.sleep(1)
                    gameover()
                if coll3:

                
                    car1Ychange = 0
                    car2Ychange = 0
                    car3Ychange = 0
                    car1Y = 0
                    car2Y = 0
                    car3Y = 0
                    maincarX_change = 0
                    maincarY_change = 0
                    pygame.mixer.music.stop()
                    crash_sound.play()
                    time.sleep(1)
                    gameover()

                if car1Ychange == 0 and car2Ychange == 0 and car3Ychange == 0 :
                  pass
              
                with open ("Python\Car racing\highscore.txt","w") as f:
                    f.write(str(highscore))


                pygame.display.update()
                os.system('cls')
        introscreen()
    elif choise==5:
        pygame.init()
        yellow = (255, 255, 102)
        black = (0, 0, 0)
        green = (0, 255, 0)
        blue = (50, 153, 213)

        dis_width = 700
        dis_height =600

        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game by Aayansh')

        clock = pygame.time.Clock()

        snake_block = 10
        snake_speed = 15

        font_style = pygame.font.SysFont("bahnschrift", 25)
        score_font = pygame.font.SysFont("comicsansms", 35)


        def Your_score(score):
            value = score_font.render("Your Score: " + str(score), True, yellow)
            dis.blit(value, [0, 0])



        def our_snake(snake_block, snake_list):
            for x in snake_list:
                pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


        def message(msg, color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [dis_width / 6, dis_height / 3])


        def gameLoop():
            game_over = False
            game_close = False

            x1 = dis_width / 2
            y1 = dis_height / 2

            x1_change = 0
            y1_change = 0

            snake_List = []
            Length_of_snake = 1

            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            while not game_over:
            
                while game_close == True:
                    dis.fill(blue)
                    message("It was an good try Press C-Replay Q-quit",black)
                    Your_score(Length_of_snake - 1)
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False
                            if event.key == pygame.K_c:
                                gameLoop()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0

                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                dis.fill(blue)
                pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]

                for x in snake_List[:-1]:
                    if x == snake_Head:
                        print()

                our_snake(snake_block, snake_List)
                Your_score(Length_of_snake - 1)

                pygame.display.update()

                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 2

                clock.tick(snake_speed)

            pygame.quit()
            quit()


        gameLoop()        
    elif choise==6:
        webbrowser.open('https://www.youtube.com/results?search_query=best+songs+hindi')
        webbrowser.open('https://www.youtube.com/results?search_query=latest+hindi+songs')
        webbrowser.open('https://www.youtube.com/results?search_query=hit+songs+hindi+latest')
        exit()
     
if __name__ =="__main__":
    clear = lambda: os.system('cls')
    clear()
    wishMe(' Sir')
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            wikipedia_search(query)
        elif "search for" in query and "in dictionary" in query:
            query=query.replace("search for","")
            query=query.replace("in dictionary","")
            print("Searching!!!")
            speak("Searching dictionary")
            dict_fir="https://www.dictionary.com/browse/"
            dict_link=dict_fir+query
            webbrowser.open(dict_link)
            exit()
        elif "search for" in query and "on dictionary" in query:
            query=query.replace("search for","")
            query=query.replace("on dictionary","")
            print("Searching!!!")
            speak("Searching dictionary")
            dict_fir="https://www.dictionary.com/browse/"
            dict_link=dict_fir+query
            webbrowser.open(dict_link)
            exit()
        elif "search" in query and "on dictionary" in query:
            query=query.replace("search","")
            query=query.replace("on dictionary","")
            print("Searching!!!")
            speak("Searching dictionary")
            dict_fir="https://www.dictionary.com/browse/"
            dict_link=dict_fir+query
            webbrowser.open(dict_link)
            exit()
        elif "search" in query and "in dictionary" in query:
            query=query.replace("search","")
            query=query.replace("in dictionary","")
            print("Searching!!!")
            speak("Searching dictionary")
            dict_fir="https://www.dictionary.com/browse/"
            dict_link=dict_fir+query
            webbrowser.open(dict_link)
            exit()
        elif "dictionary" in query or "in dictionary" in query or "on dictionary" in query or "what is the meaning of" in query or "please tell the meaning of " in query:
            query=query.replace("on dictionary","")
            query=query.replace("dictionary","")
            query=query.replace("what is the meaning of","")
            query=query.replace("in dictionary","")
            query=query.replace("please tell the meaning of ","")
            print("Searching!!!")
            speak("Searching dictionary")
            dict_fir="https://www.dictionary.com/browse/"
            dict_link=dict_fir+query
            webbrowser.open(dict_link)
            exit()
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            exit()
        elif "open amazon" in query:
            print("opening")
            speak("opening")
            webbrowser.open('https://www.amazon.in/')
            exit()
        elif "open flipkart" in query:
            print("Opening")
            speak("opening")
            webbrowser.open("https://www.flipkart.com/")
            exit()
        elif("amazon cart") in query or ("amazon card") in query:
            print("opening")
            speak('opening')
            webbrowser.open("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
            exit()
        elif("filpkart cart") in query or ("flipkart card") in query:
            print("Opening")
            speak("opening")
            webbrowser.open("https://www.flipkart.com/viewcart?otracker=Cart_Icon_Click")
            exit()
        elif "send whatsapp message" in query:
            message()
            clear()
            exit()
        elif "search" in query and "on amazon" in query:
            query=query.replace("search","")
            query=query.replace("on amazon","")
            query=query.replace("for","")
            amfir="https://www.amazon.in/s?k="
            amlas="&ref=nb_sb_noss_2"
            amlink=amfir+query+amlas
            webbrowser.open(amlink)
            exit()
        elif "search" in query and "on flipkart" in query:
            query=query.replace("search","")
            query=query.replace("on","")
            query=query.replace("flipkart","")
            item1="searching"+query
            print(item1)
            speak(item1)
            fkfir="https://www.flipkart.com/search?q="
            fklas="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
            fklink=fkfir+query+fklas
            webbrowser.open(fklink)
        elif 'itutor' in query:
            print("Opening I tutor. Happy Studys")
            speak("opening I tutor. Happy study")
            webbrowser.open("https://learn.aakashitutor.com/subject/details?cat_id=2726")
            exit()
        elif 'open youtube' in  query:
            print("Opening Youtube")
            speak("Opening Youtube")
            webbrowser.open('www.youtube.com')
            exit()
        elif 'open google' in query:
            print("Opening Google")
            speak("opening google")
            webbrowser.open('www.google.com')
            exit()
        elif 'Meet' in query:
            print("Opening Google Meet")
            speak("opening google Meet")
            webbrowser.open('meet.google.com')
            exit()
        elif 'Classroom' in query:
            print("Opening Google classroom")
            speak("opening google classroom")
            webbrowser.open('meet.google.com')
            exit()
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")   
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif 'exit' in query or 'bye' in query:
            speak("Thanks for giving me your time")
            clear()
            exit()
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow. Happy coding")
            webbrowser.open("stackoverflow.com") 
            exit()
        elif "search"in query or 'song'in query or 'play' in query or 'youtube' in query:
            query=query.replace("search","",10)
            query=query.replace("youtube","",10)
            query=query.replace("play","",10)
            query=query.replace("song","",10)
            query=query.replace("on","")
            query=query.replace("for","")
            print("Searching")
            speak("Searching")
            First=("https://www.youtube.com/results?search_query=")
            link=First+query
            webbrowser.open(link)
            exit()
        elif "who am i" in query:
            print("If you talk then definitely your human.")
            speak("If you talk then definitely your human.")
        elif "why you came to world" in query:
            print("Thanks to Aayansh. further It's a secret")
            speak("Thanks to Aayansh. further It's a secret")
        elif 'is love' in query:
            print("It is 7th sense that destroy all other senses")
            speak("It is 7th sense that destroy all other senses")
        elif "who are you" in query:
            print("I am your virtual assistant created by Aayansh")
            speak("I am your virtual assistant created by Aayansh")
        elif 'reason for you' in query:
            print("I was created as a Major project made by Aayansh ")
            speak("I was created as a Major project made by Aayansh ")
        elif 'clear' in query:
            speak("Everything is getting cleared")
            clear()
        elif"hello" in query:
            Hello="Hello How can I help you sir"
            print(Hello)
            speak(Hello)
        elif "assistant" in query:
            print("Assistant 1 point o in your service Mister ")
            speak("Assistant 1 point o in your service Mister ")
        elif 'joke' in query:
            joke=(pyjokes.get_joke())
            print(joke)
            speak(joke)
        elif 'you are mad' in query:
            Ans1=[
                  "Let me tell you what little Alice said to the Mad Hatter, “ You’re entirely bonkers. But I’ll tell you a secret. All the best people are.",
                  "Sir I am really sorry to make you feel bad But I will take care from next time",
                  "I think being mad is not bad till the time we are not doing bad" ]
            Ans1a= random.choice(Ans1)
            print(Ans1a)
            speak(Ans1a)
        elif "start calculator" in query:
            calculator()
        elif "would you like to meet" in query:
            query=query.replace("would you like to meet","")
            print("Yes why not sir. I would be happy to meet her")
            speak("Yes why not sir. I would be happy to meet her")
            wishMe(query)
            print("It was nice to meet you")
            speak("It was nice to meet you")
        elif "electricity rate" in query:
            clear()
            I=0
            while I!=1:
                a=int(input("enter the watt of the appliance \n:"))
                c=a/136.40776699
                print("The bill of this item per hour will be: ",c,"Rs")
                d=c*24
                print("The bill of this item per day will be:  ",d,"Rs")
                e=d*30
                print("The bill of this item per month will be:",e,"Rs")
                f=e*12
                print("The bill of this item per year will be: ",f,"Rs")
                z=input("To re run the program press R and to end press E ")
                clear()
                z.lower()
                if z=="r":
                    I=0
                elif z=="e":
                    I=1
        elif "i am bored" in query:
            print("There are many things to keep your boredom sideway")
            speak("There are many things to keep your boredom sideway")
            print('1-Talk with me')
            print('2-Play Dino game')
            print('3-Play flappy bird')
            print('4-play car racing game')
            print('5-play snake game')
            print('6-listen songs on youtube')
            print("Please tell Your choise")
            speak("Please tell your choise")
            choise=int(input())
            boredome(choise)
        elif "weather" in query:
            webbrowser.open('https://www.google.com/search?q=weather&rlz=1C1CHBF_enIN958IN958&oq=weather&aqs=chrome..69i57j0i131i433i512j0i131i433i457i512j0i402l2j0i131i433i512j0i512j0i131i433i512l2j0i433i512.1540j1j7&sourceid=chrome&ie=UTF-8')
            exit()
        elif "news" in query:
            webbrowser.open('https://www.aajtak.in/')
            exit()
        elif "i am hungry" in query or "order something to eat" in query:
            print("You can order something")
            speak("You can order something")
            webbrowser.open('https://www.zomato.com/kanpur')
        elif "what do you eat" in query:
            print("I eat information and I give it to you")
            speak("I eat information and I give it to you")
        elif "do you go to washroom" in query:
            print("I do but aati nahi")
            speak("I do but aati nahi")
        elif "what can you do" in query:
            whatcanyoudo=["1-I can search for you on Wikipedia",
                          "2-I can search words in dictionary",
                          "3-I can search on youtube",
                          "4-I can search on Amazon and flipkart",
                          "5-I can open websites",
                          "6-I can tell the time",
                          "7-I can talk with you",
                          "8-I can start calculator",
                          "9-You can tell me if you are bored",
                          "10-I can tell you jokes",
                          "11-I can tell you the weather ",
                          "12-I can tell you the news"]
            print(whatcanyoudo[0])            
            print(whatcanyoudo[1])
            print(whatcanyoudo[2])
            print(whatcanyoudo[3])
            print(whatcanyoudo[4])
            print(whatcanyoudo[5])
            print(whatcanyoudo[6])
            print(whatcanyoudo[7])
            print(whatcanyoudo[8])
            print(whatcanyoudo[9])
            print(whatcanyoudo[10])
            print(whatcanyoudo[11])            
            speak(whatcanyoudo[0])            
            speak(whatcanyoudo[1])
            speak(whatcanyoudo[2])
            speak(whatcanyoudo[3])
            speak(whatcanyoudo[4])
            speak(whatcanyoudo[5])
            speak(whatcanyoudo[6])
            speak(whatcanyoudo[7])
            speak(whatcanyoudo[8])
            speak(whatcanyoudo[9])
            speak(whatcanyoudo[10])
            speak(whatcanyoudo[11])      
        elif "What is your Family" in query:
            print("My family is Aayansh")     
            speak("My family is Aayansh")
        elif "where do you live" in query:
            print("I live in the server")
            speak("I live in the server")
        elif "Tell my internet speed" in query:
            webbrowser.open
        else:   
            print("I was not able to understand")
            speak("I was not able to understand")
            clear()
else:
    print("This program is being called from another file")
