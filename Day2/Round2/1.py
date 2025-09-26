#In the hall of echoes, a word walks in and sees itself forward or backward, it never changes. Find the word (or write the spell/code) that reads the same from both sides. What is this special kind of word? 
w = input("Type a word: ")
if w == w[::-1]:
    print("This word is a Special word")
else:
    print("This word is NOT a Special word")
