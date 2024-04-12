__all__=['build_suffix_tree']

def build_suffix_tree(text):
    tree = {0: {}}
    suffix_positions = {}
    suffix_positions[0] = 0
    active_node = 0
    active_edge = 0
    text_len = len(text)
    for i in range(1, text_len + 1):
        suffix_positions[i] = active_node
        leaf_node = active_node
        active_edge = active_edge if active_edge else i - 1
        while active_node in tree and active_edge in tree[active_node]:
            last_child = max(k for k in tree[active_node] if k < len(active_edge))
            last_child_edge = tree[active_node][last_child]
            if text[last_child_edge] == text[i - 1]:
                leaf_node = last_child
                break
            active_node = last_child
        if text[active_edge] != text[i - 1]:
            tree[active_node][i] = i
            active_node = i
            tree[active_node] = {}
            suffix_positions[i] = active_node
        active_edge = i - 1
    return tree, suffix_positions

def suffix_tree_substr(text, pattern):
    tree, suffix_positions = build_suffix_tree(text)
    active_node = 0
    active_edge = 0
    pattern_len = len(pattern)
    for i in range(len(text)):
        if active_edge == pattern_len:
            return suffix_positions[i - pattern_len + 1:i + 1]
        if text[active_edge] == pattern[active_edge]:
            active_edge += 1
            active_node = suffix_positions[i]
        else:
            active_edge = 0
            while active_node in tree and text[i] != tree[active_node][active_edge]:
                active_node = tree[active_node][active_edge]
                active_edge = 0
            if active_node in tree and text[i] == tree[active_node][active_edge]:
                active_edge += 1
            else:
                active_node = 0
    if active_edge == pattern_len:
        return suffix_positions[i - pattern_len + 1:i + 1]
    return []

def main():
    s = input("Enter string:\n")
    t = input("Enter substring:\n")
    print(suffix_tree_substr(s, t))

if __name__ == "__main__":
    main()