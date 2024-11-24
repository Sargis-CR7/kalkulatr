import math
def number():
    while True:
          try:
            x=float(input("asa tiv"))
          except ValueError:
              print("miayn tver")




def choice():
     while True:
        try:
            ch=("+","-","/","*","ast","armat")
            z=input("yntreq gorcoxutyun")
            if z not in ch:
                raise Exception
        except Exception:
            print("ch i meji gorcoxutyun")
        else:
            return z


def result():

    y=number()
    z=choice()
    c=number()


def gumarum(y,c):
     return sum(c,y)
        
def hanum(y,c):
 return y-c

def bajanum(y,c):
    try:
        if y!=0:
            return y//c
    except ZeroDivisionError:
        print("tivy zroyi chi bajanvum")
           

def bazmapatkum(y,c):
  
            return y*c

def astichan(y,c):
      return math.pow(y,c)
        
        
def armat(a):
    try:
        if a>0:
            return math.sqrt(a)
        elif a<0:
            raise Exception
    except Exception:
        print("tivy 0 ic mec petq e lini")



while True:
    
    a=int(input("asa tiv"))
    b=int(input("asa tiv"))
    x=input("yntreq gorcoxutyun")
    if x=="+":
        print(gumarum(a,b))
        
    elif  x=="-":
        print(hanum(a,b))
    
    elif x=="//":
        print(bajanum(a,b))

    elif x=="*":
        print(bazmapatkum(a,b))

    elif x=="ast":
        print(astichan(a,b))
    elif x=="armat":
        print(armat(a))





          
