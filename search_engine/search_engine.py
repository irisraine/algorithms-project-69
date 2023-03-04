import re
from math import log2


def search(documents, query):
    inverted_index = get_inverted_index(documents)
    result_without_relevance = set()
    result_with_relevance = []
    relevance = {}
    query_tokens = tokenize(query)
    for query_token in query_tokens:
        documents_has_token = inverted_index.get(query_token)
        if not documents_has_token:
            continue
        for document in documents_has_token:
            id = document['id']
            result_without_relevance.update([id])
            relevance.setdefault(id, 0)
            token_tf_idf = (list(filter(
                lambda doc: doc['id'] == id, inverted_index[query_token]
            ))[0]['tf-idf'])
            relevance[id] += token_tf_idf
    for id in result_without_relevance:
        result_with_relevance.append(
            {'id': id, 'relevance': relevance[id]}
        )
    result_with_relevance.sort(
        key=lambda item: (item['relevance']),
        reverse=True
    )
    result = [item['id'] for item in result_with_relevance]

    return result


def get_inverted_index(documents):
    inverted_index = {}
    tokens_all = set()
    documents_as_tokens = []
    documents_count = len(documents)
    for document in documents:
        document_tokens = tokenize(document['text'])
        documents_as_tokens.append(
            {'id': document['id'], 'tokens': document_tokens}
        )
        tokens_all.update(document_tokens)
    for token in tokens_all:
        inverted_index[token] = []
        documents_has_token = len(
            list(filter(
                lambda item: token in item['tokens'], documents_as_tokens
            )))
        idf = log2(1 + (documents_count - documents_has_token + 1) / (documents_has_token + 0.5))
        for document in documents_as_tokens:
            if token in document['tokens']:
                tf = document['tokens'].count(token) / len(document['tokens'])
                inverted_index[token].append(
                    {'id': document['id'], 'tf-idf': round(tf * idf, 4)}
                )
    return inverted_index


def tokenize(text):
    tokens = []
    lines = text.split('\n')
    for line in lines:
        line_as_list_of_tokens = [get_term(token) for token in line.split(' ') if token]
        tokens.extend(line_as_list_of_tokens)
    return tokens


def get_term(token):
    return re.sub(r'[^\w\s]', '', token).lower()
