# function_lines(f: Callable\[\[Number\], Number\], start: Number, end: Number, n: int = 100) -> tuple\[tuple\[Number, Number\]\]

The function first stores the results of calling the helper function _function_points on with the parameters f, start,
end, and n + 1. The n + 1 is necessary because the function needs n + 1 ordered pairs of points to calculate n lines
(because lines are formed in between the sets of ordered pairs). The length is calculated with the distance formula and
the heading is calculated from the slope.

The function takes an average of 6.93e-05 seconds to calculate the 100 lines for a parabola, with a maximum memory usage
of 68030 bytes during this process. The complexity of this function is on the order of n * m where m is the complexity
of the function that generates the points.

The data the function generates can be used to allow a turtle to approximate that function. The data can also be used to
approximate shapes in other contexts.