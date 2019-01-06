# -*- coding: utf-8 -*-

####################################################################### F-string

f'{a} % {b} = {a % b}'

name = 'Python'
f'{name} rocks!'


class Person:
    def __init__(self, name, age, **custom_attributes):
        self.name = name
        self.age = age
        for attr_name, attr_value in custom_attributes.items():
            setattr(self, attr_name, attr_value) 
            
            
            
############################################################## Switch Simulation  


def dow_swtich_fn(dow):
    if dow ==1:
        fn = lambda: print('Mon')
    elif dow==2:
        fn = lambda: print('Tue')
    elif dow==3:
        fn = lambda: print('Wed')        
    elif dow==4:
        fn = lambda: print('Thur')       
    elif dow==5:
        fn = lambda: print('Fri')
    else:
        fn = lambda: print('asd')        
    return fn()    
         

##########################

 
def dow_swtich_dict(dow):     
    dow_dict = {
            1: lambda: print('Mon'),
            2: lambda: print('Tue'),
            3: lambda: print('Wed'),
            4: lambda: print('Thu'),
            5: lambda: print('Fri'),
            'default': lambda: print('asd'),
            }     
    
    return dow_dict.get(dow, dow_dict['default'])()
    
    
################    
    

def switcher(fn):
    registry = dict()
    registry['default'] = fn
    
    def register(case):
        def inner(fn):
            registry[case] = fn
            return fn
        return inner
    
    def decorator(case):
        fn = registry.get(case, registry['default'])
        return fn()
    
    decorator.register = register
    return decorator
            
    
@switcher
def dow():
    print('asd')

dow.register(1)(lambda: 'Mon')
dow.register(2)(lambda: 'Tue')
dow.register(3)(lambda: 'Wed')
dow.register(4)(lambda: 'Thu')
dow.register(5)(lambda: 'Fri')

  
    
####################################################################### __main__    
    
print(f'loading run.py: __name__ = {__name__}')    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    