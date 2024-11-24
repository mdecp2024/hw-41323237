import math

# 函數：列印10x10的正圓形
def print_perfect_circle(radius, size=10):
    # 圓心的位置設為 (radius, radius)
    for y in range(size):
        for x in range(size):
            # 計算當前點與圓心 (r, r) 的距離
            distance = (x - radius) ** 2 + (y - radius) ** 2
            # 若距離小於或等於半徑的平方，則在此位置列印 "*"
            if distance <= radius ** 2:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# 示範輸出，圓形半徑設為 5
print_perfect_circle(5)