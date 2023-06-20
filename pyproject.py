x = str(input()) #поллиндром или хз как
print(x)
x = x.lower() # все символы находятся в нижнем регистре
x = x.replace(" ","") # без пробелов
print(x)

def func(x):
    y = x[::-1]
    if y == x:
        return True
    else:
        return False

print(func(x))