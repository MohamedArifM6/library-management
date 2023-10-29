# Library Management Task

#------adding books------------------------
class manager:
    books=[]
    def book(self):
        nob=int(input("Enter Number of Books :"))
        for i in range(nob):
            b_name=input("Enter a book name :")
            author=input("Enter Author name :")
            rate=int(input("Enter Book rate :"))
            year=int(input("Enter a year :"))
            add=[b_name,author,rate,year]
            self.books.append(add)
        print(self.books)
        print("Registered Successfully")

class customer(manager):
    rbooks=[]
#---------------search books-------------------------
    def search(self):
        if len(self.books)==0:
            print("Not Available")
        else:
            
                print("Available")
                search=input("Enter book name or author name or year :")
                if search.lower()=="book name":
                    bookname=input("Enter Book Name :")
                    for i in self.books:
                        if bookname in i:
                            print("Book name :",i[0],"\nAuthor Name :",i[1])
                            break
                    else:
                        print("Not available")
                elif search.lower()=="author name":
                    a_name=input("Enter Author Name :")
                    for i in self.books:
                        if a_name in i:
                            print("Book name :",i[0],"\nAuthor Name :",i[1],"\nPrice :",i[2],"\nYear :",i[3])
                            break
                    else:
                        print("Not available")
                elif search.lower()=="year":
                    yr=int(input("Enter Year :"))
                    for i in self.books:
                        if len(i)>1:
                            if yr>i[3]:
                                print("Book name :",i[0])
                else:
                    print("please check your value")

#----------purchasing books---------------------------
                    
    def purchase(self):
        bsearch=input("Enter Book Name :")
        for i in self.books:
            if bsearch in i:
                rent=100
                rentd=int(input("Enter no of days you want rent :"))
                print("Per Day Rent Amount is :",rent)
                print("Rent Amount :",rentd*rent)
                print("Thanks for purchase")
                for j in i:
                    self.rbooks.append([j,rentd])
                    break 
                i.clear()
                break
        else:
            if len(self.rbooks)>0:
                for i in self.rbooks:
                    if bsearch in i:
                        print(bsearch,"Book is",i[1],"days unavailable")
                        break
                else:
                    print("Not Available")
            else:
                print("Not Available")

obj=customer()
#-----------main program start------------------------------
while True:
    print("Library management")
    print("1 - Manager\n2 - People\n3 - Rent\n4 - Exit")
    enter=int(input("Enter a number :"))
    if enter==1:
        obj.book()
    elif enter==2:
        obj.search()
    elif enter==3:
        obj.purchase()
    elif enter==4:
        print("Thank You")
        break
    else:
        print("please check your value")
