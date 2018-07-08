from trie import TrieNode


def test_should_create_trie_node():
    trie_node = TrieNode('a')
    assert trie_node.char == 'a'
    assert trie_node.is_last_node is False
    assert trie_node.has_children() is False


def test_should_add_child_node_to_an_existent_node():
    trie_node = TrieNode('a')
    b_node = trie_node.add_child_node('b', True)
    assert trie_node.has_children()
    assert trie_node.get_child_node('b') is not None
    assert b_node.char == 'b'
    assert b_node.is_last_node
    assert b_node.has_children() is False


def test_should_get_child_node():
    trie_node = TrieNode('a')
    trie_node.add_child_node('b')
    b_node = trie_node.get_child_node('b')
    assert b_node.char == 'b'


def test_should_get_or_add_child_node():
    trie_node = TrieNode('a')
    b_node = trie_node.get_or_add_child_node('b')
    assert trie_node.get_child_node('b') is not None
    assert trie_node.get_or_add_child_node('b') == b_node


def test_should_trie_node_has_children_be_false():
    trie_node = TrieNode('a')
    assert trie_node.has_children() is False


def test_should_set_trie_node_as_the_least_node():
    trie_node = TrieNode('a')
    trie_node.set_as_last_node()
    assert trie_node.is_last_node


def test_should_trie_node_has_a_child_node():
    a_trie_node = TrieNode('a')
    a_trie_node.add_child_node('b')
    assert a_trie_node.get_child_node('b') is not None


def test_should_get_word_from_parent_trie_node():
    trie_node = TrieNode('f')
    current_node = trie_node
    for char in 'acebook':
        current_node = current_node.add_child_node(char)
    current_node.set_as_last_node()
    word = ''.join(list(trie_node.get_word('f')))
    assert word == 'facebook'
