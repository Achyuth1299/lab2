# Mapper function
def mapper(input_text):
    words = input_text.strip().split()
    for word in words:
        yield (word, 1)

# Reducer function
def reducer(key, values):
    yield (key, sum(values))

# Main function to run the MapReduce job
# Simulating the input text file
input_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Donec condimentum elit vel mauris varius, id laoreet tortor placerat.
Nulla scelerisque felis ac risus varius, sit amet luctus elit mattis."""

    # Step 1: Mapping
mapped_data = [mapper(line) for line in input_text.splitlines()]

    # Step 2: Shuffling and Sorting (Not required in this example)

    # Step 3: Reducing
word_counts = {}
for mapped_item in mapped_data:
    for key, value in mapped_item:
        if key in word_counts:
            word_counts[key].append(value)
        else:
            word_counts[key] = [value]

    # Output the results
for word, counts in word_counts.items():
    total_count = sum(counts)
    print(f'"{word}" {total_count}')


