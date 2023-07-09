# import pygame library
import pygame
import random
import time
from suduko_list import bord


pygame.font.init()

screen = pygame.display.set_mode((500, 630))

pygame.display.set_caption("Its Suduko time!")
img = pygame.image.load('21.png')
pygame.display.set_icon(img)

x = 0
y = 0
dif = 500 / 9
val = 0
    
grid= random.choice(bord)

font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
def get_cord(pos):
	global x
	x = pos[0]//dif
	global y
	y = pos[1]//dif

def draw_box():
	for i in range(2):
		pygame.draw.line(screen, (255, 0, 0), (x * dif-2, (y + i)*dif), (x * dif + dif + 2, (y + i)*dif), 5)
		pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 5)

def draw():		
	for i in range (9):
		for j in range (9):
			if grid[i][j]!= 0:
				pygame.draw.rect(screen, (0, 153, 34), (i * dif, j * dif, dif + 1, dif + 1))
				text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
				screen.blit(text1, (i * dif + 15, j * dif))
		
	for i in range(10):
		if i % 3 == 0 :
			thick = 5
		else:
			thick = 2
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

    
def draw_val(val):
	text1 = font1.render(str(val), 1, (0, 0, 0))
	screen.blit(text1, (x * dif + 15, y * dif))

def raise_error1():
	text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))
def raise_error2():
	text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))


def valid(m, i, j, val):
	for it in range(9):
		if m[i][it]== val:
			return False
		if m[it][j]== val:
			return False
	it = i//3
	jt = j//3
	for i in range(it * 3, it * 3 + 3):
		for j in range (jt * 3, jt * 3 + 3):
			if m[i][j]== val:
				return False
	return True

# Backtracking Algorithm
def solve(grid, i, j):	
	while grid[i][j]!= 0:
		if i<8:
			i+= 1
		elif i == 8 and j<8:
			i = 0
			j+= 1
		elif i == 8 and j == 8:
			return True
	pygame.event.pump()

	for it in range(1, 10):
		if valid(grid, i, j, it)== True:
			grid[i][j]= it
			global x, y
			x = i
			y = j
			screen.fill((255, 255, 255))
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(20)
			if solve(grid, i, j)== 1:
				return True
			else:
				grid[i][j]= 0
			screen.fill((255, 255, 255))
		
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(50)
	return False

# instruction
def instruction():
	text1 = font2.render("PRESS R TO RESET", 1, (0, 0, 0))
	text2 = font2.render("ENTER VALUES / PRESS ENTER TO SEE MAGIC", 1, (0, 0, 0))
	screen.blit(text1, (10, 540))	
	screen.blit(text2, (10, 520))

def result():
	text1 = font1.render("FINISHED PRESS R", 1, (0, 0, 0))
	screen.blit(text1, (10, 570))

run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

while run:	
	screen.fill((255, 255, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			flag1 = 1
			pos = pygame.mouse.get_pos()
			get_cord(pos)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x-= 1
				flag1 = 1
			if event.key == pygame.K_RIGHT:
				x+= 1
				flag1 = 1
			if event.key == pygame.K_UP:
				y-= 1
				flag1 = 1
			if event.key == pygame.K_DOWN:
				y+= 1
				flag1 = 1
			if event.key == pygame.K_1:
				val = 1
			if event.key == pygame.K_2:
				val = 2
			if event.key == pygame.K_3:
				val = 3
			if event.key == pygame.K_4:
				val = 4
			if event.key == pygame.K_5:
				val = 5
			if event.key == pygame.K_6:
				val = 6
			if event.key == pygame.K_7:
				val = 7
			if event.key == pygame.K_8:
				val = 8
			if event.key == pygame.K_9:
				val = 9
			
			if event.key == pygame.K_RETURN:
				flag2 = 1

			if event.key == pygame.K_r:
				rs = 0
				error = 0
				flag2 = 0
				grid= random.choice(bord)
				
			
	if flag2 == 1:
		if solve(grid, 0, 0)== False:
			error = 1
		else:
			rs = 1
		flag2 = 0
	if val != 0:		
		draw_val(val)
		if valid(grid, int(x), int(y), val)== True:
			grid[int(x)][int(y)]= val
			flag1 = 0
		else:
			grid[int(x)][int(y)]= 0
			raise_error2()
			pygame.time.delay(500)
		val = 0
	
	if error == 1:
		raise_error1()
		pygame.time.delay(500)
	if rs == 1:
		result()	
	draw()
	if flag1 == 1:
		draw_box()	
	instruction()
	pygame.display.update()

pygame.quit()	
	
