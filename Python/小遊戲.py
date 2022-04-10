# iGame:Fans of youtube
# Author: 10731835賴芊樺
# Version:
# Date: 2019/04/12
# 題庫參考 http://www.taiwantestcentral.com/Quiz/Quiz.aspx?MainCategoryID=17&CategoryID=21&IsEngQ=0&ProblemCount=10

# random的函數參考資料： http://docs.python.org/lib/module-random.html

# 時間函數參考http://tw.gitbook.net/python/python_date_time.html

# ----------引入必要模組----------------#
import random
import time
from os import system

# ----------設定重要全域變數與初始值----------------#
Roles = ['波特王and雷翔', '蔡阿嘎', '黃大謙', '阿滴', '茵聲', '小玉', '笑笑', '放火', '碰碰', '以上皆非']  # 角色清單
訂閱者 = [1000, 500, 2000, 5000, 2000, 2000, 3000, 1000, 2000, 1000]  # 血量清單
贊助商 = [4, 5, 3, 1, 2, 2, 2, 4, 2, 4]  # 生命值清單
訂閱者 = 0  # 血量初始值
贊助商 = 0  # 生命值初始值
Role = 'NONAME'  # 角色初始值
level = 1  # 關卡初始值
觀看次數 = 0  # 玩家經驗值

# ----------存放題目清單與答案清單-------#
'''

'''


# ----------定義遊戲關卡----------------#
def level1():
    global 觀看次數
    print('*************************')
    print('Level 1')
    Q1 = ['阿滴2018年的愚人節影片主題是甚麼?\n1.我開了家全科補習班 \n2.滴妹其實不存在 \n3.我要離開這個頻道了', '滴妹喜歡甚麼甜度的飲料?\n1.半糖\n2.少糖(7分糖)\n3.全糖',
          '下列哪個人沒有上過阿滴英文的頻道?\n1.Kurt Hugo Schneider\n2.蔡佩軒\n3.周興哲\n4.小玉',
          '小玉喜歡的韓團是誰?\n1.Exo\n2.Bts\n3.Got7\n4.Seventeen', '小玉2018年的愚人節影片主題是什麼?\n1.跟放火吵架\n2.跟笑笑交往\n3.被變態跟蹤',
          '下列哪一首歌不是小玉的?\n1.沒用的大學生\n2.ㄅㄆㄇ注音歌\n3.社會亂源', '蔡阿嘎的小孩叫什麼?\n1.蔡桃貴 \n2.蔡包 \n3.蔡花',
          '黃大謙的臉是幾度角?\n1.90 \n2.120\n3.100\n4.135', '古娃娃有什麼稱號?\n1.便當店女神\n2.便利商店女神\n3.全聯女神']
    A1 = [1, 3, 4, 2, 1, 2, 1, 2, 3, 2]
    items = range(6)
    nums = random.sample(items, 3)
    for i in nums:
        print(Q1[i])
        ans = int(input('你的答案是:'))
        if ans == A1[i]:
            print("成功擊敗一隻刺球丸子,+1000XP")
            觀看次數 += 1000
        else:
            print('遭受來自黑暗火焰蛇的攻擊!,正確答案為', A1[i])
            訂閱者 = - 1000
        if 訂閱者 == 0:
            global 贊助商
            贊助商 = - 1
            print('你承受不住大量傷害,生命值-1')
            print('目前生命值', 贊助商 - 1)
    print('*************************')


# ----------定義遊戲關卡----------------#
def level2():
    global 觀看次數
    print('*************************')
    print('Level 2')
    Q1 = ['阿滴2018年的愚人節影片主題是甚麼?\n1.我開了家全科補習班 \n2.滴妹其實不存在 \n3.我要離開這個頻道了', '滴妹喜歡甚麼甜度的飲料?\n1.半糖\n2.少糖(7分糖)\n3.全糖',
          '下列哪個人沒有上過阿滴英文的頻道?\n1.Kurt Hugo Schneider\n2.蔡佩軒\n3.周興哲\n4.小玉',
          '小玉喜歡的韓團是誰?\n1.Exo\n2.Bts\n3.Got7\n4.Seventeen', '小玉2018年的愚人節影片主題是什麼?\n1.跟放火吵架\n2.跟笑笑交往\n3.被變態跟蹤',
          '下列哪一首歌不是小玉的?\n1.沒用的大學生\n2.ㄅㄆㄇ注音歌\n3.社會亂源', '蔡阿嘎的小孩叫什麼?\n1.蔡桃貴 \n2.蔡包 \n3.蔡花',
          '黃大謙的臉是幾度角?\n1.90 \n2.120\n3.100\n4.135', '古娃娃有什麼稱號?\n1.便當店女神\n2.便利商店女神\n3.全聯女神']
    A1 = [1, 3, 4, 2, 1, 2, 1, 2, 3, 2]
    items = range(6)
    nums = random.sample(items, 3)
    for i in nums:
        print(Q1[i])
        ans = int(input('你的答案是:'))
        if ans == A1[i]:
            print("成功擊敗一隻刺球丸子,+1000XP")
            觀看次數 += 1000
        else:
            print('遭受來自黑暗火焰蛇的攻擊!,正確答案為', A1[i])
            訂閱者 = - 1000
        if 訂閱者 == 0:
            global 贊助商
            贊助商 = - 1
            print('你承受不住大量傷害,生命值-1')
            print('目前生命值', 贊助商 - 1)
    print('*************************')


