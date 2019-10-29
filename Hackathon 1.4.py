# Proof of Concept 1.4

import pygame
import random
pygame.init()

background = pygame.image.load("Shooty Game Background.png")
p1 = pygame.image.load("Player 1.png")
e1 = pygame.image.load("Boss 1.png")

xval = 1200
yval = 700
SIZE = (1200, 700)

x1 = 150
xb1a = x1
x2 = [950,950,950]
xb2 = [x2[0],x2[1],x2[2]]
y = 500
yb1a = y
y2  = [500, 300, 700]
yb2a = [y2[0],y2[1],y2[2]]

#win = pygame.display.set_mode ((xval,yval))
win = pygame.display.set_mode(SIZE,pygame.FULLSCREEN)
pygame.display.set_caption ("Simply Fighting Game 2.0")

width = 40
height = 60 
#vel = 50
open = True
fire1a = False
fire1b = False
fire1c = False
fire1d = False

fire2a = False

p1hp = int(100)
p2hp = int(500) #default 250
spazz = int(0)
charge = int(0)

p1hit = False

enemyhit = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #list, if value is zero then not hit but if value is one then hit
enemyhp = [500,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #for the enemy, generte it's corosponding HP value

Yellow = (255,255,0)
Black = (0,0,0)
Red = (255,0,0)
Blue = (0,0,255)
White = (255, 255,255)

font = pygame.font.SysFont('comicsans', 30, True)

run = True
while run:
    #win.blit (background, (0, 0))  
    #pygame.time.delay (1)
    
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False
     
    keys = pygame.key.get_pressed()
    
    if charge <= 0:
        charge = 0
    
    # Player 1 Controls
    if keys [pygame.K_a]: 
                x1 -= 5
                if p1hp <= 25:
                    x1 -= 5
    
    if keys [pygame.K_s]: 
            y += 5  
            if p1hp <= 25:
                y += 5            
            
    if keys [pygame.K_w]: 
                y -= 5  
                if p1hp <= 25:
                    y -= 5                
    
    if keys [pygame.K_d]: 
                x1 += 5 
                if p1hp <= 25:
                    x1 += 5                
    
    if keys [pygame.K_DOWN] and fire1d == False and fire1a == False and fire1b == False and fire1c == False:
        fire1d = True 
        #fire1a = False
        #fire1b = False
        #fire1c = False        
        #pygame.draw.circle(win, Red, (x1, y + 50), 25)
    if keys [pygame.K_LEFT] and fire1d == False and fire1a == False and fire1b == False and fire1c == False:
        fire1c = True 
        fire1a = False
        fire1b = False
        fire1d = False        
        #pygame.draw.circle(win, Red, (x1 - 50, y), 25)
    if keys [pygame.K_UP] and fire1d == False and fire1a == False and fire1b == False and fire1c == False:
        fire1b = True 
        fire1a = False
        fire1d = False
        fire1c = False        
        #pygame.draw.circle(win, Red, (x1, y - 50), 25)
    if keys [pygame.K_RIGHT] and fire1d == False and fire1a == False and fire1b == False and fire1c == False:
        fire1a = True
        fire1d = False
        fire1b = False
        fire1c = False        
        #pygame.draw.circle(win, Red, (x1 + 50, y), 25)
    
    if keys [pygame.K_x]:        
        #if keys [pygame.K_DOWN]:
            #fire1d = True 
        #if keys [pygame.K_LEFT]:
            #fire1c = True 
        #if keys [pygame.K_UP]:
            #fire1b = True 
        if keys [pygame.K_RIGHT]:
            fire1a = True
        else:
            if charge <= 100:
                charge += 1
            #fire1a = True 

    # Alternate fire button
    #if keys [pygame.K_x]: 
        #fire1a = True
        
    # Player 2 Controls 
    if x1 <= x2[0] : 
        x2[0]  -= 1    
      
    if x1 >= x2[0] : 
        x2[0]  += 1 
        
    if x1 <= x2[1] : 
        x2[1]  += 1    

    if x1 >= x2[1] : 
        x2[1]  -= 1 
        
    if x1 <= x2[2] : 
        x2[2]  -= 1    

    if x1 >= x2[2] : 
        x2[2]  += 1 
        
        
    if y <= y2[0] :
        y2[0]  -= 1
            
    if y >= y2[0] :
        y2[0]  += 1  
        
    if y <= y2[1] :
        y2[1] += 1

    if y >= y2[1] :
        y2[1] -= 1 
        
    if y <= y2[2] :
        y2[2]  -= 1

    if y >= y2[2] :
        y2[2]  -= 1  
        
    fire2a = True
            
# Collision Detection    
    if x1 <= 0:
        x1 = 0
         
    if x2[0]  <= 0:
        x2[0]  = 0   
        
    if x2[1]  <= 0:
        x2[1]  = 0   
        
    if x2[2]  <= 0:
        x2[2]  = 0   
        
    if y <= 0:
        y = 0    
        
    if y2[0]  <= 0:
        y2[0]  = 0
    
    if y2[1]  <= 0:
        y2[1]  = 0
    
    if y2[2]  <= 0:
        y2[2]  = 0
    
    if x1 >= xval:
        x1 = xval

    if x2[0]  >= xval:
        x2[0]  = xval   

    if y >= yval:
        y = yval    

    if y2[0]  > yval:
        y2[0]  = yval
        
    if y2[1]  > yval:
        y2[1]  = yval
        
    if y2[2]  > yval:
        y2[2]  = yval
    
    #Damage    
    if x1 + 25 >= xb2[0] and x1 - 25 <= xb2[0] and y + 25 >= yb2a[0]  and y - 25 <= yb2a[0] :
        #hp1 -= 1
        p1hit = True
        
    if x1 + 25 >= xb2[1] and x1 - 25 <= xb2[1] and y + 25 >= yb2a[1]  and y - 25 <= yb2a[1] :
        #hp1 -= 1
        p1hit = True
        
    if x1 + 25 >= xb2[2] and x1 - 25 <= xb2[2] and y + 25 >= yb2a[2]  and y - 25 <= yb2a[2] :
        #hp1 -= 1
        p1hit = True
        
    if xb1a + 25 >= x2[0]  and xb1a - 25 <= x2[0]  and yb1a + 25 >= y2[0]  and yb1a - 25 <= y2[0] :
        charge -= 5
    
    # Enemy Damage
    
    if x2[0]  + 150 >= xb1a + 25 - charge and x2[0]  - 150 <= xb1a - 25 + charge and y2[0]  + 150 >= yb1a + 25 - charge and y2[0]  - 150 <= yb1a - 25 + charge:
        #hp1 -= 1
        enemyhit[0] = 1  
        
    if x2[1]  + 150 >= xb1a + 25 - charge and x2[1]  - 150 <= xb1a - 25 + charge and y2[1]  + 150 >= yb1a + 25 - charge and y2[1]  - 150 <= yb1a - 25 + charge:
        #hp1 -= 1
        enemyhit[0] = 1  
        
    if x2[2]  + 150 >= xb1a + 25 - charge and x2[2]  - 150 <= xb1a - 25 + charge and y2[2]  + 150 >= yb1a + 25 - charge and y2[2]  - 150 <= yb1a - 25 + charge:
        #hp1 -= 1
        enemyhit[0] = 1  
    
    win.fill ((0,0,0))
    
    #win.blit (p1, (x1, y))
    #surf = pygame.transform.scale (p1, (50, 50))
    #win.blit(surf, (x1 - 25, y -25))
    
    #pygame.draw.rect(win, (255,0,0), (x1,y,width,height))
         
    # Blasts and Players    
    
    if fire1a == True or fire1b == True or fire1c == True or fire1d == True:
        #if fire1a == True:
            #pygame.draw.circle(win, Red, (x1 + 50, y), 25)
            #xb1a += 5
            #if p1hp <= 25:
                #xb1a += 5            
        
        if fire1b == True:
            pygame.draw.circle(win, Red, (x1, y - 50), 25)
            yb1a -= 5 
            if p1hp <= 25:
                yb1a -= 5
                    
        if fire1c == True:
            pygame.draw.circle(win, Red, (x1 - 50, y), 25)
            xb1a -= 5
            if p1hp <= 25:
                xb1a -= 5            
    
        if fire1d == True:
            pygame.draw.circle(win, Red, (x1, y + 50), 25)
            #fire1c = False
            yb1a += 5 
            if p1hp <= 25:
                yb1a += 5
        
        if fire1a == True:
            pygame.draw.circle(win, Red, (x1 + 50, y), 25)
            xb1a += 5
            if p1hp <= 25:
                xb1a += 5            

    else:
        xb1a = x1
        yb1a = y

    if fire2a == True:
        if x2[0]  <= x1:
            xb2[0] += 5
        if x2[0]  >= x1:
            xb2[0] -= 5 
        if x2[1]  <= x1:
            xb2[1] += 5
        if x2[1]  >= x1:
            xb2[1] -= 5 
        if x2[2]  <= x1:
            xb2[2] += 5
        if x2[2]  >= x1:
            xb2[2] -= 5 
    else:
        xb2[0] = x2[0] 
        yb2a[0]  = y2[0] 
        
    if xb2[0] > 1200:
        xb2[0] = x2[0] 
        yb2a[0]  = y2[0] 
        fire2a = False  
        
    if xb2[0] < 0:
        xb2[0] = x2[0] 
        yb2a[0]  = y2[0] 
        fire2a = False 
        
    if xb2[0] > 1200:
        xb2[0] = x2[0] 
        yb2a[0]  = y2[0] 
        fire2a = False  
        
    if xb2[0] < 0:
        xb2[0] = x2[0] 
        yb2a[0]  = y2[0] 
        fire2a = False 
        
    if xb2[1] > 1200:
        xb2[1] = x2[1] 
        yb2a[1]  = y2[1] 
        fire2a = False  
        
    if xb2[2] < 0:
        xb2[2] = x2[2] 
        yb2a[2]  = y2[2] 
        fire2a = False 
        
    if xb1a == xb2[0] and yb1a == yb2a[0] :
        fire1a = False
        fire1b = False
        fire1c = False
        fire1d = False  
        
        fire2a = False

        
    # Blasts
    pygame.draw.circle(win, Red, (xb1a, yb1a), 25 + charge)    
    #if xb1a != x1 and yb1a != y:
        #pygame.draw.circle(win, Red, (xb1a, yb1a), 25) 
    if xb2[0] != x2[0] :
        pygame.draw.circle(win, Blue, (xb2[0], yb2a[0] ), 25) 
        pygame.draw.circle(win, Blue, (xb2[1], yb2a[1] ), 25) 
        pygame.draw.circle(win, Blue, (xb2[2], yb2a[2] ), 25) 
      
    # Player 1 and 2   
    if open == True:
        surf = pygame.transform.scale (p1, (50, 50))
        surf2 = pygame.transform.scale (e1, (250, 250))
        win.blit(surf, (x1 - 25, y -25))    
        win.blit(surf2, (x2[0]  - 125, y2[0]  - 125)) 
        win.blit(surf2, (x2[1]  - 125, y2[1]  - 125)) 
        win.blit(surf2, (x2[2]  - 125, y2[2]  - 125)) 
        #surf = pygame.transform.scale (p1, (p1hp, p1hp))
        #pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 250)
        #open = False           
    else:
        surf = pygame.transform.scale (p1, (50, 50))
        win.blit(surf, (x1 - 25, y -25))        
        #pygame.draw.circle(win, Red, (x1, y), p1hp)
        #pygame.draw.circle(win, Black, (x1, y), 25)
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 150)               
        
    if p1hit == True:
        p1hp -= 1
    
    if enemyhit[0] == 1:
        enemyhp[0] -= 1
    
    p1hit = False
    enemyhit[0] = 0
            
    # Health
    text = font.render('Health 1: ' + str(p1hp), 1, (255,0,0))  
    win.blit (text, (300, 10))
    
    text = font.render('Health 2: ' + str(enemyhp[0]), 1, (0,0,255))  
    win.blit (text, (700, 10)) 
    
    #if fire1a == False and fire1b == False and fire1c == False and fire1d == False:
        #xb1a = x1
        #yb1a = y        
        
    if xb1a > 1200:
        xb1a = x1
        yb1a = y
        fire1a = False
        fire1b = False
        fire1c = False
        fire1d = False  
        charge = 0
    
    if xb1a < 0:
        xb1a = x1
        yb1a = y        
        fire1a = False
        fire1b = False
        fire1c = False
        fire1d = False  
        charge = 0
        
    if yb1a > 700:
        xb1a = x1
        yb1a = y
        fire1a = False
        fire1b = False
        fire1c = False
        fire1d = False 
        charge = 0
    
    if yb1a < 0:
        xb1a = x1
        yb1a = y        
        fire1a = False
        fire1b = False
        fire1c = False
        fire1d = False
        charge = 0    
    
    pygame.display.update()
    
    if p1hp <= 0 and enemyhp[0] > 0:
        #draw explosion at the coordinates of player 1
        pygame.draw.circle(win, Red, (x1, y), 75)  
        pygame.display.update()        
        pygame.time.delay (10)  
        pygame.draw.circle(win, Red, (x1, y), 100)
        pygame.display.update()        
        pygame.time.delay (10)         
        pygame.draw.circle(win, Red, (x1, y), 150) 
        pygame.display.update()        
        pygame.time.delay (10)         
        pygame.draw.circle(win, Red, (x1, y), 250)   
        pygame.display.update()        
        pygame.time.delay (10)         
        pygame.draw.circle(win, Red, (x1, y), 450)      
        pygame.display.update()        
        pygame.time.delay (10)          
        text = font.render('Player 2 wins', 1, (0,0,255))  
        win.blit (text, (525, 300))        
        pygame.display.update()        
        pygame.time.delay (150)               
        break
    
    if enemyhp[0] <= 0 and p1hp > 0:
        
        #draw explosion at the coordinates of player 
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 75)        
        pygame.display.update()        
        pygame.time.delay (10) 
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 10)        
        pygame.display.update()        
        pygame.time.delay (10)     
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 150)        
        pygame.display.update()        
        pygame.time.delay (10)     
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 250)   
        pygame.display.update()        
        pygame.time.delay (10)     
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 450)   
        pygame.display.update()        
        pygame.time.delay (10)          
        text = font.render('Player 1 wins', 1, (255,0,0))  
        win.blit (text, (525, 300))        
        pygame.display.update()        
        pygame.time.delay (150)             
        break
        
    #if p2hp <= 0:
        #run = false  
    
    if enemyhp[0] <= 0 and p1hp <= 0:      
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 75)        
        pygame.display.update()        
        pygame.time.delay (10) 
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 10)        
        pygame.display.update()        
        pygame.time.delay (10)     
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 150)        
        pygame.display.update()        
        pygame.time.delay (10)     
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 250)   
        pygame.display.update()        
        pygame.time.delay (10)     
        pygame.draw.circle(win, Blue, (x2[0] , y2[0] ), 450)   
        pygame.display.update()        
        pygame.time.delay (10) 
        pygame.draw.circle(win, Red, (x1, y), 75)  
        pygame.display.update()        
        pygame.time.delay (10)  
        pygame.draw.circle(win, Red, (x1, y), 100)
        pygame.display.update()        
        pygame.time.delay (10)         
        pygame.draw.circle(win, Red, (x1, y), 150) 
        pygame.display.update()        
        pygame.time.delay (10)         
        pygame.draw.circle(win, Red, (x1, y), 250)   
        pygame.display.update()        
        pygame.time.delay (10)         
        pygame.draw.circle(win, Red, (x1, y), 450)      
        pygame.display.update()        
        pygame.time.delay (10)    
        text = font.render('Tie', 1, (0,0,255))  
        win.blit (text, (525, 300))        
        pygame.display.update()        
        pygame.time.delay (150)               
        break        
   
   # Kill switch
    if keys [pygame.K_SPACE]: 
        break
    
    #win.fill ((0,0,0))
    #win.blit (background, (0, 0))  

pygame.time.delay (50)        
pygame.quit ()

# Add this Version:
#Better Hitboxes
#Multiple enemies
#Graphics to scale with screen (as percentages/ fractions)
#variable efficiency
#shots cancel out