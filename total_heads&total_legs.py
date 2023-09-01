def solve_chicken_rabbit(total_heads, total_legs):
    # 鸡兔总数最大值为总头数
    max_chicken_rabbit = total_heads

    for chicken_count in range(max_chicken_rabbit + 1):
        rabbit_count = total_heads - chicken_count
        if (chicken_count * 2) + (rabbit_count * 4) == total_legs:
            return chicken_count, rabbit_count

    # 无解情况返回None
    return None

# 获取用户输入
heads = int(input("请输入鸡兔总头数: "))
legs = int(input("请输入鸡兔总腿数: "))

# 解决问题并输出结果
solution = solve_chicken_rabbit(heads, legs)
if solution:
    chicken, rabbit = solution
    print(f"鸡的数量为: {chicken}")
    print(f"兔的数量为: {rabbit}")
else:
    print("无法解决该问题")
