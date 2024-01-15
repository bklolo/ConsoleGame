import pygame
import os

class Controller:
    
    def __init__(self, spriteSheet, startPosition, speed, world_width, world_height):
        #size
        self.width = 16
        self.height = 16
        self.world_width = world_width
        self.world_height = world_height
        
        #movement
        self.world_position = startPosition
        self.speed = speed
        self.currentSpeed = 0
        
        self.direction = 0,0
        self.isPressed_left = False
        self.isPressed_right = False
        self.isPressed_up = False
        self.isPressed_down = False

        #Sprite sheet splits
        self.spriteSheet = spriteSheet
        self.spriteSheet_down = [spriteSheet[0],spriteSheet[1]]
        self.spriteSheet_left = [spriteSheet[2],spriteSheet[3]]
        self.spriteSheet_up = [spriteSheet[4], spriteSheet[5]]
        self.spriteSheet_right = [spriteSheet[6],spriteSheet[7]]

        #Animation 
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
            screen.blit(self.spriteSheet_down[0], self.world_position)
        elif self.direction == (-1,0):
            if(self.currentSpeed > 0):
                screen.blit(self.spriteSheet_left[self.count%2], self.world_position)
            else:
                screen.blit(self.spriteSheet_left[0], self.world_position)
        elif self.direction == (1,0):
            if(self.currentSpeed > 0):
                screen.blit(self.spriteSheet_right[self.count%2], self.world_position)
            else:
                screen.blit(self.spriteSheet_right[0], self.world_position)
        elif self.direction == (0, -1):
            if(self.currentSpeed > 0):
                screen.blit(self.spriteSheet_up[self.count%2], self.world_position)
            else:
                screen.blit(self.spriteSheet_up[0], self.world_position)
        elif self.direction == (0,1):
            if(self.currentSpeed > 0):
                screen.blit(self.spriteSheet_down[self.count%2], self.world_position)
            else:
                screen.blit(self.spriteSheet_down[0], self.world_position)
        
    def Move(self):
        #Check if any of the movement keys are currently down. If they are move, else don't. 
        if self.isPressed_left or self.isPressed_right or self.isPressed_up or self.isPressed_down:
            self.currentSpeed = self.speed
        else:
            self.currentSpeed = 0

        #Move character by current speed amount TODO:Delta time?
        x,y = self.world_position
        x = self.clamp(x + (self.currentSpeed * self.direction[0]), 0, self.world_width - self.width)         
        y = self.clamp(y + (self.currentSpeed * self.direction[1]), 0, self.world_height - self.height)    
        self.world_position = x,y      
                    
    def GetInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); os.sys.exit()
                main = False
            
            if event.type == pygame.KEYDOWN:
                x,y = self.direction
                
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    x = -1;y = 0
                    self.isPressed_left = True
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x = 1;y = 0
                    self.isPressed_right =True
                if event.key == pygame.K_UP or event.key == ord('w'):
                    x = 0;y = -1
                    self.isPressed_up =True
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    x = 0;y = 1
                    self.isPressed_down =True
                self.direction = x,y

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                   self.isPressed_left = False 
                   self.checkDirection()
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.isPressed_right = False
                    self.checkDirection()
                if event.key == pygame.K_UP or event.key == ord('w'):
                    self.isPressed_up = False
                    self.checkDirection()
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                   self.isPressed_down = False
                   self.checkDirection()
    
    #Only use when a direction key is released
    #checks to see if any other direction keys are currently pressed down
    #if they are the character is reoriented to that direction
    def checkDirection(self):
        x,y = self.direction
        if self.isPressed_left:
            x = -1;y = 0
        elif self.isPressed_right:
            x = 1;y = 0
        elif self.isPressed_up:
            x = 0;y = -1
        elif self.isPressed_down:
            x = 0;y = 1
        self.direction = x,y

    def clamp(self, n, min, max):
        if n < min:
            return min
        if n > max:
            return max 
        return n        