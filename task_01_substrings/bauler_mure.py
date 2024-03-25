def find_all_substrs(source: str, substr: str) -> list[str]:
    N: int = len(source)
    M: int = len(substr)
    ALPHABET: set[str] = set(substr)
    badSym: list[dict[str, int]] = []
    goodSuff: list[int] = [0 for _ in range(M + 1)]

    suff: str = ""
    for i in range(M - 1, -1, -1):
        sub = substr[:i]
        row = {}
        for SYM in ALPHABET:
            row[SYM] = i - sub.rfind(SYM)
        badSym.append(row)

        suff = substr[i] + suff
        suffIndex = sub.rfind(suff)
        if suffIndex != -1:
            goodSuff[i] = i - suffIndex
            continue
        goodSuff[i] = goodSuff[i + 1]
        if goodSuff[i] == 0:
            goodSuff[i] = M
    goodSuff[M] = 1
    res: list[int] = []
    i = 0
    while i <= N - M:
        j = M - 1
        while j >= 0 and substr[j] == source[i + j]:
            j -= 1
        if j != -1:
            try:
                indent = badSym[M - j - 1][source[i + j]]
            except KeyError:
                indent = j
            i += max(1, indent, goodSuff[j + 1])
            continue
        res.append(i)
        i += max(1, goodSuff[0])
    return res


def main() -> None:
    s = input("Enter string:\n")
    t = input("Enter substring:\n")
    print(find_all_substrs(s, t))


if __name__ == "__main__":
    main()
