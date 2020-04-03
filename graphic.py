import pygame
import time


pygame.font.init()

#color init
black=(0,0,0)
white=(255,255,255)
dark_grey=(77,77,77)
grey=(102,102,102)
red=(255,0,0)
light_grey=(128,128,128)

#variable initialization
display_height=750
display_width=1000
ar=[34,67,23,70,10,50,6,4,45,6,7,4,5,8,80]
#display init
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Sorting Algorithm')
clock=pygame.time.Clock()

def bars(array,change):

    n=len(array)
    big=max(array)
    arry=[]
    try:
        ratio=700/big
    except ZeroDivisionError:
        ratio = 1
    if n>7:
        mode=1
        w=(display_width/(n+(n+1)*0.2))
        w_gap=(w*0.2)
    else:
        w=100
        w_gap=25
    
    for i in array:
        arry.append(i*ratio)
    print(change)    

    for x in range(n):
        if x in change:
            pygame.draw.rect(screen,red,[(w_gap*(x+1))+w*x,display_height-arry[x],w,arry[x]])
        else:
            pygame.draw.rect(screen,white,[(w_gap*(x+1))+w*x,display_height-arry[x],w,arry[x]])

    pygame.display.update()





def display_loop(numbers,a):
    '''The loop governs the repeated dispaly of updates in frames'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(light_grey)

        bars(numbers,a)        

        pygame.display.update()
        clock.tick(60)

