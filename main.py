print("Welcome to my library! ")
book = input("Which book do you want to buy? ")
type = input("Which author do you like most? ")
pricebook = input("Budget")

print("Yes", book, "is a really nice book,", type, "is also a fantastic author!")

if pricebook >= 500:
    print("The book is too costly")

    wants_to_play = input("Do you want to buy anyways? ")


else:
    print("Not sufficient budget.....")