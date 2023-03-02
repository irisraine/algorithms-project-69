import re


def search(documents, query):
    result_with_relevance = []
    query_term = re.findall(r'\w+', query)[0]
    for document in documents:
        id, text = document['id'], document['text']
        document_terms = re.findall(r'\w+', text)
        if query_term in document_terms:
            relevance = document_terms.count(query_term)
            result_with_relevance.append({'id': id, 'relevance': relevance})
    result_with_relevance.sort(
        key=lambda item: item['relevance'],
        reverse=True
    )
    result = [item['id'] for item in result_with_relevance]

    return result
