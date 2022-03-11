#Q1. Write a function that finds the sum of the
#a) first n odd terms
#b) first n even terms
#c) 1, 2, 4, 3, 5, 7, 9, 6, 8, 10, 11, 13.. till n-th term

def A():
   n=int(input("enter n:"))
   s=0
   for a in range(1,n+1):
     if (a%2)==1:
         s=s+a
   print("sum:",s)

def B():
    n=int(input("enter n:"))
    s=0
    for a in range(1,n+1):
       if (a%2)==0:
          s=s+a
    print("sum:",s)
def C():
    num =int(input("enter"))
    if num < 0:
      print("Enter a positive number")
    else:
      sum = 0
   
      while(num > 0):
        sum += num
        num -= 1
      print("The sum is", sum)

    
print("a) first n odd terms")
print("b) first n even terms")
print("c) 1, 2, 4, 3, 5, 7, 9, 6, 8, 10, 11, 13.. till n-th term")
f =input("enter choice-")
if f=='a':
    A()
    
if f=='b':
    B()
if f=='c':
    C()
