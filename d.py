def replace_except_first(s):
    if len(s) > 0:
        first_char = s[0]
    replaced_string = first_char + s[1:].replace(first_char, '#')
    return replaced_string 
s = "restart"
result = replace_except_first(s)
print(result)
