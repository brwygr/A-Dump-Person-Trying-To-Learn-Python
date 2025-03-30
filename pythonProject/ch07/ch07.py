# # class Student:
# #     def __init__(self, student_id, name, age, scores):
# #         """初始化学生对象"""
# #         self.student_id = student_id  # 学号
# #         self.name = name  # 姓名
# #         self.age = age  # 年龄
# #         self.scores = scores  # 成绩（字典，键是课程名，值是分数）
# #
# #     def calculate_average(self):
# #         """计算并返回学生的平均成绩"""
# #         if not self.scores:
# #             return 0  # 如果没有成绩，返回0
# #         total_score = sum(self.scores.values())  # 成绩的总和
# #         num_courses = len(self.scores)  # 课程的数量
# #         return total_score / num_courses  # 返回平均成绩
# #

# #     def print_details(self):
# #         """打印学生的详细信息"""
# #         print(f"学号: {self.student_id}")
# #         print(f"姓名: {self.name}")
# #         print(f"年龄: {self.age}")
# #         print("成绩:")
# #         for course, score in self.scores.items():
# #             print(f"{course}: {score}")
# #         average_score = self.calculate_average()
# #         print(f"平均成绩: {average_score:.2f}")
# #
# #
# # 示例：创建一个 Student 对象并展示功能
# student_1 = Student(
#     student_id="2023001",
#     name="张三",
#     age=18,
#     scores={
# #         "数学": 90,
# #         "英语": 85,
# #         "物理": 88,
# #         "化学": 92
# #     }
# # )
# #
# # # 打印学生的详细信息
# # student_1.print_details()
#
# class BankAccount:
#     def __init__(self, account_number, account_holder, balance=0):
#         """初始化银行账户"""
#         self.account_number = account_number  # 账户号
#         self.account_holder = account_holder  # 账户名
#         self.balance = balance  # 账户余额
#
#     def deposit(self, amount):
#         """存款"""
#         if amount > 0:
#             self.balance += amount
#             print(f"成功存入 {amount} 元")
#         else:
#             print("存款金额必须大于 0")
#
#     def withdraw(self, amount):
#         """取款"""
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"成功取出 {amount} 元")
#         else:
#             print("取款金额无效或余额不足")
#
#     def get_balance(self):
#         """查看余额"""
#         return self.balance
#
#     def print_details(self):
#         """打印账户详细信息"""
#         print(f"账户号: {self.account_number}")
#         print(f"账户名: {self.account_holder}")
#         print(f"余额: {self.balance:.2f}")
#
#
# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
#         """初始化储蓄账户"""
#         super().__init__(account_number, account_holder, balance)
#         self.interest_rate = interest_rate  # 利率
#
#     def withdraw(self, amount):
#         """重写取款方法，计算利息"""
#         if amount > 0 and amount <= self.balance:
#             # 在取款前，计算利息并加到余额
#             interest = self.balance * self.interest_rate
#             self.balance += interest
#             print(f"存入利息 {interest:.2f} 元")
#             self.balance -= amount
#             print(f"成功取出 {amount} 元，扣除利息后余额为 {self.balance:.2f}")
#         else:
#             print("取款金额无效或余额不足")
#
#     def print_details(self):
#         """打印账户详细信息"""
#         super().print_details()
#         print(f"利率: {self.interest_rate * 100:.2f}%")
#
#
# class CheckingAccount(BankAccount):
#     def __init__(self, account_number, account_holder, balance=0, fee=5):
#         """初始化支票账户"""
#         super().__init__(account_number, account_holder, balance)
#         self.fee = fee  # 支票手续费
#
#     def withdraw(self, amount):
#         """重写取款方法，扣除手续费"""
#         if amount > 0 and amount + self.fee <= self.balance:
#             self.balance -= (amount + self.fee)
#             print(f"成功取出 {amount} 元，扣除手续费 {self.fee} 元，余额为 {self.balance:.2f}")
#         else:
#             print("取款金额无效或余额不足")
#
#     def print_details(self):
#         """打印账户详细信息"""
#         super().print_details()
#         print(f"支票手续费: {self.fee} 元")
#
#
# # 示例：创建不同类型的账户并进行操作
#
# # 创建一个储蓄账户
# savings_account = SavingsAccount(
#     account_number="SA1001",
#     account_holder="李华",
#     balance=1000,
#     interest_rate=0.03
# )
#
# # 创建一个支票账户
# checking_account = CheckingAccount(
#     account_number="CA2001",
#     account_holder="王强",
#     balance=500,
#     fee=10
# )
#
# # 操作储蓄账户
# savings_account.deposit(500)
# savings_account.withdraw(200)
# print(f"储蓄账户当前余额: {savings_account.get_balance():.2f}")
# savings_account.print_details()
#
# # 操作支票账户
# checking_account.deposit(200)
# checking_account.withdraw(150)
# print(f"支票账户当前余额: {checking_account.get_balance():.2f}")
# checking_account.print_details()

# class Book:
#     def __init__(self, title, author, isbn, published_year, price):
#         """初始化图书对象"""
#         self.title = title  # 标题
#         self.author = author  # 作者
#         self.isbn = isbn  # 国际标准书号
#         self.published_year = published_year  # 出版年份
#         self.price = price  # 价格
#
#     def __str__(self):
#         """返回图书的字符串表示"""
#         return (f"图书信息:\n"
#                 f"标题: {self.title}\n"
#                 f"作者: {self.author}\n"
#                 f"ISBN: {self.isbn}\n"
#                 f"出版年份: {self.published_year}\n"
#                 f"价格: {self.price:.2f} 元")
#
#     def discount_price(self, discount_rate):
#         """计算打折后的价格"""
#         if 0 <= discount_rate <= 1:
#             discounted_price = self.price * (1 - discount_rate)
#             return discounted_price
#         else:
#             raise ValueError("折扣率必须在 0 到 1 之间")
#
#
# # 示例：创建一个 Book 对象，并展示功能
# book_1 = Book(
#     title="Python编程基础",
#     author="张伟",
#     isbn="978-7-123-45678-9",
#     published_year=2022,
#     price=89.99
# )
#
# # 打印图书详细信息
# print(book_1)
#
# # 计算并打印打折后的价格
# discount_rate = 0.2  # 20% 折扣
# discounted_price = book_1.discount_price(discount_rate)
# print(f"打折后的价格: {discounted_price:.2f} 元")
# x=3
#
# y=3
# x**=y
# print(x)
def bouncy_balls(height_0, n):
    height_n = height_0
    distance_n = height_0
    for i in range(1, n):
        height_n *= 0.52
        distance_n += (height_n * 2)
        return height_n, distance_n
    height_0 = int(input("高度:"))
    n = int(input("次数:"))
    height, distance = bouncy_balls(height_0, n)
    print(f"初始高度{height_0}次数{n},反弹高:{height},总共{distance}")
