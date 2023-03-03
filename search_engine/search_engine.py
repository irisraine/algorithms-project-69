import re


def search(documents, query):
    inverted_index = get_inverted_index(documents)
    result_without_relevance = set()
    result_with_relevance = []
    relevance = {}
    query_terms = re.findall(r'\w+', query)
    for query_term in query_terms:
        documents_has_term = inverted_index.get(query_term)
        if not documents_has_term:
            break
        for document in documents_has_term:
            result_without_relevance.update([document['id']])
            relevance.setdefault(document['id'], {'match': 0, 'weight': 0})
            relevance[document['id']]['match'] += 1
            relevance[document['id']]['weight'] += document['weight']
    for document_id in result_without_relevance:
        result_with_relevance.append(
            {'id': document_id, 'relevance': relevance[document_id]}
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
                inverted_index[term].append(
                    {
                        'id': document['id'],
                        'weight': document['terms'].count(term)
                    }
                )

    return inverted_index
