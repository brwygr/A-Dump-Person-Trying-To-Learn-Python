def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # 初始化前两项
    sequence = [0, 1]
    # 迭代生成后续项
    for i in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence


# 示例：生成前10项斐波那契数列
n = 10
print(f"前{n}项斐波那契数列:", fibonacci_sequence(n))
