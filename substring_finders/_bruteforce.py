__all__ = ["bruteforce"]


def bruteforce(source: str, substr: str) -> list[int]:
    N: int = len(source)
    M: int = len(substr)
    res: list[int] = []
    for i in range(N - M + 1):
        j = 0
        while j < M and substr[j] == source[i + j]:
            j += 1
        if j == M:
            res.append(i)
    return res


def main():
    s = input("Enter string:\n")
    t = input("Enter substring:\n")
    print(bruteforce(s, t))


if __name__ == "__main__":
    main()
