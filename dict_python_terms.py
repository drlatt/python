python_terms = {'tuple':'a fixed list',
                'dictionary':'list of key/value pairs',
                'sort':'function to create output in an ordered fashion',
                'sorted':'function to order items without necessarily altering the original list',
                'list':'store items for retrieval later on',
                }
print(python_terms)

for term, definition in python_terms.items():
    print(term + " : " + definition)
