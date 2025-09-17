def get_book_word_count(book):
    return len(book.split())

def get_book_character_count(book):
    book = book.lower()
    book_dict = {}

    for c in book:
        if c in book_dict:
            book_dict[c] += 1
        else:
            book_dict[c] = 1 

    return book_dict

def sort_on(items):
    return items["num"]

def get_book_sorted_list(book_dict):
    book_list = []
    for c , n in book_dict.items():

        book_list.append({"char" : c , "num" : n })
    book_list.sort(reverse=True,key=sort_on)
    return book_list
