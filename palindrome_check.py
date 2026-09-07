#Problem:Write a function that takes a string and returns True if it reads the same forwards and backwards, False otherwise.
word = input("Enter a word you would like to check if it is a palindrome:")
def is_palindrome(word):
    N = len(word)
    for i in range(N//2):
        if word[i] != word[N-1-i]:
            return False
    return True    
print(is_palindrome(word))        
 