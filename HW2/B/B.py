def solution(x):
    replacement = x.replace('h', 'H', x.count('h') - 1)
    replacement = replacement.replace('H', 'h', 1)
    words = list(replacement)
    for word in words:
        if word == ' ':
            words.remove(word)
    words = words[::3]
    words = ' '. join(words)
    words = words.replace('1', 'one')
    return words
