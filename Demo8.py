class Demo :
    def __init__(self) :
        print("Constriuctor ");
    def display(self):
        print("Hello ");

class Clerk :
    def __init__(self) :
        print(" clerk Constriuctor ");
    def display(self):
        print("Helo clerk ");

class Dev(Clerk,Demo):
    def __init__(self) :
        print(" Dev  Constriuctor ");
    def display(self):
        print("Helo Dev  ");

d =Dev();
d.display();

#single 
#multilevel
#multile
#hybried
#Hyrichy

#over loging is not pissible         
