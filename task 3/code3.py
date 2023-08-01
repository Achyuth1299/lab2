import sys
import re

# Regular expression to split text into words
word_pattern = re.compile(r"[\w']+")

# Retrieve the document name from the input file name
document_name = sys.argv[1]

for line in sys.stdin:
    words = word_pattern.findall(line)
    for word in words:
        # Output the word and its document as key-value pair
        print(f'"{word}" "{document_name}"')

inverted_index = {}

for line in sys.stdin:
    word, document = line.strip().split()
    # Add the document to the list of occurrences for the word
    if word in inverted_index:
        inverted_index[word].append(document)
    else:
        inverted_index[word] = [document]

# Output the inverted index
for word, documents in inverted_index.items():
    # Format the list of documents as a comma-separated string
    document_list = ', '.join(documents)
    print(f'"{word}" {document_list}')
