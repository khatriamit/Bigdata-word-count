import sys


class Mapper(object):
    def __init__(self, text):
        super(Mapper, self).__init__()
        self.text = text

    def map(self):
        self.words = self.text.split()
        self.map_output = []
        for words in self.words:
            self.map_output.append({words: 1})


class Reducer(object):
    def __init__(self, map_list):
        super(Reducer, self).__init__()
        self.map_list = map_list

    def reduce(self):
        self.reduce_output = {}
        for length in range(0, len(self.map_list)):
            current_pair = self.map_list[length]
            current_word = current_pair.keys()
            current_count = 0
        for i in self.map_list:
            key = i.keys()
        if current_word == key:
            current_count = current_count + 1
        self.reduce_output[current_word[0]] = current_count


text = "ram is a good boy. ram is first boy in the class"
mapper_obj = Mapper(text)
mapper_obj.map()
map_output = mapper_obj.map_output

reducer_obj = Reducer(map_output)
reducer_obj.reduce(map_output)
reducer_obj.reduce()

for frequency in reducer_obj.reduce_output.keys():
    print(f"{frequency}={reducer_obj.reduce_output[frequency]}")
