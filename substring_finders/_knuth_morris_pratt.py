from typing import List

__all__ = ['knuth_morris_pratt']


def kmp(source: str, substr: str) -> List[int]:
    lps: List[int] = [0] * len(substr)
    j: int = 0
    for i in range(1, len(substr)):
        while j > 0 and substr[i] != substr[j]:
            j = lps[j-1]
        if substr[i] == substr[j]:
            j += 1
        lps[i] = j

    j = 0
    matches: List[int] = []
    for i in range(len(source)):
        while j > 0 and source[i] != substr[j]:
            j = lps[j-1]
        if source[i] == substr[j]:
            j += 1
        if j == len(substr):
            matches.append(i - len(substr) + 1)
            j = lps[j-1]

    return matches


knuth_morris_pratt = kmp


def main():
    s: str = input("Enter string:\n")
    t: str = input("Enter substring:\n")
    print(kmp(s, t))


if __name__ == "__main__":
    main()
