'''fname=input("Enter any filename:")
f1=open(fname,"w")
f1=open(fname,"r")
print("File-name:",f1.name);
print("File-is Mode",f1.mode);
print("File-is Readable",f1.readable());
print("File-is Writable",f1.writable());
print("File-is Closed:",f1.closed);
f1.close();
print("File-is Closed:",f1.closed)
'''

fname=input("Enter any filename:")
f1=open(fname,"w")
f1=open(fname,"a")
print("File-is opened for Writing data");
# f1.write("Sai Kumar\n");
# f1.write("India Country\n");
# f1.write("Hyderabad City\n");
list1 = ["Sai\n","Ram\n","Ali\n","Tom\n","Pop\n"];
f1.writelines(list1);
f1.close();
print("File-Data Writing is done");