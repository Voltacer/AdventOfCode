class Waypoints:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.history = []

    def getPosition(self):
        return {'x': self.x, 'y': self.y}

    def move(self, x, y):
        if self.x != 0 and self.y != 0:
            self.history.append({'x': self.x, 'y': self.y})
        self.x = x
        self.y = y

    def getHistory(self):
        return self.history

def move(instruction, waypoints):
    type = instruction[:1]
    distance = int(instruction[1:])

    waypoint = waypoints.getPosition()

    if type == 'R':
        waypoints.move(waypoint['x'] + distance, waypoint['y'])

    if type == 'L':
        waypoints.move(waypoint['x'] - distance, waypoint['y'])

    if type == 'U':
        waypoints.move(waypoint['x'], waypoint['y'] + distance)

    if type == 'D':
        waypoints.move(waypoint['x'], waypoint['y'] - distance)

intersects = []
def move_and_compare(instruction, drawnWaypoints, waypoints):
    global intersects
    position = waypoints.getPosition()

    for wp in drawnWaypoints:
        if wp.get('x') == position.get('x') and wp.get('y') == position.get('y'):
            intersects.append(position)

    move(instruction, waypoints)


f = open('input.txt', 'r')
line_instructions = []
line = f.readline().strip()
line_instructions.append([line])
line = f.readline().strip()
line_instructions.append([line])

waypointlist = []

first_line_instructions = line_instructions[0][0].split(',')
waypoints = Waypoints(0, 0)
for instr in first_line_instructions:
    move(instr, waypoints)

second_waypoints = Waypoints(0, 0)
second_line_instructions = line_instructions[1][0].split(',')
for instr in second_line_instructions:
    move_and_compare(instr, waypoints.getHistory(), second_waypoints)

print(intersects)
