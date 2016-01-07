#coding=utf8
import math

def vector_length(z):
    return math.sqrt(z[0] * z[0] + z[1] * z[1]) + 1e-8
    
def vector(a, b, op):
    if op == '+':
        return (a[0] + b[0], a[1] + b[1])
    elif op == '-':
        return (a[0] - b[0], a[1] - b[1])
    elif op == '*':
        return a[0] * b[0] + a[1] * b[1]
        
def dis(a, b):
    return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])) + 1e-8

def point_line(c, a, b):
    m = a[0] - b[0]
    n = a[1] - b[1]
    t = a[0] * b[1] - a[1] * b[0]
    up = math.fabs(n * c[0] - m * c[1] + t)
    down = math.sqrt(m * m + n * n)
    return up/down
    
def reflect(v, a, b):
    m = a[0] - b[0]
    n = a[1] - b[1]
    down = m * m + n * n
    upx = (m * m - n * n) * v[0] + 2 * m * n * v[1]
    upy = (n * n - m * m) * v[1] + 2 * m * n * v[0]
    return (upx / down + 1e-8, upy / down + 1e-8)    

def qiedian(c, a, b):
    m = a[0] - b[0]
    n = a[1] - b[1]
    t = a[0] * b[1] - a[1] * b[0]
    l = - (m * c[0] + n * c[1])
    down = m * m + n * n
    upx = -(m * l + n * t)
    upy = m * t - n * l
    return (upx / down + 1e-8, upy / down + 1e-8)        

def perfect(z):
    old = vector_length(z)
    x = [int(z[0]), math.ceil(z[0])]
    y = [int(z[1]), math.ceil(z[1])]
    tmp = []
    cha = []
    for i in x:
        for j in y:
            tmp.append((i, j))
            cha.append(math.fabs(vector_length((i, j)) - old))
            
    for i in range(len(tmp)):
        if cha[i] == min(cha):
            return tmp[i]
            
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
               
def e(z):
    z_mod = vector_length(z)
    return(z[0] / z_mod + 1e-8, z[1] / z_mod + 1e-8)
    
def boom(c, v, r, a, b, rad, ball_id, line_id):
    
    if vector_length(v) > 10:
        v = (6 * e(v)[0], 6 * e(v)[1]) 
    A = vector(a, b, '-')
    B = vector(c, a, '-')
    C = vector(c, b, '-')
    center = ((a[0] + b[0])/2.0, (a[1] + b[1])/2.0)
    if vector(A, B, '*') * vector(A, C, '*') <= 0:
        if point_line(c, a, b) <= r and ball_id != line_id:
            mark = "bian"
            ball_id = line_id
        else:
            mark = "no"
    else:
        if dis(b, c) <= r:
            mark = "b"
            ball_id = line_id
        elif dis(a, c) <= r:
            mark = "a"
            ball_id = line_id
        else:
            mark = "no"
    if mark == "bian":
        q = qiedian(c, a, b)
        n1 = vector(c, q, '-')
        n1_mod = vector_length(n1)
        n = (n1[0] / n1_mod + 1e-8, n1[1] / n1_mod + 1e-8)
        line_r = dis(center, q)
        line_v = line_r * rad + 1e-8
        tmp_v = (line_v * n[0] + 1e-8, line_v * n[1] + 1e-8)
        
        now_v = reflect(v, a, b)
        
        if vector(now_v, tmp_v, '*') < 0:
            tmp_v = (-tmp_v[0], -tmp_v[1])
        new_v = vector(now_v, tmp_v, '+')
        
        if vector_length(new_v) < 8:
            E = e(new_v)
            new_v = (8 * E[0], 8 * E[1])
            
        return (perfect(new_v), ball_id)
    elif mark == "b" or mark == "a":
        return ((-v[0], -v[1]), ball_id)
    else:
        return (v, ball_id)
    
def boom_norotate(c, v, r, a, b):
    A = vector(a, b, '-')
    B = vector(c, a, '-')
    C = vector(c, b, '-')
    if vector(A, B, '*') * vector(A, C, '*') <= 0:
        if point_line(c, a, b) <= r:
            mark = "bian"
        else:
            mark = "no"
    else:
        if dis(b, c) <= r:
            mark = "b"
        elif dis(a, c) <= r:
            mark = "a"
        else:
            mark = "no"
    if mark == "bian":
        return reflect(v, a, b)
    elif mark == "b" or mark == "a":
        return (-v[0], -v[1])
    else:
        return v

	
	
