import csv

with open('devices.txt', encode='*') as file:
    a = reader('devices.txt')
    answer = {}
    
    for company, product, typeName, inches, cpu, ram, memory, gpu, price in file:
        