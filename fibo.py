
start = input()
numbers = {float(numbers.strip()) for numbers in start.split(", ")}
final_list = []
fibo = 1
fibo2 = 1
max_num = max(numbers)
if 0 in numbers:
    final_list.append(0)
while fibo < max_num:
    if fibo in numbers:
        final_list.append(fibo)
    fibo2, fibo = fibo, fibo2 + fibo
print(f"{final_list}")
