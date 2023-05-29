class library2:
    def __init__(self,name,list):
        self.bname=name
        self.blist=list
        self.lenddict={}
    def display_book(self):
        print(f"We have following books in our Library - {self.bname}")
        for book in self.blist:
            print(book)
    def lendbok(self, user_name, book_name):
        if book_name not in self.blist:
            print("This book is not available in library")
        else:    
            if book_name not in self.lenddict.keys():
                self.lenddict.update({book_name : user_name})
                print('Your book has been updated')
            else:
                print(f"This book is already owned by {self.lenddict[book_name]}")
    def return_bok(self,book_name):
        if book_name in self.lenddict.keys():
            del self.lenddict[book_name]
            print("Your book has been returned")
        else:
            print("Enter Valid name of book")

    def add_book(self, book_nme):
        self.blist.append(book_nme)
        print("Your book has been added")

sch_lib=library2('Library 1960', ['harry potter', '101 stories', "guliver's travel", "anna frank",
 "lord of the rings", "dictionery","war and peace",'the guide','the white tiger','a suitable boy'])        
while True:
    print(f"Welcome to {sch_lib.bname}\nPress 1 for display books\n Press 2 for lend a book \nPress 3 for Return a book\n Press 4 for Add a book")
    user_input=input('')
    if user_input=='1':
        sch_lib.display_book()
    elif user_input=='2':
        Your_name=input("Enter your name  :")
        book=(input("Enter name of book you want to lend  :")).lower()
        sch_lib.lendbok(Your_name, book)
    elif user_input=='3':
        Enter_book=input("Enter Name of book you want to return  :")
        sch_lib.return_bok(Enter_book)
    elif user_input=='4':
        ad_book_name=input("Enter name of book you want to Add  :")
        sch_lib.add_book(ad_book_name)
    else:
        print("Enter vaild option")
        continue
    choice=''
    while choice!=('c').lower() and choice!= ('q').lower():
        choice=input("Press 'c' for Continue or Press 'q' for quit  :")
        if choice==('c').lower():
            continue
        elif choice==('q').lower():
            quit()


        


