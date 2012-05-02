function[x, y, theta] = hw8()

x = 0;
y = 0;
theta = 0;
t = 0;
dt = 4;
v = 10;
w = pi/8;
T = 16;

e = T/dt;

for i = 1:e
	x = x + v * dt * cos(theta)
	y = y + v * dt * sin(theta)
	theta = theta + w * dt
end