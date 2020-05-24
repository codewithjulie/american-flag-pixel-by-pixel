from simpleimage import SimpleImage

WIDTH = 693
HEIGHT = 416
BLUE_WIDTH = 282
BLUE_HEIGHT = 224
LENGTH_BETWEEN_STRIPES = HEIGHT // 13
START_STARS_X = 12
START_STARS_Y = 13
STARS_WIDTH = 18
STARS_HEIGHT = 17
WIDTH_SPACER = 6
HEIGHT_SPACER = 5


def draw_star(pixel, x, y, k, l):
    if y == k and (x == (l + 8) or x == (l + 9)):
        pixel.red = pixel.green = pixel.blue = 255
    if (y == (k + 1) or y == (k + 2)) and (x >= (l + 7) and x <= (l + 10)):
        pixel.red = pixel.green = pixel.blue = 255
    if (y == (k + 3) or y == (k + 4)) and (x >= (l + 6) and x <= (l + 11)):
        pixel.red = pixel.green = pixel.blue = 255
    if y == (k + 5) and (x >= l and x <= (l + 17)):
        pixel.red = pixel.green = pixel.blue = 255
    if (y == (k + 6)) and (x >= (l + 1) and x <= (l + 16)):
        pixel.red = pixel.green = pixel.blue = 255
    if y == (k + 7) and (x >= (l + 2) and x <= (l + 15)):
        pixel.red = pixel.green = pixel.blue = 255
    if y == (k + 8) and (x >= (l + 3) and x <= (l + 14)):
        pixel.red = pixel.green = pixel.blue = 255
    if (y == (k + 9) or y == (k + 10)) and (x >= (l + 4) and x <= (l + 13)):
        pixel.red = pixel.green = pixel.blue = 255
    if (y == (k + 11) or y == (k + 12)) and (x >= (l + 3) and x <= (l + 14)):
        pixel.red = pixel.green = pixel.blue = 255
    if y == (k + 13) and ((x >= (l + 2) and x <= (l + 7)) or ((x >= (l + 10) and x <= (l + 15)))):
        pixel.red = pixel.green = pixel.blue = 255
    if y == (k + 14) and ((x >= (l + 2) and x <= (l + 6)) \
        or ((x >= (l + 11) and x <= (l + 15)))):
            pixel.red = pixel.green = pixel.blue = 255
    if y == (k + 15) and ((x >= (l + 1) and x <= (l + 4)) \
        or ((x >= (l + 14) and x <= (l + 16)))):
            pixel.red = pixel.green = pixel.blue = 255 
    if y == (k + 16) and ((x >= l and x <= (l + 2) \
        or (x >= (l + 16) and x <= (l + 17)))):
            pixel.red = pixel.green = pixel.blue = 255


def draw_six_by_five_stars(pixel, x, y):
    for k in range(START_STARS_Y, BLUE_HEIGHT, (STARS_HEIGHT + HEIGHT_SPACER) * 2):
        for l in range(START_STARS_X, BLUE_WIDTH, (STARS_WIDTH + WIDTH_SPACER) * 2):
            draw_star(pixel, x, y, k, l)


def draw_five_by_four_stars(pixel, x, y):
    for k in range(START_STARS_Y + STARS_HEIGHT + HEIGHT_SPACER, BLUE_HEIGHT - 15, (STARS_HEIGHT + HEIGHT_SPACER) * 2):
        for l in range(START_STARS_X + STARS_WIDTH + WIDTH_SPACER, BLUE_WIDTH - 15, (STARS_WIDTH + WIDTH_SPACER) * 2):
            draw_star(pixel, x, y, k, l)


def draw_blue_rectangle(pixel, x, y):
    if (x < BLUE_WIDTH) and (y < BLUE_HEIGHT): 
        pixel.red, pixel.green, pixel.blue = 30, 50, 100
    if x >= BLUE_WIDTH and y < BLUE_HEIGHT:  # prints shorter stripes
        for i in range(0, BLUE_HEIGHT, LENGTH_BETWEEN_STRIPES * 2):
            if y >= i and y < (i + LENGTH_BETWEEN_STRIPES):
                pixel.red, pixel.green, pixel.blue = 255, 0, 0
    if y >= BLUE_HEIGHT:  # prints longer stripes
        for j in range(128, WIDTH, LENGTH_BETWEEN_STRIPES * 2):
            if y >= j and y < (j + LENGTH_BETWEEN_STRIPES):
                pixel.red, pixel.green, pixel.blue = 255, 0, 0


def draw_american_flag():
    flag = SimpleImage.blank(WIDTH, HEIGHT)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pixel = flag.get_pixel(x, y)
            draw_blue_rectangle(pixel, x, y)
            draw_six_by_five_stars(pixel, x, y)
            draw_five_by_four_stars(pixel, x, y)
    return flag


def main():
    american_flag = draw_american_flag()
    american_flag.show()


if __name__ == "__main__":
    main()
