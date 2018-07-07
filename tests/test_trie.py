from trie import WILDCARD_CHAR, Trie, TrieNode


def test_wildcard():
    assert WILDCARD_CHAR == '*'


def test_should_create_trie_node():
    trie_node = TrieNode('a')
    assert trie_node.char == 'a'
    assert trie_node.is_last_node is False
    assert trie_node.has_children() is False


def test_should_add_child_node_to_node():
    trie_node = TrieNode('a')
    b_node = trie_node.add_child_node('b', True)
    assert trie_node.has_children()
    assert trie_node.has_child_node('b')
    assert b_node.char == 'b'
    assert b_node.is_last_node
    assert b_node.has_children() is False


def test_should_get_child_node_from_trie_node():
    trie_node = TrieNode('a')
    trie_node.add_child_node('b')
    b_node = trie_node.get_child_node('b')
    assert b_node.char == 'b'


def test_should_get_word_from_parent_trie_node():
    trie_node = TrieNode('f')
    current_node = trie_node
    for char in 'acebook':
        current_node = current_node.add_child_node(char)
    current_node.set_as_last_node()
    word = ''.join(list(trie_node.get_word('f')))
    assert word == 'facebook'


def test_should_create_trie_with_head_wildcard_node():
    trie = Trie()
    assert trie.head_node.char == WILDCARD_CHAR
    assert trie.head_node.has_children() is False


def test_should_insert_word_in_trie():
    trie = Trie()
    trie.insert('facebook')
    assert trie.contains('facebook')


def test_should_insert_and_flag_last_node():
    trie = Trie()
    trie.insert('facebook')
    last_node = trie.get_last_word_node('facebook')
    assert last_node.is_last_node


def test_word_not_found_in_trie():
    trie = Trie()
    trie.insert('Facebook')
    assert trie.contains('facebok') is False
    assert trie.contains('foo') is False


def test_list_trie_words_by_prefix():
    trie = Trie()
    trie.insert('Facebook')
    trie.insert('Facebook Lite')
    trie.insert('Faca')
    result = list(trie.iteritems('face'))
    assert result == ['Facebook', 'Facebook Lite']


def test_list_all_trie_words():
    trie = Trie()
    trie.insert('foo')
    trie.insert('bar')
    result = list(trie.iteritems())
    assert result == ['foo', 'bar']
