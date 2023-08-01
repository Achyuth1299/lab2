import sys
from collections import defaultdict
# List of stopwords
stopwords = set(["the", "and", "of", "a", "to", "in", "is", "it"])

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        # Convert the word to lowercase
        word_lower = word.lower()

        # Check if the word is not a stopword
        if word_lower not in stopwords:
            # Output the word with count 1
            print(f"{word_lower} 1")
#reducer

word_counts = defaultdict(int)

for line in sys.stdin:
    word, count = line.strip().split()
    count = int(count)
    word_counts[word] += count

# Output the results
for word, count in word_counts.items():
    print(f'"{word}" {count}')
