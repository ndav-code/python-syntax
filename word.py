def print_upper_words(words):
    """ For a list of words, print out each word on a separate line in all uppercase.
print_upper_words(["ebook", "tree", "Ekamy", "chair"]) 
    """
    
    for word in words:
        print(word.upper())

print_upper_words(["ebook", "tree", "Ekamy", "chair"]) 


def print_upper_words2(words):
    """Change that function so that it only prints words that start with the letter ‘e’ 
    (either upper or lowercase)
    print_upper_words(["ebook", "tree", "Ekamy", "chair"])
    EBOOK
    EKAMY """

    for word in words:
       if word.startswith("e") or word.startswith("E"):
           print (word.upper())

print_upper_words2(["ebook", "tree", "Ekamy", "chair"]) 

def print_upper_words3(words, start_with):

    """Make your function more general: you should be able to pass in a set of letters, and it only prints
    words that start with one of those letters. For example: 
    this should print "HELLO", "HEY", "YO", and "YES"
    print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})"""
 
    for word in words:
        for letter in start_with:
            if word.startswith(letter):
                print(word.upper())
                
print_upper_words3(["ebook", "tree", "Ekamy", "chair"],start_with=["c","t"])            

# print(print_upper_words(["ebook", "tree", "Ekamy", "chair"]), "should be: EBOOK TREE EKAMY CHAIR") 
#print(print_upper_words2(["ebook", "tree", "Ekamy", "chair"]), "should be: EBOOK EKAMY") 
# print(print_upper_words3(["ebook", "tree", "Ekamy", "chair"],start_with=["c","t"]), "should be:TREE CHAIR")
