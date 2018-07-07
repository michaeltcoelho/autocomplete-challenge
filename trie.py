
WILDCARD_CHAR = '*'


class TrieNode:

    def __init__(self, char, is_last_node=False):
        self.char = char
        self.children = {}
        self.is_last_node = is_last_node

    def has_children(self):
        return not self.children == {}

    def has_child_node(self, char):
        return char in self.children

    def get_child_node(self, char):
        return self.children[char]

    def add_child_node(self, char, is_last_node=False):
        node = self.children[char] = TrieNode(char, is_last_node)
        return node

    def get_word(self, prefix):
        if self.is_last_node:
            yield prefix
        for char, node in self.children.items():
            yield from node.get_word(prefix + char)

    def set_as_last_node(self):
        self.is_last_node = True


class Trie:

    def __init__(self):
        self.head_node = TrieNode(WILDCARD_CHAR)

    def insert(self, word):
        current_node = self.head_node
        for char in word:
            if current_node.has_child_node(char):
                current_node = current_node.get_child_node(char)
            else:
                current_node = current_node.add_child_node(char)
        current_node.set_as_last_node()

    def get_last_word_node(self, word):
        current_node = self.head_node
        for char in word:
            if not current_node.has_child_node(char):
                return None
            current_node = current_node.get_child_node(char)
        return current_node

    def contains(self, word):
        return self.get_last_word_node(word) is not None

    def iteritems(self, prefix=''):
        current_node = self.head_node
        for char in prefix:
            current_node = current_node.get_child_node(char)
        yield from current_node.get_word(prefix)
