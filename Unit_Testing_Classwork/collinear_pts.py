def input_interface():
    x_1 = float(input("Enter x1 coordinate: "))
    y_1 = float(input("Enter y1 coordinate: "))
    x_2 = float(input("Enter x2 coordinate: "))
    y_2 = float(input("Enter y2 coordinate: "))
    x_3 = float(input("Enter x3 coordinate: "))
    coord1 = (x_1, y_1)
    coord2 = (x_2, y_2)
    return collinear_driver()


def collinear_driver():
    y_3 = find_collinear_pt(coord1, coord2, x_3)
    coord3 = (x_3, round(y_3, 2))
    return display_interface(coord1, coord2, coord3)


def find_collinear_pt(coord1, coord2, x_3):
    m = (coord2[1] - coord1[1]) / (coord2[0] - coord1[0])
    b = coord1[1] - (m * coord1[0])
    y_3 = (m * x_3) + b
    return y_3


def display_interface(coord1, coord2, coord3):
    print(f"The y-coordinate for the point is:{coord3[1]}")
    print(f"{tuple(coord1)},{tuple(coord2)} and {coord3} lie on the same line")


if __name__ == "__main__":
    input_interface()
