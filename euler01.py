def is_multiple_of_3(num):
    if num % 3 == 0:
        return True
    else:
        return False

def is_multiple_of_5(num):
    if num % 5 == 0:
        return True
    else:
        return False

print(is_multiple_of_5(44))
print(is_multiple_of_5(78))
print(is_multiple_of_5(90))

def is_multiple_of_5_or_3(num):
    return is_multiple_of_5(num) or is_multiple_of_3(num)

print(is_multiple_of_5_or_3(45))
print(is_multiple_of_5_or_3(40))
print(is_multiple_of_5_or_3(9))
print(is_multiple_of_5_or_3(19))
