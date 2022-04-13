#1) необходимо разработать функцию, принимающую список строк и строку, и
#выполняющую вставку строки в середину списка (если длина списка 
#нечетная, то вставлять строку перед серединным элементом);<<<<<<< nikolaev
#1
str = list(input("Введите список: ").split())
s = input("Введите строку: ")
def paste(a:list, b):
    if len(a) % 2 == 0:
        a.insert(len(a)//2, b)
    else:
        a.insert((len(a)//2)+1, b)
    return a
print(paste(str, s))
#2) необходимо разработать функцию, принимающую список строк, число и
#строку, и выполняющую вставку строки в указанную позицию, если вставка 
#на указанную позицию невозможна, то вернуть сообщение «paste operation is
#not possible»;

#2
s = input("Введите строку: ")
index = int(input("Введите позицию: "))
b = input("Введите строку: ")
def insert_dash(s, index):
    if index > len(s):
        return print("paste operation is not possible")
    return s[:index] + b + s[index:]
print(insert_dash(s, index)) 

#3) необходимо разработать функцию, принимающую список строк и число, и 
#выполняющую удаление строки по указанной позицию списка, если удаление
#невозможно, то вернуть сообщение «delete operation is not possible».
#3
s = list(input("Введите строку: "))
print(s[2])
a = int(input("Введите позицию: "))
def str(s, a):
    if a > len(s):
        return print("delete operation is not possible")
    del s[a]
    return "".join(s)
print(str(s, a))

