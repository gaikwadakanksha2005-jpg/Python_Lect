def longestWord(sentence:str)->str:
    words=sentence.split()
    longest=""
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest
sentence=input("Enter a Sentence:")
print(longestWord(sentence))       