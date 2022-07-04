#read the file

f =open("Emp.txt","r");
print(f.read());

f2 =open("C:\\Users\Thanesh\Desktop\Angualr\MyData.txt","r");
print(f2.read());

# write the data :

a =open("Emp.txt","a");
a.write("/n HI Just To check ");
a.close();




newFile= open("Emp1.txt","x");
