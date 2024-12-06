# deep_unpack(seq: Iterable\[Iterable\], ignores: type | UnionType = str, _parents:tuple=()) -> list

The first thing this function does is check if the sequence in question is a member of the list of types to ignore. If
this is the case, it simply returns the sequence. If not, the function will iterate through the elements in the
sequence. If the element is not an Iterable, it is simply added to the result. If the element is an iterable and is not
on the ignore list, the result is extended by the result of recursively deep unpacking the element. The _parents
parameter should not be specified by the user and is used only during recursion to combat Iterables that either directly
or indirectly yield themselves. It works by container that holds the sequence being examined, and the container that
holds that container, and so on. The function does assume that the iterables passed will