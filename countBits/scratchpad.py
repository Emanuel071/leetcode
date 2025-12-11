
 
n = 5

list_factorial = [1] * (n + 1)
print(list_factorial)
count = 0

temp = n 

# while temp >= 0:
#     list_reverse_factorial.append(n - temp)
#     temp -= 1
# print(list_reverse_factorial)

for i in range(0, n + 1):
    print(f"i: {i}")
    if i == 0:
        print("i is zero")
        count = 0
    else:
        while i:
            count += i & 1
            i >>= 1
    list_factorial[i] = count
    count = 0
    
print(list_factorial)
    

