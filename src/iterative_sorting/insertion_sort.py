def simple_implementation(arr):
    # loop from 1 to end of array
    for i in range(1, len(arr)):
        temp = arr[i]

        j = i 

        while j > 0 and temp < arr[j - 1]:
            # copy element to left to this position
            arr[j] = arr[j-1]

            j -= 1

        arr[j]  = temp 
    return arr 



# Sorting books!

class Book:
    def __init__(self, author, title, genre):
        self.author = author 
        self.title = title 
        self.genre = genre 


    def __repr__(self):
        return f'{self.title} by {self.author} in {self.genre}'



def insertion_sort(books): 
    for i in range(1, len(books)):

        temp = books[i]

        j = i
        print(type(temp))
        # while we're not at the front of the list and these two should be swapped
        while j > 0 and temp.genre < books[j-1].genre: 
            books[j] = books[j -1]
            j -= 1 

        books[j] = temp 
    return books 


books = [Book("Melville", "Moby Dick", "Whale Stories"), Book("Hamlet", "Immortal William", "emo danish prince")]
print(insertion_sort(books))