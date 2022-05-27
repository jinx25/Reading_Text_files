# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename,"r") as file:
        content = file.read()
    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
   
    # dict to hold key=value of words/number of occurrence

    dictionary = {}

    # converting the string into list
    text_to_list = text.split() #list

    # return {"a":10, "would":20}
    for word in text_to_list:
        dictionary[word] = text_to_list.count(word)

    return dictionary

dictionary = count_words()
print(dictionary)

count_words()    
