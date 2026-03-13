def fractional_knapsack(capacity, items):
    """
    分数背包问题 - 贪心算法
    
    参数:
        capacity: 背包容量
        items: 物品列表，每个物品为[价值, 重量]
    
    返回:
        最大总价值
    """
    # 计算价值密度并排序（按单位价值降序）
    items_with_density = []
    for value, weight in items:
        density = value / weight
        items_with_density.append([value, weight, density])
    
    # 按密度降序排序
    items_with_density.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    
    for value, weight, density in items_with_density:
        if remaining_capacity <= 0:
            break
            
        if weight <= remaining_capacity:
            # 可以拿整个物品
            total_value += value
            remaining_capacity -= weight
            print(f"拿取整个物品: 价值={value}, 重量={weight}")
        else:
            # 只能拿一部分
            fraction = remaining_capacity / weight
            total_value += value * fraction
            print(f"拿取物品的一部分: 价值={value*fraction:.2f}, 重量={remaining_capacity} (占比={fraction:.2f})")
            remaining_capacity = 0
    
    return total_value


# 示例使用
if __name__ == "__main__":
    # 物品格式: [价值, 重量]
    items = [
        [60, 10],   # 物品A: 价值60, 重量10 (密度6)
        [100, 20],  # 物品B: 价值100, 重量20 (密度5)
        [120, 30]   # 物品C: 价值120, 重量30 (密度4)
    ]
    capacity = 50
    
    print("背包容量:", capacity)
    print("物品列表: 价值-重量")
    for i, (value, weight) in enumerate(items):
        print(f"  物品{i+1}: {value}元, {weight}kg (密度={value/weight:.2f})")
    
    print("\n贪心选择过程:")
    max_value = fractional_knapsack(capacity, items)
    print(f"\n最大总价值: {max_value:.2f}元")