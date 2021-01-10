from collections import defaultdict

def num_encoding_1(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1:
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += num_encoding(s[2:])
    
    total += num_encoding(s[1:])
    return total

val = num_encoding_1('202')
print(val)

#===========================================

def num_encoding_2(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(s)]

    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2] <= 26):
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]
