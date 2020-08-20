# def ask_for_name():
#     name = input("Introduce yourself: ")
#     print("Hello " + name)
#
# ask_for_name()


### Pętle
# print("FOR LOOP")
# for i in range(10): # 0 - 9
#     print(i)
#
# print("WHILE LOOP")
# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
# name = "Marta"
# if len(name) == len("Matix"):
#     print("Niech żyje zbrodniczy reżim")
# else:
#     print("Niech nie żyje")

def sum_all_smaller(num):
    output = 0
    for i in range(1, num):
        output = output + i
    return output

print(sum_all_smaller(10))

def factorial(num):
    output = 1
    for i in range(1, num+1):
        output = output * i
    return output

print(factorial(5))
