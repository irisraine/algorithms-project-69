# Search engine

### Hexlet tests and linter status:
[![Actions Status](https://github.com/irisraine/algorithms-project-69/workflows/hexlet-check/badge.svg)](https://github.com/irisraine/algorithms-project-69/actions)
[![Actions Status](https://github.com/irisraine/algorithms-project-69/workflows/pytest/badge.svg)](https://github.com/irisraine/algorithms-project-69/actions/workflows/pytest.yml)
[![Actions Status](https://github.com/irisraine/algorithms-project-69/workflows/flake8/badge.svg)](https://github.com/irisraine/algorithms-project-69/actions/workflows/flake8.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/c8addab484aecf9f90c8/maintainability)](https://codeclimate.com/github/irisraine/algorithms-project-69/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c8addab484aecf9f90c8/test_coverage)](https://codeclimate.com/github/irisraine/algorithms-project-69/test_coverage)

### Description

Educational project. The search engine project involve implementing the data structures and algorithms 
required for building the inverted index and calculating relevance scores. The search engine uses an inverted index to 
efficiently retrieve documents containing a given search term. The project also incorporates a TF-IDF relevance metric 
to rank the retrieved documents based on the importance of the search term within each document. The program returns 
the top-ranked documents to the user.

The inverted index created by parsing through a collection of documents and creating a dictionary 
that maps each word to a list of documents that contain that word. The TF-IDF metric calculated by multiplying 
the term frequency (the number of times a word appears in a document) by the inverse document frequency 
(the logarithm of the total number of documents divided by the number of documents containing the word). 





