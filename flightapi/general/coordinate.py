
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

def point_bounds(points):
    min_longitude = 180
    max_longitude = -180
    max_latitude = -90
    min_latitude = 90
    lon_overflow = False
    last_lon = 0
    def between(v, l, h):
        return v <= h and v >= l
    for p in points:
        if p[0] < min_longitude:
            min_longitude = p[0]
        elif p[0] > max_longitude:
            max_longitude = p[0]
        if p[1] < min_latitude:
            min_latitude = p[1]
        elif p[1] > max_latitude:
            max_latitude = p[1]
    return {'min_longitude': min_longitude, 'max_longitude': max_longitude,
            'min_latitude': min_latitude, 'max_latitude': max_latitude}