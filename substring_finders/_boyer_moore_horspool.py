from typing import Dict, List

__all__=['boyer_moore_horspool']

def boyer_moore_horspool(source: str, substring: str) -> List[int]:
    results = []
    n = len(source)
    m = len(substring)
    bad_character = {}
    if m == 0:
        return results

    for i in range(len(substring) - 1):
        bad_character[substring[i]] = len(substring) - 1 - i
    
    i = m - 1
    while i < n:
        k = 0
        while k < m and substring[m - 1 - k] == source[i - k]:
            k += 1
        if k == m:
            results.append(i - m + 1)
            bad_character_shift = bad_character.get(source[i], m)
            i += bad_character_shift
        else:
            bad_character_shift = bad_character.get(source[i], m)
            i += bad_character_shift
            
    return results

def main():
    s: str = input("Enter string:\n")
    t: str = input("Enter substring:\n")
    print(boyer_moore_horspool(s, t))


if __name__ == "__main__":
    main()
