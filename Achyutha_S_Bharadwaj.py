a = int(input("Enter Number :"))
b = int(input("Enter Number :"))
c = int(input("Enter Number :"))
if a>b>c:
    print(b)
else:
    if a>c>b:
        print(c)
    else:
        if b>c>a:
            print(c)
        else:
            if b>a>c:
                print (a)
            else:
                if c>a>b:
                    print(a)
                else:
                    if c>b>a:
                        print(b)
                    else:
                        print("ALL THE NUMBERS ARE EQUAL")
 # Name=Achyutha S Bharadwaj
 # Email:asb20029@gmail.com 
