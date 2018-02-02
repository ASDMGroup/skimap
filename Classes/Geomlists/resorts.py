#!/usr/bin/env python3

"""Resorts"""

#Setup plotting and load useful modules
import matplotlib.pyplot as plt
import matplotlib.pylab
import numpy as np
from .Point2D import Point2D as Point2D


#Create a list class to define properties of list objects containing sets of points
class GeomList(list):
    """A list class which contains Point2D objects."""
    def dataextract(self,filename):
        """This method extracts data from the file specified in the method's argument into the GeomList as a series of Point2D objects.

        Parameters
        ----------
        filname: str
            the name of the file to extract data from

        Examples
        --------
        >>>geomety = GeomList()
        >>>geometry.dataextract(data.txt)
        """

        #Open the file
        filedata = open(filename,'r')
        # Extract data from each line of the file into x and y coordinates of Point2D objects and append to the GeomList
        for line in filedata.readlines():
            coords=line.split()
            self.append(Point2D(float(coords[0]),float(coords[1])))
        #Close the file
        filedata.close()
        #return the list of data from the list
        return filedata

        #Open the file
        filedata = open(filename,'r')
        # Extract data from each line of the file into x and y coordinates of Point2D objects and append to the GeomList
        for line in filedata.readlines():
            coords=line.split()
            self.append(Circle(float(coords[0]),float(coords[1]),float(radius)))
        #Close the file
        filedata.close()
        #return the list of data from the list
        return filedata

    def __setitem__(self,i,geometry):
        """This method asserts that only Point2D() objects can be put into a GeomList.
        """
        assert isinstance(point, Point2D)
        super().__setitem__(i,geometry)

    def append(self,point):
        """This method appends a new object to the Geomlist. It will only append Point2D objects to the list.

        Parameters
        ----------
        point : Point2D
            This is the Point2D object that will be appended to the list

        Example
        -------
        >>>examplegeomlist.append([Point2D])
        """
        assert isinstance(point,Point2D)
        super().append(point)

    def __repr__(self):
        """The __repr__ method defines what is returned by 'print([GeomList])

        Example
        -------
        >>>print(examplegeomlist)
        1, 2
        3, 2
        4, 6
        """
        for i in self:
            i.__repr__

    def plotsetup(self,title,other):
        fig, ax = plt.subplots()
        plt.title(title)
        plt.axis(self.minmax(other))

    def plot(self, colour):
        """Plots the points in the GeomList

        Parameters
        ----------
        col:
            the colour to plot points in your GeomList

        """
        #Creating a subplot
        for i in self:
            #print(colour)
            i.plot(colour)

    def minmax(self,other):
        """Returns the minimum and maximum extents of points self and another Geomlist defined by 'other'.
        Information is returned in the format ([x_minumum], [x_maximum],[y_minimum],[y_maximum]).
        If the point (0,0) is greater than the (x,y) maxima, or less than the (x,y) minima.

        Parameters
        ----------
        other: GeomList
            the name of the file to extract data from

        """
        xs = list()
        ys = list()
        for i in self:
            xs.append(i.x)
            ys.append(i.y)
        for i in other:
            xs.append(i.x)
            ys.append(i.y)
        return min((min(xs)*1.25),0),max((max(xs)*1.25),0),min((min(ys)*1.25),0),max((max(ys)*1.25),0)

    def translateplot(self,dx,dy,col):
        """Translates the points in your geomlist by (dx,dy) where dx is the change in the x coordinate and dy is the change in the y coordinate.

        Parameters
        ----------
        dx : float
            the change in the x coordinate
        dy : float
            the change in the y coordinate.

        Examples
        --------
        >>>point1,point2 = Point2D(1,1),Point2D(5,3)
        >>>geometry = GeomList()
        >>>geometry.append(point1)
        >>>geometry.append(point2)
        >>>print (geometry)
        1, 1
        5, 3
        >>>geometry.translate(1,-1)
        >>>print (geometry)
        2, 0
        6, 2
        """
        for i in self:
            i.translate(dx,dy)
        self.plot(col)


    """def poly(self,degree,col,label):
        """Finds the polynomial line of best fit for your GeomList and plots it in colour 'col'.

        Parameters
        ----------
        col : str
            the colour that your polynomial will be plotted
        """
        xs = list()
        ys = list()
        for i in self:
            xs.append(i.x)
            ys.append(i.y)
        z = np.polyfit(xs, ys, deg=degree, rcond=None, full=False, w=None, cov=False)
        p = np.poly1d(z)
        plt.plot(xs, p(xs),'--', linewidth=2, color=col, label=label)"""
