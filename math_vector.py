import math
def transform_o1_to_o(z1, angle, o1):
    x = z1[0]*math.cos(angle) - z1[1]*math.sin(angle) + o1[0]
    y = z1[1]*math.cos(angle) + z1[0]*math.sin(angle) + o1[1]
    z = (x, y)
    return z
	
def transform1_o_to_o1(z, angle, o1):
    x1 = (z[0] - o1[0])*math.cos(angle) + (z[1] - o1[1])*math.sin(angle)
    y1 = (z[1] - o1[1])*math.cos(angle) - (z[0] - o1[0])*math.sin(angle)
    z1 = (x1, y1)
    return z1

def transform_v_o1_to_o(z1, angle, o1):
    x = z1[0]*math.cos(angle) - z1[1]*math.sin(angle)
    y = z1[1]*math.cos(angle) + z1[0]*math.sin(angle)
    z = (x, y)
    return z
	
def transform1_v_o_to_o1(z, angle, o1):
    x1 = (z[0])*math.cos(angle) + (z[1])*math.sin(angle)
    y1 = (z[1])*math.cos(angle) - (z[0])*math.sin(angle)
    z1 = (x1, y1)
    return z1

def e(z):
    z_mod = vector_length(z)
    return(z[0] / z_mod + 1e-8, z[1] / z_mod + 1e-8)    

def transform(o, angle, length):
    angle = math.pi - angle + 1e-8
    r = length / 2.0
    if angle == math.pi / 2:
        return((o[0], o[1] + r), (o[0], o[1] - r))
    else:
        k = math.tan(angle)
        down = math.sqrt(k * k + 1)
        return((int(o[0] + r / down + 1e-8), int(o[1] + k * r / down + 1e-8)), \
               (int(o[0] - r / down + 1e-8), int(o[1] - k * r / down + 1e-8)))
	
def qiedian(c, a, b):
    m = a[0] - b[0]
    n = a[1] - b[1]
    t = a[0] * b[1] - a[1] * b[0]
    l = - (m * c[0] + n * c[1])
    down = m * m + n * n
    upx = -(m * l + n * t)
    upy = m * t - n * l
    return (upx / down + 1e-8, upy / down + 1e-8)        

def reflect(v, a, b):
    m = a[0] - b[0]
    n = a[1] - b[1]
    down = m * m + n * n
    upx = (m * m - n * n) * v[0] + 2 * m * n * v[1]
    upy = (n * n - m * m) * v[1] + 2 * m * n * v[0]
    return (upx / down + 1e-8, upy / down + 1e-8)    

def vector(a, b, op):
    if op == '+':
        return (a[0] + b[0], a[1] + b[1])
    elif op == '-':
        return (a[0] - b[0], a[1] - b[1])
    elif op == '*':
        return a[0] * b[0] + a[1] * b[1]

def vector_length(z):
    return math.sqrt(z[0] * z[0] + z[1] * z[1]) + 1e-8
    	
def dis(a, b):
    return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])) + 1e-8

def point_line(c, a, b):
    m = a[0] - b[0]
    n = a[1] - b[1]
    t = a[0] * b[1] - a[1] * b[0]
    up = math.fabs(n * c[0] - m * c[1] + t)
    down = math.sqrt(m * m + n * n)
    return up/down


	
	
	
