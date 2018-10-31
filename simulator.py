import numpy as np
from numpy import random


class Box:
    """This class is creating for box generating with set parameters including generating various numbers of points
    in it."""

    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step
        self.x_plane = np.round(np.arange(0, x + step, step), 1)
        self.y_plane = np.round(np.arange(0, y + step, step), 1)
        self.points = list()

    def add_point(self, x, y, velocity_x, velocity_y, diameter):
        if x not in self.x_plane:
            raise ValueError("The parameter X of the ball does not match the range of the plane X.")
        elif y not in self.y_plane:
            raise ValueError("The parameter Y of the ball does not match the range of the plane Y.")

        if diameter <= 0 or diameter not in self.x_plane or diameter not in self.y_plane:
            raise ValueError("Diameter must be more than 0 and match range of planes.")
        else:
            self.points.append(Point(x, y, velocity_x, velocity_y, diameter))

    def add_random_points(self, n):
        for n in range(n):
            x = random.choice(self.x_plane)
            y = random.choice(self.y_plane)
            velocity_x = round(random.uniform(0, 10), 2)
            velocity_y = round(random.uniform(0, 10), 2)
            diameter = self.point_diameter()
            self.add_point(x, y, velocity_x, velocity_y, diameter)

    def point_diameter(self):
        diameter_range = np.round(np.arange(0, 1+self.step, self.step), 1)
        while True:
            diameter = random.choice(diameter_range)
            if diameter > 0:
                return diameter

    def show_points(self):
        print("\nList contains {0} points: \n{1}\n".format(len(self.points), self.points))


class Point:
    """This class is responsible for creating point information"""

    def __init__(self, x, y, velocity_x, velocity_y, diameter):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.diameter = diameter

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def velocity(self):
        velocity = np.sqrt(self.velocity_x ** 2 + self.velocity_y ** 2)
        return velocity

    def move(self, t):
        x = self.x + self.velocity_x * t
        y = self.y + self.velocity_y * t

        return x, y

    def move_process(self, t, dt):
        move_list = list()

        for i in range(0, t + 1, dt):
            x = self.move(i)[0]
            y = self.move(i)[1]
            move_list.append([x, y, i])

        self.x = x
        self.y = y

        return move_list

    def save_move(self, t, dt):
        with open('move.csv', 'w') as my_file:
            for x, y, t in self.move_process(t, dt):
                my_file.write('%d,%d,%d\n' % (x, y, t))

    def show(self):
        print("Coordinate [x,y]: %d, %d" % (self.x, self.y))
        print("Velocity: %0.2f" % self.velocity())


my_box = Box(100000, 100000, step=0.2)

my_box.add_random_points(10)
my_box.show_points()

# for one, two in zip(my_box.x_plane, my_box.y_plane):
# print(one, two)
