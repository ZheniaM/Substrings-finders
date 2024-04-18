__all__=['build_suffix_tree']

import math

def build_suffix_array(s):
    n = len(s)
    suffixes = [(i, s[i:]) for i in range(n)]
    suffixes.sort(key=lambda x: x[1])
    position = [0] * n
    for i in range(n):
        position[suffixes[i][0]] = i
    lcp = [0] * n
    h = 0
    for i in range(1, n):
        k = suffixes[i][0]
        while h > 0 and suffixes[i][1][:h] != suffixes[position[k]][1][:h]:
            h = lcp[h - 1]
        h += 1
        lcp[i] = h
    return suffixes, position, lcp

def search_substring(s, substring):
    suffixes, position, lcp = build_suffix_array(s)
    n = len(s)
    m = len(substring)
    lo = 0
    hi = n - m
    occurrences = []
    while lo < hi:
        mid = (lo + hi) // 2
        if substring < suffixes[mid][1][:m]:
            hi = mid
        elif suffixes[mid][1][:m] < substring:
            lo = mid + 1
        else:
            i = position[mid]
            j = 0
            while i < n and j < m and suffixes[i][1][j] == substring[j]:
                occurrences.append(i)
                i += 1
                j += 1
            lo = mid + 1
    if lo < n and s[lo:lo + m] == substring:
        occurrences.append(lo)
    return occurrences


def main():
    s = input("Enter the string: ")
    substring = input("Enter the substring: ")
    occurrences = search_substring(s, substring)
    print(occurrences)
    
    
if __name__ == "__main__":
    main()