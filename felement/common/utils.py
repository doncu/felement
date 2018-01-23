
__all__ = ['chunks', 'transliterate']


def chunks(lst, size):
    """Yield successive size chunks from lst."""
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


TRANSLIT_LOWER_REPLACEMENTS = {
    # 0-9
    u'0': u'0',
    u'1': u'1',
    u'2': u'2',
    u'3': u'3',
    u'4': u'4',
    u'5': u'5',
    u'6': u'6',
    u'7': u'7',
    u'8': u'8',
    u'9': u'9',

    # a-z
    u'a': u'a',
    u'b': u'b',
    u'c': u'c',
    u'd': u'd',
    u'e': u'e',
    u'f': u'f',
    u'g': u'g',
    u'h': u'h',
    u'i': u'i',
    u'j': u'j',
    u'k': u'k',
    u'l': u'l',
    u'm': u'm',
    u'n': u'n',
    u'o': u'o',
    u'p': u'p',
    u'q': u'q',
    u'r': u'r',
    u's': u's',
    u't': u't',
    u'u': u'u',
    u'v': u'v',
    u'w': u'w',
    u'x': u'x',
    u'y': u'y',
    u'z': u'z',

    # а-я
    u'а': u'a',
    u'б': u'b',
    u'в': u'v',
    u'г': u'g',
    u'д': u'd',
    u'е': u'e',
    u'ё': u'e',
    u'ж': u'zh',
    u'з': u'z',
    u'и': u'i',
    u'й': u'y',
    u'к': u'k',
    u'л': u'l',
    u'м': u'm',
    u'н': u'n',
    u'о': u'o',
    u'п': u'p',
    u'р': u'r',
    u'с': u's',
    u'т': u't',
    u'у': u'u',
    u'ф': u'f',
    u'х': u'h',
    u'ц': u'ts',
    u'ч': u'ch',
    u'ш': u'sh',
    u'щ': u'sch',
    u'ъ': u'',
    u'ы': u'y',
    u'ь': u'',
    u'э': u'e',
    u'ю': u'yu',
    u'я': u'ya',
}


def transliterate(string, words_separator=u'-'):
    """
    Transliterates a string char by char, without regular expressions,
    replace() calls and checking for missing cyrillic symbols.
    :param string: string to transliterate
    :param words_separator: symbol to replace symbols not from the replacement
    dictionary
    :return: transliterated string in lowercase
    """
    string = string.lower()
    fragments = []
    for char in string:
        new_fragment = TRANSLIT_LOWER_REPLACEMENTS.get(char, words_separator)
        if new_fragment != words_separator or (fragments and fragments[-1] != words_separator):
            fragments.append(new_fragment)
    return ''.join(fragments).strip(words_separator)
