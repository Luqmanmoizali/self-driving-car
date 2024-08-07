import sys
import serial
import pygame
from skimage import io
import cv2
import numpy as np

global url, fnum, bnum, rnum, lnum, snum
fnum = 0
snum = 0
bnum = 0
rnum = 0
lnum = 0
znum = 0
gnum = 0
pnum = 0

url = "http://192.168.0.103:8080/shot.jpg"
com_port = "COM3"
baud_rate = 9600
s = serial.Serial(com_port, baud_rate)

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Self Driving Car")

running = True
clock = pygame.time.Clock()
while running:

    img = io.imread(url)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    scale_percent = 40  
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    
    img_surface = pygame.surfarray.make_surface(np.rot90(resized_img))

   
    screen.blit(img_surface, (0, 0))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                img = io.imread(url)
                io.imsave(f'Images/redlight_{znum}.jpg', img)
                znum += 1
                print("Red Light")
            elif event.key == pygame.K_g:
                img = io.imread(url)
                io.imsave(f'Images/greenlight_{gnum}.jpg', img)
                gnum += 1
                print("Green Light")
            elif event.key == pygame.K_p:
                img = io.imread(url)
                io.imsave(f'Images/stopsign_{pnum}.jpg', img)
                pnum += 1
                print("Stop Sign")
            elif event.key == pygame.K_UP:
                s.write(b'f')
                img = io.imread(url)
                io.imsave(f'Images/forward_{fnum}.jpg', img)
                fnum += 1
                print("Forward")
            elif event.key == pygame.K_LEFT:
                s.write(b'l')
                img = io.imread(url)
                io.imsave(f'Images/left_{lnum}.jpg', img)
                lnum += 1
                print("Left")
            elif event.key == pygame.K_RIGHT:
                s.write(b'r')
                img = io.imread(url)
                io.imsave(f'Images/right_{rnum}.jpg', img)
                rnum += 1
                print("Right")
            elif event.key == pygame.K_DOWN:
                s.write(b'b')
                img = io.imread(url)
                io.imsave(f'Images/backward_{bnum}.jpg', img)
                bnum += 1
                print("Backward")
            elif event.key == pygame.K_s:
                s.write(b's')
                img = io.imread(url)
                io.imsave(f'Images/stop_{snum}.jpg', img)
                snum += 1
                print("Stop")
            elif event.key == pygame.K_q:  
                running = False

    pygame.display.flip()
cv2.destroyAllWindows()
pygame.quit()
s.close()
sys.exit()
