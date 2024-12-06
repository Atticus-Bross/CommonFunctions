# rows(values: list, rows2: int) -> list\[list\]

This function works by computing the length of each row and then using that information to create slices of the data
that correspond to those rows (from row_index * row_len up to but not including (row_index + 1) * row_len). The function
assumes that the data it is given can be divided evenly into the given number of rows and that it represents a table
with the items listed starting with the top-left element, going to the end of the row, going to start of the row one
column down, going to the end of that row, and so on.

This function has an average execution time of 5.83e-6 seconds on lists 100 elements long being divided into 10
columns and the maximum memory usage during execution is 61,815 bytes under the same conditions. Overall this function
has a complexity on the order of n<sup>2</sup>.

This functions would normally be used to look turn a table represented as a list of items into a table represented as a
list of rows, either for viewing or to do some sort of operation on each row. It can also be used to divide data into a
series of blocks of the same length.