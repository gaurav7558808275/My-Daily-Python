def reverse_string(str):
    txt = ""
    for t in str:
        txt = t + txt
    return txt


s = "kumar gaurav"
print("reversed string is: ", reverse_string(s))
"""print(reverse_string(s))"""
