#!/usr/bin/env python3

"""Point2D"""

#Setup plotting and load useful modules
import matplotlib.pyplot as plt
import matplotlib.pylab
import copy
import numpy as np



#Define 2D point class
class Point2D(object):
    """A two dimensional point.

    Parameters
    ----------
    x : float
        the x coordinate
    y : float
        the y coordinate
    """
    #Method to create a Point2D object
    def __init__(self,x,y):
        """A Point2D object requires an x cooordinate and a y coordinate.

        Parameters
        ----------
        x : float
            the x coordinate
        y : float
            the y coordinate.

        Examples
        --------
        >>>pnt = Point2D(1,2)
        """
        #the Point2D's x property should correspond to the x argument in the __init__ function
        self.x = x
        #the Point2D's y property should correspond to the y argument in the __init__ function
        self.y = y

    #define what a print statement returns
    def __repr__(self):
        """The __repr__ method defines what is returned by 'print([Point2D])'.

        Examples
        --------
        >>>print(Point2D(1,2)
        1, 2
        """
        #define how Point2D object are printed
        print (str(self.x)+', '+str(self.y))

    def plot(self, col):
        """The plot method calls matplotlib.pyplot.plot using the coordinates contained in the x and y attributes of your Point2D.
        'colour' defines what colour they are plotted.

        Parameters
        ----------
        colour: str
            the colour that the Point2D should be plotted in.

        Examples
        --------
        >>>point.plot("red")
        """
        #plot the Point2D object using the x and y value of the object
        plt.plot(self.x,self.y,'o', color=str(col))

    def translate(self,dx,dy):
        """Translate your point by dx and dy where dx is the change in the x coordinate and dy is the change in the y coordinate.

        Parameters
        ----------
        dx : float
            the change in the x coordinate
        dy : float
            the change in the y coordinate.

        Examples
        --------
        >>>point = Point2D(1,1)
        >>>point.translate(1,-1)
        >>>print (point)
        2, 0
        """
        #redefine the x and y values of your Point2D as (x + dx) and (y + dy)
        self.x = self.x + dx
        self.y = self.y + dy

    def dilate(self,dilation,Sx,Sy):
        """Dilate your point from the centre (Sx,Sy), by a factor defined by the value of the dilation argument

        Parameters
        ----------
        dilation : float
            the factor of dilation
        dx : float
            the x coordinate of the sourse of dilation
        dy : float
            the y coordinate of the sourse of dilation

        Examples
        --------
        >>>point.dilate(2,0,0)
        """
        #redefine the x and y values of your Point2D using the dilation equation
        self.x = Sx + ((self.x-Sx) * dilation)
        self.y = Sx + ((self.y-Sy) * dilation)
