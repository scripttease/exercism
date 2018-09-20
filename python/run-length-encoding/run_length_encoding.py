def decode(string):
    if len(string) <= 1:
        return string
    else:
    # if the 0th elem is a digit
        if string[0].isdigit():
            i = 1
            end = len(string)
    # while 0th elem to ith elem are all digits
            while string[i].isdigit() and i < end:
                i += 1
            return int(string[:i]) * string[i] + decode(string[(i+1):])
        else:
            head = string[0]
            i = 1
            return head + decode(string[i:])

def encode(string):
    if len(string) <= 1:
        return string
    else:
        i = 1
        head = string[0]
        end = len(string)

        # while first elem is same as ith elem, increment i
        while i < end and head == string[i]:
            i += 1
        # when first elem is different to ith elem, slice string at i and encode tail.
        if i <= 1:
            return head + encode(string[i:])
        else:
            return str(i) + head + encode(string[i:])


# def encode(string):
#     head = string[0]
#     max_index = len(string)
#     ind = 1
#     while ind < max_index and head == string[ind]:
#         ind += 1
#         # tail = string[ind:]
#     return head + str(ind) + encode(string[ind:])
