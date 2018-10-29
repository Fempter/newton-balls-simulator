import numpy as np
import random


class Box:
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step
        self.x_plane = np.round(np.arange(0, x + step, step), 1)
        self.y_plane = np.round(np.arange(0, y + step, step), 1)
        self.points = list()

    def add_point(self, x, y, velocity_x, velocity_y, diameter):
        if x not in self.x_plane:
            raise ValueError("Parametr X kulki nie zgadza się z zakresem płaszczyzny X")
        elif y not in self.y_plane:
            raise ValueError("Parametr Y kulki nie zgadza się z zakresem płaszczyzny Y")
        elif diameter <= 0:
            raise ValueError("Średnica musi być większa od 0")
        else:
            self.points.append(Point(x, y, velocity_x, velocity_y, diameter))

    def add_random_points(self, n):
        for n in range(n):
            x = np.round(random.choice(np.arange(0, self.x + self.step, self.step)), 1)
            y = np.round(random.choice(np.arange(0, self.y + self.step, self.step)), 1)
            velocity_x = round(random.uniform(0, 10), 2)
            velocity_y = round(random.uniform(0, 10), 2)
            while True:
                diameter = round(random.uniform(0, 1.), 2)
                if diameter > 0:
                    break
            self.add_point(x, y, velocity_x, velocity_y, diameter)

        # siatka co 0.5 i losowanie co 0.5 - OGARNĄĆ!!!!!!!!

    def show_points(self):
        print("\nList contains {0} points: \n{1}".format(len(self.points), self.points))


class Point:
    def __init__(self, x, y, velocity_x, velocity_y, diameter):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.diameter = diameter

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
        print("Współrzędne [x,y]: %d, %d" % (self.x, self.y))
        print("Prędkość: %0.2f" % self.velocity())

    def __repr__(self):
        return u"Point(%s, %s)" % (self.x, self.y)


'''
b1 = Ball(x=0,y=0,velocity_x=2,velocity_y=3)
b1.save_move(300, 5)
print()
b1.show()
b1.box
'''

my_box = Box(100000, 100000, step=0.2)

my_box.add_random_points(10)
my_box.show_points()

# for one, two in zip(my_box.x_plane, my_box.y_plane):
# print(one, two)
