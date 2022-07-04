import os

myfile=input("Enter the file name to Delete ? ");


if os.path.exists(myfile):
    os.remove(myfile);
    print("FIle Deleted ");
else:
    print("FIle Does Not Exists ..!");
