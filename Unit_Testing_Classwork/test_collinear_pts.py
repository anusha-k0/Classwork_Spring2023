import pytest


def create_coord():
    from random import uniform
    num_default_coords = 5
    inp_coords = []
    for _ in range(num_default_coords):
        inp_coords.append(round(uniform(-1000, 1000), 2))
        # -1000 to 1000 was arbitrarily selected as range of coordinate values
    test_coordinates = list(zip(inp_coords[::2], inp_coords[1::2]))
    test_coordinates.append(inp_coords[-1])
    return test_coordinates


def test_for_collinearity():
    from collinear_pts import find_collinear_pt
    test_coordinates = create_coord()
    print(test_coordinates)
    coord1 = test_coordinates[0]
    coord2 = test_coordinates[1]
    x3 = test_coordinates[2]
    y3 = find_collinear_pt(coord1, coord2, x3)
    print(y3)
    coord3 = (x3, y3)
    answer = (
            coord1[0] * (coord2[1] - coord3[1]) + coord2[0] *
            (coord3[1] - coord1[1]) + coord3[0] * (coord1[1] - coord2[1]))
    assert round(answer, 5) == 0
