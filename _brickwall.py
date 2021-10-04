"""
The decision for "brickwall" task with graphics display.
"""
import random
import pprint
from PIL import Image, ImageDraw, ImageFont


def brickwall_draw(brickwall, result):
    """
    draw our brickwall with redlines and numerical scale, parameters:
    brickwall (list),
    results (number of min intersections, positions list)
    """
    (_, positions) = result

    # set parameters
    margin = 10
    scale = 20
    padding = 4
    indent = 20
    font_size = 10

    wall_height = len(brickwall)
    wall_width = brickrow_width(brickwall[0])
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", font_size)

    canvas_width = wall_width * scale + 2 * margin
    canvas_height = wall_height * scale + 2 * margin + indent
    # print(f'canvas_width = {canvas_width}, canvas_height = {canvas_height}')

    img = Image.new('RGB', (canvas_width, canvas_height), (20, 20, 20))
    draw = ImageDraw.Draw(img)

    # draw brickwall
    for i in range(wall_height):
        row = brickwall[i]
        brick_quantity = len(row)

        row_accum = 0
        for j in range(brick_quantity):
            brick_width = row[j]
            draw.rectangle((
                margin + row_accum,
                margin + scale*i,
                margin + scale*brick_width + row_accum,
                margin + scale*i + scale
            ), fill=(
                random.randint(35, 40),
                random.randint(35, 40),
                random.randint(35, 40)),
            outline=(255, 255, 255))
            row_accum += brick_width * scale

    # draw red lines for sough intersections
    for k in positions:
        draw.rectangle((
            margin - padding + scale * (k+1),
            margin - padding + 0,
            margin + padding + scale * (k+1),
            margin + padding + scale * wall_height
        ), fill=None, outline=(255, 0, 0))

    # draw numerical scale
    for i in range(wall_width-1):
        text = str(i)
        draw.text((25+i*scale, canvas_height-indent), text, font = font, align ="left")

    img.show()


def brickrow_width(row: list):
    """docstring"""
    width = 0
    for i in row:
        width += i
    return width


def generate_brickwall(width: int, height: int, max_brick_size: int) -> list:
    """
    Generate brickwall with parametres:
        width of wall: 1st parameter,
        height of wall: 2nd parameter,
        width of brick: random range from 1 to 3rd parameter
    """
    wall = []
    for _ in range(height):
        row = []
        total_width = 0
        while brickrow_width(row) < width:
            brick = random.randint(1, max_brick_size)
            row.append(brick)
            total_width += brick
            if width - total_width < max_brick_size and width - total_width != 0:
                row.append(width - total_width)
        wall.append(row)
    return wall


def min_quantity_brick_cross(brickwall: list):
    """docstring"""
    height = len(brickwall)
    brickwall_width = brickrow_width(brickwall[0])
    wall_map = [0] * (brickwall_width-1)
    for i in range(height):
        brick_quantity = len(brickwall[i])
        row_map = [0] * (brickwall_width-1)
        item = 0
        for j in range(brick_quantity-1):
            item += brickwall[i][j]
            row_map[item-1] = 1
        wall_map = map(sum, zip(wall_map, row_map))
    wall_map = list(wall_map)
    print(wall_map)

    max_cross = 0
    for i in wall_map:
        if i > max_cross:
            max_cross = i

    positions = [i for i, x in enumerate(wall_map) if x == max_cross]
    result = height - max_cross
    return (result, positions)


generated_brickwall = generate_brickwall(40, 20, 4)
pprint.pprint(generated_brickwall)

crosses_and_positions = min_quantity_brick_cross(generated_brickwall)
print(f'Min crosses = {crosses_and_positions[0]}, in positions: {crosses_and_positions[1]}')

brickwall_draw(generated_brickwall, crosses_and_positions)
