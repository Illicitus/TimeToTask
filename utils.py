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


def time_seconds(self, obj, field_name, format='%d %b %Y %H:%M:%S'):
    """
    Take object, field name with date field and strftime format.
    By default format "%d %b %Y %H:%M:%S".
    Return date in that format.
    """
    return obj.date.strftime("%d-%m-%Y")

time_seconds.admin_order_field = 'date'
time_seconds.short_description = 'Precise Time'



# if __name__ == '__main__':
#     reverse_string("I love hamburgers")
#     words_count("I love hamburgers")
