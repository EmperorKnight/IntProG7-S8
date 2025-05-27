# num1=25
# num2=25

# print("1) ",num1 > num2)
# print("2) ",num1 < num2)
# print("3) ",num1 == num2)
# print("4) ",num1 != num2)
# print("5) ",num1 >= num2)
# print("6) ",num1 <= num2)
# print("7) ",not (num1) == num2)
# print("8) ",not (num1))
# print("9) ",not (num1) > num2)
# print("10) ",not (num1) < num2)
# print("11) ",not (num1) != num2)

# #suma de dos numeros 

# num1 = int(input(f"Dime un número: \n-> "))
# num2 =  int(input(f"Dime otro número: \n-> "))
# suma = num1 + num2
# print(f"La suma de \n  {num1:>9,} \n+ {num2:>9,}\n--------------\n= {suma:>9,}")

# n = 5
# for i in range(1,n+1):
#     # printing spaces
#     for j in range(i-1):
#         print(" ",end = "")
#         # printing stars
#     for j in range(2*(n-i)+1):
#         print("*",end="")
#     print()

cont = 11
x = ""
lista = []
for i in range(1,11):
    p = "•" * i
    n = " " * (cont - 1)
    d = f"{i*10}%"
    print(f"{p}{n}{d}\n",end = "")
    cont -=1