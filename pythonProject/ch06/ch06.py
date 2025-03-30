# # def filter_and_group(lst, condition):
# #     # 使用列表推导式来筛选符合条件的元素
# #     group_true = [item for item in lst if condition(item)]
# #     group_false = [item for item in lst if not condition(item)]
# #
# #     return group_true, group_false
# #
# #
# # # 示例条件函数：筛选出所有偶数
# # def is_even(x):
# #     return x % 2 == 0
# #
# #
# # # 主程序
# # if __name__ == "__main__":
# #     # 示例列表
# #     lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #
# #     # 调用filter_and_group函数，传入条件函数is_even
# #     even_numbers, odd_numbers = filter_and_group(lst, is_even)
# #
# #     # 打印分组结果
# #     print("偶数:", even_numbers)
# #     print("奇数:", odd_numbers)
#
# from functools import lru_cache
#
# # 递归实现斐波那契数列第n项
# @lru_cache(None)  # 使用缓存来优化递归效率
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# # 计算斐波那契数列前n项的和
# def fibonacci_sum(n):
#     return sum(fibonacci(i) for i in range(n))
#
# if __name__ == "__main__":
#     # 计算斐波那契数列前10项的和
#     n = 10
#     result = fibonacci_sum(n)
#     print(f"斐波那契数列前{n}项的和是: {result}")

# 递归实现阶乘函数
def factorial(n):
    # 基本情况：0! = 1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 计算组合数 C(n, k) = n! / (k! * (n - k)!)
def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# 主程序
if __name__ == "__main__":
    # 示例：计算5的阶乘
    n = 5
    print(f"{n}的阶乘是: {factorial(n)}")  # 应该输出 5! = 120

    # 示例：计算从5个元素中选取3个元素的组合数
    n, k = 5, 3
    print(f"C({n}, {k}) = {combination(n, k)}")  # 应该输出 C(5, 3) = 10
