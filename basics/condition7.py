email=input("enter your email=>")

if '@' not in email:
    print("your email doe not have @")

elif len(email)<11:
    print("length of email not valid")

elif".com" not in email and ".org"  not in email:#here we use and not or.
            print("invalid domain")
else:
         print("your email looks valid")#work like interpreter and recommended by developers (professional way)
        
