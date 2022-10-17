import pygame
import random
# Define some colors 
width = 700
length = 500
BLACK = (0, 0, 0)
WHITE_1 = (244,235,255)
WHITE = (152,182,155)
TREE_GREEN = (71,141,108)
TREE_GREEN_1 = (54,117,69)
WHITE_2 = (255,255,232)
YELLOW = (205,195,162)
GREEN = (40, 51, 44)
DARKGREEN = (26, 37, 31)
DARKERGREEN = (17, 24, 20)
NAVY = (15, 55, 90)
STAR = (255, 255, 144)
BLUE = (153,204,255)
PI = 3.141592653
star_size = 5
star_pos = [random.randrange(0, width-star_size), random.randrange(0, length/2)]
star_list = [star_pos]
star_x = 60
star_y = 8
star_change_x = 5
star_change_y = 2
moon_x = 90
moon_y = 80
pygame.init()
# Set the width and height of the screen [width, height]
size = (width, length)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Night")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done: 
  # --- Main event loop
   rain_xpos = random.randrange(0, width)
   rain_xpos_1 = random.randrange(0, width)
   rain_xpos_2 = random.randrange(0, width)
   rain_ypos = random.randrange(0, length)
   rain_ypos_1 = random.randrange(0, length)
   rain_ypos_2 = random.randrange(0, length)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True
   # --- Game logic should go here
   # --- Screen-clearing code goes here
   # Here, we clear the screen to white. Don't put other drawing commands
   # above this, or they will be erased with this command.
   # If you want a background image, replace this clear with blit'ing the
   # background image.
   screen.fill(NAVY)
   # --- Drawing code should go here
  
   # Draw ellipes 
   if len(star_list) < 20:
    pos_x = float(random.randrange(0, width-star_size))
    pos_y = float(random.randrange(0, length/2))
    star_list.append([pos_x,pos_y])
  
   for star_pos in star_list:
     pygame.draw.ellipse (screen, WHITE_2, (star_pos[0],star_pos[1],star_size,star_size))

   # Draw mountains
   pygame.draw.arc(screen,BLACK,[-50, 170+125, 100, 400], 0, PI / 2,100)
   pygame.draw.arc(screen,DARKGREEN,[20, 200+125, 250, 400], 0, PI, 350)
   pygame.draw.arc(screen,GREEN,[200, 240+125, 380, 300], 0, PI, 300)
   pygame.draw.arc(screen,DARKERGREEN,[450, 210+125, 300, 400], 0, PI, 300)

   # Draw rain
   pygame.draw.rect(screen,BLUE,[rain_xpos,rain_ypos,2,8])
   pygame.draw.rect(screen,BLUE,[rain_xpos_1,rain_ypos_2,2,8])
   pygame.draw.rect(screen,BLUE,[rain_xpos_2,rain_ypos_2,2,8]) 

   # Draw trees
   x_value = 20
   y_value = 200
   pygame.draw.polygon(screen,WHITE,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,WHITE,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,WHITE,[x_value+4,length-y_value+15,2,10])
   x_value = 60
   y_value = 130
   pygame.draw.polygon(screen,TREE_GREEN_1,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,TREE_GREEN_1,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,TREE_GREEN_1,[x_value+4,length-y_value+15,2,10])
   x_value = 150
   y_value = 150
   pygame.draw.polygon(screen,WHITE,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,WHITE,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,WHITE,[x_value+4,length-y_value+15,2,10])
   x_value = 110
   y_value = 70
   pygame.draw.polygon(screen,WHITE,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,WHITE,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,WHITE,[x_value+4,length-y_value+15,2,10])
   x_value = 120
   y_value = 190
   pygame.draw.polygon(screen,TREE_GREEN,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,TREE_GREEN,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,TREE_GREEN,[x_value+4,length-y_value+15,2,10])
   x_value = 190
   y_value = 50
   pygame.draw.polygon(screen,WHITE,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,WHITE,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,WHITE,[x_value+4,length-y_value+15,2,10])
   x_value = 220
   y_value = 80  
   pygame.draw.polygon(screen,TREE_GREEN_1,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,TREE_GREEN_1,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,TREE_GREEN_1,[x_value+4,length-y_value+15,2,10])
   x_value = 450
   y_value = 120
   pygame.draw.polygon(screen,TREE_GREEN_1,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,TREE_GREEN_1,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,TREE_GREEN_1,[x_value+4,length-y_value+15,2,10])
   x_value = 320
   y_value = 130  
   pygame.draw.polygon(screen,WHITE,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,WHITE,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,WHITE,[x_value+4,length-y_value+15,2,10])
   x_value = 370
   y_value = 30
   pygame.draw.polygon(screen,WHITE,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,WHITE,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,WHITE,[x_value+4,length-y_value+15,2,10])
   x_value = 480
   y_value = 70   
   pygame.draw.polygon(screen,TREE_GREEN,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,TREE_GREEN,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,TREE_GREEN,[x_value+4,length-y_value+15,2,10])
   x_value = 650
   y_value = 100
   pygame.draw.polygon(screen,TREE_GREEN_1,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,TREE_GREEN_1,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,TREE_GREEN_1,[x_value+4,length-y_value+15,2,10])
   x_value = 570
   y_value = 40
   pygame.draw.polygon(screen,WHITE,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,WHITE,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,WHITE,[x_value+4,length-y_value+15,2,10])
   x_value = 635
   y_value = 80   
   pygame.draw.polygon(screen,WHITE,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,WHITE,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,WHITE,[x_value+4,length-y_value+15,2,10])
   x_value = 595
   y_value = 180 
   pygame.draw.polygon(screen,TREE_GREEN,([x_value,length-y_value+5],[x_value+5,length-y_value], [x_value+10,length-y_value+5]))
   pygame.draw.polygon(screen,TREE_GREEN,([x_value-(5/2),length-y_value+15],[x_value+5,length-y_value+5],[x_value+(25/2),length-y_value+15]))
   pygame.draw.rect(screen,TREE_GREEN,[x_value+4,length-y_value+15,2,10])

   # Draw a shooting star
   star_x += star_change_x 
   star_y += star_change_y 
   
   if rain_xpos >= 370 and rain_xpos <= 401:
    if rain_ypos >= 302 and rain_ypos <= 365:
     star_x += star_change_x 
     star_y += star_change_y 
     if star_x > 700:
        star_x = 0
        star_y = 0

   pygame.draw.line(screen,STAR,(star_x,star_y),(star_x+10,star_y),1)
   pygame.draw.line(screen,STAR,(star_x+12.5,star_y),(star_x+2.5,star_y+6.875),1)
   pygame.draw.line(screen,STAR,(star_x+2.5,star_y+6.875),(star_x+6.25,star_y-4),1)
   pygame.draw.line(screen,STAR,(star_x+6.25,star_y-4),(star_x+10,star_y+6.875),1)
   pygame.draw.line(screen,STAR,(star_x+10,star_y+6.875),(star_x,star_y),1)

   # Draw a moon
   pygame.draw.ellipse(screen,YELLOW,[moon_x,moon_y,70,70])
   # Draw a man
   pygame.draw.ellipse (screen,WHITE_1, [380,187+125,10,10])
   pygame.draw.polygon(screen,WHITE_1,([384,197+125],[376,230+125], [400,229+125]))
   pygame.draw.line(screen, WHITE_1, [387,230+125],[387,240+125],1 )
   pygame.draw.line(screen, WHITE_1, [390,229+125],[390,240+125],1 )
   
   # --- Go ahead and update the screen with what we've drawn.
   pygame.display.flip()
   # --- Limit to 60 frames per second
   clock.tick(14)
# Close the window and quit.
pygame.quit()
