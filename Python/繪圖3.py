#設計者：Lydia Lai

#創作理念：
#版本：1.0
#創作日期：2018/12/14
#授權方式：姓名標示─非商業性─相同方式分享 (http://creativecommons.tw/explore)



#-------START HERE---------------#
from turtle import *



#-------DEFINE FUNCIOTN----------#
def star(m,n):
  for i in range(7):
    lt(36)
    fd(m)
    lt(79)
    fd(n)
    lt(132)
    fd(n)
    lt(79)
    fd(m)
    rt(18)



def jump(x,y):
  pu()
  goto(x,y)
  pd()










#-------MAIN TASK----------------#
speed(0)

#-------START DRAWING------------#

star(25,40)








#-------END DRAWING--------------#

hideturtle()
done()