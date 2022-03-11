#3. Write a menu driven program to perform the following functions on strings:
#a. Find the length of string
#b. Return maximum of three strings
#c. Accept a string and replace every successive character with ‘#’ Example- For Given string ‘Hello World’ returned string is ‘H#l#o W#r#d’.
#d. Find number of words in the given string

def A():
    a=input("enter the string: ")
    l=len(a)
    print('length:  ',l)
    
def B():
    a=input("enter 1st: ")
    b=input("enter 2nd: ")
    c=input("enter 3rd: ")
    m=max(len(a),len(b),len(c))
    if m==len(a):
        s=a
    if m==len(b):
        s=b
    if m==len(c):
        s=c
    print('maximum:', s)
    
def C():
    a=input("enter the string: ")
    a=a+" "
    r=""
    str=""
    l=len(a)
    for x in range(0,l):
        if a[x]!=' ':
            r=r+a[x]
         
        elif a[x]==' ':
        
            for s in range(0,len(r)):
                if s%2!=0:
                    str=str+'#'
                elif s%2==0:
                    str=str+r[s]
            str=str+' '
            r=""
    print(str)

def D():   
    a=input("enter the string: ")
    a=a+" "
    c=0
    r=""
    l=len(a)
    for x in range(0,l):
        if a[x]!=' ':
            r=r+a[x]
        
        elif a[x]==' ':
            c+=1
    print(c)

print("""a. Find the length of string
b. Return maximum of three strings
c. Accept a string and replace every successive character with ‘#’ Example- For Given string ‘Hello World’ returned string is ‘H#l#o W#r#d’.
d. Find number of words in the given string
""")
f= input("enter choice")
if f=='a':
    A()
    
if f=='b':
    B()
if f=='c':
    C()
if f=='d':
    D() 
