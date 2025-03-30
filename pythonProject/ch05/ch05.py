# # 创建字典存储账号和密码
# accounts = {
#     "user1": "password123",
#     "admin": "adminpass",
#     "guest": "guestpass"
# }
#
# max_attempts = 3
#
#
# # 登录功能
# def login_system(accounts, max_attempts):
#     attempts = 0
#     while attempts < max_attempts:
#         # 输入账号和密码
#         username = input("请输入账号: ")
#         password = input("请输入密码: ")
#
#         # 验证账号和密码
#         if username in accounts and accounts[username] == password:
#             print("登录成功！")
#             return True
#         else:
#             attempts += 1
#             print(f"账号或密码错误！你还有 {max_attempts - attempts} 次机会。")
#
#     print("登录失败，已超过最大尝试次数！")
#     return False
#
#
# # 运行登录系统
# login_system(accounts, max_attempts)


# # 定义列表对象
# my_list = ['广州理工学院', '计算机学院', '计算机系', '计算机学院', 'China', 'it', 'well', 'it', 'best']
#
# # 定义一个空集合
# my_set = set()
#
# # 遍历列表
# for item in my_list:
#     # 判断是否包含子字符串“学院”或“China”
#     if "学院" in item or "China" in item:
#         my_set.add(item)  # 将符合条件的元素添加到集合中
#
# # 打印集合
# print("最终集合 my_set:", my_set)
#
# # 打印集合的长度
# print("集合的长度:", len(my_set))

# 初始化姓名列表和房间列表
list_name = ["张无忌", "赵敏", "周芷若"]
list_room = [101, 102, 103]

# 练习1：将两个列表合并为一个字典
dict_room_name = dict(zip(list_room, list_name))
print("练习1结果：", dict_room_name)

# 练习2：颠倒练习1字典的键值
dict_name_room = {value: key for key, value in dict_room_name.items()}
print("练习2结果：", dict_name_room)
