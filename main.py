#!/usr/bin/python
#encoding:utf-8

import random                                       # 导入随机函数库

"""随机生成的四个阿拉伯数字"""
def Anum(x=1):
    anNum = []                                      # 定义anNum为空列表
    while x <= 4:                                   # 使用循环while循环4次
        anNumber = random.randint(0, 9)             # 使用随机函数从0-9中随机一个整数
        if anNumber in anNum:                       # 判断随机数是否重复出现，重复则跳过
            continue
        else:
            anNum.append(anNumber)                  # 不重复时加入列表，直到获取4个
            x = x + 1                               # 给x值加一，进入下一次有效循环
    return anNum                                    # 返回anNum的值


"""将玩家输入的数字与正确答案进行判断"""
def Judge(num,guess,y=0,a=0,b=0):
    while y < 4:                                    # 使用while循环，通过y值进行控制，循环4次
        if int(guess[y]) == num[y]:                 # 使用if判断guess猜测数字与num正确数字在相同位置对应上
            a = a + 1                               # a的值加一
        elif int(guess[y]) in num:                  # 猜测的值不与正确答案对应时，判断是否存在正确答案中
            b = b + 1                               # b的值加一
        y = y + 1                                   # y的值加一，进入下一个循环
    return a, b                                     # 返回a,b的值


"""修改正确答案功能"""
def Change(N):
    while 1:                                                            # while 1表示无限循环
        try:                                                            # 使用try语句检测输入是否存在异常
            oldNum = int(input("请输入需要更改的数字："))               # oldNum接收需要更改的数字，先字符串后强转为整数
            newNum = int(input("请输入更改后的数字："))                   # newNum接收更改后的数字，先字符串后强转为整数
        except ValueError:                                              # 当try中的语句发生错误时执行下面语句
            print("输入错误请重新输入！")                                      # 输出提示
            continue                                                       # 跳出循环

        if oldNum in N and newNum in range(0, 9):                       # 使用if判断oldNum是否存在于正确答案newNum是否属于0-9
            N[N.index(oldNum)] = newNum                                 # 将newNum的值覆盖在N列表中
            break                                                       # 跳出循环
        else:                                                           # 对需要更改和更改后的数字做出限制
            print('请检查被更改数字是否正确，更改后数字是否为0-9！')            # 输出提示
    return N                                                            # 返回列表N


"""特殊指令功能"""
def Function(list):
    test = input("请输入指令：")                                      # 接收字符串进行判断
    if test == '1':                                                     # 查询功能
        print(list)                                                      # 直接输出正确答案的列表
    elif test == '2':                                                   # 修改功能
        list = Change(list)                                             # 调用Change函数，使用修改功能
    elif test == '3':                                                   # 重置功能
        list = Anum()                                                   # 调用随机生成函数，输出一个新的列表
        print("重置成功！")                                               # 输出提示
    elif test == 'q':                                                   # 退出特殊指令功能，当输入q时退出
        print("退出特殊指令！")                                            # 输出提示
    else:                                                               # 对test的输入起到一个限制作用
        print("请输入正确的指令！")                                         # 输出提示
    return list, test                                                     # 返回list列表，test的值


number = Anum()                                                         # 调用随机函数得到符合正确答案要求的列表
# print number   # 测试时可通过此语句直接显示正确答案
while 1:                                                                # 使用无限循环
    print("\n特殊指令请按 * ")                                            # 输出特殊指令提示
    anGuess = input("请输入四个阿拉伯数字：\n")                         # 获取玩家猜测答案

    if anGuess == '*':                                                  # 判断是否是特殊指令
        print("欢迎使用特别指令：\n查询答案请按1\n修改答案请按2\n重置答案请按3\n退出请按q\n")  # 输出指令提示
        while 1:                                                        # 使用无限循环
            number, t = Function(number)                                # 调用特殊指令函数
            if t == 'q':                                                # 判断是否为退出特殊指令的字符
                break                                                   # 跳出循环
    elif anGuess.isdigit() == False or len(anGuess) != 4:               # isdigit()判断玩家输入的字符是否由数字组成，限制玩家输入字符长度不能超过4
        print('请输入正确的四个阿拉伯数字！')                                # 输出提示
        continue                                                        # 中断循环
    else:                                                               # 玩家输入正确后
        A, B = Judge(number, anGuess)                                   # 调用判断函数，获取A，B的值
        print(A, 'A', B, 'B')                                           # 输出A，B
        if A == 4 and B == 0:                                           # 游戏结束判断条件
            print('猜测正确！游戏结束！')                                   # 输出游戏结束提示
            break                                                       # 跳出循环，游戏程序结束

