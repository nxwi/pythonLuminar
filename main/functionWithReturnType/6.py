# Solve quadratic equation using funtion with multiple return

def quad(a, b, c):
    x1 = (-b - (b**2 - 4 * a * c) ** 0.5) / 2 * a
    x2 = (-b + (b**2 - 4 * a * c) ** 0.5) / 2 * a
    return '%d %d' % (x1, x2)


x = int(input("Enter x:"))
y = int(input("Enter y:"))
z = int(input("Enter z:"))

print(quad(x, y, z))
