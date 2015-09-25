from vecutil import *
from plotting import *
_browser = None

def getitem(l,d):
    return l.lines[d]

def setitem(l,d,val):
    l.lines[d] = val

class Graph:
	"""docstring for Foo"""
	def __init__(self):
		self.lines = {}
		self.points = {}

	__getitem__ = getitem

	__setitem__ = setitem

	def add_point(self, pt, name,color=None):
		self.points[name] = {'pt':pt, 'color':color}

	def add_line(self, l, name, color=None):
		""" add a line to the lines
		    input: l is a list of two tuples or lists ---> [(1,3), (6,2)] or [[1,3], [6,2]
		"""
		if len(l) == 2:
			self.lines[name] = {'line':l, 'color':color}
		else:
			raise ValueError

	def show(self, browser=None):
	    scalar = 200./10
	    # origin = (210, 210)
	    dot_size = 3
	    origin = 210
	    hpath = create_temp('.html')
	    with open(hpath, 'w') as h:
	        h.writelines(
	            ['<!DOCTYPE html>\n'
	            ,'<head>\n'
	            ,'<title>plot</title>\n'
	            ,'</head>\n'
	            ,'<body>\n'
	            ,'<svg height="420" width=420 xmlns="http://www.w3.org/2000/svg">\n'
	            ,'<line x1="0" y1="210" x2="420" y2="210"'
	            ,'style="stroke:rgb(0,0,0);stroke-width:2"/>\n'
	            ,'<line x1="210" y1="0" x2="210" y2="420"'
	            ,'style="stroke:rgb(0,0,0);stroke-width:2"/>\n'])
	        for line in self.lines:
	            l = self.lines[line]
	            x1, y1 = vec2list(l['line'][0])
	            x2, y2 = vec2list(l['line'][1])
	            h.writelines(['<line x1="%d" y1="%d" x2="%d" y2="%d" style="stroke:%s;stroke-width:2"/>\n'
	                          % (origin+x1*scalar,origin-y1*scalar,origin+x2*scalar,origin-y2*scalar,l['color'])])
	        for pts in self.points:
	            pt = self.points[pts]
	            x,y = vec2list(pt['pt'])
	            h.writelines(['<circle cx="%d" cy="%d" r="%d" fill="%s"/>\n'
	                        % (origin+scalar*x,origin-scalar*y,dot_size,pt['color'])])
	        h.writelines(['</svg>\n</body>\n</html>'])
	    if browser is None:
	        browser = _browser
	    webbrowser.get(browser).open('file://%s' % hpath)




	
# class Lines:
# 	def __init__(self):
# 		self.lines = {}

# 	__getitem__ = getitem

# 	__setitem__ = setitem

# 	def __iter__(self):
# 		return self.lines.__iter__()

# 	def add_line(self, l, name):
# 		""" add a line to the lines
# 		    input: l is a list of two tuples or lists ---> [(1,3), (6,2)] or [[1,3], [6,2]
# 		"""
# 		if len(l) == 2:
# 			self.lines[name] = l
# 		else:
# 			raise ValueError

