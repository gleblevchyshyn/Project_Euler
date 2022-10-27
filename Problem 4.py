def is_palindrome(digit):
    return list(str(digit)) == list(str(digit)[::-1])


def largest_palindrome(n):
    palindroms = []
    upper_limit = (10 ** n) - 1

    lower_limit = 1 + upper_limit//10

    for i in range(upper_limit, lower_limit, -1):
        for j in range(i, lower_limit, -1):
            product = i * j
            if is_palindrome(product):
                palindroms.append(product)

    return max(palindroms)


print(largest_palindrome(3))