import pygame
import time
pygame.font.init()
def outer(numbers,a):
    
    
    #color init
    black=(0,0,0)
    white=(255,255,255)
    dark_grey=(77,77,77)
    grey=(102,102,102)
    red=(255,0,0)
    lime=(51,255,51)
    light_green=(200,255,200)
    light_grey=(128,128,128)
    back=(199,209,199)

    #variable initialization
    display_height=750   
    display_width=1000

    #display init
    screen = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Sorting Algorithm')
    clock=pygame.time.Clock()
        

    def text_objects(text,font):
        textSurface = font.render(text, True, dark_grey)
        return textSurface, textSurface.get_rect()

    def bars(array,change):

        n=len(array)
        big=max(array)
        small=min(array)
        r=big
        shift=0
        if small<0:
            r=abs(small)+big
            
        arry=[]
        if n<20:
            a=1
            message_font=pygame.font.SysFont('arial.ttf',40)
        elif 19<n<50:
            a=2
            message_font=pygame.font.SysFont('arial.ttf',20)
        else:
            a=3
            message_font=pygame.font.SysFont('Arial.ttf',15)


        try:
            ratio=(display_height-50)/r
            
        except ZeroDivisionError:
            ratio = 1
        if n>6:
            w=(display_width/(n+(n+1)*0.2))
            w_gap=(w*0.2)
        else:
            w=100
            w_gap=60
        
        for i in array:
            arry.append(i*ratio)
        if small<0:
                ss=min(arry)
                shift=shift-ss+20

        for x in range(n):
            if x in change:
                pygame.draw.rect(screen,lime,[(w_gap*(x+1))+w*x,display_height-arry[x]-shift,w,arry[x]])
            else:
                pygame.draw.rect(screen,light_green,[(w_gap*(x+1))+w*x,display_height-arry[x]-shift,w,arry[x]])
            TextSurf , TextRect = text_objects(str(array[x]),message_font)
            if arry[x]>=0:
                TextRect.center=(((w_gap*(x+1))+w*x+w/2),(display_height-arry[x]-shift-20/a))
            if arry[x]<0:
                TextRect.center=(((w_gap*(x+1))+w*x+w/2),(display_height-(20/a)-shift))
            screen.blit(TextSurf,TextRect)
        pygame.display.update()
        return




    def display_loop():
        '''The loop governs the repeated dispaly of updates in frames'''

        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(back)

            bars(numbers,a)        

            pygame.display.update()
            clock.tick(60)
            time.sleep(0.1)
            return
    display_loop()

def exit():
    x=0
    

    for event in pygame.event.get():
        if event.type==pygame.Quit:
            pygame.quit()
        x+=1
        if x>1000:
            break

    time.sleep(5)
    pygame.quit()
    