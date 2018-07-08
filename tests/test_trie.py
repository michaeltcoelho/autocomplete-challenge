from trie import WILDCARD_CHAR, Trie


def test_should_instance_trie_with_head_wildcard_char_node():
    trie = Trie()
    assert trie.head_node.char == WILDCARD_CHAR
    assert trie.head_node.has_children() is False


def test_should_insert_word_with_success():
    trie = Trie()
    trie.insert_word('facebook')
    assert trie.contains('facebook')


def test_should_insert_word_flag_last_node():
    trie = Trie()
    trie.insert_word('facebook')
    last_node = trie.get_last_word_node('facebook')
    assert last_node.is_last_node


def test_should_get_last_node():
    trie = Trie()
    trie.insert_word('facebook')
    last_node = trie.get_last_word_node('facebook')
    assert last_node.char == 'k'
    assert last_node.is_last_node


def test_should_contains_return_false():
    trie = Trie()
    trie.insert_word('Facebook')
    assert trie.contains('facebok') is False
    assert trie.contains('foo') is False


def test_should_iterwords_return_by_prefix():
    trie = Trie()
    words = ['Facebook', 'Facebook Lite', 'Faca']
    trie.insert_words(words)
    result = list(trie.iterwords('face'))
    assert result == ['Facebook', 'Facebook Lite']


def test_should_iterwords_return_all():
    trie = Trie()
    words = ['foo', 'bar', 'buzz']
    trie.insert_words(words)
    result = list(trie.iterwords())
    assert result == words
