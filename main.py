import math
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Rabbit Game")
C = pygame.image.load("carrot.png")
pygame.display.set_icon(C)
Back = pygame.image.load("greengrass.jpeg")
Back = pygame.transform.scale(Back , (800,600))
R = pygame.image.load("rabbit.png")
R = pygame.transform.scale(R , (65,65))
Rx = 400
Ry = 300
Rxchange = 0
Rychange = 0

score = 0
lives = 3

style = pygame.font.SysFont("Dancing Script" , 30)
style2 = pygame.font.SysFont("Dancing Script" , 70)

def display():
  gift = style.render("Score: " + str(score) , True , "white")
  screen.blit(gift , (10,10))
  gift2 = style.render("Lives: " + str(lives) , True , "gray")
  screen.blit(gift2 , (700,10))


def gameover():
  gift = style2.render("GAMEOVER" , True , "yellow")
  screen.blit(gift , (200,250))
  gift = style2.render("GAMEOVER" , True , "red")
  screen.blit(gift , (203,253))
  


  
def win():
  gift = style2.render("YOU WIN!!!" , True , "#3870ff")
  screen.blit(gift , (200,250))
  gift = style2.render("YOU WIN!!!" , True , "#57e02b")
  screen.blit(gift , (203,253))
carrot = []
carrotx = []
carroty = []
c = pygame.image.load("carrot.png")
c = pygame.transform.scale(c , (65,65))
for i in range(10):
  carrot.append(c)
  carrotx.append(random.randint(0,735))
  carroty.append(random.randint(0,535))

def placecarrot(i):
  screen.blit(carrot[i] , (carrotx[i] , carroty[i]))

fox = []
foxx = []
foxy = []
foxxchange = []
foxychange = []

f = pygame.image.load("fox.png")
f = pygame.transform.scale(f , (65,65))
for i in range(6):
  fox.append(f)
  foxx.append(random.randint(0,735))
  foxy.append(random.randint(0,535))
  foxxchange.append(2)
  foxychange.append(40)

def placefox(i):
  screen.blit(fox[i] , (foxx[i] , foxy[i]))

def happy(x1 , y1 , x2 ,y2):
  d = math.sqrt( math.pow(x2 - x1 , 2) + math.pow(y2-y1 ,2 ) )
  if d < 25:
    return True
  else:
    return False 
gamestatus = True
while True:
  screen.fill("white")
  screen.blit(Back , (0,0))
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        Rxchange = 2
      if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        Rxchange = -2
      if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        Rychange = 2
      if event.key == pygame.K_w or event.key == pygame.K_UP:
        Rychange = -2
    if event.type == pygame.KEYUP:
      Rxchange = 0
      Rychange = 0
  Rx = Rx + Rxchange
  Ry = Ry + Rychange
  if Rx > 735:
    Rx = 0
  if Ry > 535:
    Ry = 0
  if Rx < 0:
    Rx = 735
  if Ry < 0:
    Ry = 535
  display()
  for i in range(10):
    placecarrot(i)
    if happy( Rx ,Ry , carrotx[i] , carroty[i]):
      if gamestatus == True:
        score = score+1
      carrotx[i] = random.randint(0,735)
      carroty[i] = random.randint(0,535)
  for i in range(5):
    placefox(i)
    if happy( Rx ,Ry , foxx[i] , foxy[i]):
      if gamestatus == True:
        lives = lives-1
      foxx[i] = random.randint(0,735)
      foxy[i] = random.randint(0,535)
    foxx[i] = foxx[i] + foxxchange[i]
    if foxx[i] > 735:
      foxy[i] = foxy[i] + foxychange[i]
      foxxchange[i] = -2
    if foxx[i] < 0:
      foxy[i] = foxy[i] + foxychange[i]
      foxxchange[i] = 2
    if foxy[i] > 535:
      foxx[i] = random.randint(0,735)
      foxy[i] = random.randint(0,400)
      
  if lives == 0:
    gameover()
    gamestatus = False
  if score == 15:
    win()
    gamestatus = False
  screen.blit(R , (Rx,Ry))
  pygame.display.update()
