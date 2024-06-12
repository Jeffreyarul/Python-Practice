def find_second_most_repeated_word(text):
    words = text.split()

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_word_count) >= 2:
        return sorted_word_count[1][0]
    else:
        return None

input_text = "I realized my happiness was artificial."

second_most_repeated_word = find_second_most_repeated_word(input_text)

print("Second most repeated word:", second_most_repeated_word)
