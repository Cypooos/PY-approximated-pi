import pygame,math,sys,time,random

show = int(input("Montrer le graphique (1/0) (+lent ?) => "))
pre = int(input("Calculer combien de fois (présicion ?) ? => "))
v=0
points = []

def addpoints():
    global v
    for _ in range(0,100000):
        x,y = (float(random.randint(0,1000)/1000),float(random.randint(0,1000)/1000))
        points.append((x,y))
        if x**2+y**2 <1: v+=1;pygame.draw.circle(screen,(255,255,255),(int(x*w),int(y*w)),0)
        else:pygame.draw.circle(screen,(255,0,0),(int(x*w),int(y*w)),0)
    pygame.display.flip()


def addpoints_noshow():
    global v
    for _ in range(0,100000):
        x,y = (float(random.randint(0,1000)/1000),float(random.randint(0,1000)/1000))
        points.append((x,y))
        if x**2+y**2 <1: v+=1


if show == 1:
    w = 800
    hw = int(w/2)
    pygame.init()
    screen = pygame.display.set_mode((w,w))
    clock = pygame.time.Clock()
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255),(0,0),w)
    pygame.draw.circle(screen,(0,0,0),(0,0),w-1)
    for x in range(1,pre):
        addpoints()
        print(str(4*v/len(points)))
else:
    for x in range(1,pre):
        addpoints_noshow()
        print(str(4*v/len(points)))
