
def triangle_area(vertices):                                            # Lager en formel med navn triangle_area med variabel
    return (1/2)*abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)     # formelen

v1 =[0,0]
v2 =[1,0]
v3 =[0,2]

x1 = v1[0]  # gir x1 en verdi fra v1 list
y1 = v1[1]  # Repeter som over men andre lister etterhert
x2 = v2[0]
y2 = v2[1]
x3 = v3[0]
y3 = v3[1]

vertices = [v1, v2, v3]  # lager en nested list

triangle_area(vertices) #setter in vertics / den nestede lista i formelen 
print(triangle_area(vertices))

def test_triangle_area():
    """
    Verify the area of a triangle with vertices
    (0,0), (1,0), and (0,2).
    """
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg

"""
Terminal> py.exe triangle_area.py











