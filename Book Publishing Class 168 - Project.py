class bookshelf:
    def __init__(self,name,author,price,year):
        self.name= name
        self.author=author
        self.price = price
        self.year= year
        
    def add_book(self):
        print("Name : " +self.name)
        print("Author : " +self.author)
        print("Price : " +str(self.price))
        print("Publishing Year : " +self.year)
        print("Book Added")
  
    def years_since_published(self):
        published_year= 2022-int(self.year)
        print("This book was published " +str(published_year)+" years ago")
     

book1 = bookshelf("One Of us is lying","Karen M. McManus",306,"2017")
book1.add_book()
book1.years_since_published()

book2 = bookshelf("One Of Us is Next","Karen M. McManus",272,"2020")
book2.add_book()
book2.years_since_published()
