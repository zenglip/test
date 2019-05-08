# def play():
#     print("返回值：")
#     return [5,6],[7,8]
# # a = 1
# # b = 2
# res = play()
# print("函数返回值{}".format(play()))
# print(type(res))
# print(type(None))
# s = 0
# for i in range(101):
#     s = i +s
# print(s)
# d = 0
# s = 0
# for i in range(101):
#     if i%2==0:
#         d=i+d
#     else:
#         s=i+s
# print("奇数和：{0}，偶数和：{1}".format(s,d))
# for i in range(1,6):
#     print("*"*i)
#用for筛选符合条件的人数
# count = 0
# for i in range(1,6):
#     sex=input("请输入性别：")
#     if sex == "m" or sex == "f":
#         if sex == "f":
#             age = input("请输入年龄：")
#             if age.isdigit():
#                 if 10<=int(age)<=12:
#                     print("通过")
#                     count+=1
#                 else:
#                     print("不通过")
#             else:
#                 print("请按格式输入")
#         else:
#             print("不通过")
#     else:
#         print("请按正确格式输入")
# print(count)
#用while筛选符合条件的人数
# count = 0
# i = 0
# while i <= 5:
#     sex=input("请输入性别：")
#     i+=1
#     if sex == "m" or sex == "f":
#         if sex == "f":
#             age = input("请输入年龄：")
#             if age.isdigit():
#                 if 10<=int(age)<=12:
#                     print("通过")
#                     count+=1
#                 else:
#                     print("不通过")
#             else:
#                 print("请按格式输入")
#         else:
#             print("不通过")
#     else:
#         print("请按正确格式输入")
# print(count)
#判断价格(含小数）
# price = input("输入总价：")
# if price.isalnum():#如果输入数字和字母
#     if price.isdigit() :#如果输入数字
#         if int(price)>100:
#             print("折扣20%，实际价格：{0}".format(int(price)*0.8))
#         else:
#             if int(price)>=50:
#                 print("折扣10%，实际价格：{0}".format(int(price)*0.9))
#             else:
#                 print("无折扣，实际价格:{0}".format(price))
#     else:
#         print("重新输入")
# else:
#     if float(price) > 100:
#         print("折扣20%，实际价格：{0}".format(float(price) * 0.8))
#     else:
#         if float(price) >= 50:
#             print("折扣10%，实际价格：{0}".format(float(price) * 0.9))
#         else:
#             print("无折扣，实际价格:{0}".format(price))
#根据输入判断成绩（含小数）
# score = input("请输入分数：")
# if score.isalnum():#如果输入是字母和数字
#     if score.isdigit():#如果输入是数字
#         if int(score)<0:
#             print("请输入正确分数")
#         elif int(score)<60:
#             print("不及格")
#         elif int(score)<70:
#             print("及格")
#         elif int(score)<80:
#             print("中等")
#         elif int(score)<90:
#             print("良好")
#         elif int(score)<=100:
#             print("优秀")
#         else:
#             print("请输入正确分数")
#     else:#如果输入是字母
#         print("请输入正确分数")
# else:#如果输入是浮点数
#     if float(score) < 0:
#         print("请输入正确分数")
#     elif float(score) < 60:
#         print("不及格")
#     elif float(score) < 70:
#         print("及格")
#     elif float(score) < 80:
#         print("中等")
#     elif float(score) < 90:
#         print("良好")
#     elif float(score) <= 100:
#         print("优秀")

#判断一个数能否被3和5同时整除
# n = input("请输入一个整数：")
# if n.isdigit():
#     if int(n)%3==0 and int(n)%5==0:
#         print("通过！{}能被3和5同时整除".format(n))
#     else:
#         print("不通过！{}不能被3和5同时整除".format(n))
# else:
#     print("请重新输入正确的整数！")
#判断闰年
# year = input("请输入年份:")
# if year.isdigit():
#     if int(year)%400==0:
#         print("闰年")
#     else:
#         if int(year)%4==0 and int(year)%100!=0:
#             print("闰年")
#         else:
#             print("不是闰年")
# else:
#     print("请重新输入")
#判断回文
# n = input("输入一个五位数：")
# if len(n)==5:#判断长度是否为5
#     if n.isdigit():#判断输入是否为数字
#         if int(n[0])==0:#判断首位是否为0
#             print("请输入正确的五位数")#首位为0，提示
#         elif int(n[0])==int(n[-1]) and int(n[1])==int(n[-2]):#判断是否为回文
#             print("通过！是回文")
#         else:
#             print("不通过！不是回文")
#     else:
#         print("请输入正确的五位数")#输入不是数字，提示
# else:
#     print("请输入正确的五位数")#输入不是五位数，提示

#随机数和输入数比较（可运算小数）
# import random #调用随机函数库
# a = random.randint(1,9) #生成随机整数
# b = input("输入一个数字：")
# if b.isalnum():#判断输入是否为字母和数字
#     if b.isdigit():#如果是数字
#         if int(b)>a:
#             print("bigger")
#         elif int(b)<a:
#             print("less")
#         else:
#             print("equal")
#     else:#如果是字母
#         print("请输入数字")
# else:#如果是小数
#     if float(b) > a:
#         print("bigger")
#     elif float(b) < a:
#         print("less")
#     else:
#         print("equal")
#登录功能
# dict ={"name":"huahua","pwd":"123456"}
# name = input("用户名：")
# pwd = input("pwd:")
# if name in dict.values():
#     if pwd == dict.get("pwd"):
#         print("登录成功")
#     else:
#         print("密码错误")
# else:
#     print("用户名错误")
# #四位数加密输出
# num = input("输入四位数：")
# # num = "1234"
# L = []
# for i in num:
#     i=(int(i)+5)%10
#     L.append(i)
# s= ""
# print(L[::-1])
# for j in L[::-1]:
#     s += str(j)
# print(s)
#打印乘法表
# for j in range(1,10):
# #     for i in range(1,j+1):
# #         print("{0}*{1}={2}".format(i,j,i*j),end="\t")
# #         # print(str(i)+"*"+str(j)+"="+str(i*j),end="\t")
# #     print()
