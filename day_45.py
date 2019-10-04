#-------- DAY 45 "iterators" --------
print("Lesson 45: Iterators")
# An iterator is an object that contains a countable number of values
# Methods:
#     1. iter(): used to get an iterator
#     2. next(): to take the next value
# String, list, tuple, set and dictionary are all iterable objects
tuple, txt = ('red', 'white', 'blue'), 'amani'
tupit = iter(tuple)
print("The colors of French flag are:", next(tupit) + ",", next(tupit), "and", next(tupit))
print('---------------------\nThese are my letters:')
# The for loop actually creates an iterator object & executes the next() method for each loop
for x in txt:
    print(x)
print('---------------------\nCount with me:')
# Create an iterator in classes
class count:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 12:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

obj = count()
objit = iter(obj)
for k in objit:
    print(k)
