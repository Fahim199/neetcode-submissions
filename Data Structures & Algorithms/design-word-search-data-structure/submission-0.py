class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd= True

    def search(self, word: str) -> bool:
        curr = self.root
        


        def dfs(i, node):

            # We finished searching the word
            if i == len(word):
                return node.isEnd

            # Wildcard case
            if word[i] == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True

                return False

            # Normal character case
            if word[i] not in node.children:
                return False

            return dfs(i + 1, node.children[word[i]])
            
            

        return dfs(0, curr)


