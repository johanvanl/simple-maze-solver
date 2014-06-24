# http://stackoverflow.com/questions/12995434/representing-and-solving-a-maze-given-an-image

import numpy as NP
import Image, ImageDraw
import Queue

start = (402, 987)
end = (396, 19)

img = Image.open("binary.gif")
img_size = img.size
pixels = img.load()

# False if black / wall
maze = NP.empty(img_size, dtype=bool)

# True if has been visited
distance = NP.empty(img_size, dtype=NP.dtype(int))

for x in range(img_size[0]):
    for y in range(img_size[1]):
        distance[x][y] = -1
        if pixels[x,y] == 0:
            maze[x][y] = False
        else:
            maze[x][y] = True
        
img = img.convert('RGB')
draw = ImageDraw.Draw(img)

distance[start[0]][start[1]] = 0

q = Queue.Queue()
q.put(start)
while not q.empty():
    point = q.get()
    if point == end:
        break
    dist = distance[point[0]][point[1]]
    if maze[point[0]+1][point[1]] and distance[point[0]+1][point[1]] < 0:
        distance[point[0]+1][point[1]] = dist + 1
        q.put((point[0]+1, point[1]))
    if maze[point[0]-1][point[1]] and distance[point[0]-1][point[1]] < 0:
        distance[point[0]-1][point[1]] = dist + 1
        q.put((point[0]-1, point[1]))
    if maze[point[0]][point[1]+1] and distance[point[0]][point[1]+1] < 0:
        distance[point[0]][point[1]+1] = dist + 1
        q.put((point[0], point[1]+1))
    if maze[point[0]][point[1]-1] and distance[point[0]][point[1]-1] < 0:
        distance[point[0]][point[1]-1] = dist + 1
        q.put((point[0], point[1]-1))

point = end
index = distance[end[0]][end[1]]
while index > 1:
    draw.point(point, fill='red')
    if distance[point[0]+1][point[1]] == index - 1:
        point = (point[0]+1, point[1])
        index -= 1
        continue
    if distance[point[0]-1][point[1]] == index - 1:
        point = (point[0]-1, point[1])
        index -= 1
        continue
    if distance[point[0]][point[1]+1] == index - 1:
        point = (point[0], point[1]+1)
        index -= 1
        continue
    if distance[point[0]][point[1]-1] == index - 1:
        point = (point[0], point[1]-1)
        index -= 1
        continue

draw.point(point, fill='red')
draw.point(start, fill='red')
    
img.save("solved.png", "PNG")
