from search.uninformed.dls import depth_limited_search

def iterative_deepening_search(problem, max_depth=None):
    """
    Iterative Deepening Depth-First Search (IDDFS).
    Repeatedly applies Depth-Limited Search with increasing limits.
    """

    depth = 0

    while max_depth is None or depth <= max_depth:
        result = depth_limited_search(problem, depth)

        if result != "cutoff":
            return result
        
        depth += 1 

    return None

