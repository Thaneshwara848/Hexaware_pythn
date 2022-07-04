class Employee :
    def __init__(xyz):
        xyz.uid= input("Enter ID : ");
        xyz.name =input("ENter Name :");
        xyz.age = input ("ENter Age :");
        xyz.salary= input("ENter Salary :");
        xyz.designation=input("ENter Designation :");

        #print("Name :",name , "Age :",age ," Salary :",salary ," Designation :",designation)
    def display(xyz):
        print("ID :",xyz.uid )
        print("Name :",xyz.name );
        print("Age :",xyz.age ,)
        print(" Salary :",xyz.salary );
        print(" Designation :",xyz.designation)
        

e=Employee();
e.display();



def  emp():
        uid= input("Enter ID : ");
        name =input("ENter Name :");
        age = input ("ENter Age :");
        salary= input("ENter Salary :");
        designation=input("ENter Designation :");
    
        print("ID :",uid )
        print("Name :",name );
        print("Age :",age ,)
        print(" Salary :",salary );
        print(" Designation :",designation)

emp();
