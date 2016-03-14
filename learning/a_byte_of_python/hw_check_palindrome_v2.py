# Time-stamp: <2016-03-14 Mon 13:55:41 Shaikh>
# Check an input (string) whether it's palindrome
# regardless of the white spaces or punctuation in it.


def is_palindrome(text):
    """Check every character in text.

    If it is alphabetic, append it to a list.
    Lowercase the list first to make it case insensitive
    and then reverse the list. At last, return whether it
    is the same as the un-reversed version."""
    text_l = list()
    for l in text:
        if l.isalpha():
            text_l.append(l.lower())
    text_rev = text_l.copy()
    text_rev.reverse()
    return text_l == text_rev


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is palindrome.")
else:
    print("Oops, no, it's not palindrome.")
