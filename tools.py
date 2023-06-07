from main import logger
class FlatIterator:
    def __init__(self, nested_list):  # конструктор принимает два аргумента low и high (помимо self)
        self.flat_list = []
        self.flatten(nested_list)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self, *args):
        if self.index < len(self.flat_list):
            item = self.flat_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def flatten(self, nested_list):
        for item in nested_list:
            if isinstance(item, list):
                self.flatten(item)
            else:
                self.flat_list.append(item)
@logger(path='log_4.log')
def test_3():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]