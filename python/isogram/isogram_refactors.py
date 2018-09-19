def is_isogram(string):
    # Use a filter which filters out the rhs if the lhs fn returns false(?)
    alpha_string = list(filter(str.isalpha, string.lower()))
    return len(set(alpha_string)) == len(alpha_string)

# Attempt 2

def is_isogram(string):
    alpha_string = string.lower().replace(" ", "").replace("-","")
    # NB don't need if/else
    return len(set(alpha_string)) == len(alpha_string)

# Attempt 1

def is_isogram(string):
    alpha_string = string.lower().replace(" ", "").replace("-","")
    if len(set(alpha_string)) == len(alpha_string):
        return True
    else:
        return False
