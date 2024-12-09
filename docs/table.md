# table(col: int, *items: str) -> str

The function first checks that the data can be evenly divided into the specified number of columns and that there will
be at least two rows; it raises a ValueError if these conditions are not met. Then, the function uses the value
representing the number of rows
that it calculated to check that there are at least two rows to construct the rows of the Markdown table
by slicing the data and then calling a helper function _table_row on each slice. The function then inserts the row
below the headers that Markdown tables need to function. The function then joins the rows it has made with '\n' and
returns the value.

The function takes has an average computation time of 8.92e-6 seconds to turn a list of 100 objects into a table with 10
columns. The maximum memory usage during this process is 59,395 bytes. The function's complexity is on the order of
n<sup>3</sup>.

The most obvious use case for this function is to create a Markdown table to write to a Markdown file, but the function
can also be used a skeleton off of which to build other table-making functions.