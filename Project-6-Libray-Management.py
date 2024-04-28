books=[]#Created a empty list
no_of_books=1#for counting the no of books
class Library_management:
    def __init__(self,book,no_of_book):
        self.book=book
        self.no_of_book=no_of_book
        books.append(self.book)#putting book in the empty list
    def manager_of_library(self):
        for index,book in enumerate(books):
            print(f"{index+1}.{book}")
        print(f"The total number of books in the library is {no_of_books}")
def main_work():# ye function banaya gya sirf {DRY} code maintain karne ke liye
    global no_of_books# ye is liye diye hai kyuki library variable jo niche hai usme no' of books me error aa raha tha.
    book=input("Provide name of the book:")
    library=Library_management(book,no_of_books)
    library.manager_of_library()
    no_of_books=no_of_books+1#adding the books as it work infinately through while loop
main_work()
while True:
    try:
        ask=int(input("Choose (1) for continue adding books in library or (2) for Quit:"))
        if ask==2:
            break
        elif ask==1:
            main_work()
        else:
            print('provide "1" and "2" only')
    except:
        print('provide integer only')
