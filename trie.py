
WILDCARD_CHAR = '*'


class TrieNode:

    def __init__(self, char, is_last_node=False):
        self.char = char
        self.children = {}
        self.is_last_node = is_last_node

    def sanitize_char(self, char):
        return char.lower()

    def has_children(self):
        return True if self.children else False

    def has_child_node(self, char):
        sanitized_char = self.sanitize_char(char)
        return sanitized_char in self.children

    def get_child_node(self, char):
        sanitized_char = self.sanitize_char(char)
        return self.children[sanitized_char]

    def add_child_node(self, char, is_last_node=False):
        sanitized_char = self.sanitize_char(char)
        node = self.children[sanitized_char] = TrieNode(char, is_last_node)
        return node

    def get_or_add_child_node(self, char, is_last_node=False):
        child_node = None
        if self.has_child_node(char):
            child_node = self.get_child_node(char)
        else:
            child_node = self.add_child_node(char)
        return child_node

    def get_word(self, prefix):
        if self.is_last_node:
            yield prefix
        for char, node in self.children.items():
            yield from node.get_word(prefix + node.char)

    def set_as_last_node(self):
        self.is_last_node = True


class Trie:

    def __init__(self):
        self.head_node = TrieNode(WILDCARD_CHAR)

    def insert_word(self, word):
        current_node = self.head_node
        for char in word:
            current_node = current_node.get_or_add_child_node(char)
        current_node.set_as_last_node()

    def insert_words(self, words):
        for word in words:
            self.insert_word(word)

    def get_last_word_node(self, word):
        current_node = self.head_node
        for char in word:
            if not current_node.has_child_node(char):
                return None
            current_node = current_node.get_child_node(char)
        return current_node

    def contains(self, word):
        return self.get_last_word_node(word) is not None

    def iterwords(self, prefix=''):
        current_node = self.head_node
        node_chars = []
        for char in prefix:
            current_node = current_node.get_child_node(char)
            node_chars.append(current_node.char)
        prefix = ''.join(node_chars)
        yield from current_node.get_word(prefix)
