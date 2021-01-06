#example from MRJob and intro

from mrjob.job import MRJob
class MRWordCountUtility(MRJob):

    def __init__(self, *args, **kwargs):
        super(MRWordCountUtility, self).__init__(*args, **kwargs)
        self.chars = 0
        self.words = 0
        self.lines = 0

    def mapper(self, _, line):
        self.chars += len(line) +1
        self.words += sum(1 for word in line.split() if word.strip())
        self.lines += 1

    def mapper_final(self):
        yield('chars', self.chars)
        yield('words', self.words)
        yield('lines', self.lines)

    def reducer(self, key, values):
        yield(key, sum(values))


if __name__ == '__main__':
    MRWordCountUtility.run()

#to execute from command prompt: 
#python ex_1\char_word_line_count.py input_data\Life_of_PI_good_review.txt