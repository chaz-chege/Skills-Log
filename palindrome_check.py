#Problem:Write a function that takes a string and returns True if it reads the same forwards and backwards, False otherwise.
word = "racecar"
def is_palindrome(word):
    N = len(word)
    for i in range(N):
        if word[i] != word[N-1-i]:
            return False
    return True    
print(is_palindrome(word))        
 