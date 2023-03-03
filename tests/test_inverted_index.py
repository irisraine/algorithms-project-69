from search_engine import get_inverted_index

docs_simple = [
    {'id': 'doc1', 'text': "some text"},
    {'id': 'doc2', 'text': "some text too"},
]

expected_inverted_index = {
    'some': ['doc1', 'doc2'],
    'text': ['doc1', 'doc2'],
    'too': ['doc2']
}


def test_get_inverted_index():
    result = get_inverted_index(docs_simple)
    assert result == expected_inverted_index
