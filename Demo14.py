month= set(["Jan","Feb","March","April"])
print(month);
month.add("Dec");

print(month);
for i in month:
    print(i);

print("======== Update =====");
month.update(["May","JUne","JUly"]);
print(month);

print("========Discard=======");
month.discard("Jan");
print(month);

print("========Remove =======");
month.remove("Feb");
print(month);

print("========POP  =======");
month.pop();
print(month);

print("========CLear   =======");
month.clear()
print(month);

print("=================UNION ==========");
d1={"A","B","C","X"}
d2={"D","E","F","X"}

print(d1.union(d2));

print(d1 & d2 );
print(d1.intersection(d2) );


 


