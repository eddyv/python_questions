from typing import List


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = dict()

    def __repr__(self):
        return f"isWord: {self.isWord}, children: {self.children}"


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord

    def starts_with(self, prefix) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # In this case, if it has been inserted, it means that there MUST be a word that starts with this prefix
        return True

    def all_words_starting_with(self, prefix) -> List[str]:
        words = []
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return words
            curr = curr.children[char]
        return self.all_words(curr, prefix, words)

    def all_words(self, curr_node, chars, words) -> List[str]:
        if curr_node.isWord:
            words.append(chars)
        for char in curr_node.children:
            self.all_words(curr_node.children[char], chars + char, words)
        return words


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("ape")
    trie.insert("Anna")
    trie.insert("Ana")
    trie.insert("soccer")
    trie.insert("basketball")
    print(trie.all_words_starting_with("a"))
    print(trie.all_words_starting_with("ap"))
    print(trie.all_words_starting_with("app"))
    print(trie.all_words_starting_with("A"))
    print(trie.all_words_starting_with("Ana"))
    trie.insert("Socccer")
    trie.insert("Soccer")
    trie.insert("Socks")
    print(trie.all_words_starting_with("S"))
    print(trie.all_words_starting_with("Soc"))
    print(trie.all_words_starting_with("Sock"))
    print(trie.all_words_starting_with("Socc"))
