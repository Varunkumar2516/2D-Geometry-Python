## ===================================================
#        DAY 14 - 2D coordinate Geometry :Line Class
#                    Menu driven Practice
#         Creation using class magicfunctions
# ===================================================

#Importing the previous point class
from APointClass3D import Point3D
import math

class Line:
    
    #constructor __init__()
    def __init__(self,point1,point2):
      self.point1=point1
      self.point2=point2
      self.equation=''

      def helper(x,val):
       if val==0:
          return x
       else:
          sign='+' if val>0 else '-'
          return f'{x} {sign} {abs(val)}'
       
      self.dx = self.point2.x - self.point1.x
      self.dy = self.point2.y - self.point1.y
      self.dz = self.point2.z - self.point1.z
      self.equation=f"{helper('x',self.point1.x)}/{self.dx} = {helper('y',self.point1.y)}/{self.dy} = {helper('z',self.point1.z)}/{self.dz}"


    def Direction_ratio(self):
       linescope=self.point1.Direction_ratio(self.point2)
       return linescope

    def linemid(self):
       mid_point=self.point1.Midpoint(self.point2)
       return mid_point
    def Equation(self,other):

       return self.equation

    def __str__(self):
      return self.equation
    
    def check_point(self,point,epsilon=1e-6):
       
            t1 = (point.x - self.point1.x) / self.dx if self.dx != 0 else None
            t2 = (point.y - self.point1.y) / self.dy if self.dy != 0 else None
            t3 = (point.z - self.point1.z) / self.dz if self.dz != 0 else None

            t_values = [t for t in (t1, t2, t3) if t is not None]
            return all(abs(t - t_values[0]) < epsilon for t in t_values)
    #Line checking :: Perpendicular or paralel
    def check_lines(self,other):
       if self.dx*other.dx +self.dy*other.dy +self.dz*other.dz==0:
          return f"Perpendicular lines "
       elif abs(self.dx/other.dx)==abs(self.dy/other.dy)==abs(self.dz/other.dy):
          return f"Parallel Lines"
    

    def angle_lines(self,other):
       dr1=self.point1.Direction_ratio(self.point2)
       dr2=other.point1.Direction_ratio(other.point2)
       dot=dr1.x*dr2.x+dr1.y*dr2.y+dr1.x*dr2.x
       magdr1=math.sqrt(dr1.x**2 +dr1.y**2 +dr1.z**2)
       magdr2=math.sqrt(dr2.x**2 +dr2.y**2 +dr2.z**2)
      
       
       if magdr1 == 0 or magdr2 == 0:
        raise ValueError("Zero length direction vector")
       
       #angles in radians
       cos=dot/(magdr1*magdr2)
       #in radian
       angle=math.acos(cos)

       #in degree
       angleDeg=math.degrees(angle)
       return angleDeg

def main():
    print("=== 3D Line Geometry Menu Program ===\n")

    str1 = input("Enter coordinates of (x1, y1, z1): ")
    a, b, c = map(int, str1.replace(',', ' ').split())
    P1 = Point3D(a, b, c)

    str2 = input("Enter coordinates of (x2, y2, z2): ")
    d, e, f = map(int, str2.replace(',', ' ').split())
    P2 = Point3D(d, e, f)

    line = Line(P1, P2)

    while True:
        print("\nChoose Operation:")
        print("1. Print Line Equation")
        print("2. Get Direction Ratio")
        print("3. Get Midpoint")
        print("4. Check if a Point Lies on Line")
        print("5. Check Two Lines Relation")
        print("6. Find Angle Between Two Lines")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            print("Line Equation:", line)
        elif choice == '2':
            print("Direction Ratio of Line:", line.Direction_ratio())
        elif choice == '3':
            print("Midpoint:", line.linemid())
        elif choice == '4':
            str3 = input("Enter coordinates of test point (x3, y3, z3): ")
            x, y, z = map(int, str3.replace(',', ' ').split())
            test_point = Point3D(x, y, z)
            if line.check_point(test_point):
                print(" Point lies on the line.")
            else:
                print(" Point does NOT lie on the line.")
        elif choice == '5':
            str4 = input("Enter coordinates of 1st point of second line: ")
            x1, y1, z1 = map(int, str4.replace(',', ' ').split())
            str5 = input("Enter coordinates of 2nd point of second line: ")
            x2, y2, z2 = map(int, str5.replace(',', ' ').split())
            line2 = Line(Point3D(x1, y1, z1), Point3D(x2, y2, z2))
            print("Relation:", line.check_lines(line2))
        elif choice == '6':
            str4 = input("Enter coordinates of 1st point of second line: ")
            x1, y1, z1 = map(int, str4.replace(',', ' ').split())
            str5 = input("Enter coordinates of 2nd point of second line: ")
            x2, y2, z2 = map(int, str5.replace(',', ' ').split())
            line2 = Line(Point3D(x1, y1, z1), Point3D(x2, y2, z2))
            angle = line.angle_lines(line2)
            print(f"Angle between lines: {angle:.2f} degrees")
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
