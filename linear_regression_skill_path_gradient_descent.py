

def get_gradient_at_b(x,y,m,b):
    diff = 0
    N = len(x)
    for i in range(N):
        y_val = y[i]
        x_val = x[i]
        diff += (y_val - (m*x_val+b))
    b_gradient =  -2/N * diff
    return b_gradient

def get_gradient_at_m(x,y,m,b):
    diff = 0
    N = len(x)
    for i in range(N):
        y_val = y[i]
        x_val = x[i]
        diff += x_val * (y_val - (m * x_val + b))
    m_gradient = -2/N * diff
    return m_gradient

def step_gradient(x, y, b_current, m_current):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current -(0.01 * b_gradient)
    m = m_current -(0.01 * m_gradient)
    return [b , m]

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# current intercept guess:
b = 0
# current slope guess:
m = 0

# Call your function here to update b and m

print(get_gradient_at_b([1, 2], [1, 2], 1, 1))
print(get_gradient_at_m([1, 2], [1, 2], 1, 1))

b, m = step_gradient(months, revenue, b , m)
print(b, m)
print(step_gradient(x = months, y = revenue , b_current = b, m_current = m ))
b, m = step_gradient(months, revenue, b , m)
print(b, m)
print(step_gradient(x = months, y = revenue , b_current = b, m_current = m ))
b, m = step_gradient(months, revenue, b , m)
print(b, m)
print(step_gradient(x = months, y = revenue , b_current = b, m_current = m ))