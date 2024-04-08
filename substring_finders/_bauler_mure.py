__all__ = ["bauler_mure"]


def bauler_mure(source: str, substr: str) -> list[str]:
    N: int = len(source)
    M: int = len(substr)
    alphabet: set[str] = set(substr)
    sym_list: list[dict[str, int]] = []
    suffs: list[int] = [0 for _ in range(M + 1)]

    suff: str = ""
    for i in range(M - 1, -1, -1):
        sub = substr[:i]
        row = {}
        for sym in alphabet:
            row[sym] = i - sub.rfind(sym)
        sym_list.append(row)

        suff = substr[i] + suff
        suffIndex = sub.rfind(suff)
        if suffIndex != -1:
            suffs[i] = i - suffIndex
            continue
        suffs[i] = suffs[i + 1]
        if suffs[i] == 0:
            suffs[i] = M
    suffs[M] = 1
    res: list[int] = []
    i = 0
    while i <= N - M:
        j = M - 1
        while j >= 0 and substr[j] == source[i + j]:
            j -= 1
        if j != -1:
            try:
                indent = sym_list[M - j - 1][source[i + j]]
            except KeyError:
                indent = j
            i += max(1, indent, suffs[j + 1])
            continue
        res.append(i)
        i += max(1, suffs[0])
    return res


def main() -> None:
    s = input("Enter string:\n")
    t = input("Enter substring:\n")
    print(bauler_mure(s, t))


if __name__ == "__main__":
    main()
