def is_isogram(string):
    alpha_string = list(filter(str.isalpha, string.lower()))
    return len(set(alpha_string)) == len(alpha_string)

