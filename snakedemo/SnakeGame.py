import random
import pygame
import sys
from pygame.locals import *
snake_speed=6 #贪吃蛇的速度
windows_width=800
windows_height=600
cell_size=20  #贪吃蛇方块的大小

#贪吃蛇有尺寸因此地图实际尺寸是相对于贪吃蛇大小尺寸而言的
map_with=int(windows_width/cell_size)
map_height=int(windows_height/cell_size)

#颜色定义
white=(255,255,255)
black=(0,0,0)
gray=(230,230,230)
dark_gray=(40,40,40)
DARKGreen=(0,155,0)
Green=(0,255,0)
Red=(255,0,0)
blue=(0,0,255)
dark_blue=(0,0,139)
BG_COLOR=black
#定义方向
UP=1
DOWN=2
LEFT=3
RIGHT=4

HEAD=0
#主函数
def main():
    pygame.init()#模块的初始化
    snake_speed_clock=pygame.time.Clock()#创建时钟对象
    screen=pygame.display.set_mode((windows_width,windows_height))
    screen.fill(white)
    pygame.display.set_caption("Python 贪吃蛇小游戏")#设置标题
    show_start_info(screen)
    while True:
        running_game(screen,snake_speed_clock)
        show_gameover_info(screen)
#游戏的主体
def running_game(screen,snake_speed_clock):
    startx=random.randint(3,map_with-8)#开始位置
    starty=random.randint(3,map_height-8)
    #初始化贪吃蛇
    snake_coords=[{'x':startx,'y':starty},
                  {'x':startx-1,'y':starty-1},
                  {'x': startx - 2, 'y': starty - 2}
    ]
    #开始是向右走的
    direction=RIGHT
    food=get_random_location()#初始化食物
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            elif event.type==KEYDOWN:
                if (event.key==K_LEFT or event.key==K_a) and direction !=RIGHT:
                    direction=LEFT
                elif (event.key==K_RIGHT or event.key==K_d) and direction !=LEFT:
                    direction=RIGHT
                elif (event.key==K_UP or event.key==K_w) and direction !=DOWN:
                    direction=UP
                elif (event.key==K_DOWN or event.key==K_s) and direction !=UP:
                    direction=DOWN
                elif event.key==K_ESCAPE:
                    terminate()
        move_snake(direction,snake_coords)#移动贪吃蛇
        ret=snake_is_alive(snake_coords)
        if not ret:
            break #蛇死了
        snake_is_eat_food(snake_coords,food)#判断蛇是否吃到食物
        screen.fill(BG_COLOR)
        draw_grid(screen)
        draw_snake(screen,snake_coords)
        draw_food(screen,food)
        draw_scorce(screen,len(snake_coords)-3)
        pygame.display.update()
        snake_speed_clock.tick(snake_speed)


#画食物
def draw_food(screen,food):
    x=food['x']*cell_size
    y=food['y']*cell_size
    appleRect=pygame.Rect(x,y,cell_size,cell_size)
    pygame.draw.rect(screen,Red,appleRect)
#画贪吃蛇
def draw_snake(screen,snake_coords):
    for coord in snake_coords:
        x = coord['x'] * cell_size
        y = coord['y'] * cell_size
        wormSegmentRect=pygame.Rect(x,y,cell_size,cell_size)
        pygame.draw.rect(screen,dark_blue,wormSegmentRect)
        wormInnerSegmentRect=pygame.Rect(x+4,y+4,cell_size-8,cell_size-8)
        pygame.draw.rect(screen,blue,wormInnerSegmentRect)#蛇身子里面的颜色就是蓝色


#画网格
def draw_grid(screen):
    # 水平线
    for x in range(0,windows_width,cell_size):
        pygame.draw.line(screen,dark_gray,(x,0),(x,windows_height))
    #垂直划线
    for y in range(0,windows_height,cell_size):
        pygame.draw.line(screen,dark_gray,(0,y),(windows_width,y))



#移动贪吃蛇
def move_snake(disrection,snake_coords):
    if disrection==UP:
        newHead={'x':snake_coords[HEAD]['x'],'y':snake_coords[HEAD]['y']-1}
    elif disrection==DOWN:
        newHead={'x':snake_coords[HEAD]['x'],'y':snake_coords[HEAD]['y']+1}
    elif disrection==LEFT:
        newHead={'x':snake_coords[HEAD]['x']-1,'y':snake_coords[HEAD]['y']}
    elif disrection==RIGHT:
        newHead={'x':snake_coords[HEAD]['x']+1,'y':snake_coords[HEAD]['y']}
    snake_coords.insert(0,newHead)
#判断蛇是否死了没有
def snake_is_alive(snake_coords):
    tag=True
    if snake_coords[HEAD]['x']==-1 or snake_coords[HEAD]['x']==map_with or snake_coords[HEAD]['y']==map_height:
        tag=False  #撞墙了
    for snake_body in snake_coords[1:]:
        if snake_body['x']==snake_coords[HEAD]['x'] and snake_body['y']==snake_coords[HEAD]['y']:
            tag=False #碰到自己的身体了
    return  tag
#判断贪吃蛇是否吃到食物
def snake_is_eat_food(snake_coords,food):
    if snake_coords[HEAD]['x']==food['x'] and snake_coords[HEAD]['y']==food['y']:
        food['x']=random.randint(0,map_with-1)
        food['y']=random.randint(0,map_height-1)
    else:
        del snake_coords[-1]#没有吃到食物就删除尾部一格

#食物随机生成
def get_random_location():
    return {'x':random.randint(0,map_with-1),'y':random.randint(0,map_height-1)}

#显示开机信息
def show_start_info(screen):
    font=pygame.font.Font('myfont.ttf',40)
    tip=font.render('按任意键开始游戏...',True,(65,105,225))
    gamestart=pygame.image.load('gamestart.png')
    screen.blit(gamestart,(140,30))
    screen.blit(tip,(240,550))
    pygame.display.update()
    #键盘的监听
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            elif event.type==KEYDOWN:
                if (event.key==K_ESCAPE):#终止程序
                    terminate()
                else:
                    return  #结束当前的函数

   

#结束信息
def show_gameover_info(screen):
    font = pygame.font.Font('myfont.ttf', 40)
    tip = font.render('按Q或者ESC退出游戏，任意键重新开始游戏...', True, (65, 105, 225))
    gameover = pygame.image.load('gameover.png')
    screen.blit(gameover, (60, 0))
    screen.blit(tip, (80, 300))
    pygame.display.update()
    # 键盘的监听
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_ESCAPE or event.key==K_q):  # 终止程序
                    terminate()
                else:
                    return  # 结束当前的函数

#画分数
def draw_scorce(screen,score,):
    font = pygame.font.Font('myfont.ttf', 30)
    scoreSurf=font.render('得分:%s'%score,True,Green)
    scoreRect=scoreSurf.get_rect()
    scoreRect.topleft=(windows_width-120,10)
    screen.blit(scoreSurf,scoreRect)
#终止程序
def terminate():
    pygame.quit()
    sys.exit()

main()
