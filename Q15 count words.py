# 15.	Count Words in a String – Count number of words in a sentence.
sentence = input("Enter a sentence: ")
word= sentence.split()
word_count = len(word)
print (word_count)
# for counting letters only 
letters_only = sentence.replace(" ", "")
letter_count = len(letters_only)
print(f"Total letters: {letter_count}")