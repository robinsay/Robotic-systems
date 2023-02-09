def backward(self,speed):
        current_angle = self.dir_current_angle
        if current_angle != 0:
            abs_current_angle = abs(current_angle)
            # if abs_current_angle >= 0:
            if abs_current_angle > 40:
                abs_current_angle = 40
            power_scale = (100 - abs_current_angle) / 100.0 
            # print("power_scale:",power_scale)
            if (current_angle / abs_current_angle) > 0:
                self.set_motor_speed(1, -1*speed)
                self.set_motor_speed(2, speed * power_scale)
            else:
                self.set_motor_speed(1, -1*speed * power_scale)
                self.set_motor_speed(2, speed )
        else:
            self.set_motor_speed(1, -1*speed)
            self.set_motor_speed(2, speed)  
def forward(self,speed):
    current_angle = self.dir_current_angle
    if current_angle != 0:
        abs_current_angle = abs(current_angle)
            # if abs_current_angle >= 0:
        if abs_current_angle > 40:
            abs_current_angle = 40
            power_scale = (100 - abs_current_angle) / 100.0
            # print("power_scale:",power_scale)
            if (current_angle / abs_current_angle) > 0:
                self.set_motor_speed(1, 1*speed * power_scale)
                self.set_motor_speed(2, -speed) 
                # print("current_speed: %s %s"%(1*speed * power_scale, -speed))
            else:
                self.set_motor_speed(1, speed)
                self.set_motor_speed(2, -1*speed * power_scale)
                # print("current_speed: %s %s"%(speed, -1*speed * power_scale))
        else:
            self.set_motor_speed(1, speed)
            self.set_motor_speed(2, -1*speed)

def parallel_park_right (self, speed = 50,):
        current_dir = -1
        angle = 45
        #turn 45 degress 
        # start and stop into place 
        self.drive(-speed, angle)
        time.sleep(0.5)
        self.stop()
        self.drive(-speed, -angle)
        time.sleep(0.5)
        self.stop()
        self.drive(speed, 10)
        time.sleep(0.25)
        self.stop()
        self.drive(speed, 0)
        time.sleep(0.5)
        self.stop()

def parallel_park_left (self, speed = 50,):
        current_dir = 1
        angle = 45
        #turn 45 degress 
        # start and stop into place 
        self.drive(-speed, angle)
        time.sleep(0.5)
        self.stop()
        self.drive(-speed, -angle)
        time.sleep(0.5)
        self.stop()
        self.drive(speed, 10)
        time.sleep(0.25)
        self.stop()
        self.drive(speed, 0)
        time.sleep(0.5)
        self.stop()