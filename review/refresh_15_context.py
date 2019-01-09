# -*- coding: utf-8 -*-


################################################################ Context Manager

with open('test.txt', 'r') as f:
    print(f.readlines())
    
    
## issue with returning lazy iterator    
import csv

def read_data():
    with open('file.txt') as f:
        return csv.reader(f, delimiter = ',')
    
reader = read_data()    
    
for row in reader:
    print(row)    
    
## fix
def read_data():
    with open('file.txt') as f:
        yield from csv.reader(f, delimiter = ',')    

reader = read_data() 

for row in reader:
    print(row)    
        
## fix 2 (memory hungry)  

def read_data():
    with open('file.txt') as f:
        return list(csv.reader(f, delimiter = ','))
    
reader = read_data()    
    
for row in reader:
    print(row)  
    
#################################################### Generator + context manager  

def my_gen():
    try:
        print('create context')
        yield [1,2,3,4]
    finally:
        print('exiting context')



































  