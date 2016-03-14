# Time-stamp: <2016-03-14 Mon 13:19:27 Shaikh>
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


def ex_alpha(text):
    result = list()
    for l in text:
        if l.isalpha():
            result.append(l)
    return ''.join(result).lower()

something = input('Enter text:')
if is_palindrome(ex_alpha(something)):
    print("Yes, it is palindrome.")
else:
    print("Oop, no, it's not palindrome.")
