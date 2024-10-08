first=input("1-е число: ")
second=input("2-е число: ")
third=input("3-е число: ")
if first==second==third:
    print("все 3 числа равны")
elif first==second or first==third or second==third:
    print("2 числа равны")
else:
    print("0 - равных чисел нет")
