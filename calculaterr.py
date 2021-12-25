x=int(input("enter a number:-"))

y=int(input("enter a number:-"))

o=input("enter operation:-")



if (o=="+"):
    print(f"{x}+{y}={x+y}")
    
elif (o=="-"):
    print(f"{x}-{y}={x-y}")
    
elif (o=="*"):
    print(f"{x}*{y}={x*y}")
    
elif (o=="/"):
    print(f"{x}/{y}={x/y}")
    
elif (o=="//"):
    print(f"{x}//{y}={x//y}")
    
elif (o=="%"):
    print(f"{x}%{y}={x%y}")
    
else:
    ("invalid operator")
