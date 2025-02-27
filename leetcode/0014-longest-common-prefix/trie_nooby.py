from typing import List, Dict, Self


class TrieNode:
    children: Dict[str, Self]
    is_complete_word: bool

    def __init__(self, is_complete_word: bool = False):
        self.children = {}
        self.is_complete_word = is_complete_word


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie_root = TrieNode()
        for string_under_test in strs:
            trie_curr = trie_root
            if len(string_under_test) == 0:
                trie_root.is_complete_word = True
            for index, character in enumerate(string_under_test):
                if character in trie_curr.children:
                    trie_curr = trie_curr.children.get(character)
                else:
                    trie_curr.children[character] = TrieNode()
                    trie_curr = trie_curr.children[character]
                if index + 1 == len(string_under_test):
                    trie_curr.is_complete_word = True

        prefix = ""
        trie_curr = trie_root
        while True:
            if len(trie_curr.children) == 1 and not trie_curr.is_complete_word:
                character, next_node = trie_curr.children.popitem()
                prefix += character
                trie_curr = next_node
            else:
                return prefix


if __name__ == "__main__":
    solution = Solution()
