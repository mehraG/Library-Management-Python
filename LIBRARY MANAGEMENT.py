import MenuLib
import Book
import issue
while True:
 Book.clrscreen()
 print("\t\t\t Library Management\n")
 print("==============================================================")
 print("1. Book Management ")
 print("2. Members Management ")
 print("3. Issue/Return Book ")
 print("4. Exit ")
 print("===============================================================")
 choice=int(input("Enter Choice between 1 to 4-------> : "))
 if choice==1:
     MenuLib.MenuBook()
 elif choice==2:
     MenuLib.MenuMember()
 elif choice==3:
     MenuLib.MenuIssueReturn()
 elif choice==4:
     break
 else:
     print("Wrong Choice......Enter Your Choice again")
     input("Enter any key to continue")
