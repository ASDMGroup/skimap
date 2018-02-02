#!/usr/bin/env python3

"""Nodes"""

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
