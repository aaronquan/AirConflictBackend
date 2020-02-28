
def is_latitude_intersection(l1, u1, l2, u2):
    assert(l1 >= -90 and l2 >= -90)
    assert(u1 <= 90 and u2 <= 90)
    assert(l1 < u1 and l2 < u2)
    return is_range_intersecting(l1, u1, l2, u2)

# l - lower / u - upper (lon range)
def is_longitude_intersecting(l1, u1, l2, u2):
    assert(all(v <= 180 and v > -180 for v in [l1,u1,l2,u2]))
    out = False
    if l1 < u1 and l2 < u2:
        out = is_range_intersecting(l1, u1, l2, u2)
    elif l1 > u1 and l2 > u2:
        out = True # must always overlap through 180 degrees
    elif l1 > u1:
        out = l1 < u2 or l2 < u1 
    elif l2 > u2:
        out = l1 < u2 or l2 < u1 
    return out

# tests for value range intersections (overlaps) l: low, h: high
def is_range_intersecting(l1, h1, l2, h2):
    return l1 < u2 and l2 < u1 