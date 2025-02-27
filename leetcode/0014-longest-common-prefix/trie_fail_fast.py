from typing import List, Dict, Self


class TrieNode:
    children: Dict[str, Self]
    is_complete_word_or_branch: bool

    def __init__(self, is_complete_word_or_branch: bool = False):
        self.children = {}
        self.is_complete_word_or_branch = is_complete_word_or_branch


class Solution:
    """Doesn't actually perform better than the 'nooby' trie yet :/"""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if any([len(str_under_test) == 0 for str_under_test in strs]):
            return ""

        trie_root = TrieNode()

        for string_under_test in strs:
            trie_curr = trie_root
            for index, character in enumerate(string_under_test):
                if len(trie_curr.children) == 0:
                    trie_next = TrieNode()
                    trie_curr.children[character] = trie_next
                    trie_curr = trie_next
                else:
                    if character in trie_curr.children:
                        trie_curr = trie_curr.children.get(character)
                    else:
                        trie_curr.is_complete_word_or_branch = True
                        break

                if index + 1 == len(string_under_test):
                    trie_curr.is_complete_word_or_branch = True

        prefix = ""
        trie_curr = trie_root
        while True:
            if (
                len(trie_curr.children) == 1
                and not trie_curr.is_complete_word_or_branch
            ):
                character, next_node = trie_curr.children.popitem()
                prefix += character
                trie_curr = next_node
            else:
                return prefix


if __name__ == "__main__":
    solution = Solution()
