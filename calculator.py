#!/usr/bin/env python

def add(a,b):
    return a+b

def sub(a,b):
    return (a-b)

def mult(a,b):
     retrun (a*b)

def div(a,b):
     return (a/b)

if __name__ == "__main__":
    while(True):
       # a=int(raw_input("Enter first number : "))
       # b=int(raw_input("Enter second number : "))
    
        print " \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit"
        choice=int(raw_input("Enter your choice : "))
        a=int(raw_input("Enter first number : "))
        b=int(raw_input("Enter second number : "))
        
       # choice=int(raw_input())
        if choice==1:
            res=add(a,b)
	    print res
        elif choice==2:
            res=sub(a,b)
	    print res
        elif choice==3:
	    res=mult(a,b)
	    print res
        elif choice==4:
            res=div(a,b)
	    print res
        elif choice==5:
	    exit(0)
