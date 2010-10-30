# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius
class Triangle(Shape):
    def __init__(self,b,h):
        """
        h: length of side of the square
        """
        self.h = float(h)
	self.b=float(b)
    def area(self):
        """
        Returns area of the square
        """
        return 0.5*self.b*self.h 
    def __str__(self):
        return 'Triangle with side ' + str(self.b) + str(self.h)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Triangle and self.b == other.b and self.h==other.h

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
	self.i=0
	self.list=[]
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO D
	def fn(x):
                return x[0]
	if isinstance(sh,Circle):


		for x,y,z in self.list:
			if x=='C' and y==sh.radius:
				break
		else:
			self.list.append(('C',sh.radius,0))


	elif isinstance(sh,Square):

		for x,y,z in self.list:
			if x=='S' and y==sh.side:
				break
		else:

			self.list.append(('S',sh.side,0))



	elif isinstance(sh,Triangle):
		for x,y,z in self.list:
			if x=='T' and y==sh.b and z==sh.h:
				break
		else:	 
			self.list.append(('T',sh.b,sh.h))


	self.list=sorted(self.list,key=fn)

		
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        self.i=len(self.list)

	return(self)
		
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO



	return(str(self.list))		
    def next(self):
	self.i=self.i-1	

	if self.i>=0:
		return self.list[-self.i-1]
	else:
		raise StopIteration


        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO

    max=0 	
  
    for a in shapes:
    	if a[0]=='C':
		print a[0]
		a1=3.14*a[1]**2


		
	elif a[0]=='S':
		a1=a[1]**2



	else: 
		a1=0.5*a[1]*a[2]
	if max<a1:
		max=a1
		c=a

    print 'shape with largest area is ',c
		
	

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    f=open(filename)
    s=ShapeSet()
    for l in f:
	h=l.split(',')
	h[1]=h[1].strip()
	if l[0]=='c':
		s.addShape(Circle(float(h[1])))
	elif l[0]=='s':
		s.addShape(Square(float(h[1])))
	else:
		h[2]=h[2].strip()
		s.addShape(Triangle(float(h[1]),float(h[2])))
    print s
	
