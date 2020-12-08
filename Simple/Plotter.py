import math

class Plotter:
    def __init__(self, inner_arm, outer_arm):
        self.inner_arm = inner_arm
        self.outer_arm = outer_arm

    def calc_angles(self, x, y):
        hypotenuse = math.sqrt(x**2 + y**2)
        hypotenuse_angle = math.asin(x/hypotenuse)
        inner_angle = math.acos((self.inner_arm**2 + hypotenuse**2 - self.outer_arm**2)/(2*self.inner_arm*hypotenuse))
        shoulder_motor_angle = hypotenuse_angle - inner_angle

        elbow_angle = math.acos((self.inner_arm**2 + self.outer_arm**2 - hypotenuse**2)/ (2*self.inner_arm*self.outer_arm))
        elbow_motor_angle = math.pi - elbow_angle

        return math.degrees(shoulder_motor_angle), math.degrees(elbow_motor_angle)


if __name__ == '__main__':
    p = Plotter(8, 8)
