a = int(input())
b = int(input())
c = int(input())


d = b**2 - 4 * a * c

if d > 0:
    print(f"x1 {(-b + d**0.5) / (2 * a)}")  
    print(f"x2 {(-b - d**0.5) / (2 * a)}")
elif d == 0:
    print(f"x1,2 = {-b / (2 * a)}")
else:
    print("в области действительных чисел нет решения")
