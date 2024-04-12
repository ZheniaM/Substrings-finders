__all__=['knuth_morris_pratt']

def kmp(source, substr):
    lps = [0] * len(substr)
    j = 0
    for i in range(1, len(substr)):
        while j > 0 and substr[i] != substr[j]:
            j = lps[j-1]
        if substr[i] == substr[j]:
            j += 1
        lps[i] = j

    j = 0
    matches = []
    for i in range(len(source)):
        while j > 0 and source[i] != substr[j]:
            j = lps[j-1]
        if source[i] == substr[j]:
            j += 1
        if j == len(substr):
            matches.append(i - len(substr) + 1)
            j = lps[j-1]

    return matches

def main():
    s = input("Enter string:\n")
    t = input("Enter substring:\n")
    print(kmp(s, t))


if __name__ == "__main__":
    main()