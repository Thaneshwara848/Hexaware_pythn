try :
    age=int(input("Enter Age :"))
    if age < 18 :
        raise ValueError;
    else:
        print("The age is valid ...!");
    
except  ValueError as v :
    print("The age must mre then 18  ")

