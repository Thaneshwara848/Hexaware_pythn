
mydata=[]; list

for i in range(5):
    name = input("ENter Name : ");
    mydata.append(name);

for data in mydata :
    print(data);


#mydata.remove("A");

#for data in mydata :
#   print(data);



print("Length : " , len(mydata));
print("Max : ", max(mydata));
print("Min : ", min(mydata));
