def anagram_groups(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w.replace(" ", "")))
        if key not in groups:
            groups[key] = set()
        groups[key].add(w)
    return list(groups.values())

words_list = ['listen', 'silent', 'triangle', 'integral', 'debit card', 'bad credit']
print(anagram_groups(words_list))