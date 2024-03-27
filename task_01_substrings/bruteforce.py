def find_all_substrs(source: str, substr: str)-> list[str]:
    n = len(source)
    m = len(substr)
    result = []
    for i in range(n - m + 1):
        j = 0
        while j < m and substr[j] == source[i + j]:
            j += 1
        if j == m:
            result.append(i)
    return result


def main():
    s = input("Enter string:\n")
    t = input("Enter substring:\n")
    print(find_all_substrs(s, t))