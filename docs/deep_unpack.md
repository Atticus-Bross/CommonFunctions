# deep_unpack(seq: Iterable\[Iterable\], ignores: type | UnionType = str, _parents:tuple=()) -> list

The first thing this function does is check if the sequence in question is a member of the list of types to ignore. If
this is the case, it simply returns the sequence. If not, the function will iterate through the elements in the
sequence. If the element is not an Iterable, it is simply added to the result. If the element is an iterable and is not
on the ignore list, the result is extended by the result of recursively deep unpacking the element. The _parents
parameter should not be specified by the user and is used only during recursion to deal with Iterables that either
directly
or indirectly yield themselves. It works by container that holds the sequence being examined, and the container that
holds that container, and so on. The function does assume that the iterables passed will not cause infinite recursion
for other reasons.

The function takes an average of 3.11e-5 seconds to unpack a list of 10 lists of 10 numbers. The function's maximum
memory usage during execution is 59,399 bytes. The complexity of the function is in the order of n. The function was
implemented recursively in order to make the implementation easier.
However, this leads to more memory usage.

This function is useful when the user wants to iterate through all elements of a complex data structure, rather than
substructures of the superstructure that actually contain those elements.