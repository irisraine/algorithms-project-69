import re


def search(documents, query):
    result = []
    query_term = re.findall(r'\w+', query)[0]
    for document in documents:
        id, text = document['id'], document['text']
        document_as_list_of_terms = re.findall(r'\w+', text)
        if query_term in document_as_list_of_terms:
            result.append(id)

    return result
