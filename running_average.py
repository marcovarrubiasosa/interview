def running_average(numbers):
    averages = []
    total = 0

    for i in range(len(numbers)):
        total += numbers[i]
        averages.append(total / (i + 1))

    return averages

nums = [10, 20, 30, 40]

print(running_average(nums))
print("--------------")

total = 0
count = 0

def running_average2(value):
    global total, count
    total += value
    count += 1
    return total / count

print(running_average2(10))  # 10.0
print(running_average2(20))  # 15.0
print(running_average2(30))  # 20.0
print(running_average2(40))  # 25.0
