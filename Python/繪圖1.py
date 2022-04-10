#視覺化程式設計
#模組化程式設計 - 繪圖篇
#運算思維 - 問題拆解、尋找規律
#學習內容 - 迴圈、函式
#可用指令
#forward(p)：向前方移動 p 個像素距離
#backward(p)：向後方移動 p 個像素距離
#right(t)：順時針旋轉 t 度
#left(t)：逆時針旋轉 t 度
#更多指令：https://docs.python.org/3.3/library/turtle.html?highlight=turtle
###########################################################################
# Author:Lydia Lai
# Date:2018/11/16
###########################################################################

#程式從這裡開始
#引入必要套件 (turtle為繪圖套件)
from turtle import *

#任務-01 邊長100的正方形
speed(0)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

#任務-02 邊長100的三角形
forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)

#任務-03 邊長100的五邊形
forward(100)
right(72)
forward(100)
right(72)
forward(100)
right(72)
forward(100)
right(72)
forward(100)
right(72)

#任務-04 邊長100的六邊形
forward(100)
right(60)
forward(100)
right(60)
forward(100)
right(60)
forward(100)
right(60)
forward(100)
right(60)
forward(100)
right(60)

#任務-05 邊長100的八邊形
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)

#任務-06 邊長100的十二邊形
forward(100)
right(30)
forward(100)
right(30)
forward(100)
right(30)
forward(100)
right(30)
forward(100)
right(30)
forward(100)
right(30)
forward(100)
right(30)
forward(100)
right(30)
forward(100)
right(30)
forward(100)
right(30)
forward(100)
right(30)
forward(100)
right(30)

#任務-07 邊長100的星星
penup()
left(90)
forward(100)
right(90)
pendown()

begin_fill()
color("yellow")
for i in range(5):
    fd(100)
    rt(144)
end_fill()