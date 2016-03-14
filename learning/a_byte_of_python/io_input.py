# Time-stamp: <2016-03-14 Mon 09:18:59 Shaikh>
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input('Enter text:')
if is_palindrome(something):
    print("Yes, it is palindrome.")
else:
    print("No, it is not a palindrome.")
