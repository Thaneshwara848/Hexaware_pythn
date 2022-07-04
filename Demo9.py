class Demo9:
    name="Thanesh";
   # age=35; ## __ private : __age =35
   # _salary=35000; ## _protected : _salary =35000 
    def __init__(self,name,age,salary):
        print("COnstructor ");
        self.name=name;
        self.age=age;
        self.salary=salary;

    def mthod(self):
        print("HI Method...!");
        print("Name: ",self.name)
        print("Age :",self.age);
        print("Salary :",self.salary);


class D (Demo9):
    def __init__(self):
        print("D class COnstructor ",self.name); # public  no under score 
        #print("D class COnstructor ",self.age); # private  __ double underscore 
        #print("D class COnstructor ",self.salary); # proteted  _ single underscore 
        
        
d=Demo9("Raju",25,35000);
d.mthod();



d1=D();

#print("My Name is ",d.name) public 
