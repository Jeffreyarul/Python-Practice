def swap_first_chars(s1, s2):
    if len(s1) > 0 and len(s2) > 0:
        s1, s2 = s2[0] + s1[1:], s1[0] + s2[1:]
        return " ".join([s1, s2])

s1 = "welcome" 
s2 = "good"
result = swap_first_chars(s1, s2)
print(result)
