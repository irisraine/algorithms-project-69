import re


def search(documents, query):
    result_with_relevance = []
    query_terms = re.findall(r'\w+', query)
    for document in documents:
        document_terms = re.findall(r'\w+', document['text'])
        relevance = {'match': 0, 'weight': 0}
        for query_term in query_terms:
            if query_term in document_terms:
                relevance['match'] += 1
                relevance['weight'] += document_terms.count(query_term)
        if relevance['match']:
            result_with_relevance.append(
                {'id': document['id'], 'relevance': relevance}
            )
    result_with_relevance.sort(
        key=lambda item: (
            item['relevance']['match'],
            item['relevance']['weight']
        ),
        reverse=True
    )
    result = [item['id'] for item in result_with_relevance]

    return result


def get_inverted_index(documents):
    inverted_index = {}
    terms_all = set()
    documents_as_list_of_terms = []
    for document in documents:
        document_terms = re.findall(r'\w+', document['text'])
        documents_as_list_of_terms.append(
            {'id': document['id'], 'terms': document_terms}
        )
        terms_all.update(document_terms)
    for term in terms_all:
        inverted_index[term] = []
        for document in documents_as_list_of_terms:
            if term in document['terms']:
                inverted_index[term].append(document['id'])

    return inverted_index
