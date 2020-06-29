# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:44:04 2020

@author: noah2
"""

import pygame
import math

#Initialize pygame
pygame.init()

canvasWidth = 800
canvasHeight = 800

brushRadius = math.floor(canvasWidth/40)
originalBrushRadius = brushRadius

addition = pygame.image.load("a-plus-logo-vector-png-free-vector-plus-icon-png-560.png")
minus = pygame.image.load("6916926_preview.png")

#Create the canvas
canvas = pygame.display.set_mode((canvasWidth, canvasHeight))
canvas.fill((255, 255, 255))

class clearButton():
    def __init__(self):
        font = pygame.font.Font('freesansbold.ttf', int(round(canvasHeight * .075, 0))) 
        self.width = canvasWidth
        self.height = canvasHeight/10
        self.x_pos = 0
        self.y_pos = canvasHeight - canvasHeight/10
        self.button = pygame.draw.rect(canvas, (255, 0,0 ), (self.x_pos, self.y_pos, self.width, self.height))
        clearText = font.render("CLEAR", True, (255, 255, 255)) 
        textSizeX, textSizeY = font.size("CLEAR")
        canvas.blit(clearText, (self.button.x + (self.button.width - textSizeX)/2, self.button.y + (self.button.height - textSizeY)/2))
    def clear_clicked(self, x, y):
        if self.button.collidepoint((x, y)):
            canvas.fill((255, 255, 255))
            clearButton()
            paletteWindow()
            
        
class paletteWindow():
    def __init__(self):
        self.width = canvasWidth
        self.height = canvasHeight/5
        self.x_pos = 0
        self.y_pos = canvasHeight - canvasHeight/5 - canvasHeight/10
        #pygame.draw.rect(canvas, (255, 255, 255), (self.x_pos, self.y_pos, self.width, self.height))
        pygame.draw.rect(canvas, (0, 0, 0), (self.x_pos, self.y_pos - canvasHeight/100, self.width, canvasHeight/100))
        self.red = pygame.draw.circle(canvas, (250, 76, 60), (int(round(self.x_pos + canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/6, 0)))
        self.orange = pygame.draw.circle(canvas, (243, 156, 18), (int(round(self.x_pos + 2*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/6, 0)))
        self.yellow = pygame.draw.circle(canvas, (255, 234, 0), (int(round(self.x_pos +  3*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/6, 0)))
        self.green = pygame.draw.circle(canvas, (46, 220, 113), (int(round(self.x_pos +  4*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/6, 0)))
        self.blue = pygame.draw.circle(canvas, (52, 152, 219), (int(round(self.x_pos +  5*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/6, 0)))
        self.dblue = pygame.draw.circle(canvas, (44, 62, 80), (int(round(self.x_pos +  6*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/6, 0)))
        self.purple = pygame.draw.circle(canvas, (155, 89, 182), (int(round(self.x_pos +  7*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/6, 0)))
        self.gray = pygame.draw.circle(canvas, (189, 195, 199), (int(round(self.x_pos +  canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/6, 0)))
        self.turquoise = pygame.draw.circle(canvas, (26, 188, 175), (int(round(self.x_pos +  2*canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/6, 0)))
        self.dred = pygame.draw.circle(canvas, (180, 65, 50), (int(round(self.x_pos +  3*canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/6, 0)))
        self.pink = pygame.draw.circle(canvas, (255, 192, 203), (int(round(self.x_pos +  4*canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/6, 0)))
        self.black = pygame.draw.circle(canvas, (0, 0, 0), (int(round(self.x_pos +  5*canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/6, 0)))
        self.erase_outline = pygame.draw.circle(canvas, (0, 0, 0), (int(round(self.x_pos +  6*canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/6, 0)))
        self.erase = pygame.draw.circle(canvas, (255, 255, 255), (int(round(self.x_pos +  6*canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/7, 0)))
        add = pygame.transform.scale(addition, (originalBrushRadius * 2, originalBrushRadius * 2))
        subtract = pygame.transform.scale(minus, (int(round(originalBrushRadius * 2/1.5, 0)), originalBrushRadius * 2))
        canvas.blit(add, (math.floor(canvasWidth * 39/48), math.floor(canvasHeight * 79/96)))
        canvas.blit(subtract, (math.floor(canvasWidth * 43/48), math.floor(canvasHeight * 79/96)))
        self.add = add.get_rect()
        self.subtract = subtract.get_rect()
        self.add.x = math.floor(canvasWidth * 39/48)
        self.add.y = math.floor(canvasHeight * 79/96)
        self.subtract.x = math.floor(canvasWidth * 43/48)
        self.subtract.y = math.floor(canvasHeight * 79/96)
            
    def clear_now(self):
        pygame.draw.rect(canvas, (255, 255, 255), (self.x_pos, self.y_pos, self.width, self.height))
        
    def select_color(self, x, y):
        self.selected = None
        global brushRadius
        increment = math.ceil(originalBrushRadius/20)
        if self.yellow.collidepoint((x, y)):
            self.selected = "Yellow"
            return (255, 234, 0)
        elif self.orange.collidepoint((x, y)):
            self.selected = "Orange"
            return (243, 156, 18)
        elif self.red.collidepoint((x, y)):
            self.selected = "Red"
            return (250, 76, 60)
        elif self.green.collidepoint((x, y)):
            self.selected = "Green"
            return (46, 220, 113)
        elif self.blue.collidepoint((x, y)):
            self.selected = "Blue"
            return (52, 152, 219)
        elif self.dblue.collidepoint((x, y)):
            self.selected = "Dblue"
            return (44, 62, 80)
        elif self.purple.collidepoint((x, y)):
            self.selected = "Purple"
            return (155, 89, 182)
        elif self.gray.collidepoint((x, y)):
            self.selected = "Gray"
            return (189, 195, 199)
        elif self.turquoise.collidepoint((x, y)):
            self.selected = "Turquoise"
            return (26, 188, 175)
        elif self.dred.collidepoint((x, y)):
            self.selected = "Dred"
            return (180, 65, 50)
        elif self.pink.collidepoint((x, y)):
            self.selected = "Pink"
            return (255, 192, 203)
        elif self.black.collidepoint((x, y)):
            self.selected = "Black"
            return (0, 0, 0)
        elif self.erase_outline.collidepoint((x, y)):
            self.selected = "Erase"
            return (255, 255, 255)
        elif self.add.collidepoint((x, y)):
            if brushRadius <= 100:
                brushRadius = brushRadius + increment
            return None
        elif self.subtract.collidepoint((x, y)):
            if brushRadius > 1:
                brushRadius = brushRadius - increment
            return None
        else:
            return None
    
    def highlight_selected(self):
        if self.selected == "Red":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  1*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/5, 0)))
        if self.selected == "Orange":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  2*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/5, 0)))
        if self.selected == "Yellow":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  3*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/5, 0)))
        if self.selected == "Green":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  4*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/5, 0)))
        if self.selected == "Blue":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  5*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/5, 0)))
        if self.selected == "Dblue":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  6*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/5, 0)))
        if self.selected == "Purple":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  7*canvasWidth/8, 0)), int(round(self.y_pos + self.height/3, 0))), int(round(self.height/5, 0)))
        if self.selected == "Gray":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/5, 0)))
        if self.selected == "Turquoise":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  2 * canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/5, 0)))
        if self.selected == "Dred":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  3 * canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/5, 0)))
        if self.selected == "Pink":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos +  4 * canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/5, 0)))
        if self.selected == "Black":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos + 5 * canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/5, 0)))    
        if self.selected == "Erase":
            self.clear_now()
            pygame.draw.circle(canvas, (0, 255, 255), (int(round(self.x_pos + 6 * canvasWidth/8, 0)), int(round(self.y_pos + self.height/1.33, 0))), int(round(self.height/5, 0)))
      
        
mainClearButton = clearButton()
palette = paletteWindow()

def Brush(x, y, dragging, color):
    palette = paletteWindow()
    y_invalid = int(round(y, 0)) in range(int(round(palette.y_pos - canvasHeight/100)) - int(round(brushRadius)), canvasHeight)
    if y_invalid == False and color != None:
        pygame.draw.circle(canvas, color, (x, y), brushRadius)

run = True
dragging = False
current_color = None

while run:
    
    for event in pygame.event.get():
        #pygame.QUIT is the x button
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            mainClearButton.clear_clicked(mouse_x, mouse_y) 
            new_color = palette.select_color(mouse_x, mouse_y)
            palette.highlight_selected()
            if new_color != None:
                current_color = new_color
            brush_mark = Brush(mouse_x, mouse_y, dragging, current_color)       
            dragging = True                        
        elif event.type == pygame.MOUSEMOTION:
            if dragging == True:
                 mouse_x, mouse_y = event.pos
                 brush_mark = Brush(mouse_x, mouse_y, dragging, current_color)               
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            drawing_color = new_color
  
    #Update the display
    pygame.display.update()
    
#End Program            
pygame.quit()