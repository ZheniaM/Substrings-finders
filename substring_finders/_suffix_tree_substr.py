from typing import List, Dict, Union

__all__ = ["suffix_tree_substr"]

def build_suffix_tree(s: str) -> Dict[str, Union[int, Dict]]:
    suffix_tree = {}
    for i in range(len(s)):
        current_node = suffix_tree
        for suffix in s[i:]:
            if suffix not in current_node:
                current_node[suffix] = {}
            current_node = current_node[suffix]
        current_node['$'] = i
    return suffix_tree

def suffix_tree_substr(suffix_tree: Dict, substring: str) -> List[int]:
    results = []
    current_node = suffix_tree
    for char in substring:
        if char in current_node:
            current_node = current_node[char]
        else:
            return results
    def find_endings(node: Dict) -> None:
        if '$' in node:
            results.append(node['$'])
        for key in node.keys():
            if key != '$':
                find_endings(node[key])
    find_endings(current_node)
    return results

def main():
    s = input("Enter the source string:\n")
    substring = input("Enter the substring:\n")
    tree = build_suffix_tree(s)
    occurrences = suffix_tree_substr(tree, substring)
    print(occurrences)

if __name__ == "__main__":
    main()