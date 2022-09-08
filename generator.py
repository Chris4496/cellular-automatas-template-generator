import cairo


def draw_square(cr, x, y, size):
    cr.rectangle(x, y, size, size)
    cr.stroke()


def calculate_number_of_cells(depth):
    return 2 * depth + 1


depth = int(input("Enter the depth of the fractal: "))
cell_width = int(input("Enter the width of the cells: "))
line_width = int(input("Enter the line width (deafault = 1): ") or 1)


width = calculate_number_of_cells(depth) * cell_width
height = depth * cell_width

center = width / 2

# print info
print(f"depth: {depth}")
print(f"cell width: {cell_width}")
print(f"line width: {line_width}")
print(f"width: {width}")
print(f"height: {height}")
print(f"center: {center}")


def main():
    file_name = f"template_{depth}_{cell_width}_{line_width}.svg"
    with cairo.SVGSurface(file_name, width, height) as surface:
        context = cairo.Context(surface)
        context.set_line_width(line_width)
        # draw a cellular automatas
        for layer in range(depth):
            y = layer * cell_width
            num_of_cells = calculate_number_of_cells(layer)
            for cell in range(num_of_cells):
                x = center - (num_of_cells / 2 - cell) * cell_width
                draw_square(context, x, y, cell_width)

    print("Saved in current directory:", file_name,
          "(template_{depth}_{cell_width}_{line_width}.svg)")


if __name__ == "__main__":
    main()
