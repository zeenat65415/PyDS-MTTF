#func2 -function returning values(output)
#return keyword is used in python to get back the answer


def get_salary():#(function) get_salary: () -> float
    val = int(input("Enter SALARY =>"))#in function we generally dont use input(unless it is input taking function)
    fine= .9
    return val * fine
     
print("salary", get_salary())   #empty round bracket means taking no input 

final_salary = get_salary() + 1000
print("Final salary =>", final_salary)
#or
ans = get_salary()
print("sal =>", ans)

final_salary = ans+ 1000
print("Final sal =>", final_salary)

def amount():
    p = int(input('Enter Principal:'))
    r = float(input("Enter Rate:"))
    t = int(input("Enter Time:"))
    si = p*r*t / 100
    amt = p + si
    return amt , si

amt , si= amount()#(function) amount: () -> tuple[float, float]
print(f"the Amount will be {amt} on Simple interest {si}")
#or this way
print(f"the Amount will be {amount()}")
# print(f"the Amount will be {amount()[0]}")#if [2] or more  is given IndexError: tuple index out of range

    