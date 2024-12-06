# function_lines(f: Callable\[\[Number\], Number\], start: Number, end: Number, n: int = 100) -> tuple\[tuple\[Number, Number\]\]

The function first stores the results of calling the helper function _function_points on with the parameters f, start,
end, and n + 1. The n + 1 is necessary because the function needs n + 1 ordered pairs of points to calculate n lines
(because lines are formed in between the sets of ordered pairs).