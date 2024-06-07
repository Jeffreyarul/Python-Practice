def reversewords(sentence):
    words = sentence.split()  
    reversedwords = [word[::-1] for word in words] 
    reversedsentence = ' '.join(reversedwords) 
    return reversedsentence

input = input("Enter a sentence: ")
reversedsentence = reversewords(input)
print("Reversed words:", reversedsentence)
