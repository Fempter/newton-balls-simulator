import numpy as np
import time


class Box:
    """This class is made for box generating with set parameters including generating various numbers of points
    in it."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_plane = range(x)
        self.y_plane = range(y)
        self.points_list = list()

    def add_point(self, x, y, velocity_x, velocity_y):
        if x not in self.x_plane:
            raise ValueError("The parameter X of the ball does not match the range of the plane X.")
        elif y not in self.y_plane:
            raise ValueError("The parameter Y of the ball does not match the range of the plane Y.")
        else:
            self.points_list.append(Point(x, y, velocity_x, velocity_y))

    def movement(self, t, dt):
        for n in range(0, t+1, dt):
            for point in self.points_list:
                point.x, point.y = point.move(t)
                while point.x not in self.x_plane:
                    point.x = self.x_plane[0] + point.x - self.x_plane[-1]
                while point.y not in self.y_plane:
                    point.y = self.y_plane[0] + point.y - self.y_plane[-1]

                if point.x not in self.x_plane or point.y not in self.y_plane:
                    print("Błąd")
            self.save_ppm('%s.ppm' % n)

    def add_random_points(self, percentage):
        percentage = percentage / 100

        n = round(self.x * self.y * percentage)
        for n in range(n):
            x = np.random.choice(self.x_plane)
            y = np.random.choice(self.y_plane)
            velocity_x = np.random.randint(0, 10)
            velocity_y = np.random.randint(0, 10)
            # diameter = self.point_diameter()
            self.add_point(x, y, velocity_x, velocity_y)

    def point_diameter(self):
        diameter_range = np.round(np.arange(0, 1), 1)
        while True:
            diameter = np.random.choice(diameter_range)
            if diameter > 0:
                return diameter

    def check_diameter(self):
        """Checking is point with diameter not out of X plane or Y plane"""
        pass

    def show_points(self):
        print("\nList contains {0} points: \n{1}\n".format(len(self.points_list), self.points_list))

    def get_position_list(self):
        return [[0 for i in range(self.x)] for j in range(self.y)]

    def save_ppm(self, file_name):
        with open(file_name, "w") as file:
            file.write("P1\n")
            file.write("{0} {1}\n".format(self.x, self.y))
        PPM(self.points_list, self.get_position_list()).save(file_name)


class Point:
    """This class is responsible for creating point information"""

    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

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


class PPM:

    def __init__(self, points_list, position_list):
        self.position_list = position_list

        for my_point in points_list:
            self.position_list[my_point.x][my_point.y] = 1

    def save(self, file_name):
        with open(file_name, "a") as file:
            for line in self.position_list:
                for value in line:
                    file.write("%s " % value)
                file.write("\n")


t1 = time.time()
my_box = Box(500, 500)

my_box.add_random_points(0.01)  # percentage
# my_box.save_ppm("image.ppm")
my_box.movement(10, 0.1)
print("Execution time: {0:.2f}s".format(time.time() - t1))
# for one, two in zip(my_box.x_plane, my_box.y_plane):
# print(one, two)