# ----------定義遊戲關卡----------------#
def level3():
    global 觀看次數
    print('*************************')
    print('Level 3')
    Q1 = ['阿滴2018年的愚人節影片主題是甚麼?\n1.我開了家全科補習班 \n2.滴妹其實不存在 \n3.我要離開這個頻道了', '滴妹喜歡甚麼甜度的飲料?\n1.半糖\n2.少糖(7分糖)\n3.全糖',
          '下列哪個人沒有上過阿滴英文的頻道?\n1.Kurt Hugo Schneider\n2.蔡佩軒\n3.周興哲\n4.小玉',
          '小玉喜歡的韓團是誰?\n1.Exo\n2.Bts\n3.Got7\n4.Seventeen', '小玉2018年的愚人節影片主題是什麼?\n1.跟放火吵架\n2.跟笑笑交往\n3.被變態跟蹤',
          '下列哪一首歌不是小玉的?\n1.沒用的大學生\n2.ㄅㄆㄇ注音歌\n3.社會亂源', '蔡阿嘎的小孩叫什麼?\n1.蔡桃貴 \n2.蔡包 \n3.蔡花',
          '黃大謙的臉是幾度角?\n1.90 \n2.120\n3.100\n4.135', '古娃娃有什麼稱號?\n1.便當店女神\n2.便利商店女神\n3.全聯女神']
    A1 = [1, 3, 4, 2, 1, 2, 1, 2, 3, 2]
    items = range(6)
    nums = random.sample(items, 3)
    for i in nums:
        print(Q1[i])
        ans = int(input('你的答案是:'))
        if ans == A1[i]:
            print("成功擊敗一隻刺球丸子,+1000XP")
            觀看次數 += 1000
        else:
            print('遭受來自黑暗火焰蛇的攻擊!,正確答案為', A1[i])
            訂閱者 = - 1000
        if 訂閱者 == 0:
            global 贊助商
            贊助商 = - 1
            print('你承受不住大量傷害,生命值-1')
            print('目前生命值', 贊助商 - 1)
    print('*************************')


# ----------SHOW GAME MESSAGE----------------#
def showGameMessage():
    print('Welcome to fans of youtube')


# ----------Choose a Role----------------#
def chooseRole():
    global Role
    global 訂閱者
    global 贊助商

    print('為自己取個名字吧\n請輸入:')


# choose = int(input('開始'))
# k = random.randint(0,4)   #抽選角色號碼
# Role = Roles[k]
# HP += HPs[k]
# Life = Lifes[k]
# print('妳有一隻寵物小精靈:', Role)


# ----------Show Status----------------#
def showStatus():
    print('*************************')
    print('目前總訂閱者:', 訂閱者)
    print('目前贊助商:', 贊助商)
    print('目前觀看次數:', 觀看次數)
    print('*************************')


# ----------定義關卡選單----------------#
def chooseLevel():
    global level
    print('*************************')
    print('1:Level 1')
    print('2:Level 2')
    print('3:Level 3')
    print('0:Quit')
    print('*************************')
    level = int(input('Choose a Level:'))


# ----------定義GAME OVER----------------#
def gameOver():
    print('YOU LOSE!!')
    system().exit()


# ----------設計主程式流程----------------#

showGameMessage()

while True:
    chooseRole()
    showStatus()
    chooseLevel()

    if level == 1:
        level1()
    elif level == 2:
        level2()
    elif level == 3:
        level3()
else:
    print('Thank you~~ 掰掰~')

    showStatus()

# ----------程式結束----------------#