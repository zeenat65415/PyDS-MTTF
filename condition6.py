email=input("Enter your email=>")
if '@' in email and len(email)>=11 and (".com" in email or "org" in email):
    print("badiya email hai")
else:
    print("ye email toh ni lag ra")   # same as condition4.py but more secure (AS exact error canot be verified by only authentic user easily)