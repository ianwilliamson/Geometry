'''
support for geometric computation

'''

try:
    __import__('pkg_resources').declare_namespace(__name__)
except:
    from pkgutil import extend_path
    __path__ = extend_path(__path__,__name__)

from .point import Point
from .circle import Circle
from .ellipse import Ellipse
from .line import Line
from .triangle import Triangle
from .rectangle import Rectangle
from .graph import Node, Edge, Graph
from .constants import *
from .exceptions import *
#
#__all__ =  [ 'Point',
#             'Line','Segment','Ray',
#             'Triangle','Rectangle',
#             'Graph','Node','Edge' ]



