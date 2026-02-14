n = int(input("Enter the number of positive numbers: "))
sum = 0
count = 0

while count < n:
    num = int(input("Enter a number: "))
    if num > 0:
        sum += num
        count += 1
    else:
        continue

avg = sum / n
print("sum =", sum)
print("average =", avg)