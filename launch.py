import pygame
import alphabet
import copy

# making window and declaring other variables
width = 750
height = 750
screen = pygame.display.set_mode((width, height))

points = []         # points that are currently displayed on screen
endgoal = []        # points of the next letter that will be displayed
queue = []          # queue where sequence of letters will be stored
error = 0.01        # smaller --> slower transition (more smooth)
increment = 120      # larger --> slower transition (more smooth)

screen.fill("black")


def add_points_start(q1, q2):           # where q1 length is greater than that of q2 and q2 is start
    """
    add points to starting queue because it does not have enough points
    :param q1: larger queue, also the end goal letter
    :param q2: shorter queue, also the starting letter
    :return: None
    """
    global points, endgoal              # get variables from outer scope
    points, endgoal = [], []            # clear lists because creating new lists
    rep = len(q1) - len(q2)             # how many extra points
    points = copy.deepcopy(q2)          # copy starting letter points without reference

    # inserting new points into starting queue
    for ind in range((rep+1)//2):
        points.append(q2[len(q2)-1])
    for ind in range(rep//2):
        points.insert(0, q2[0])

    # setting ending queue to ending letters
    endgoal = copy.deepcopy(q1)


def add_points_end(q1, q2):             # where q1 length is greater than that of q2 and q1 is start
    """
    add points to ending queue because it does not have enough points
    :param q1: larger queue, also the starting letter
    :param q2: shorter queue, also the end goal letter
    :return: None
    """
    global points, endgoal              # get variables from outer scope
    points, endgoal = [], []            # clear lists because creating new ones
    rep = len(q1) - len(q2)             # how many extra points
    endgoal = copy.deepcopy(q2)         # copy ending letter points without reference

    # inserting new points into ending queue
    for ind in range((rep+1)//2):
        endgoal.append(q2[len(q2)-1])
    for ind in range(rep//2):
        endgoal.insert(0, q2[0])

    # setting starting queue to starting letter
    points = copy.deepcopy(q1)


def move_points(start, end):
    """
    move one point a little bit towards another point
    :param start: starting point
    :param end: point to move towards
    :return: tuple of new coords of the point
    """
    dx = (end[0] - start[0])/increment      # move only a little bit towards the end
    dy = (end[1] - start[1])/increment      # before:   * ----------
                                            #           (start)     (end)
    if abs(dx) + abs(dy) < error:           # after:     * ---------
        return end                          #           (new pt)    (end)
    return start[0]+dx, start[1]+dy


# string of letters to morph into one-by-one
letters = 'Hi I love you'

# adding letters into the queue
queue.append('cdot')        # start with a center dot for aesthetics
for c in letters:
    if c == ' ':            # spaces turn into center dots
        queue.append('cdot')
    else:                   # only use capital letters
        queue.append(c.upper())


loop = True         # so that the letters will loop forever
cur = 0             # current index of letter

while loop:
    # set endgoal and starting points
    if len(alphabet.chars[queue[cur]]) < len(alphabet.chars[queue[(cur+1) % len(queue)]]):
        add_points_start(alphabet.chars[queue[(cur+1) % len(queue)]], alphabet.chars[queue[cur]])
    else:
        add_points_end(alphabet.chars[queue[cur]], alphabet.chars[queue[(cur+1) % len(queue)]])
    cur = (cur+1) % len(queue)
    endgoal.reverse()

    # draw current letter
    pygame.draw.lines(screen, "cyan", False, points, 4)
    pygame.display.flip()           # updating screen
    pygame.time.wait(100)           # wait for a bit for letter to stay a bit longer

    # moving points in start closer to endgoal until they are practically the same
    while points != endgoal:
        # fill screen with black before redrawing moved points
        screen.fill("black")
        pygame.draw.lines(screen, "cyan", False, points, 4)

        # moving each point in queue by a little bit
        for i in range(len(points)):
            points[i] = move_points(points[i], endgoal[i])
            pygame.display.flip()

    pygame.time.wait(750)       # making the letter stay for a bit longer

pygame.time.wait(5000)          # never reaches here, but if it does, pauses at last letter for longer
pygame.quit()
