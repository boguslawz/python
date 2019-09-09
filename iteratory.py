class ExampleIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):


            raise StopIteration()
        rslt = self.data[self.index]
        self.index += 1
        return rslt

class ExampleIterable:

    def __init__(self):
        self.data = [1,2,3]

    def __iter__(self):
        return ExampleIterator(self.data)

for i in ExampleIterable():
    print(i)

print([i*3 for i in ExampleIterable()])

# class AlternateIterable:
#     def __init__(self):
#         self.data = [1, 2, 3]
#
#         def __getitem__(self, idx):
#             return self.data[idx]
#
# print([i for i in AlternateIterable()])

with open('example_text.txt', 'rt') as f:
    for line in iter(lambda: f.readline().strip(), 'END'):
        print(line)