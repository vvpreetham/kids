file = ['dabu','yaju','athu','dabu','athu','athu','yaju']
word_count =[]
word_exists=[]

def fetch(find_word, word_count):
    row=0
    for word_tuple in word_count:
        word, count = word_tuple[0], word_tuple[1]
        if(find_word==word):
            return count, row
        row+=1
        
for word in file:
    if(word not in word_exists):
        word_count.append([word,1])
        word_exists.append(word)
    else:
        count, row = fetch(word, word_count)
        count+=1
        word_count[row][1]=count
        
print(word_count)
