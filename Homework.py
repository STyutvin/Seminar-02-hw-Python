# Задача №1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
n=input('Введите число: ')
format_n=n.replace('.','')
i=0
sum=0
while i<=int(len(format_n))-1:
    sum=sum+int(format_n[i])
    i+=1
print(sum)