import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа

number_of_points = 10000
x_random = np.random.uniform(a, b, number_of_points)
f_values = f(x_random)
integral_monte_carlo = (b - a) * np.mean(f_values)
print(f"Estimated Integral: {integral_monte_carlo}")


x = sp.Symbol("x")
f_sympy = x**2
integral_exact = sp.integrate(f_sympy, (x, 0, 2))
print(f"Exact Integral: {integral_exact.evalf()}")


# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Налаштування графіка
ax.set_xlim((x[0], x[-1]))
ax.set_ylim(0, max(y) + 0.1)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title(f"Графік інтегрування f(x) = x^2 від {a} до {b}")
plt.grid()
plt.show()
