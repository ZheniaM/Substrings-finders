__all__=['boyer_moore_horspool']

def boyer_moore_horspool(source, substr):
    m = len(substr)
    n = len(source)
    bad_char_table = {char: m for char in set(substr)}
    for i in range(m - 1):
        bad_char_table[substr[i]] = m - i - 1
    shift = m
    indices = []
    while shift <= n:
        i = m - 1
        while i >= 0 and substr[i] == source[shift - 1]:
            i -= 1
            shift -= 1
        if i == -1:
            indices.append(shift)
            shift += m
        if shift < n:
            if source[shift] not in bad_char_table:
                shift += m
            else:
                shift += max(bad_char_table[source[shift]], m - i - 1)
    return indices

def main():
    s = input("Enter string:\n")
    t = input("Enter substring:\n")
    print(boyer_moore_horspool(s, t))


if __name__ == "__main__":
    main()
