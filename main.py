try:
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    c = float(input("Input c: "))
except ValueError:
    print("введённые значения не являются числовыми")
    exit(1)


a = a or 1

d = b**2 - 4 * a * c

if d > 0:
    print(f"x1 {(-b + d**0.5) / (2 * a)}")  
    print(f"x2 {(-b - d**0.5) / (2 * a)}")
elif d == 0:
    print(f"x1,2 = {-b / (2 * a)}")
else:
    print("в области действительных чисел нет решения")
