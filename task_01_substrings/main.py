import bruteforce
import automaton
import rabin_carp
import bauler_mure


def main() -> None:
    s = input("Enter a string to search for:\n")
    t = input("Enter substrung to find for:\n")
    print()
    print(f"bruteforce : {bruteforce.find_all_substrs(s, t)}")
    print(f"bauler mure: {bauler_mure.find_all_substrs(s, t)}")
    print(f"rabin carp : {rabin_carp.find_all_substrs(s, t)}")
    print(f"automaton  : {automaton.find_all_substrs(s, t)}")


if __name__ == "__main__":
    main()
