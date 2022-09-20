def get_coordinates(coord_01, coord_02):
    x1, y1 = coord_01[0], coord_01[1]
    x2, y2 = coord_02[0], coord_02[1]

    w = x2 - x1
    h = y2 - y1
    dx1, dy1 = 0, 0
    dx2, dy2 = 0, 0

    dx1 = -1 if w < 0 else 1
    dy1 = -1 if h < 0 else 1
    dx2 = -1 if w < 0 else 1

    longest = abs(w)
    shortest = abs(h)

    if not (longest > shortest):
        longest = abs(h)
        shortest = abs(w)
        dy2 = -1 if h < 0 else 1
        dx2 = 0

    numerator = longest >> 1
    coordinates = []
    for i in range(0, longest):
        coordinates.append((x1, y1))
        numerator += shortest
        if not (numerator < longest):
            numerator -= longest
            x1 += dx1
            y1 += dy1
        else:
            x1 += dx2
            y1 += dy2
    return coordinates


