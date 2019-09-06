positives = filter(lambda x: x>0, [1,2,3,4,5,-5,0,-3])
print(positives)
print(list(positives))

print("Dzial Reduce: ")

from functools import reduce
import operator

print(reduce(operator.add, [1,2,3,4,5]))
numbers = [1,2,3,4,5]
accumulator  = operator.add(numbers[0], numbers[1])

def count_words(doc):
    normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalised_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

documents = [
    "koszmar minionego lata",
    "pamietniki z wakacji",
    "diabel mowi dobranoc"
]
counts = map(count_words, documents)
print(list(counts))
#
# def combine_counts(d1, d2):
#     d = d1.copy()
#     for word, count in d2.items():
#         d[word] = d.get(word, 0) + count
#     return d
# total_counts = reduce(combine_counts, counts)
# print(total_counts)

