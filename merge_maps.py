def merge_maps_update(map1, map2):
    """
    Merges two maps using the update() method.
    Modifies map1 in place.
    """
    merged = map1.copy()
    merged.update(map2)
    return merged

def merge_maps_unpacking(map1, map2):
    """
    Merges two maps using dictionary unpacking (**).
    """
    return {**map1, **map2}

def merge_maps_operator(map1, map2):
    """
    Merges two maps using the union operator (|).
    Valid for Python 3.9+.
    """
    return map1 | map2

if __name__ == "__main__":
    map_a = {'a': 1, 'b': 2}
    map_b = {'b': 3, 'c': 4}

    print(f"Map A: {map_a}")
    print(f"Map B: {map_b}")

    # Method 1: update()
    result1 = merge_maps_update(map_a, map_b)
    print(f"Merged (update): {result1}")

    # Method 2: Unpacking
    result2 = merge_maps_unpacking(map_a, map_b)
    print(f"Merged (unpacking): {result2}")

    # Method 3: Union Operator (Python 3.9+)
    try:
        result3 = merge_maps_operator(map_a, map_b)
        print(f"Merged (| operator): {result3}")
    except TypeError:
        print("Merged (| operator): Not supported in this Python version (requires 3.9+)")
