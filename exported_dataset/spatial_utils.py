"""
Spatial utilities
"""

from scipy.spatial import ConvexHull, convex_hull_plot_2d
import math

def dist_to_line(x1, y1, x2, y2, px, py) -> float:
    """Find shortest distance of a point to a line segment
    
    (px, py) are the coords of the point to compare to the line given by (x1, y1), (x2, y2).
    
    Reference: from http://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment
    
    For GIS, this cheats by using Euclidean 2D distance rather than a geodesic, but we should be close enough at the scale
    of a state to identify which convex hull line to use. Then we can measure more precisely.
    """
    dx = x2 - x1
    dy = y2 - y1
    u =  ((px - x1) * dx + (py - y1) * dy) / (dx*dx + dy*dy)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    return (x1 + u * dx, y1 + u * dy)

def sq_dist(x1, y1, x2, y2) -> float:
    """Utility to return the squared distance between point (x1, y1) and (x2, y2).
    """
    dx = x1 - x2
    dy = y1 - y2
    return dx*dx + dy*dy