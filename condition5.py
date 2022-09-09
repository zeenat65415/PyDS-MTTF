#nested condition(we can also use logical operator : (if con1 and cond2:))
email=input("Enter your email=>")

if '@'in email:
    if len(email)>=11:
        if".com"in email or ".org" in email:
            print("Your email look valid")
        else:
            print("INVALID domain")
    else:
            print("Lengrh of email not valid")
else:
    print("Your email does not have @")     #nested condition is applied .if we do not want nested condition we can use Logical OPERATORh(if cond 1 and cond2:)     
