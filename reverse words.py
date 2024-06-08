def reversewords(sentence):
    words = sentence.split()  
    print(words)
    reversedwords=[word[::-1] for word in words] 
    reversedsentence = ' '.join(reversedwords) 
    return reversedsentence

input = input("Enter a sentence: ")
print(type(input))
reversedsentence = reversewords(input)
print("Reversed words:", reversedsentence)
