# Apostolico-Crocemor
__all__ = ["ac"]


def preKmp(substr: str, kmpNext: list[int]) -> None:
    x = substr
    M: int = len(x) - 1
    i: int = 0
    j: int = -1
    kmpNext[0] = -1
    while i < M:
        while j > -1 and x[i] != x[j]:
            j = kmpNext[j]
        i += 1
        j += 1
        kmpNext[i] = kmpNext[j] if x[i] == x[j] else j


def ac(source: str, substr: str) -> list[int]:
    N: int = len(source)
    M: int = len(substr)
    kmpNext: list[int] = [0] * (M + 1)
    x = substr
    y = source
    res: list[int] = []

    preKmp(x, kmpNext)
    ell: int = 1
    while x[ell - 1] == x[ell]:
        ell += 1
    if ell == M:
        ell = 0

    i: int = ell
    j: int = 0
    k: int = 0
    while j <= N - M:
        while i < M and x[i] == y[i + j]:
            i += 1
        if i >= M:
            while k < ell and x[k] == y[j + k]:
                k += 1
            if k >= ell:
                res.append(j)
        j += i - kmpNext[i]
        if i == ell:
            k = max(0, k - 1)
        else:
            if kmpNext[i] <= ell:
                k = max(0, kmpNext[i])
                i = ell
            else:
                k = ell
                i = kmpNext[i]
        if not i and not j:
            res.append(k)

    return res


def main() -> None:
    s = "mama myla ramy"
    t = "am"
    print(f"{ac(s, t)=}")


if __name__ == "__main__":
    main()
