# rows(values: list, rows2: int) -> list\[list\]

This function works by computing the length of each row and then using that information to create slices of the data
that correspond to those rows (from row_index * row_len up to but not including (row_index + 1) * row_len). The function
assumes that the data it is given can be divided evenly into the given number of rows and that it represents a table
with the items listed starting with the top-left element, going to the end of the row, going to start of the row one
column down, going to the end of that row, and so on.

