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
            result_without_relevance.update([document['id']])
            relevance.setdefault(document['id'], 0)
            token_tf_idf = get_tf(document['id'], documents_has_token)
            relevance[document['id']] += token_tf_idf
    for document_id in result_without_relevance:
        result_with_relevance.append(
            {'id': document_id, 'relevance': relevance[document_id]}
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
        idf = get_idf(documents_count, documents_has_token)
        for document in documents_as_tokens:
            if token in document['tokens']:
                tf = document['tokens'].count(token) / len(document['tokens'])
                inverted_index[token].append(
                    {'id': document['id'], 'tf-idf': round(tf * idf, 4)}
                )
    return inverted_index


def tokenize(text):
    tokens = []
    text_lines = text.split('\n')
    for line in text_lines:
        line_tokenized = [
            get_term(token)
            for token in line.split(' ') if token
        ]
        tokens.extend(line_tokenized)
    return tokens


def get_term(token):
    return re.sub(r'[^\w\s]', '', token).lower()


def get_tf(document_id, documents_has_token):
    filter_token = filter(
        lambda document: document['id'] == document_id, documents_has_token
    )
    tf_idf = list(filter_token)[0]['tf-idf']
    return tf_idf


def get_idf(documents_count, documents_has_token):
    return log2(1 + (documents_count - documents_has_token + 1) / (documents_has_token + 0.5))
