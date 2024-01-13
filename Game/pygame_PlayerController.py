import pygame
import os

class pygame_PlayerController:
    
    def __init__(self, spriteSheet, position, speed):
        self.spriteSheet = spriteSheet
        self.position = position
        self.speed = speed
        self.direction = 0,0
        pass

    def clamp(self, n, min, max):
        if n < min:
            return min
        if n > max:
            return max 
        return n 

    def update(self):
        self.GetInput()
        self.Move()

    def draw(self,screen):
        screen.blit(self.spriteSheet[0], self.position)

    def Move(self):
        x,y = self.position
        
        x = self.clamp(x + (self.speed * self.direction[0]), 0,1050)         
        y = self.clamp(y + (self.speed * self.direction[1]), 0, 700)
        
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
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x = 1
                if event.key == pygame.K_UP or event.key == ord('w'):
                    y = -1
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    y = 1
                self.direction = x,y

            if event.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                x,y = self.direction
                
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    x = 0
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x = 0
                if event.key == pygame.K_UP or event.key == ord('w'):
                    y = 0
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    y = 0
                self.direction = x,y
    
        