f= open("MyEmp.txt","x");


a =open("MyEmp.txt","a");

name =input("ENter Name :");
age = input ("Enter Age :");
salary = input ("Enter Salary ");
Desigantion= input ("Enter Desigantion :");

a.write(name)
a.write(age )
a.write(salary)
a.write(Desigantion);

a.close();


readdate =open("MyEmp.txt","r");
print(readdate.read());
