def avg(num1, num2):
    return (num1 + num2) / 2


# common pts:
minx = 275
maxx = 475
midx = avg(minx, maxx)
miny = 225
maxy = 525
midy = avg(miny, maxy)
c = 40

chars = {
    'cdot': [(midx, midy), (midx, midy)],
    'tldot': [(minx, miny), (minx, miny)],
    'trdot': [(maxx, miny), (maxx, miny)],
    'bldot': [(minx, maxy), (minx, maxy)],
    'brdot': [(maxx, maxy), (maxx, maxy)],
    'A': [(minx, maxy), (midx, miny), (avg(avg(midx, maxx), maxx), avg(midy, maxy)),
          (avg(avg(midx, minx), minx), avg(midy, maxy)), (avg(avg(midx, maxx), maxx), avg(midy, maxy)),
          (maxx, maxy)],
    'B': [(minx, miny), (maxx - c, miny), (maxx, miny + c), (maxx, midy - c),
          (maxx - c, midy), (minx, midy), (maxx - c, midy), (maxx, midy + c),
          (maxx, maxy - c), (maxx - c, maxy), (minx, maxy), (minx, miny)],
    'C': [(maxx, miny + c), (maxx - c, miny), (minx + c, miny), (minx, miny + c),
          (minx, maxy - c), (minx + c, maxy), (maxx - c, maxy), (maxx, maxy - c)],
    'D': [(minx, maxy), (maxx - c, maxy), (maxx, maxy - c),
          (maxx, miny + c), (maxx - c, miny), (minx, miny), (minx, maxy)],
    'E': [(maxx, miny), (minx, miny), (minx, midy), (midx+c, midy), (minx, midy),
          (minx, maxy), (maxx, maxy)],
    'F': [(maxx, miny), (minx, miny), (minx, midy), (midx+c, midy), (minx, midy),
          (minx, maxy)],
    'G': [(maxx, miny + c), (maxx - c, miny), (minx + c, miny), (minx, miny + c),
          (minx, maxy - c), (minx + c, maxy), (maxx - c, maxy), (maxx, maxy - c),
          (maxx, midy + c), (maxx - 1.5 * c, midy + c)],
    'H': [(minx, miny), (minx, maxy), (minx, midy), (minx, midy), (maxx, midy), (maxx, maxy), (maxx, miny)],
    'I': [(midx+c, miny), (midx-c, miny), (midx, miny), (midx, maxy), (midx+c, maxy), (midx-c, maxy)],
    'J': [(midx-1.5*c, miny), (midx+1.5*c, miny), (midx, miny), (midx, maxy-c), (midx-c/2, maxy),
          (minx+c/2, maxy), (minx, maxy-c)],
    'K': [(minx, miny), (minx, maxy), (minx, midy), (maxx-c, miny), (minx, midy), (maxx-c, maxy)],
    'L': [(minx, miny), (minx, miny), (minx, maxy), (maxx-c, maxy)],
    'M': [(minx, maxy), (minx, miny), (midx, midy), (maxx, miny), (maxx, maxy)],
    'N': [(minx, maxy), (minx, miny), (maxx, maxy), (maxx, miny)],
    'O': [(minx, miny + c), (minx + c, miny), (maxx - c, miny), (maxx, miny + c),
          (maxx, maxy - c), (maxx - c, maxy), (minx + c, maxy), (minx, maxy - c),
          (minx, miny + c)],
    'P': [(minx, maxy), (minx, miny), (maxx-2*c, miny), (maxx-c, miny+c), (maxx-c, midy-c),
          (maxx-2*c, midy), (minx, midy)],
    'Q': [(maxx, maxy), (maxx-1.5*c, maxy-1.5*c), (maxx-c/2, maxy-c/2), (maxx-c, maxy),
          (minx+c, maxy), (minx, maxy-c), (minx, miny+c), (minx+c, miny), (maxx-c, miny),
          (maxx, miny+c), (maxx, maxy-c), (maxx-c/2, maxy-c/2)],
    'R': [(minx, maxy), (minx, miny), (maxx-2*c, miny), (maxx-c, miny+c), (maxx-c, midy-c),
          (maxx-2*c, midy), (minx, midy), (minx+c, midy), (maxx-c, maxy)],
    'S': [(maxx, miny+c), (maxx-c, miny), (minx+c, miny), (minx, miny+c), (minx, midy-c),
          (minx+c, midy), (maxx-c, midy), (maxx, midy+c), (maxx, maxy-c), (maxx-c, maxy),
          (minx+c, maxy), (minx, maxy-c)],
    'T': [(midx, maxy),  (midx, miny), (midx-2*c, miny), (midx+2*c, miny)],
    'U': [(minx+c/2, miny), (minx+c/2, maxy-c), (minx+1.5*c, maxy), (maxx-1.5*c, maxy),
          (maxx-c/2, maxy-c), (maxx-c/2, miny)],
    'V': [(minx, miny), (midx, maxy), (maxx, miny)],
    'W': [(minx, miny + c), (minx + c / 2, maxy), (midx, midy),
          (maxx - c / 2, maxy), (maxx, miny + c)],
    'X': [(maxx, miny), (minx, maxy), (midx, midy), (minx, miny), (maxx, maxy)],
    'Y': [(minx, miny), (midx, midy-c), (maxx, miny), (midx, midy-c), (midx, maxy)],
    'Z': [(minx, miny), (maxx, miny), (minx, maxy), (maxx, maxy)],
    '.': [(maxx-c, maxy-c), (maxx-c/4-c, maxy-c), (maxx-c/4-c, maxy-c/4-c),
          (maxx-c, maxy-c/4-c), (maxx-c, maxy-c)]
}

