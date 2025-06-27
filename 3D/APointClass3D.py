## ===================================================
#         3D coordinate Geometry :Point Class
#                    Menu driven Practice
#         Creation using class magicfunctions
# ===================================================

import math

class Point3D:
#1
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
#2
    def distance(self,other):
     return math.sqrt((other.x-self.x)**2 +(other.y-self.y)**2 + (other.z-self.z)**2)
    def zerodistance(self):
       return math.sqrt(self.x**2+self.y**2+self.z**2)
 #3   
    def Direction_ratio(self,other):
       
       self.dr=Point3D((other.x-self.x),(other.y-self.y),(other.z-self.z))
       return self.dr
#4
    def Midpoint(self,other):
       Midpoint=Point3D((self.x+other.x)/2,(self.y+other.y)/2,(self.z+other.z)/2)
       return Midpoint
#5
    def __str__(self):
       return f"({self.x},{self.y},{self.z})"
#6    
    def checkCollinear(self,other,other2):
       return self.distance(other2)==self.distance(other)+other.distance(other2)
 #7   
    def __eq__(self,other):
       return self.x==other.x and self.y==other.y and self.z==other.z
    

def wait():
   input("\nPress Enter To Continue :")
def main():
    print("\n 3D Coordinate Geometry Menu")
    str1=input("Enter cordinates of (x1,y1,z1)= :")
    a,b,c=map(int,str1.strip().split(",") if ',' in str1 else str1.strip().split() )
    P1=Point3D(a,b,c)
    str2=input("Enter cordinates of (x2,y2,z2)= :")
    c,d,e=map(int,str2.strip().split(",") if ',' in str2 else str2.strip().split() )
    P2=Point3D(c,d,e)
    while True:
     print("1. Show both points")
     print("2. Distance between points")
     print("3. Midpoint")
     print("4. Direction Ratios")
     print("5. Are the points equal?")
     print("6. Distance From Origin to Point")
     print("7. Check Three points are Collinear")
     print("8. Exit")
     user=input("Enter the Input")
     if user=='1':
        print("\n\tFirst Point    :(x,y)",P1)
        print("\tSecond  Point  :(x,y)",P2)
        wait()
     elif user=='2':
        dist=P1.distance(P2)
        print("\n\tDistance Between Two Points :",round(dist,2)," Units")
        wait()
     elif user=='3':
        midpoint=P1.Midpoint(P2)
        print("\n\tMid-Point Between Two Points :",midpoint)
        wait()
     elif user=='4':
        slope=P1.Direction_ratio(P2)
        print("\n\tDIRECTION RATIO Of Two points ",slope)

        print(slope)
        print(type(slope))
        wait()
     elif user=='5':
        print("\n\tIs Both Points Are Equal?  :",P1==P2)
        wait()
     elif user=='6':
        distzero1=P1.zerodistance()
        distzero2=P2.zerodistance()
        
        #round(variable,points) =>>  #round(variable,2)
        #round is used to give the numeric results from 1.2234132 => 1.22 only 
        print("\n\tDistance From Zero To First Point ",round(distzero1,2)," Units")
        print("\tDistance From Zero To Second Point ",round(distzero2,2)," Units")
        wait()
        
     elif user=='7':
        str2=input("Enter THird Point cordinates of (x3,y3,z3)= :")
        f,g,h=map(int,str2.strip().split(",") if ',' in str2 else str2.strip().split() )
        P3=Point3D(f,g,h)
        if P1.checkCollinear(P2,P3):
           print("THree Points Are Collinear")
           wait()
     elif user=='8':
        print("THank You")
        break
     else:
        print("Invalid Option! Try Again")


#when we use it as Module And Import it in another file
#__name__ becomes "That script name"
#so the main() function not runs only the class (Point) can be used in that file
if __name__=="__main__":
   main()
      
    


 
       

       