class Shapes:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def shape_method_1(self):
        print(f"Shape: shape_method_1 call and Variable 1 = {self.var1}")

    def shape_method_2(self):
        print(f"Shape: shape_method_2 call and Variable 2 = {self.var2}")


class Triangle(Shapes):
    def __init__(self, var3, var1, var2):
        self.var3 = var3
        Shapes.__init__(self, var1, var2)

    def shape_method_1(self):
        print(f"Shape: Overridden shape_method_1 method call in Triangle and Variable 1 = {self.var1}")

    def triangle_method_1(self):
        print(f"Triangle: triangle_method_1 call and Variable 1 = {self.var3}")


class ChildTriangle(Triangle):
    def __init__(self, var4, var3, var1, var2):
        self.var4 = var4
        Triangle.__init__(self, var3, var1, var2)

    def triangle_method_1(self):
        print(f"Triangle: Overridden triangle_method_1 call in ChildTriangle and Variable 1 = {self.var3}")

    def child_triangle_1(self):
        print(f"ChildTriangle: child_triangle_1 method call and Variable 1 = {self.var4}")


class Quadrilateral(Shapes):
    def __init__(self, var5, var1, var2):
        self.var5 = var5
        Shapes.__init__(self, var1, var2)

    def shape_method_2(self):
        print(f"Shape: Overridden shape_method_2 method call in Quadrilateral and Variable 1 = {self.var2}")

    def quadrilateral_method_1(self):
        print(f"Quadrilateral: quadrilateral_method_1 call and Variable 1 = {self.var5}")


class ChildQuadrilateral(Quadrilateral):
    def __init__(self, var6, var5, var1, var2):
        self.var6 = var6
        Quadrilateral.__init__(self, var5, var1, var2)

    def quadrilateral_method_1(self):
        print(
            f"Quadrilateral: Overridden quadrilateral_method_1 call in QuadrilateralChild and Variable 1 = {self.var5}")

    def child_quadrilateral_1(self):
        print(f"ChildQuadrilateral: child_quadrilateral_1 method call and Variable 1 = {self.var6}")


shape_var_1 = 10
shape_var_2 = 15
triangle_var_1 = 30
child_triangle_var_1 = 130
quadrilateral_var_1 = 67
child_quadrilateral_var_1 = 90

# Create object of shape class
shapes = Shapes(shape_var_1, shape_var_2)

# create object of Triangle and ChildTriangle class
triangle = Triangle(triangle_var_1, shape_var_1, shape_var_2)
child_triangle = ChildTriangle(child_triangle_var_1, triangle_var_1, shape_var_1, shape_var_2)

# Create object of Quadrilateral and ChildQuadrilateral Class
quadrilateral = Quadrilateral(quadrilateral_var_1, shape_var_1, shape_var_2)
child_quadrilateral = ChildQuadrilateral(child_quadrilateral_var_1, quadrilateral_var_1, shape_var_1, shape_var_2)

# Now Calling

# Shapes Method Call (Parent class)
shapes.shape_method_1()
shapes.shape_method_2()
print("\n")

# Triangle's Method Call (Child of Shapes Class) 
triangle.shape_method_1()
triangle.triangle_method_1()
print("\n")

# ChildTriangle's Method Call (Child of Triangle Class)
child_triangle.triangle_method_1()
child_triangle.child_triangle_1()
print("\n")

# Quadrilateral's Method Call (Child of Shapes Class)
quadrilateral.shape_method_2()
quadrilateral.quadrilateral_method_1()
print("\n")

# ChildTriangle's Method Call (Child of Triangle Class)
child_quadrilateral.quadrilateral_method_1()
child_quadrilateral.child_quadrilateral_1()
