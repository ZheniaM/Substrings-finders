from typing import Final


__all__ = ["rabin_carp"]


MOD: Final[int] = 1_689_931


def is_substring(source: str, substr: str, index: int) -> bool:
    for j in range(len(substr)):
        if source[index + j] != substr[j]:
            break
    else:
        return True
    return False


def hash_power_of(substr) -> int:
    global MOD
    hash_power: int = 1
    for i in range(1, len(substr)):
        hash_power = (hash_power * 256) % MOD
    return hash_power


def source_and_substr_hashes(source, substr) -> tuple[int, int]:
    global MOD
    sub_hash: int = 0
    str_hash: int = 0
    for i in range(len(substr)):
        sub_hash = (sub_hash * 256 + ord(substr[i])) % MOD
        str_hash = (str_hash * 256 + ord(source[i])) % MOD
    return (str_hash, sub_hash)


def rabin_carp(source: str, substr: str) -> list[int]:
    global MOD
    res: list[int] = []
    N, M = len(source), len(substr)
    hash_power = hash_power_of(substr)
    str_hash, sub_hash = source_and_substr_hashes(source, substr)

    for i in range(N - M + 1):
        if sub_hash == str_hash:
            if is_substring(source, substr, i):
                res.append(i)
        if i < N - M:
            str_hash = (str_hash - ord(source[i]) * hash_power) % MOD
            str_hash = (str_hash * 256 + ord(source[i + M])) % MOD
    if str_hash == sub_hash:
        if is_substring(source, substr,  N - M):
            res.append(N - M)

    return res


def main() -> None:
    source = input("Enter the source string:\n")
    substr = input("Enter the substring:\n")
    print(rabin_carp(source, substr))


if __name__ == "__main__":
    main()
