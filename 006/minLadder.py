# 爱因斯坦的难题

# 爱因斯坦曾出过这样一道有趣的数学题：
# 有一个长阶梯;
# 若每步上2阶，最后剩1阶；
# 若每步上3阶，最后剩2阶；
# 若每步上5阶，最后剩4阶；
# 若每步上6阶，最后剩5阶；
# 只有每步上7阶，最后刚好一阶也不剩。

# 定義一個程序總數範圍
total = input('請輸入一個限定的總階梯數(默認不輸入為200): ')
# 默認不輸入為100
if total == '':
    total = '200'

while not total.isdigit():
    total = input('您輸入的不是一個整數,請重新輸入: ')
total = int(total)

# 由於只有每步上7阶，最后刚好一阶也不剩。ladderNum移動式7的倍數；先定義一個ladderNum=7
ladderNum = 7
# 定義i=0用作循環使用
i = 0
# 定義 標誌位 flag = True;True表示計算成功，False表示計算失敗
flag = False

while not flag:
    # 初始定義為0，在進入while循環后先加1，省得每個if里都寫一遍，優化代碼
    i += 1
    if (ladderNum % 2 == 1 and ladderNum % 3 == 2
        and ladderNum % 5 == 4 and ladderNum % 6 == 5
        and ladderNum % 7 == 0):
        flag = True
    else:
        ladderNum = 7 * i
        flag = False
        if ladderNum > total:
            # 在程序限定的total階梯內，未找到符合條件的答案~~break跳出
            break
if flag:
    print('该阶梯至少有', ladderNum, '阶')
else:
    print('在程序限定的', total, '階梯內,未找到符合條件的答案~~')
