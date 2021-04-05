import pygame
import alphabet
import copy


def add_points_start(q1, q2):           # where q1 length is greater than that of q2 and q2 is start
    """

    :param q1:
    :param q2:
    :return:
    """
    global points, endgoal
    points, endgoal = [], []            # clear lists
    rep = len(q1) - len(q2)
    """for ind in range(len(q2)):
        points.append(q2[ind])
        if ind < rep:
            points.append(q2[ind])"""
    points = copy.deepcopy(q2)
    for ind in range((rep+1)//2):
        points.append(q2[len(q2)-1])
    for ind in range(rep//2):
        points.insert(0, q2[0])
    endgoal = copy.deepcopy(q1)


def add_points_end(q1, q2):             # where q1 length is greater than that of q2 and q1 is start
    """

    :param q1:
    :param q2:
    :return:
    """
    global points, endgoal
    points, endgoal = [], []            # clear lists
    rep = len(q1) - len(q2)
    """for ind in range(len(q2)):
        endgoal.append(q2[ind])
        if ind < rep:
            endgoal.append(q2[ind])
            """
    endgoal = copy.deepcopy(q2)
    for ind in range((rep+1)//2):
        endgoal.append(q2[len(q2)-1])
    for ind in range(rep//2):
        endgoal.insert(0, q2[0])
    points = copy.deepcopy(q1)


def move_points(start, end):
    """

    :param start:
    :param end:
    :return: tuple
    """
    dx = (end[0] - start[0])/60
    dy = (end[1] - start[1])/60

    if abs(dx) < 0.03 and abs(dy) < 0.03:
        return end
    return start[0]+dx, start[1]+dy


width = 500
height = 500
screen = pygame.display.set_mode((width, height))

points = []
endgoal = []

if len(alphabet.chars['A']) < len(alphabet.chars['B']):
    add_points_start(alphabet.chars['B'], alphabet.chars['A'])
else:
    add_points_end(alphabet.chars['A'], alphabet.chars['B'])

print(points)
print(endgoal)
pygame.draw.lines(screen, "cyan", False, points, 2)
pygame.display.flip()
pygame.time.wait(50)

ind = 0
while points != endgoal:
    screen.fill("black")
    pygame.draw.lines(screen, "cyan", False, points, 2)
    pygame.display.flip()

    for i in range(len(points)):
        points[i] = move_points(points[i], endgoal[i])
        print(points[i], "", endgoal[i])
        pygame.display.flip()
    pygame.time.wait(6)
    ind += 1

pygame.time.wait(5000)
pygame.quit()
