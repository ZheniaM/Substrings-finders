def make_dfa(source: str, alphabet: set[str]) -> list[dict[str, int]]:
    table: list[dict[str, int]] = []
    substring: str = ""
    for i in source:
        row: dict = {}
        for symbol in alphabet:
            sub = substring + symbol
            for _ in range(len(sub)):
                if (sub == source[:len(sub)]):
                    row[symbol] = len(sub)
                    break
                *sub, _ = sub
            else:
                row[symbol] = 0
        substring += i
        table.append(row)
    return table


def find_all_substrs(source: str, substr: str) -> list[int]:
    alphabet = set(substr)
    dfa = make_dfa(substr, alphabet)
    state = 0
    FINAL = len(dfa)
    result = []
    for i, c in enumerate(source):
        if (FINAL == state):
            result.append(i - FINAL)
            state = 0
            continue
        state = dfa[state][c] if c in alphabet else 0
    return result


def main() -> None:
    source = input("Enter the source string:\n")
    substr = input("Enter the substring:\n")
    print(find_all_substrs(source, substr))


if __name__ == "__main__":
    main()
