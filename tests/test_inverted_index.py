from search_engine import get_inverted_index

docs_simple = [
    {'id': 'doc1', 'text': "some text"},
    {'id': 'doc2', 'text': "some text too"},
]

expected_inverted_index = {
    'some': [
        {'id': 'doc1', 'tf-idf': 0.0},
        {'id': 'doc2', 'tf-idf': 0.0}
    ],
    'text': [
        {'id': 'doc1', 'tf-idf': 0.0},
        {'id': 'doc2', 'tf-idf': 0.0}
    ],
    'too': [
        {'id': 'doc2', 'tf-idf': 0.3333}
    ]
}


def test_get_inverted_index():
    result = get_inverted_index(docs_simple)
    assert result == expected_inverted_index
