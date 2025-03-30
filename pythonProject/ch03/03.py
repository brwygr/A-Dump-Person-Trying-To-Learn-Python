# num=int(input('input a number :'))
# if num%2==0:
#     print(num,'是偶数')
# else:
#     print(num,'是奇数')
# a = int(input('请输入PM2.5的值：'))
# if 0 < a <= 35:
#     print('优')
# elif 35 < a <= 75:
#     print('良')
# elif 75 < a <= 115:
#     print('轻度污染')
# elif 115 < a <= 150:
#     print('中度污染')
# elif 150 < a <= 250:
#     print('重度污染')
# elif a > 250:
#     print('严重污染')
# w = 1
# while w < 10:
#     n = 1
#     while n <= w:
#         print("%d * %d = %d" %(n,w,w*n),end="\t")
#         n+=1
#     w+=1
#     print()
# w = 1
# while w < 10:
#     for n in range(1,w+1):
#         print("%d * %d = %d" % (n, w, w * n), end="\t")
#     w+=1
#     print()
# for w in range(1,10):
#     for n in range(1,w+1):
#         print("%d * %d = %d" % (n, w, w * n), end="\t")
#         n+=1
#     w+=1
#     print()
# num=0
# for i in range(1,101):
#     if i %3==0:
#         if i%5 !=0:
#             print(i,end="\t")
# 题目：
# 有一分数序列：
# 2/1，3/2，5/3，8/5，13/8，21/13...
# 求出这个数列的前n项之和

# n = int(input("请输入求和项数："))
# n_sum = 0   # 记录前n项和
# a = 1   # 分母
# b = 2   # 分子
# for i in range(n):
#     n_sum += b / a
#     a, b = b, a + b
# print("数列前 %d 项和为 %f" % (n, n_sum))
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end="\t")


