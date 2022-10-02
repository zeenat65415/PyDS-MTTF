#Final salary of an employee including DA and HRA

salary=int(input("Enter the salary => "))
if(10000 < salary <= 20000):
    da=salary*0.022
    hra=salary*0.06
    print("Final salary is=",salary+da+hra)
elif(20000 < salary <= 30000):
    da=salary*0.022
    hra=salary*0.07
    print("Final salary is=",salary+da+hra)
elif(30000 < salary <= 40000):
    da=salary*0.022 
    hra=salary*0.08
    print("Final salary is=",salary+da+hra)
elif(40000< salary <= 50000):
    da=salary*0.025
    hra=salary*0.077
    print("Final salary is=",salary+da+hra)
elif(50000 < salary <= 60000):
    da=salary*0.025
    hra=salary*0.08
    print("Final salary is=",salary+da+hra)
elif(60000 < salary <= 80000):
    da=salary*0.028
    hra=salary*0.09
    print("Final salary is=",salary+da+hra)
elif(80000 < salary <=100000):
    da=salary*0.032
    hra=salary*0.09
    print("Final salary is=",salary+da+hra)
elif(salary >100000):
    da=salary*0.035
    hra=salary*0.091
    print("Final salary is=",salary+da+hra)     
else:
    print("Final salary including DA and HRA is not calculated for salary below or equal to 10000")                           