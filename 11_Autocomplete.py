WORDS = ['foo', 'bar', ...]
def autocomplete(s):
    result = []
    for w in WORDS:
        if w.startswith(s):
            result.append(w)
    return result