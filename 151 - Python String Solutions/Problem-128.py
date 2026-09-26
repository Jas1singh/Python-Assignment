# Problem 128:

pattern = "abba"
s = "dog cat cat dog"

words = s.split()

if len(pattern) != len(words):
    print(False)
else:
    p_to_word = {}
    word_to_p = {}
    valid = True

    for i in range(len(pattern)):
        p = pattern[i]
        word = words[i]

        if p in p_to_word and p_to_word[p] != word:
            valid = False
            break

        if word in word_to_p and word_to_p[word] != p:
            valid = False
            break

        p_to_word[p] = word
        word_to_p[word] = p

    print(valid)
