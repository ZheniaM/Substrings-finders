__all__ = ["z_func"]


def make_z_funcs(s: str) -> list[int]:
    z: list[int] = [0] * len(s)
    left: int = 0
    right: int = 0
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z


def z_func(source: str, substr: str) -> list[int]:
    N: int = len(source)
    M: int = len(substr)
    z = make_z_funcs(f"{substr}\0{source}")
    res: list[int] = []
    for i in range(M + 1, N + 2):
        if z[i] == M:
            res.append(i-M-1)
    return res


def main():
    s = input("Enter string:\n")
    t = input("Enter substring:\n")
    print(z_func(s, t))


if __name__ == "__main__":
    main()
