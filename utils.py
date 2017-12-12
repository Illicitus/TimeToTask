def reverse_string(phrase):
    """
    Takes a phrase, reverse ech of words in phrase, without changing their
    position number and return it.
    """
    reverse_list = []

    for word in phrase.split(' '):
        reverse_list.append(word[::-1])

    return ' '.join(reverse_list)


def word_counts(phrase):
    """
    Takes a phrase, and return the count of words in it.
    """
    return len(phrase.split(' '))


# if __name__ == '__main__':
#     reverse_string("I love hamburgers")
#     words_count("I love hamburgers")
