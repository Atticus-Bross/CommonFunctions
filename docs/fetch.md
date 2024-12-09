# fetch(seq: Sequence | Mapping, indexes: list) -> list:

The function starts by making an empty list in which to store the results. Then, the function iterates through the list
of indexes. If the item is a not a list, the item corresponding to that index is added to the results. If the item is a
list, the function recursively fetches from the sequence that is keyed to by the first element in that list, with the
remaining elements in the list acting the same way the overall index list does. The function assumes that everything
is given is either a valid key for the sequence or a list starting with a valid key for a sequence within the sequence,
with the other elements being similarly valid access paths for the inner sequence.

The function takes an average of 8.57e-6 seconds to retrieve 100 items from a list (time taken is independent of the
size of the list). It has a maximum memory usage of 56,656 bytes during the process. Its complexity is on the order of
m, where m is the number of indexes to retrieve. The implementation of this function was simplified with recursion
at the cost of higher memory usage.

The simplest use case is to simplify the process of retrieving multiple items from a dictionary. The function is also
useful when the user needs retrieve specific data and then keep that data bundled together. A final use for this
function is when very specific data is needed and the data structure is complex
(such as when some items the user needs are in inner sequences and some are not).