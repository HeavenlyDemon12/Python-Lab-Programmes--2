start, end = 1, 100
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end = " ")
      
      
start, end = 1, 100
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end = " ")
        
        
        for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
      