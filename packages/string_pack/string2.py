def str_palindrome(x):
    """for checking palindrome"""
    if x[::] == x[::-1]:
        return 'Is palindrome'
    else:
        return 'Not palindrome'


def str_duplicate_remove(li):
    """remove duplicates"""
    s = ''
    for i in li:
        if i not in s:
            s += i
        else:
            continue
    return s
