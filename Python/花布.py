#設計者：Lydia Lai
#作品名稱：當我們相遇(When we meet)
#創作理念：BTS是我從國二開始喜歡的團體，他們也是我第一個真正去了解的團體，所以對我來說意義重大。而作品中有兩種黑色的圖案，一個是代表BTS，另一個是代表Army，而七芒星則是因為他們有七個人，希望他們能像星星一樣七個人手牽手一起走下去，少一個都不行。
#版本：1.0
#創作日期：2019/01/06
#授權方式：姓名標示─非商業性─相同方式分享 (http://creativecommons.tw/explore)


#-------START HERE---------------#
from turtle import *

#-------DEFINE FUNCIOTN----------#
def star(m,n):
  begin_fill()
  color(92,16,142)
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
  end_fill()
def jump(x,y):
  pu()
  goto(x,y)
  pd()

def Left(x,y,z):
  begin_fill()
  color("black")
  rt(117)
  fd(x)
  rt(63)
  fd(y)
  rt(63)
  fd(x)
  rt(117)
  fd(z)
  end_fill()

def Right(x,y,z):
  begin_fill()
  color("black")
  rt(180)
  Left(x,y,z)
  end_fill()

def move(w):
  penup()
  fd(w)
  pendown()

def BTS(x,y,z,w):
  lt(90)
  Left(x,y,z)
  rt(135)
  move(w)
  lt(135)
  Right(x,y,z)

def Army(x,y,z,w):
  Left(x,y,z)
  lt(169)
  move(w)
  rt(169)
  Right(x,y,z)



#-------MAIN TASK----------------#
speed(0)
canvas = Screen()
canvas.tracer(25,8)
canvas.bgcolor(248,204,253)

x=-300
y=200

#-------START DRAWING------------#
for j in range(5):
    for i in range(5):
      penup()
      goto(x + i * 100, y - j * 100)
      pendown()
      if (i + j) % 2 == 0:
        star(25,40)
      elif i % 2 != 0:
        BTS(9,11,20,28)
      else:
        Army(9,11,20,20)

pu()
star(25,40)
#-------END DRAWING--------------#
hideturtle()
done()