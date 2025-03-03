def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def get_book_words(file_path):
    book_text = get_book_text(file_path)
    words_list = book_text.split()
    words_number = len(words_list)
    return words_number

def num_char(text):
    dic  = {}
    for n in text:
        n = n.lower()
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
    return dic        

def sort_dec(dictionary):
    dic_list = []
    for char, count in dictionary.items():
        char_dict = {"char": char, "count": count}
        dic_list.append(char_dict)
    
    def get_count(item):
        return item["count"]
    
    dic_list.sort(reverse=True, key=get_count)
    
    return dic_list
       
       
