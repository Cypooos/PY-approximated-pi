import pygame,math,sys,time,random

w = 800
hw = int(w/2)
pygame.init()
screen = pygame.display.set_mode((w,w))
clock = pygame.time.Clock()

class PI_generator():

    def refresh(self):
        v = 0
        for point in self.points:
            if (point[0]-hw)**2+(point[1]-hw)**2 < hw**2:
                v +=1
                pygame.draw.circle(screen,(255,255,0),(point[0],point[1]),1)
            else: pygame.draw.circle(screen,(255,255,255),(point[0],point[1]),1)
        self.value = (4*v/len(self.points))
        print(str(self.value)+" = " + str(v)+ " / "+str(len(self.points)))
    def add_point(self,nb):
        for _ in range(0,nb):
            self.points.append([random.randint(0,w),random.randint(0,w)])
        self.refresh()

    def __init__(self):
        self.value = 0
        self.points = []


Pi = PI_generator()
n = 1

screen.fill((0,0,0))
pygame.draw.circle(screen,(255,255,255),(hw,hw),hw)
pygame.draw.circle(screen,(0,0,0),(hw,hw),hw-1)
while True:


    n *=2
    Pi.add_point(n)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: pygame.quit(); sys.exit()
        if event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()




    pygame.display.flip()
