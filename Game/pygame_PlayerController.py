import pygame
import os

class pygame_PlayerController:
    
    def __init__(self, spriteSheet, position, speed):
        #movement
        self.position = position
        self.speed = speed
        self.currentSpeed = 0
        self.direction = 0,0
        
        #animation
        self.spriteSheet = spriteSheet
        self.spriteSheet_down = [spriteSheet[0],spriteSheet[1]]
        self.spriteSheet_left = [spriteSheet[2],spriteSheet[3]]
        self.spriteSheet_up = [spriteSheet[4], spriteSheet[5]]
        self.spriteSheet_right = [spriteSheet[6],spriteSheet[7]]

        self.animationSpeed = 250; 
        self.timePassed = 0
        self.currentframe = spriteSheet[0]
        self.count=0
        pass

    def update(self):
        self.GetInput()
        self.Move()

    def draw(self,screen, deltaTime):
        #get time passed since last frame
        self.timePassed += deltaTime

        #increment if the time passed has been long enough to advance a frame
        if(self.timePassed>self.animationSpeed):
            self.count += 1
            self.timePassed = 0

        #initial left right up down
        if self.direction == (0,0):
            screen.blit(self.spriteSheet_down[0], self.position)
        elif self.direction == (-1,0):
            if(self.currentSpeed > 0):
                screen.blit(self.spriteSheet_left[self.count%2], self.position)
            else:
                screen.blit(self.spriteSheet_left[0], self.position)
        elif self.direction == (1,0):
            if(self.currentSpeed > 0):
                screen.blit(self.spriteSheet_right[self.count%2], self.position)
            else:
                screen.blit(self.spriteSheet_right[0], self.position)
        elif self.direction == (0, -1):
            if(self.currentSpeed > 0):
                screen.blit(self.spriteSheet_up[self.count%2], self.position)
            else:
                screen.blit(self.spriteSheet_up[0], self.position)
        elif self.direction == (0,1):
            if(self.currentSpeed > 0):
                screen.blit(self.spriteSheet_down[self.count%2], self.position)
            else:
                screen.blit(self.spriteSheet_down[0], self.position)
        
        
    def Move(self):
        x,y = self.position
        
        x = self.clamp(x + (self.currentSpeed * self.direction[0]), 0,1050)         
        y = self.clamp(y + (self.currentSpeed * self.direction[1]), 0, 700)
        
        self.position = x,y       
                    
    def GetInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); os.sys.exit()
                main = False
            
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                x,y = self.direction
                
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    x = -1
                    y = 0
                    self.currentSpeed = self.speed
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x = 1
                    y = 0
                    self.currentSpeed = self.speed
                if event.key == pygame.K_UP or event.key == ord('w'):
                    x = 0
                    y = -1
                    self.currentSpeed = self.speed
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    x = 0
                    y = 1
                    self.currentSpeed = self.speed
                self.direction = x,y

            if event.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.currentSpeed = 0
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.currentSpeed = 0
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.currentSpeed = 0
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                   self.currentSpeed = 0
    
    def clamp(self, n, min, max):
        if n < min:
            return min
        if n > max:
            return max 
        return n        