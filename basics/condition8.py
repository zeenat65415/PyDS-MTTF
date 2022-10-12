num=int(input("Enter a number:"))


match num:
    case 1:
       print("Sunday")
    case 2:
       print("Monday")
    case 3:
        print("Tuesday")  
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday") 
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
         print("Invalid data")# here no break like java (case _: act as default case,if none of the above mentioned case ia entered print("invalid data"))

       
       

