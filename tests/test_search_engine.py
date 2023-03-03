from search_engine import search

query = "shoot"
query_with_punctuation = "shoot!"
query_multi = 'shoot straight'

docs_simple = [
    {'id': 'doc1', 'text': "I can't shoot straight unless I've had a pint!"},
    {'id': 'doc2', 'text': "Just run away and don't look back."}
]

docs_with_punctuation = docs = [
    {'id': 'doc1', 'text': "I can't shoot straight unless I've had a pint!"},
    {'id': 'doc2', 'text': "Don't shoot shoot shoot that thing at me."},
    {'id': 'doc3', 'text': "I'm your shooter."},
    {'id': 'doc4', 'text': "Please don't shoot! If you shoot I gonna die out of fear of gunshooting."}
]

empty_docs = []

expected_result_docs_simple = ['doc1']
expected_result_docs_with_punctuation = ['doc2', 'doc4', 'doc1']
expected_result_docs_with_punctuation_query_multi = ['doc1', 'doc2', 'doc4']
expected_empty = []


def test_docs_simple_query_simple():
    result = search(docs_simple, query)
    assert result == expected_result_docs_simple


def test_docs_simple_query_with_punctuation():
    result = search(docs_simple, query_with_punctuation)
    assert result == expected_result_docs_simple


def test_docs_with_punctuation_query_simple():
    result = search(docs_with_punctuation, query)
    assert result == expected_result_docs_with_punctuation


def test_docs_with_punctuation_query_with_punctuation():
    result = search(docs_with_punctuation, query_with_punctuation)
    assert result == expected_result_docs_with_punctuation


def test_docs_with_punctuation_query_multi():
    result = search(docs_with_punctuation, query_multi)
    assert result == expected_result_docs_with_punctuation_query_multi


def test_empty_docs():
    result = search(empty_docs, query)
    assert result == expected_empty
