import math
import matplotlib.pyplot as plt

# Differential equation: dy/dx = 3 * e^(2x) * y
def equation(x, y):
    return 3 * math.exp(2 * x) * y

# Exact solution: y(x) = y_start * exp((3/2) * (e^(2x) - e^(2x_start)))
def exact_solution(x, y_start, x_start):
    return y_start * math.exp((3/2) * (math.exp(2 * x) - math.exp(2 * x_start)))

# Euler Method
def euler_method(x_start, y_start, step_size, steps):
    x_values = [x_start]
    y_values = [y_start]
    x = x_start
    y = y_start

    for _ in range(steps):
        y += step_size * equation(x, y)
        x += step_size
        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values

# Taylor Method (2nd Order)
def taylor_method(x_start, y_start, step_size, steps):
    x_values = [x_start]
    y_values = [y_start]
    x = x_start
    y = y_start

    for _ in range(steps):
        dy_dx = equation(x, y)
        d2y_dx2 = 6 * math.exp(2 * x) * y + 9 * math.exp(4 * x) * y
        y += step_size * dy_dx + (step_size**2 / 2) * d2y_dx2
        x += step_size
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

# Runge-Kutta 6th Order Method
def runge_kutta_6(x_start, y_start, step_size, steps):
    x_values = [x_start]
    y_values = [y_start]
    x = x_start
    y = y_start

    for _ in range(steps):
        k1 = equation(x, y)
        k2 = equation(x + step_size/4, y + step_size*k1/4)
        k3 = equation(x + step_size/4, y + step_size*(k1 + k2)/8)
        k4 = equation(x + step_size/2, y + step_size*(-k2 + 2*k3)/2)
        k5 = equation(x + 3*step_size/4, y + step_size*(3*k1 + 9*k4)/16)
        k6 = equation(x + step_size, y + step_size*(-3*k1 + 2*k2 + 12*k3 - 12*k4 + 8*k5)/7)
        y += step_size * (7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6) / 90
        x += step_size
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

# Parameters
x_start = 0
y_start = 0.5
step_size = 0.05
steps = 20

# Compute solutions
x_values, y_euler = euler_method(x_start, y_start, step_size, steps)
_, y_taylor = taylor_method(x_start, y_start, step_size, steps)
_, y_rk6 = runge_kutta_6(x_start, y_start, step_size, steps)
y_exact = [exact_solution(x, y_start, x_start) for x in x_values]

# Print header
print(f"{'x':>6} | {'Euler':>10} | {'Taylor':>10} | {'RK6':>10} | {'Exact':>10}")
print("-" * 60)

# Print values
for i in range(len(x_values)):
    print(f"{x_values[i]:6.2f} | {y_euler[i]:10.6f} | {y_taylor[i]:10.6f} | {y_rk6[i]:10.6f} | {y_exact[i]:10.6f}")
print()

#Print Euler table
    # Print header
print("Table 1: Euler Method")
print(f"{'x':>6} | {'Euler':>10}")
print("-" * 60)

    # Print values
for i in range(len(x_values)):
    print(f"{x_values[i]:6.2f} | {y_euler[i]:10.6f} ")
print()

#Print Taylor table
# Print header
print("Table 2: Taylor Method(2nd Order)")
print()
print(f"{'x':>6}{'Taylor':>10}")
print("-" * 60)

# Print values
for i in range(len(x_values)):
    print(f"{x_values[i]:6.2f} |{y_taylor[i]:10.6f}")
print()

#Print RK6 table
# Print header
print("Table 3: Runge- Kutta Method (6th order)")
print(f"{'x':>6}| {'RK6':>10} ")
print("-" * 60)

# Print values
for i in range(len(x_values)):
    print(f"{x_values[i]:6.2f}| {y_rk6[i]:10.6f}")
print()

# Plot 1: Euler
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_euler, 'o-', label="Euler Method", color="blue")
plt.plot(x_values, y_exact, '--', label="Exact Solution", color="black")
plt.title("Euler Method vs Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

# Plot 2: Taylor
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_taylor, 'o-', label="Taylor Method", color="green")
plt.plot(x_values, y_exact, '--', label="Exact Solution", color="black")
plt.title("Taylor Method vs Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

# Plot 3: Runge-Kutta 6
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_rk6, 'o-', label="Runge-Kutta 6th", color="purple")
plt.plot(x_values, y_exact, '--', label="Exact Solution", color="black")
plt.title("Runge-Kutta 6th Order vs Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

# Plot 4: All Methods vs Exact
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_exact, '-', label="Exact Solution", color="black", linewidth=2)
plt.plot(x_values, y_euler, 'o--', label="Euler", color="blue")
plt.plot(x_values, y_taylor, 's--', label="Taylor", color="green")
plt.plot(x_values, y_rk6, 'd--', label="Runge-Kutta 6", color="purple")
plt.title("Comparison of All Methods with Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
