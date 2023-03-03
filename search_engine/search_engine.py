import re
from math import log


def search(documents, query):
    inverted_index = get_inverted_index(documents)
    document_token_count = {
        document['id']: len(tokenize(document['text']))
        for document in documents
    }
    documents_count = len(documents)
    result_without_relevance = set()
    result_with_relevance = []
    relevance = {}
    query_tokens = tokenize(query)
    for query_token in query_tokens:
        documents_has_token = inverted_index.get(query_token)
        if not documents_has_token:
            continue
        relevance_idf = log(documents_count / len(documents_has_token))
        for document in documents_has_token:
            id = document['id']
            result_without_relevance.update([id])
            relevance_tf = document['weight'] / document_token_count[id]
            relevance_tf_idf = relevance_tf * relevance_idf
            relevance.setdefault(document['id'], 0)
            relevance[document['id']] += relevance_tf_idf
    for id in result_without_relevance:
        result_with_relevance.append(
            {'id': id, 'relevance': relevance[id]}
        )
    result_with_relevance.sort(
        key=lambda item: item['relevance'],
        reverse=True
    )
    result = [item['id'] for item in result_with_relevance]

    return result


def get_inverted_index(documents):
    inverted_index = {}
    tokens_all = set()
    documents_as_list_of_tokens = []
    for document in documents:
        document_tokens = tokenize(document['text'])
        documents_as_list_of_tokens.append(
            {'id': document['id'], 'tokens': document_tokens}
        )
        tokens_all.update(document_tokens)
    for token in tokens_all:
        inverted_index[token] = []
        for document in documents_as_list_of_tokens:
            if token in document['tokens']:
                inverted_index[token].append(
                    {
                        'id': document['id'],
                        'weight': document['tokens'].count(token)
                    }
                )

    return inverted_index


def tokenize(text):
    return [get_term(token) for token in text.split(' ')]


def get_term(token):
    return re.sub(r'[^\w\s]', '', token).lower()
