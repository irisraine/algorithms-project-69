import re
from math import log2


def search(documents, query):
    inverted_index = get_inverted_index(documents)
    result_with_relevance = {}
    query_tokens = tokenize(query)
    for query_token in query_tokens:
        documents_has_token = inverted_index.get(query_token)
        if not documents_has_token:
            continue
        for document in documents_has_token:
            result_with_relevance.setdefault(document['id'], 0)
            token_tf_idf = get_tf_idf(document['id'], documents_has_token)
            result_with_relevance[document['id']] += token_tf_idf
    result = sorted(
        result_with_relevance,
        key=result_with_relevance.get,
        reverse=True)

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


def get_tf_idf(document_id, documents_has_token):
    filter_token = filter(
        lambda document: document['id'] == document_id, documents_has_token
    )
    tf_idf = list(filter_token)[0]['tf-idf']
    return tf_idf


def get_idf(count, has_token):
    return log2(1 + (count - has_token + 1) / (has_token + 0.5))
