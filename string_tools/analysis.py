def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]