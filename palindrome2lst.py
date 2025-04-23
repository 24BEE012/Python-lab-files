lst = ['madam', 'Python', 'malayalam', 12321]

def is_palindrome(word):
    return str(word) == str(word)[::-1]

palindromes = [str(item) for item in lst if isinstance(item, str) and is_palindrome(item)]
print("Palindromes in the list:", palindromes)
