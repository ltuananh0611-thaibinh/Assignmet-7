def accelerate(self, change_of_speed):
    self.current_speed += change_of_speed

    if self.current_speed > self.max_speed:
        self.current_speed = self.max_speed

    if self.current_speed < 0:
        self.current_speed = 0
