result = []

def divider(a, b):
    try:
        a, b = int(a), int(b)
        if a < b:
            raise ValueError("а повинно бути >= b")
        if b > 100:
            raise IndexError("b не повинно бути > 100")
        return a / b
    except Exception as e:
        print(f"Ошибка при обработке ({a}, {b}): {e}")

data = ["10", "2", "2", "5", "123", "4", "18", "0", "15", "8", "4"]

for i in range(len(data) - 1):
    res = divider(data[i], data[i + 1])
    if res is not None:
        result.append(res)

print("Результат:", result)
