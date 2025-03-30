# numbers_range = tuple(range(2, 21, 2))
# print(numbers_range)
#
# numbers_comprehension = tuple(num for num in range(1, 21) if num % 2 == 0)
# print(numbers_comprehension)
# import random
#
# # (1)
# random_integers = [random.randint(1, 100) for _ in range(10)]
# print("随机整数列表:", random_integers)
#
# # (2)
# tuple_list = [(random_integers[i], random_integers[i + 1])
#               for i in range(0, len(random_integers) - 1, 2)]
# print("元组列表:", tuple_list)
#
# # (3)
# sorted_tuple_list = sorted(tuple_list, key=lambda x: (x[0], x[1]))
# # (4)
# print("排序后的元组列表:", sorted_tuple_list)
import random

even_numbers = tuple(range(2, 21, 2))
print("偶数元组:", even_numbers)
teachers = [f"老师{i+1}" for i in range(8)]
offices = [f"办公室{i+1}" for i in range(3)]
allocation = {teacher: random.choice(offices) for teacher in teachers}
print("老师与办公室分配:")
for teacher, office in allocation.items():
    print(f"{teacher} -> {office}")
