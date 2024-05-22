
class MultipleItems:

    def lists(self):

        """A list is an ordered collection of items, which can be of different data types.
        Lists are mutable, meaning their elements can be modified, added, remove and indexed.
        Indexing starts with 0"""

        mixed = ['hello', 42, True, 3.14]

        print("Original list:", mixed)

        """Index use, we can isolate each item for individual use
        thus mixed[0] gives hello"""

        Items = mixed[0]

        print("First item:", Items)

        """Remove the integer 42 from the list"""

        mixed.remove(42)
        print("List after removing 42:", mixed)

        """Next we will add an item to the list"""

        mixed.append(43)
        print("List after adding 43:", mixed)

        """NEXT we explain Splicing"""

        """
           Splicing is a way to extract a subset of elements from a list.
           The syntax is: list[start:stop:step]
           - start: the index at which to start the slice (inclusive)
           - stop: the index at which to end the slice (exclusive)
           - step: the step size (optional, defaults to 1)
           """

        # Example 1: Slice from index 1 to the end
        print("Slice from index 1 to the end:", mixed[1:])

        # Example 2: Slice from the start to index 2 (exclusive)
        print("Slice from the start to index 2:", mixed[:2])

        # Example 3: Slice with a step size of 2
        print("Slice with a step size of 2:", mixed[::2])

    def ordering(self):

        """ To reorder a list, we can use the sort() method or the sorted() function.
        The sort() method sorts the list in-place, while sorted() returns a new sorted list. """

        unsorted_list = [6, 4, 8, 1, 3, 9]
        print("Unsorted list:", unsorted_list)

        """Sort the list in ascending order"""

        unsorted_list.sort()
        print("Sorted list (ascending):", unsorted_list)


data = MultipleItems()

data.lists()
data.ordering()


