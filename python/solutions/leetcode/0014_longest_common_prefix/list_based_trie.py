from typing import List, Self


class TrieNode:
    ORD_BASE = ord("a")

    def char_to_offset(char: str) -> int:
        return ord(char) - TrieNode.ORD_BASE

    def offset_to_char(offset: int) -> str:
        return chr(TrieNode.ORD_BASE + offset)

    children: List[Self]
    link_count: int
    is_complete_word: bool

    def __init__(self, is_complete_word: bool = False):
        self.children = [None] * 26
        self.link_count = 0
        self.is_complete_word = is_complete_word

    def __getitem__(self, char: str) -> Self | None:
        offset = TrieNode.char_to_offset(char)
        return self.children[offset]

    def add_child(self, char: str):
        offset = TrieNode.char_to_offset(char)
        self.children[offset] = TrieNode()
        self.link_count += 1

    def get_first_not_none(self):
        for index, child in enumerate(self.children):
            if child is not None:
                return (TrieNode.offset_to_char(index), child)
        return None


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie_root = TrieNode()
        for string_under_test in strs:
            trie_curr = trie_root
            if len(string_under_test) == 0:
                trie_root.is_complete_word = True
            for index, character in enumerate(string_under_test):
                if trie_curr[character] is None:
                    trie_curr.add_child(character)
                trie_curr = trie_curr[character]
                if index + 1 == len(string_under_test):
                    trie_curr.is_complete_word = True

        prefix = ""
        trie_curr = trie_root
        while True:
            if trie_curr.link_count == 1 and not trie_curr.is_complete_word:
                character, next_node = trie_curr.get_first_not_none()
                prefix += character
                trie_curr = next_node
            else:
                return prefix


def visualizer_node_mapper(trie_node: TrieNode):
    import os
    import sys

    current_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.dirname(os.path.dirname(current_dir))
    sys.path.append(repo_dir)
    from tools.debug_visualizer.visualize_data_structure import NodeMetadata

    children = []
    for index, child in trie_node.children:
        if child is not None:
            children.append(
                NodeMetadata(id=id(child), label=TrieNode.offset_to_char(index))
            )

    return children


if __name__ == "__main__":
    visualizer_node_mapper(None)
    # solution = Solution()
