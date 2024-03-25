from typing import Final


MOD: Final[int] = 1_689_931


def is_substring(source: str, substr: str, index: int) -> bool:
    for j in range(len(substr)):
        if source[index + j] != substr[j]:
            break
    else:
        return True
    return False


def hash_power(substr) -> int:
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


def find_all_substrs(source: str, substr: str) -> list[int]:
    global MOD
    res: list[int] = []
    N, M = len(source), len(substr)
    hashPower = hash_power(substr)
    strHash, subHash = source_and_substr_hashes(source, substr)

    for i in range(N - M + 1):
        if subHash == strHash:
            if is_substring(source, substr, i):
                res.append(i)
        if i < N - M:
            strHash = (strHash - ord(source[i]) * hashPower) % MOD
            strHash = (strHash * 256 + ord(source[i + M])) % MOD
    if strHash == subHash:
        if is_substring(source, substr,  N - M):
            res.append(N - M)

    return res


def main() -> None:
    source = input("Enter the source string:\n")
    substr = input("Enter the substring:\n")
    print(find_all_substrs(source, substr))


if __name__ == "__main__":
    main()
