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
