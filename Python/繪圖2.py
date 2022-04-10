# 設計者：Lydia Lai
# 創作理念：
# 版本：1.0
# 創作日期：2018/12/28
# 授權方式：姓名標示─非商業性─相同方式分享 (http://creativecommons.tw/explore)


# -------START HERE---------------#
from turtle import *


# -------DEFINE FUNCIOTN----------#
def Left(x, y, z):
    rt(117)
    fd(x)
    rt(63)
    fd(y)
    rt(63)
    fd(x)
    rt(117)
    fd(z)


def Right(x, y, z):
    rt(180)
    Left(x, y, z)


def move(w):
    penup()
    fd(w)
    pendown()


def BTS(x, y, z, w):
    lt(90)
    Left(x, y, z)
    rt(135)
    move(w)
    lt(135)
    Right(x, y, z)


def Army(x, y, z, w):
    lt(90)
    Left(x, y, z)
    lt(169)
    move(w)
    rt(169)
    Right(x, y, z)


def jump(x, y):
    pu()
    goto(x, y)
    pd()


def BTSArmy(x, y, z, w, p):
    BTS(x, y, z, w)
    rt(90)
    jump(x, y)
    Army(x, y, z, p)
    rt(90)


# -------MAIN TASK----------------#
speed(0)
start_x = -200
start_y = 200

n = 3

# -------START DRAWING------------#
for j in range(n):
    for i in range(n):
        x = start_x + (2 * 28 + 10) * i
        y = start_y - (2 * 28 + 10) * j
        jump(x, y)
        BTS(9, 11, 20, 28)
        rt(90)
        jump(x, y)
        Army(9, 11, 20, 20)
        rt(90)

# -------END DRAWING--------------#

hideturtle()
done()