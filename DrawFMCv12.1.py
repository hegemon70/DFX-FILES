
import os,string,math,sys


try:
    import dxfwrite
except ImportError:
    # if dxfwrite is not 'installed' append parent dir of __file__ to sys.path
    curdir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.abspath(os.path.join(curdir, os.path.pardir)))
    
from dxfwrite import DXFEngine as dxf
from dxfwrite.const import CENTER, RIGHT, ALIGNED, FIT, BASELINE_MIDDLE
from dxfwrite.const import TOP, MIDDLE, BOTTOM

radArcMin=1
colorLine= 0#0:black 1:red 2:yellow 7:white
colorText=1
shiftTopLineText= 2.5 
sizeText=radArcMin * 5
currentLayer='layer1'
space=radArcMin * 2
#------------------------------------------
centroX=148.5
centroY=105
shiftLetras=5.771
GradosAño=12
GradosMes=1
colorLine2=1
colorLine3=3
#------------------------------------------
def dameCuadrante(ang):
	numCuadrante=1
	if ang <= 90:
		numCuadrante=1
	elif ang > 90 and ang <= 180:
		numCuadrante=2
	elif ang > 180 and ang <=270:
		numCuadrante=3
	else:
		numCuadrante=4
	return numCuadrante

def traduceElAnguloRelojATrigonometria(angO):
#pre: el angulo que esta en ang0 se basa  en las 12 del reloj
#post: se devuelve el valor de un angulo correspondiente los angulos matematicos partiendo del eje x y hacia la izquierda
#360 + 90=450 
	angD=450 - angO
	if angD > 360:
		angD = angD -360
	if angD < 0:
		angD=360 + angD
	return angD

def muestraTriangulo(draw,xCenter,yCenter,ang,radio,colorL):
#pre: x e y del cetro del arco
#una angulo en grados y un radio
#post: devuelve el otro punto extremo de la hipotenusa
	print ("desde muestra triangulo")
	print ("el anguloOrigen es:",ang) 
	ang=traduceElAnguloRelojATrigonometria(ang)
	print ("el anguloReal es:",ang) 
	cuad=dameCuadrante(ang)
	print ("este es el coseno de ang",math.cos(math.radians(ang)))
	print ("este es el seno de ang",math.sin(math.radians(ang)))

	if cuad==1:
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter + a
		yd=yCenter + b
		print ("esto es el tamaño del lado adyacente:",a)
		print ("esto es el tamaño del lado opuesto:",b)
		drawLineColoured(draw, xCenter, yCenter, xd, yCenter, colorL)
		drawLineColoured(draw, xd, yCenter, xd, yd, colorL)
	elif cuad==2:
		ang=180-ang#complementario
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter - a
		yd=yCenter + b
		print ("esto es el tamaño del lado adyacente:",a)
		print ("esto es el tamaño del lado opuesto:",b)
		drawLineColoured(draw, xCenter, yCenter, xd, yCenter, colorL)
		drawLineColoured(draw, xd, yCenter, xd, yd, colorL)
	elif cuad==3:
		ang=ang-180
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter - a
		yd=yCenter - b
		print ("esto es el tamaño del lado adyacente:",a)
		print ("esto es el tamaño del lado opuesto:",b)
		drawLineColoured(draw, xCenter, yCenter, xd, yCenter, colorL)
		drawLineColoured(draw, xd, yCenter, xd, yd, colorL)
	else:#cuad=4
		ang=360-ang
		print ("este es el angulo de calculo",ang)
		print ("este es el coseno de ang",math.cos(math.radians(ang)))
		print ("este es el seno de ang",math.sin(math.radians(ang)))
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter + a
		yd=yCenter - b
		print ("esto es el tamaño del lado adyacente:",a)
		print ("esto es el tamaño del lado opuesto:",b)
		drawLineColoured(draw, xCenter, yCenter, yd, xCenter, colorL)
		drawLineColoured(draw, yd, xCenter, xd, yd, colorL)
	return xd,yd

def damePtoArcoReloj(xCenter,yCenter,ang,radio):
#pre: x e y del cetro del arco
#una angulo en grados y un radio
#post: devuelve el otro punto extremo de la hipotenusa
	print ("el radio es: ",radio)
	print ("el anguloOriginal es:",ang) 
	ang=traduceElAnguloRelojATrigonometria(ang)
	print ("el anguloReal es:",ang) 
	cuad=dameCuadrante(ang)
	print ("el cuadrante del angulo real es:",cuad)
	print ("este es el coseno de ang",math.cos(math.radians(ang)))
	print ("este es el seno de ang",math.sin(math.radians(ang)))
	a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
	b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
	if cuad==1:
		print ("este es el angulo de calculo",ang)
		print ("este es el coseno de ang",math.cos(math.radians(ang)))
		print ("este es el seno de ang",math.sin(math.radians(ang)))
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter + a
		yd=yCenter + b
	elif cuad==2:
		ang=180-ang#complementario
		print ("este es el angulo de calculo",ang)
		print ("este es el coseno de ang",math.cos(math.radians(ang)))
		print ("este es el seno de ang",math.sin(math.radians(ang)))
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter - a
		yd=yCenter + b
	elif cuad==3:
		ang=ang-180
		print ("este es el angulo de calculo",ang)
		print ("este es el coseno de ang",math.cos(math.radians(ang)))
		print ("este es el seno de ang",math.sin(math.radians(ang)))
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter - a
		yd=yCenter - b
	else:#cuad=4
		ang=360-ang
		print ("este es el angulo de calculo",ang)
		print ("este es el coseno de ang",math.cos(math.radians(ang)))
		print ("este es el seno de ang",math.sin(math.radians(ang)))
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter + a
		yd=yCenter - b
	print ("esto es el tamaño del lado adyacente:",a)
	print ("esto es el tamaño del lado opuesto:",b)
	return xd,yd

def escribeEnArco(draw,texto,centroX,centroY,base,anguloIni,anguloFin,color,tamFte):
	#writeTextNoAling(draw,txt,px0,py0,size,colorTextt,layerTxt,angRotation)
	numLetras=len(texto)
	numGrados=anguloFin-anguloIni
	angIni=traduceElAnguloRelojATrigonometria(anguloIni)
	# if numletras < numGrados:	
	ratio=numGrados/numLetras
	angSig=angIni+ratio
	for i in range(numLetras):
		angSig=angSig+ratio
		px0,py0=damePtoArcoReloj(centroX,centroY,angSig,base)
		writeTextNoAling(draw,texto[i],px0,py0,tamFte,color,currentLayer,angSig)
	#writeTextNoAling(draw,'universidad',px0,py0,12,5,currentLayer,0)
	draw.save()
 
def dibujaArcoRelojColoreado(draw,centroX,centroY,base,anguloIni,anguloFin,colorLine2): 
	angI=traduceElAnguloRelojATrigonometria(anguloIni)
	angF=traduceElAnguloRelojATrigonometria(anguloFin)
	drawArcColoured(draw,centroX,centroY,base,angF,angI,colorLine2)

def dibujaArcoRelojColoreadoGrueso(draw,centroX,centroY,base,anguloIni,anguloFin,colorLine2,grosor):
	angI=traduceElAnguloRelojATrigonometria(anguloIni)
	angF=traduceElAnguloRelojATrigonometria(anguloFin)
	drawArcColouredWithThickness(draw,centroX,centroY,base,angF,angI,colorLine2,grosor)

def drawArcColouredWithThickness(draw, pxCentre, pyCentre, radio, AngIni, AngEnd,colorA,thickness):
	arcx = dxf.arc(radio, (pxCentre,pyCentre), AngIni, AngEnd)
	arcx['color'] = colorA
	arcx['thickness'] = thickness
	draw.add(arcx)
	draw.add_layer(currentLayer, color=colorA)

def drawSolidTriangleFMC(draw, Ax, Ay, Bx, By, Cx, Cy,colorT):
	solid=dxf.solid([(Ax,Ay),(Bx,By),(Cx,Cy)])
	solid['color'] = colorT
	draw.add(solid)
	draw.add_layer(currentLayer, color=colorT)

def drawTriangleColoured(draw, Ax, Ay, Bx, By, Cx, Cy,colorT):
	oldx,oldy=drawLineColoured(draw,Ax,Ay,Bx,By,colorT)
	oldx,oldy=drawLineColoured(draw,Bx,By,Cx,Cy,colorT)
	oldx,oldy=drawLineColoured(draw,Cx,Cy,Ax, Ay,colorT)

def drawArcColoured(draw, pxCentre, pyCentre, radio, AngIni, AngEnd,colorA):
	arcx = dxf.arc(radio, (pxCentre,pyCentre), AngIni, AngEnd)
	arcx['color'] = colorA
	draw.add(arcx)
	draw.add_layer(currentLayer, color=colorA)

def drawCircleColoured(draw,radio,pxCentre,pyCentre,colorA):
	circlex = dxf.circle(radio, (pxCentre,pyCentre))
	circlex['color']=colorA
	draw.add(circlex)


def drawArcColouredAndThickness(draw, pxCentre, pyCentre, radio, AngIni, AngEnd,colorA,thicknes):
	#pre: thicknes float
	arcx = dxf.arc(radio, (pxCentre,pyCentre), AngIni, AngEnd)
	arcx['color'] = colorA
	arcx['thickness']=thicknes
	draw.add(arcx)
	draw.add_layer(currentLayer, color=colorA)

def drawArcFMC(draw, pxCentre, pyCentre, radio, AngIni, AngEnd):
	arcx = dxf.arc(radio, (pxCentre,pyCentre), AngIni, AngEnd)
	arcx['color'] = colorLine
	draw.add(arcx)
	draw.add_layer(currentLayer, color=colorLine)

def drawLineColoured(draw, pxOrig, pyOrig, pxDstn, pyDstn, colorL):
	linex = dxf.line((pxOrig, pyOrig), (pxDstn, pyDstn))
	linex['color'] = colorL
	draw.add(linex)
	draw.add_layer(currentLayer, color=colorL)
	return pxDstn,pyDstn

def drawLineFMC(draw, pxOrig, pyOrig, pxDstn, pyDstn):
	linex = dxf.line((pxOrig, pyOrig), (pxDstn, pyDstn))
	linex['color'] = colorLine
	draw.add(linex)
	draw.add_layer(currentLayer, color=colorLine)
	return pxDstn,pyDstn

def writeTextNoAling(draw,txt,px0,py0,size,colorTextt,layerTxt,angRotation):
	text = dxf.text(txt, (px0,py0), height=size, rotation=angRotation)
	text['layer'] = layerTxt
	text['color'] = colorTextt
	#text['alignpoint']=alignPx,alignPy
	draw.add(text)

def writeTextLeft(draw,txt,px0,py0,size,colorTextt,layerTxt,angRotation):
	text = dxf.text(txt, (px0,py0), height=size, rotation=angRotation)
	text['layer'] = layerTxt
	text['color'] = colorTextt
	#text['alignpoint']=alignPx,alignPy
	draw.add(text)

def writeTextRight(draw,txt,alignpx,alignpy,size,colorTextt,layerTxt,angRotation):
	text=dxf.text(txt, halign=RIGHT, alignpoint=(alignpx,alignpy))
	text['layer'] = layerTxt
	text['color'] = colorTextt
	text['height']= size
	draw.add(text)

def writeText(draw,txt,alignpx,alignpy,size,colorTextt,layerTxt,angRotation):
	text=dxf.text(txt, halign=CENTER, alignpoint=(alignpx,alignpy))
	text['layer'] = layerTxt
	text['color'] = colorTextt
	text['height']= size
	draw.add(text)

def drawCircle(draw, cx, cy ,radius):
#pre: draw=dxf.drawing('filename.dxf'), radius > 0
#post: it draws a circle
#return point top Right of external square (out of the form)
	drawArcFMC(draw, cx, cy, radius,0, 0)
	cx +=radius
	cy +=radius
	return cx,cy

def getDestiny1():
#pre: its used on simple Coord [N,S,E,W]
#Cd1=[N,S,E,W] Cd2=[0,E,W] "like Compass Rose"
#post:return Dx, Dy coord of end point of arc
	if Cd1 == 'N':
		Dy = Oy + radius
		if Cd2 != '0':
			if Cd2 == 'E':#NE
				Dx = Ox + radius
			else:#NW
				Dx = Ox - radius
	else:#S,E,W,SE,SW
		if Cd1 == 'S':#S,SE,SW
			Dy = Oy - radius
			if Cd2 != '0':#SE,SW
				if Cd2 == 'E':#SE
					Dx = Ox + radius
				else:#SW
					Dx = Ox - radius
		else:#E,W
			if Cd1 == E:#E
				Dx = Ox + radius
			else:#W
				Dx = Ox - radius
	return Dx,Dy

def getDestiny(Cd1,Cd2,radius,Ox,Oy):
#pre: Its used on Double Coord [NE,SE,NW,SW]
#Cd1=[N,S,E,W] Cd2=[0,E,W] "like Compass Rose"
#post:return Dx, Dy coord of end point of arc
	if Cd1 == 'N':
		Dy = Oy + radius
		if Cd2 != '0':
			if Cd2 == 'E':#NE
				Dx = Ox + radius
			else:#NW
				Dx = Ox - radius
	else:#S,E,W,SE,SW
		if Cd1 == 'S':#S,SE,SW
			Dy = Oy - radius
			if Cd2 != '0':#SE,SW
				if Cd2 == 'E':#SE
					Dx = Ox + radius
				else:#SW
					Dx = Ox - radius
		else:#E,W
			if Cd1 == E:#E
				Dx = Ox + radius
			else:#W
				Dx = Ox - radius
	return Dx,Dy

def drawarcN(draw, pxOr, pyOr, size, component):
#pre: component [N]	
#pre: component [NNE,NNW] draw=dxf.drawing('filename.dxf')
#post: 
	radio=size
	if component=='NNE':
		shiftX=0.0 - size
		shiftY=0.0
		gradO=270
		gradD=0
	else:#'NNW
		shiftX=0.0 
		shiftY=0.0 - size
		gradO=90
		gradD=180
	pxC=pxOr + shiftX
	pyC=pyOr + shiftY
	drawArcFMC(draw, pxC, pyC, radio, gradO,gradD)
	return getDestiny('S','W',size,pxOr,pyOr)

def drawarcSE(draw, pxOr, pyOr, size, component):
#pre: component [SSE,ESE] draw=dxf.drawing('filename.dxf')
#post: 
	radio=size
	if component=='SSE':
		shiftX=size
		shiftY=0.0
		gradO=180
		gradD=270
	else:#'ESE
		shiftX=0.0 
		shiftY=0.0 - size
		gradO=0
		gradD=90
	pxC=pxOr + shiftX
	pyC=pyOr + shiftY
	drawArcFMC(draw, pxC, pyC, radio, gradO,gradD)
	return getDestiny('S','E',size,pxOr,pyOr)



def drawarcSW(draw, pxOr, pyOr, size, component):
#pre: component [SSW,WSW] draw=dxf.drawing('filename.dxf')
#post: 
	radio=size
	if component=='SSW':
		shiftX=0.0 - size
		shiftY=0.0
		gradO=270
		gradD=0
	else:#'WSW
		shiftX=0.0 
		shiftY=0.0 - size
		gradO=90
		gradD=180
	pxC=pxOr + shiftX
	pyC=pyOr + shiftY
	drawArcFMC(draw, pxC, pyC, radio, gradO,gradD)
	return getDestiny('S','W',size,pxOr,pyOr)

def drawarcNW(draw, pxOr, pyOr, size, component):
#pre: component [NNW,WNW] draw=dxf.drawing('filename.dxf')
#post: 
	radio=size
	if component=='NNW':
		shiftX=0.0 - size
		shiftY=0.0
		gradO=0
		gradD=90
	else:#'WNW
		shiftX=0.0
		shiftY=size 
		gradO=180
		gradD=270
	pxC=pxOr + shiftX
	pyC=pyOr + shiftY
	drawArcFMC(draw, pxC, pyC, radio, gradO,gradD)
	return getDestiny('N','W',size,pxOr,pyOr)

def drawarcNE(draw, pxOr, pyOr, size, component):
#pre: component [NNE,ENE] draw=dxf.drawing('filename.dxf')
#post: 
	radio=size
	if component=='NNE':
		shiftX=size
		shiftY=0.0
		gradO=90
		gradD=180
	else:#'ENE
		shiftX=0.0 
		shiftY=size
		gradO=270
		gradD=0
	pxC=pxOr + shiftX
	pyC=pyOr + shiftY
	drawArcFMC(draw, pxC, pyC, radio, gradO,gradD)
	return getDestiny('N','E',size,pxOr,pyOr)

def drawArcColouredNE(draw, pxOr, pyOr, size, component,colorA):
#pre: component [NNE,ENE] draw=dxf.drawing('filename.dxf') colorA int > 0
#post:
	radio=size
	if component=='NNE':
		shiftX=size
		shiftY=0.0
		gradO=90
		gradD=180
	else:#'ENE
		shiftX=0.0 
		shiftY=size
		gradO=270
		gradD=0
	pxC=pxOr + shiftX
	pyC=pyOr + shiftY
	drawArcColoured(draw, pxC, pyC, radio, gradO,gradD,colorA)
	return getDestiny('N','E',size,pxOr,pyOr)

def drawlineRight(draw, pxOr, pyOr, size):
	shiftX=size
	shiftY=0.0
	pxD=pxOr + shiftX
	pyD=pyOr + shiftY
	return drawLineFMC(draw, pxOr, pyOr, pxD, pyD)

def shiftRight(pxOr, pyOr, size):
	shiftX=size
	shiftY=0.0
	pxD=pxOr + shiftX
	pyD=pyOr + shiftY
	return pxD, pyD

def drawlineLeft(draw, pxOr, pyOr, size):
	shiftX=size
	shiftY=0.0
	pxD=pxOr - shiftX
	pyD=pyOr + shiftY
	return drawLineFMC(draw, pxOr, pyOr, pxD, pyD)

def shiftLeft(pxOr, pyOr, size):
	shiftX=size
	shiftY=0.0
	pxD=pxOr - shiftX
	pyD=pyOr + shiftY
	return pxD, pyD

def drawlineUp(draw, pxOr, pyOr, size):
	shiftX=0.0
	shiftY=size 
	pxD=pxOr + shiftX
	pyD=pyOr + shiftY
	return drawLineFMC(draw, pxOr,pyOr,pxD,pyD)

def shiftUp(pxOr, pyOr, size):
	shiftX=0.0
	shiftY=size 
	pxD=pxOr + shiftX
	pyD=pyOr + shiftY
	return pxD,pyD

	shiftX=0.0
	shiftY=size 
	pxD=pxOr + shiftX
	pyD=pyOr + shiftY
	return drawLineFMC(draw, pxOr,pyOr,size,pxD,pyD)


def drawlineDown(draw, pxOr, pyOr, size):
	shiftX=0.0
	shiftY=size	
	pxD=pxOr + shiftX
	pyD=pyOr - shiftY
	return drawLineFMC(draw, pxOr, pyOr, pxD, pyD)

def shiftDown(pxOr, pyOr, size):
	shiftX=0.0
	shiftY=size	
	pxD=pxOr + shiftX
	pyD=pyOr - shiftY
	return pxD, pyD

def drawArrowToLeftTrick(draw,Ox,Oy,radArc):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws  a head arrow with two arcs and one straight line
#and an arc of 270 grades from the middle of the straight line of head arrow
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy - radArc
	sharpx=oldx
	sharpy=oldy
	oldx,oldy=drawarcNE(draw,oldx,oldy,radArc,"ENE")#a
	auxX=oldx
	auxY=oldy
	oldx,oldy=drawarcSE(draw,sharpx,sharpy,radArc,"ESE")#b
	aux2X=oldx
	aux2Y=oldy
	cx,cy=drawLineFMC(draw,auxX,auxY,aux2X,aux2Y)#return the centre of arc
	drawArcFMC(draw, cx, cy, radArc,180, 0)
	drawArcFMC(draw, cx, cy, radArc,0, 90)
	cx +=radArc * 2 
	cy +=radArc
	return cx,cy

def drawArrowToLeft(draw,Ox,Oy,radArc,colorS):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws  a head arrow with one triangle
#and an arc of 270 grades from the middle of the straight line of head arrow
#return point top Right of external rectangle (out of the form)
	drawAux = dxf.drawing('tmp.dxf')
	sharpx = Ox
	sharpy = Oy - radArc
	Ax,Ay=drawarcNE(drawAux,sharpx,sharpy,radArc,"ENE")#a
	Bx,By=drawarcSE(drawAux,sharpx,sharpy,radArc,"ESE")#b
	drawArcColouredAndThickness(draw, Bx, By, radArc,180, 0,colorS,2.0)
	drawArcColouredAndThickness(draw, Bx, By, radArc,0, 90,colorS,2.0)
	drawTriangleColoured(draw, sharpx, sharpy, Ax, Ay, Bx, By,colorS)
	#drawArcColoured(draw, cx, cy, radArc,180, 0,colorS)
	#drawArcColoured(draw, cx, cy, radArc,0, 90,colorS)
	Bx +=radArc * 2 
	By +=radArc
	return Bx,By

def drawSolidArrowToLeft(draw,Ox,Oy,radArc,colorS):
#pre: draw=dxf.drawing('filename.dxf')  colorS > -1
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws  a head arrow with one triangle
#and an arc of 270 grades from the middle of the straight line of head arrow
#return point top Right of external rectangle (out of the form)
	drawAux = dxf.drawing('tmp.dxf')
	oldx = Ox
	oldy = Oy - radArc
	sharpx=oldx
	sharpy=oldy
	oldx,oldy=drawarcNE(drawAux,oldx,oldy,radArc,"ENE")#a
	auxX=oldx
	auxY=oldy
	oldx,oldy=drawarcSE(drawAux,sharpx,sharpy,radArc,"ESE")#b
	aux2X=oldx
	aux2Y=oldy
	#cx,cy=drawArcColoured(drawAux,auxX,auxY,aux2X,aux2Y,colorS)#return the centre of arc
	drawSolidTriangleFMC(draw,sharpx,sharpy,auxX,auxY,aux2X,aux2Y,colorS)
	cx=aux2X
	cy=aux2Y
	drawArcColouredAndThickness(draw, cx, cy, radArc,180, 0,colorS,2.0)
	drawArcColouredAndThickness(draw, cx, cy, radArc,0, 90,colorS,2.0)
	#drawArcColoured(draw, cx, cy, radArc,180, 0,colorS)
	#drawArcColoured(draw, cx, cy, radArc,0, 90,colorS)
	cx +=radArc * 2 
	cy +=radArc
	return cx,cy

def drawArrowToRight(draw,Ox,Oy,radArc,colorS):
#pre: draw=dxf.drawing('filename.dxf') colorS > -1
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws  a head arrow with one triangle
#and an arc of 270 grades from the middle of the straight line of head arrow
#return point top Right of external rectangle (out of the form)
	drawAux = dxf.drawing('tmp.dxf')
	Ax = Ox + radArc
	Ay = Oy - radArc
	Sharpx,Sharpy=drawarcSE(drawAux,Ax,Ay,radArc,"ESE")#A to sharpArrow
	Bx,By=drawarcNE(drawAux,Sharpx,Sharpy,radArc,"NNE")#sharpArrow to B
	drawArcColoured(draw, Ax, Ay, radArc,0, 270,colorS)
	drawTriangleColoured(draw, Sharpx, Sharpy, Ax, Ay, Bx, By,colorS)
	return Bx,(By + radArc)

def drawSolidArrowToRight(draw,Ox,Oy,radArc,colorS):
#pre: draw=dxf.drawing('filename.dxf')  colorS > -1
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws  a head arrow with one triangle
#and an arc of 270 grades from the middle of the straight line of head arrow
#return point top Right of external rectangle (out of the form)
	drawAux = dxf.drawing('tmp.dxf')
	oldx = Ox + radArc
	oldy = Oy - radArc
	cx=oldx
	cy=oldy
	oldx,oldy=drawarcSE(drawAux,oldx,oldy,radArc,"ESE")#c to a
	ax=oldx
	ay=oldy
	oldx,oldy=drawarcNE(drawAux,oldx,oldy,radArc,"ENE")#a to b
	bx=oldx
	by=oldy
	drawSolidTriangleFMC(draw,ax,ay,bx,by,cx,cy,colorS)
	drawArcColouredAndThickness(draw, cx, cy, radArc,0, 270,colorS,20.0)
	cx += radArc
	cy += radArc
	return cx,cy

def drawArrowToUp(draw,Ox,Oy,radArc,colorS):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws  a head arrow with one triangle
#and an arc of 90 grades from the middle of the straight line of head arrow
#and one line straigh
#return point top Right of external rectangle (out of the form)
	drawAux = dxf.drawing('tmp.dxf')
	oldx = Ox + radArc
	oldy = Oy - (radArc * 2)
	ex=oldx + (radArc * 2)
	ey=oldy
	oldx,oldy=drawLineColoured(draw,oldx,oldy,ex,ey,colorS)
	bottomArrowX,bottomArrowY=drawArcColouredNE(draw,ex,ey,radArc,"ENE",colorS)#draw and return centre bottom head arrow
	sharpArrowX=bottomArrowX
	sharpArrowY=bottomArrowY + radArc
	c1x=sharpArrowX - radArc
	c1y=sharpArrowY 
	c2x=sharpArrowX + radArc
	c2y=sharpArrowY
	dx=c2x
	dy=c2y
	Ax,Ay=drawarcSW(drawAux,c1x,c1y,radArc,"SSW")#shift sharp to A and return sharp of arrow
	Bx,By=drawarcSE(drawAux,dx,dy,radArc,"SSE")#shift B to C return wing Right of head arrow
	drawTriangleColoured(draw, sharpArrowX, sharpArrowY, Ax, Ay, Bx, By,colorS)
	return dx,dy

def drawSolidArrowToUp(draw,Ox,Oy,radArc,colorS):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws  a head arrow with one triangle
#and an arc of 90 grades from the middle of the straight line of head arrow
#and one line straigh
#return point top Right of external rectangle (out of the form)
	drawAux = dxf.drawing('tmp.dxf')
	oldx = Ox + radArc
	oldy = Oy - (radArc * 2)
	ex=oldx + (radArc * 2)
	ey=oldy
	#bottomArrowX=ex + radArc
	#bottomArrowY=ey + radArc
	#sharpArrowX=bottomArrowX
	#sharpArrowY=bottomArrowY + radArc
	#oldx,oldy = drawlineRight(draw,oldx,oldy,radArc * 2)
	oldx,oldy=drawLineColoured(draw,oldx,oldy,ex,ey,colorS)
	bottomArrowX,bottomArrowY=drawArcColouredNE(draw,ex,ey,radArc,"ENE",colorS)#draw and return centre bottom head arrow
	sharpArrowX=bottomArrowX
	sharpArrowY=bottomArrowY + radArc
	c1x=sharpArrowX - radArc
	c1y=sharpArrowY 
	c2x=sharpArrowX + radArc
	c2y=sharpArrowY
	dx=c2x
	dy=c2y
	Ax,Ay=drawarcSW(drawAux,c1x,c1y,radArc,"SSW")#shift sharp to A and return sharp of arrow
	Bx,By=drawarcSE(drawAux,dx,dy,radArc,"SSE")#shift B to C return wing Right of head arrow
	drawSolidTriangleFMC(draw,sharpArrowX,sharpArrowY,Ax,Ay,Bx,By,colorS)
	return dx,dy


def drawPieceNumberWhite(draw,Ox,Oy,radArc,length,width):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws rectangle with corners rounded
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy - radArc
	oldx,oldy=drawarcRightUp(draw,oldx,oldy,radArc)
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)
	oldx,oldy=drawarcRightDown(draw,oldx,oldy,radArc)
	endx=oldx
	endy=oldy + radArc
	oldx,oldy=drawlineDown(draw,oldx,oldy,width)
	oldx,oldy=drawarcDownLeft(draw,oldx,oldy,radArc)
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)
	oldx,oldy=drawarcUpLeft(draw,oldx,oldy,radArc)
	oldx,oldy=drawlineUp(draw,oldx,oldy,width)
	return endx,endy

def drawPieceCommandCustom(draw,Ox,Oy,radArc,shiftToSetHole,length):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on center
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy#- radArc
	dx,dy=drawPieceCommandGeneric(draw,oldx,oldy,radArc,length)
	oldx= Ox
	oldy= Oy #return to point origin
	oldy=oldy - (radArc *2.5) #line top of little rectangular form
	oldx +=shiftToSetHole
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6, radArc * 3)# mind that this lenght dont include archs
	return dx,dy

def drawPieceCommandCustomWhite(draw,Ox,Oy,radArc,shiftToSetHole,length):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 length > 0
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on center
#return point top Right of external rectangle (out of the form)
	dx,dy=drawPieceCommandCustom(draw,Ox,Oy,radArc,shiftToSetHole,length)
	return dx,dy

def drawPieceTopLoopCustom(draw,Ox,Oy,radArc,shiftToSetHole):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 shiftToSetHole > 0
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on center
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy#- radArc
	dx,dy=drawPieceTopLoopWhite(draw,oldx,oldy,radArc)
	oldx= Ox
	oldy= Oy #return to point origin
	oldy=oldy - (radArc *2.5) #line top of little rectangular form
	oldx +=shiftToSetHole
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6, radArc * 3)# mind that this lenght dont include archs
	return dx,dy

def drawPieceTopLoopCustom2(draw,Ox,Oy,radArc,shiftToSetHole,shiftTopRectangularInternal):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 shiftTopRectangularInternal float > 0.0
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on center
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy#- radArc
	dx,dy=drawPieceTopLoopWhite(draw,oldx,oldy,radArc)
	oldx= Ox
	oldy= Oy #return to point origin
	oldy=oldy - (radArc * shiftTopRectangularInternal) #line top of little rectangular form
	oldx +=shiftToSetHole
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6, radArc * 3)# mind that this lenght dont include archs
	return dx,dy

def drawPieceCommandGeneric(draw,Ox,Oy,radArc,lenght):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy - radArc
	oldx,oldy=drawarcRightUp(draw,oldx,oldy,radArc)#a
	length=radArc * 2
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#b
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#c
	length=radArc * 3
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#d
	oldx,oldy=drawarcNE(draw,oldx,oldy,radArc,"ENE")#e
	length=radArc * lenght#39
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#f
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"ESE")#g
	endx=oldx
	endy=oldy + radArc
	length=radArc * 8
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#h
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"SSW")#i
	length=radArc * lenght#39
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#j
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"SSW")#k
	length=radArc * 3
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#l
	oldx,oldy=drawarcNW(draw,oldx,oldy,radArc,"WNW")#m
	length=radArc * 2
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#n
	oldx,oldy=drawarcNW(draw,oldx,oldy,radArc,"WNW")#o
	length=radArc * 8
	oldx,oldy=drawlineUp(draw,oldx,oldy,length)#
	return endx,endy

def drawPieceRepeatLoopWhite(draw,Ox,Oy,radArc):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws 2 rectangle with externals corners rounded and internal corners straight
#join by one straigth line and on the other side two arcs and one straight line
#with two slot and two tabs
#return point top Right of external rectangle (out of the form)
	width=radArc * 11
	widthBottom=radArc * 6
	radCorner=radArc * 2 #the radius of arc of corner top is double than command or numered pieces
	oldx = Ox
	oldy = Oy - radCorner
	oldx,oldy=drawarcRightUp(draw,oldx,oldy,radCorner)#a
	length=radArc * 2
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#b
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#c
	length=radArc * 3
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#d
	oldx,oldy=drawarcNE(draw,oldx,oldy,radArc,"ENE")#e
	length=radArc * 30#39
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#f
	oldx,oldy=drawarcSE(draw,oldx,oldy,radCorner,"ESE")#g
	endx=oldx
	endy=oldy + radCorner
	length=width
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#h
	length=radArc * 29#38 make longer this line to compensate no existence of arc
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#j
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"SSW")#k
	length=radArc * 3
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#l
	oldx,oldy=drawarcNW(draw,oldx,oldy,radArc,"WNW")#m
	length=radArc * 2
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#n
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"WSW")#o
	length=radArc * 8
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#p
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#q
	length=radArc * 2 
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#m
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#c   m
	length=radArc * 3
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#d l
	oldx,oldy=drawarcNE(draw,oldx,oldy,radArc,"ENE")#e k
	length=radArc * 29#39  make longer this line to compensate no existence of arc
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#f
	length=widthBottom
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#h
	oldx,oldy=drawarcSW(draw,oldx,oldy,radCorner,"SSW")#i
	length=radArc * 30
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#j
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"SSW")#q
	length=radArc * 3
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#r
	oldx,oldy=drawarcNW(draw,oldx,oldy,radArc,"WNW")#s
	length=radArc * 2
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#b
	oldx,oldy=drawarcNW(draw,oldx,oldy,radCorner,"NWN")#k
	length=radArc * 27
	oldx,oldy=drawlineUp(draw,oldx,oldy,length)#p
	return endx,endy

def drawPieceForeverLoopWhite(draw,Ox,Oy,radArc):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws 2 rectangle with externals corners rounded and internal corners straight
#join by one straigth line and on the other side two arcs and one straight line
#with two slot and one tab
#return point top Right of external rectangle (out of the form)
	width=radArc * 11
	widthBottom=radArc * 6
	radCorner=radArc * 2 #the radius of arc of corner top is double than command or numered pieces
	oldx = Ox
	oldy = Oy - radCorner
	oldx,oldy=drawarcRightUp(draw,oldx,oldy,radCorner)#a
	length=radArc * 2
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#b
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#c
	length=radArc * 3
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#d
	oldx,oldy=drawarcNE(draw,oldx,oldy,radArc,"ENE")#e
	length=radArc * 30#39
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#f
	oldx,oldy=drawarcSE(draw,oldx,oldy,radCorner,"ESE")#g
	endx=oldx
	endy=oldy + radCorner
	length=width
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#h
	length=radArc * 29#38 make longer this line to compensate no existence of arc
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#j
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"SSW")#k
	length=radArc * 3
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#l
	oldx,oldy=drawarcNW(draw,oldx,oldy,radArc,"WNW")#m
	length=radArc * 2
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#n
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"WSW")#o
	length=radArc * 8
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#p
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#q
	length=radArc * 2 
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#m
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#c   m
	length=radArc * 3
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#d l
	oldx,oldy=drawarcNE(draw,oldx,oldy,radArc,"ENE")#e k
	length=radArc * 29#39  make longer this line to compensate no existence of arc
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#f
	length=widthBottom
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#h
	oldx,oldy=drawarcSW(draw,oldx,oldy,radCorner,"SSW")#i
	length=radArc * 37 #47 make longer this line to compensate no existence of slot
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#j
	oldx,oldy=drawarcNW(draw,oldx,oldy,radCorner,"NWN")#k
	length=radArc * 27
	oldx,oldy=drawlineUp(draw,oldx,oldy,length)#p
	return endx,endy

def drawPieceJointLoopWhite(draw,Ox,Oy,radArc):
	#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of rectangle 
#post: it draws rectangle with line straight on leftt side and two concave corners on the right side 
#return point top Right of rectangle 
	oldx = Ox
	oldy = Oy
	length=radArc * 5
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)
	endx=oldx
	endy=oldy
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"WSW")
	length=radArc * 8
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")
	length=radArc * 5
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)
	length=radArc * 10
	oldx,oldy=drawlineUp(draw,oldx,oldy,length)
	return endx,endy

def drawPieceTopLoopWhite(draw,Ox,Oy,radArc):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws rectangle with top corners rounded and bottom corners straight
#return point top Right of external rectangle (out of the form)
	width=radArc * 11
	radCorner=radArc * 2 #the radius of arc of corner top is double than command or numered pieces
	oldx = Ox
	oldy = Oy - radCorner
	oldx,oldy=drawarcRightUp(draw,oldx,oldy,radCorner)#a
	length=radArc * 2
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#b
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#c
	length=radArc * 3
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#d
	oldx,oldy=drawarcNE(draw,oldx,oldy,radArc,"ENE")#e
	length=radArc * 30#39
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#f
	oldx,oldy=drawarcSE(draw,oldx,oldy,radCorner,"ESE")#g
	endx=oldx
	endy=oldy + radCorner
	length=width
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#h
	length=radArc * 29#38 make longer this line to compensate no existence of arc
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#j
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"SSW")#k
	length=radArc * 3
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#l
	oldx,oldy=drawarcNW(draw,oldx,oldy,radArc,"WNW")#m
	length=radArc * 7 #make longer this line to close the figure and compensate no existence of arc
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#n
	length=width 
	oldx,oldy=drawlineUp(draw,oldx,oldy,length)#p
	return endx,endy

def drawPieceTopRepeatCustom(draw,Ox,Oy,radArc,shiftToSetHole,shiftTopRectangularInternal,sizeText,shiftInitText):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 shiftToSetHole > 0 shiftTopRectangularInternal float > 0.0
#sizeText > 0 int
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on 
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy
	oldx,oldy = drawPieceTopLoopWhite(draw,oldx,oldy,radArc)
	dx=oldx
	dy=oldy
	oldx = Ox + shiftToSetHole
	oldy=oldy - (radArc * shiftTopRectangularInternal) #line top of little rectangular form
	endTextX=oldx
	endTextY=oldy - sizeText
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6,radArc * 3)# mind that this lenght dont include archs
	#lengthText=getLenghtTextBeforeNumber(Ox,shiftToSetHole,shiftInitText)
	writeTitleBeforeNumber(draw,"repeat",endTextX,endTextY,sizeText,radArc,1)
	return dx,dy

def drawPieceTopRepeatReset(draw,Ox,Oy,radArc,shiftToSetHole,shiftTopRectangularInternal,sizeText,shiftInitText):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 shiftToSetHole > 0 shiftTopRectangularInternal float > 0.0
#sizeText > 0 int
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on 
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy
	oldx,oldy = drawPieceTopLoopWhite(draw,oldx,oldy,radArc)
	dx=oldx
	dy=oldy
	oldx = Ox + shiftToSetHole
	oldy=oldy - (radArc * shiftTopRectangularInternal) #line top of little rectangular form
	endTextX=oldx
	endTextY=oldy - sizeText
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6,radArc * 3)# mind that this lenght dont include archs
	#writeTitleBeforeNumber(draw,"repeat",endTextX,endTextY,sizeText,radArc,1)
	return dx,dy

def drawPieceTopForeverCustom(draw,Ox,Oy,radArc,shiftToSetHole,shiftTopRectangularInternal,sizeText,shiftInitText):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 shiftToSetHole > 0 shiftTopRectangularInternal float > 0.0
#sizeText > 0 int
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on 
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy
	oldx,oldy = drawPieceTopLoopWhite(draw,oldx,oldy,radArc)
	dx=oldx
	dy=oldy
	oldx = Ox + shiftToSetHole
	oldy=oldy - (radArc * shiftTopRectangularInternal) #line top of little rectangular form
	endTextX=oldx
	endTextY=oldy - sizeText
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6,radArc * 3)# mind that this lenght dont include archs
	#lengthText=getLenghtTextBeforeNumber(Ox,shiftToSetHole,shiftInitText)
	writeTitleBeforeNumber(draw,"forever",endTextX,endTextY,sizeText,radArc,1)
	return dx,dy

def drawPieceTopForeverReset(draw,Ox,Oy,radArc,shiftToSetHole,shiftTopRectangularInternal,sizeText,shiftInitText):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 shiftToSetHole > 0 shiftTopRectangularInternal float > 0.0
#sizeText > 0 int
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on 
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy
	oldx,oldy = drawPieceTopLoopWhite(draw,oldx,oldy,radArc)
	dx=oldx
	dy=oldy
	oldx = Ox + shiftToSetHole
	oldy=oldy - (radArc * shiftTopRectangularInternal) #line top of little rectangular form
	endTextX=oldx
	endTextY=oldy - sizeText
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6,radArc * 3)# mind that this lenght dont include archs
	#lengthText=getLenghtTextBeforeNumber(Ox,shiftToSetHole,shiftInitText)
	#writeTitleBeforeNumber(draw,"forever",endTextX,endTextY,sizeText,radArc,1)
	return dx,dy

def drawPieceBottomForeverCustom(draw,Ox,Oy,radArc,shiftToSetArrow,shiftTopRectangularInternal,sizeArrow):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of rectangle 
#post: it draws rectangle with top corners straight and bottom corners rounded
#with a one slot on top
#with uo arrow on rigth side
#return point top Right of external rectangle (out of the form)
	dx,dy=drawPieceBottomForeverWhite(draw,Ox,Oy,radArc)
	iniArrowX = Ox + shiftToSetArrow
	iniArrowY=Oy - (radArc * shiftTopRectangularInternal) #line top of little rectangular form
	drawArrowToUp(draw,iniArrowX,iniArrowY,radArc * sizeArrow,colorText)
	return dx,dy

def drawPieceBottomForeverReset(draw,Ox,Oy,radArc,shiftToSetArrow,shiftTopRectangularInternal,sizeArrow):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of rectangle 
#post: it draws rectangle with top corners straight and bottom corners rounded
#with a one slot on top
#with uo arrow on rigth side
#return point top Right of external rectangle (out of the form)
	dx,dy=drawPieceBottomForeverWhite(draw,Ox,Oy,radArc)
	#iniArrowX = Ox + shiftToSetArrow
	#iniArrowY=Oy - (radArc * shiftTopRectangularInternal) #line top of little rectangular form
	#drawArrowToUp(draw,iniArrowX,iniArrowY,radArc,colorText)
	return dx,dy

def drawPieceBottomRepeatCustom(draw,Ox,Oy,radArc,shiftToSetArrow,shiftTopRectangularInternal,sizeArrow):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 shiftToSetHole > 0 shiftTopRectangularInternal float > 0.0
#sizeText > 0 int
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on 
#return point top Right of external rectangle (out of the form)
	dx,dy=drawPieceBottomRepeatWhite(draw,Ox,Oy,radArc)
	iniArrowX = Ox + shiftToSetArrow
	iniArrowY=Oy - (radArc * shiftTopRectangularInternal) #line top of little rectangular form
	drawArrowToUp(draw,iniArrowX,iniArrowY,radArc * sizeArrow,colorText)
	return dx,dy

def drawPieceBottomRepeatReset(draw,Ox,Oy,radArc,shiftToSetArrow,shiftTopRectangularInternal,sizeArrow):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 shiftToSetHole > 0 shiftTopRectangularInternal float > 0.0
#sizeText > 0 int
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on 
#return point top Right of external rectangle (out of the form)
	dx,dy=drawPieceBottomRepeatWhite(draw,Ox,Oy,radArc)
	#iniArrowX = Ox + shiftToSetArrow
	#iniArrowY=Oy - (radArc * shiftTopRectangularInternal) #line top of little rectangular form
	#drawArrowToUp(draw,iniArrowX,iniArrowY,radArc,colorText)
	return dx,dy

def getLenghtTextBeforeNumber(Ox,shiftToSetHole,shiftInitText):
	oldx = Ox + shiftToSetHole
	endTextX=oldx
	initTextX = Ox + shiftInitText#x of init text
	lengthText=endTextX - initTextX
	return lengthText
	

def drawPieceBottomForeverWhite(draw,Ox,Oy,radArc):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of rectangle 
#post: it draws rectangle with top corners straight and bottom corners rounded
#with a one slot on top
#return point top Right of external rectangle (out of the form)
	width=radArc * 6
	radCorner=radArc * 2 #the radius of arc of corner top is double than command or numered pieces
	oldx = Ox
	oldy = Oy
	length=radArc * 7 #in order to achive the top slot
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#b  o + n
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#c   m
	length=radArc * 3
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#d l
	oldx,oldy=drawarcNE(draw,oldx,oldy,radArc,"ENE")#e k
	length=radArc * 29#39  make longer this line to compensate no existence of arc
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#f
	length=width
	endx=oldx
	endy=oldy
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#h
	oldx,oldy=drawarcSW(draw,oldx,oldy,radCorner,"SSW")#i
	length=radArc * 37 #47 make longer this line to compensate no existence of slot
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#j
	oldx,oldy=drawarcNW(draw,oldx,oldy,radCorner,"NWN")#k
	length=width
	oldx,oldy=drawlineUp(draw,oldx,oldy,length)#p
	return endx,endy

def drawPieceBottomRepeatWhite(draw,Ox,Oy,radArc):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of rectangle 
#post: it draws rectangle with top corners straight and bottom corners rounded
#with a one slot on top and other on bottom
#return point top Right of external rectangle (out of the form)
	width=radArc * 6
	radCorner=radArc * 2 #the radius of arc of corner top is double than command or numered pieces
	oldx = Ox
	oldy = Oy
	length=radArc * 7 #in order to achive the top slot
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#b  o + n
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#c   m
	length=radArc * 3
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#d l
	oldx,oldy=drawarcNE(draw,oldx,oldy,radArc,"ENE")#e k
	length=radArc * 29#39  make longer this line to compensate no existence of arc
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#f
	length=width
	endx=oldx
	endy=oldy
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#h
	oldx,oldy=drawarcSW(draw,oldx,oldy,radCorner,"SSW")#i
	length=radArc * 30
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#j
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"SSW")#q
	length=radArc * 3
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#r
	oldx,oldy=drawarcNW(draw,oldx,oldy,radArc,"WNW")#s
	length=radArc * 2
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#b
	oldx,oldy=drawarcNW(draw,oldx,oldy,radCorner,"NWN")#k
	length=width
	oldx,oldy=drawlineUp(draw,oldx,oldy,length)#p
	return endx,endy

def drawPieceCommandWhite(draw,Ox,Oy,radArc):
#pre: draw=dxf.drawing('filename.dxf')
# Ox Oy point top left of external rectangle (out of the form)
#post: it draws rectangle with corners rounded
#with one slot on top and a tab on bottom
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy - radArc
	oldx,oldy=drawarcRightUp(draw,oldx,oldy,radArc)#a
	length=radArc * 2
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#b
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"SSE")#c
	length=radArc * 3
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#d
	oldx,oldy=drawarcNE(draw,oldx,oldy,radArc,"ENE")#e
	length=radArc * 39
	oldx,oldy=drawlineRight(draw,oldx,oldy,length)#f
	oldx,oldy=drawarcSE(draw,oldx,oldy,radArc,"ESE")#g
	endx=oldx
	endy=oldy + radArc
	length=radArc * 8
	oldx,oldy=drawlineDown(draw,oldx,oldy,length)#h
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"SSW")#i
	length=radArc * 39
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#j
	oldx,oldy=drawarcSW(draw,oldx,oldy,radArc,"SSW")#k
	length=radArc * 3
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#l
	oldx,oldy=drawarcNW(draw,oldx,oldy,radArc,"WNW")#m
	length=radArc * 2
	oldx,oldy=drawlineLeft(draw,oldx,oldy,length)#n
	oldx,oldy=drawarcNW(draw,oldx,oldy,radArc,"WNW")#o
	length=radArc * 8
	oldx,oldy=drawlineUp(draw,oldx,oldy,length)#p
	return endx,endy

def drawarcRightDown(draw, pxOr, pyOr, size):
#pre: draw=dxf.drawing('filename.dxf')
#post: arc destiny SE componente ESE
	return drawarcSE(draw, pxOr, pyOr, size,'ESE')

def drawarcRightUp(draw, pxOr, pyOr, size):
#pre: draw=dxf.drawing('filename.dxf')
#post: arc destiny NE componente NNE
	return drawarcNE(draw, pxOr, pyOr, size,'NNE')

def drawarcDownLeft(draw, pxOr, pyOr, size):
#pre: draw=dxf.drawing('filename.dxf')
#post: arc destiny SW componente SSW
	return drawarcSW(draw, pxOr, pyOr, size,'SSW')

def drawarcUpLeft(draw, pxOr, pyOr, size):
#pre: draw=dxf.drawing('filename.dxf')
#post: arc destiny NW componente WNW
	return drawarcNW(draw, pxOr, pyOr, size,'WNW')

def setCursor(draw,Ox,Oy,radarc,length,width,track):
	Dx=Ox
	Dy=Oy
	shiftY=radarc + width
	shiftY=shiftY - (width / 5)
	if track == 'true':
		Dx,Dy=drawlineDown(draw,Dx,Dy,shiftY)
	else: 
		Dx,Dy=shiftDown(Dx,Dy,shiftY) #position baseline
	shiftX=radarc + length
	shiftX=shiftX - (length / 10)
	if track == 'true':
		Dx,Dy=drawlineLeft(draw,Dx,Dy,shiftX)
	else:
		Dx,Dy=shiftLeft(Dx,Dy,shiftX) #position cursor
	return Dx,Dy

def setCursor(Ox,Oy,radarc,length,width,track):
	Dx=Ox
	Dy=Oy
	shiftY=radarc + width
	shiftY=shiftY - (width / 5)
	Dx,Dy=shiftDown(Dx,Dy,shiftY) #position baseline
	shiftX=radarc + length
	shiftX=shiftX - (length / 10)
	Dx,Dy=shiftLeft(Dx,Dy,shiftX) #position cursor
	return Dx,Dy

def setAlingPoint(Ox,Oy,radarc,length,width,track):
	Dx=Ox
	Dy=Oy
	shiftY=radarc + width
	#shiftY=shiftY - (width / 5)
	Dx,Dy=shiftDown(Dx,Dy,shiftY) #position baseline
	shiftX=(radarc * 2) + (length /2) #mind lenght is at ths point (length - arc)
	Dx,Dy=shiftLeft(Dx,Dy,shiftX) #position cursor
	return Dx,Dy

def setAlingPointText(Ox,Oy,length,width,track):
	Dx=Ox
	Dy=Oy
	shiftY= width
	#shiftY=shiftY - (width / 5)
	Dx,Dy=shiftDown(Dx,Dy,shiftY) #position baseline
	shiftX=(length /2) 
	Dx,Dy=shiftLeft(Dx,Dy,shiftX) #position cursor
	return Dx,Dy

def drawPieceNumberCompleted(draw,Ox,Oy,radArc,numtxt):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0, num > 0
#post: it draws rectangle with corners rounded
#with num on center of rectangle
#return point top Right of external rectangle (out of the form)
	length=radArc * 6#   mind that this lenght dont include archs
	width=radArc * 3#    mind that this lenght dont include archs
	endX,endY=drawPieceNumberWhite(draw,Ox,Oy,radArc,length,width)
	#endX,endY=setCursor(endX,endY,radArc,length,width,'true')
	if numtxt==9:
		writeNumber9(draw,numtxt,endX,endY,radArc,length - radArc,width,0)
	else:
		writeNumber(draw,numtxt,endX,endY,radArc,length - radArc,width,0)
	return endX,endY

def drawPoolPiecesNumbered(draw,Ox,Oy,radArc,numPieces,numByColumn,distance):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 numByColumn >0, numPieces > 0
#post: it draws a pool of rectangles with corners rounded
#with num on center of rectangles
#return point top Right of external rectangle (out of the form)
#of last rectangle
	numCol=1
	oldx=Ox
	oldy=Oy
	for i in range(1,numPieces + 1): 
		oldx,oldy=drawPieceNumberCompleted(draw,oldx,oldy,radArc,i)
		dx=oldx
		dy=oldy
		oldx,oldy=shiftRight(oldx,oldy,distance)
		if (i % (numByColumn))==0.0: 
			oldx,oldy=shiftNextLine(oldx,oldy,radArc,numPieces,numByColumn,1,radArc * 5,Ox)  #mind that this lenght include archs
		else:
			oldx,oldy=shiftRight(oldx,oldy,distance)
	return dx,dy

def drawPoolPiecesNumeredWhite(draw,Ox,Oy,radArc,numPieces,numByColumn,distance):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 numByColumn >0, numPieces > 0
#post: it draws a pool of rectangles with corners rounded
#with num on center of rectangles
#return point top Right of external rectangle (out of the form)
#of last rectangle
	numCol=1
	oldx=Ox
	oldy=Oy
	for i in range(1,numPieces + 1):
		oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc, radArc * 6 , radArc * 3 )#   mind that this lenght not include archs
		dx = oldx
		dy = oldy
		oldx,oldy=shiftRight(oldx,oldy,distance)
		if (i % (numByColumn))==0.0: 
			oldx,oldy=shiftNextLine(oldx,oldy,radArc,numPieces,numByColumn,1,radArc * 5,Ox)#   mind that this lenght include archs
		else:
			oldx,oldy=shiftRight(oldx,oldy,distance)
	return dx,dy

def drawPoolPiecesCommandsWhite(draw,Ox,Oy,radArc,numPieces,numByColumn,distance):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 numByColumn >0, numPieces > 0
#post: it draws a pool of rectangles with corners rounded and one slot on top and a tab on bottom
#return point top Right of external rectangle (out of the form)
#of last rectangle
	numCol=1
	oldx=Ox
	oldy=Oy
	for i in range(1,numPieces + 1):
		oldx,oldy=drawPieceCommandWhite(draw,oldx,oldy,radArc)
		dx = oldx
		dy = oldy
		oldx,oldy=shiftRight(oldx,oldy,distance)
		if (i % (numByColumn))==0.0: 
			oldx,oldy=shiftNextLine(oldx,oldy,radArc,numPieces,numByColumn,2,radArc *11,Ox)#   mind that this lenght include archs and one tab
		else:
			oldx,oldy=shiftRight(oldx,oldy,distance)
	return dx,dy

def shiftNextLine(Ox,Oy,radArc,numPieces,numByColumn,typePieces,width,xIniColumn):
#pre: typePieces [1:numered,2:command,3:loop]
	oldx=Ox
	oldy=Oy
	if typePieces==1:
		oldx,oldy=shiftNextLinePiecesNumered(oldx,oldy,radArc,numPieces,numByColumn,xIniColumn)
	else:
		oldx,oldy=shiftDown(oldx,oldy,space + (width))
		oldx=xIniColumn
	return oldx,oldy

def shiftNextLinePiecesNumered(Ox,Oy,radArc,numPieces,numByColumn,xIniColumn):
	#length = radArc * 8
	width = radArc * 5
	oldx,oldy=shiftDown(Ox,Oy,space + (width))
	oldx=xIniColumn
	return oldx,oldy

def writeNumber(draw,message,Ox,Oy,radArc,length,width,rotation):
	alignx,aligny=setAlingPoint(Ox,Oy,radArc,length,width,'false')
	writeText(draw,message,alignx,aligny,width,colorText,currentLayer,0)

def writeTitle(draw,message,Ox,Oy,radArc,length,width,rotation):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0
#post: it draws message alingCenter
	alignx,aligny=setAlingPointText(Ox,Oy,length,width,'false')
	writeText(draw,message,alignx,aligny,width,colorText,currentLayer,0)

def writeTitleBeforeNumber(draw,message,Ox,Oy,size,margin,colorM):
	#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 margin > 0
	# Ox Oy refers point init rectangular square
	#post: it draws message alingRight reparate of Ox Oy by margin=
	oldx=Ox - margin
	oldy=Oy
	writeTextRight(draw,message,oldx,oldy,size,colorM,currentLayer,0)
	

def writeTitleAfterNumber(draw,message,Ox,Oy,size,margin,colorM):
	#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 margin > 0
	# Ox Oy refers point init rectangular square
	#post: it draws message alingRight reparate of Ox Oy by margin=
	oldx=Ox + margin
	oldy=Oy
	writeTextLeft(draw,message,oldx,oldy,size,colorM,currentLayer,0)


def writeNumber9(draw,message,Ox,Oy,radArc,length,width,rotation):
	alignx,aligny=setAlingPoint(Ox,Oy,radArc,length,width,'false')
	cx=alignx
	cy=aligny
	aligny += (width *2) /5 #up the align point to figure 9 
	size9 = (width *9) /10
	writeText(draw,message,alignx,aligny,size9,colorText,currentLayer,0)
	message="o"
	size9 = width /5
	writeText(draw,message,cx,cy,size9,colorText,currentLayer,0)
	#drawCircle(draw,cx,cy,radArc * 2)

def writeMessage(draw,message,Ox,Oy,rotation):
	writeTextNoAling(draw,message,Ox,Oy,sizeText,colorText,currentLayer,0)

def drawPieceWaitCustom(draw,Ox,Oy,radArc,shiftToSetHole,length,margin):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on center
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy#- radArc
	dx,dy=drawPieceCommandGeneric(draw,oldx,oldy,radArc,length)
	oldx= Ox
	oldy= Oy #return to point origin
	oldy=oldy - (radArc *2.5) #line top of little rectangular form
	oldx +=shiftToSetHole
	beforeNx=oldx - margin
	beforeNy=oldy - sizeText
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6, radArc * 3)# mind that this lenght dont include archs
	afterNx=oldx + margin
	afterNy=oldy - sizeText
	writeTitleBeforeNumber(draw,"wait",beforeNx,beforeNy,sizeText,radArc,margin)
	writeTitleAfterNumber(draw,"secs",afterNx,afterNy,sizeText,radArc,margin)
	return dx,dy

def drawPieceWaitReset(draw,Ox,Oy,radArc,shiftToSetHole,length,margin):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on center
#return point top Right of external rectangle (out of the form)
	#drawTmp = dxf.drawing('tmp.dxf')
	oldx = Ox
	oldy = Oy#- radArc
	dx,dy=drawPieceCommandGeneric(draw,oldx,oldy,radArc,length)
	oldx= Ox
	oldy= Oy #return to point origin
	oldy=oldy - (radArc *2.5) #line top of little rectangular form
	oldx +=shiftToSetHole
	beforeNx=oldx - margin
	beforeNy=oldy - sizeText
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6, radArc * 3)# mind that this lenght dont include archs
	afterNx=oldx + margin
	afterNy=oldy - sizeText
	#writeTitleBeforeNumber(draw,"wait",beforeNx,beforeNy,sizeText,radArc,margin)
	#writeTitleAfterNumber(draw,"secs",afterNx,afterNy,sizeText,radArc,margin)
	return dx,dy

def drawPieceMoveCustom(draw,Ox,Oy,radArc,shiftToSetHole,length,margin):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on center
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy#- radArc
	dx,dy=drawPieceCommandGeneric(draw,oldx,oldy,radArc,length)
	oldx= Ox
	oldy= Oy #return to point origin
	oldy=oldy - (radArc *2.5) #line top of little rectangular form
	oldx +=shiftToSetHole
	beforeNx=oldx - margin
	beforeNy=oldy - sizeText
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6, radArc * 3)# mind that this lenght dont include archs
	afterNx=oldx + margin
	afterNy=oldy - sizeText
	writeTitleBeforeNumber(draw,"move",beforeNx,beforeNy,sizeText,radArc,margin)
	writeTitleAfterNumber(draw,"steps",afterNx,afterNy,sizeText,radArc,margin)
	return dx,dy

def drawPieceMoveReset(draw,Ox,Oy,radArc,shiftToSetHole,length,margin):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on center
#return point top Right of external rectangle (out of the form)
	oldx = Ox
	oldy = Oy#- radArc
	dx,dy=drawPieceCommandGeneric(draw,oldx,oldy,radArc,length)
	oldx= Ox
	oldy= Oy #return to point origin
	oldy=oldy - (radArc *2.5) #line top of little rectangular form
	oldx +=shiftToSetHole
	beforeNx=oldx - margin
	beforeNy=oldy - sizeText
	oldx,oldy=drawPieceNumberWhite(draw,oldx,oldy,radArc,radArc * 6, radArc * 3)# mind that this lenght dont include archs
	afterNx=oldx + margin
	afterNy=oldy - sizeText
	#writeTitleBeforeNumber(draw,"move",beforeNx,beforeNy,sizeText,radArc,margin)
	#writeTitleAfterNumber(draw,"steps",afterNx,afterNy,sizeText,radArc,margin)
	return dx,dy

def drawPieceCustomTurn(draw,Ox,Oy,radArc,shiftToSetArrow,length,margin,direction):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 direction [0,1]
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on center
#with text: turn degrees
#with arrow
#return point top Right of external rectangle (out of the form)
	#drawTmp = dxf.drawing('tmp.dxf')
	oldx = Ox
	oldy = Oy#- radArc
	dx,dy=drawPieceCommandGeneric(draw,oldx,oldy,radArc,length)
	oldx= Ox
	oldy= Oy #return to point origin
	beforeAy = oldy - (radArc *2.5) #line top of little rectangular form
	beforeAx = oldx + shiftToSetArrow
	beforeAx -= margin
	beforeTextAx=beforeAx - margin
	beforeTextAy=beforeAy - sizeText
	writeTitleBeforeNumber(draw,"turn",beforeTextAx,beforeTextAy,sizeText,radArc,margin)
	if (direction==0):
		afterAx,afterAy=drawArrowToLeft(draw,beforeAx,beforeAy,radArc * 2,colorText)
	else:
		afterAx,afterAy=drawArrowToRight(draw,beforeAx,beforeAy,radArc * 2,colorText)
	beforeNx=afterAx + margin
	beforeNy=beforeAy#recovery align
	afterNx,afterNy=drawPieceNumberWhite(draw,beforeNx,beforeNy,radArc,radArc * 6, radArc * 3)# mind that this lenght dont include archs
	afterNx += margin
	afterNy -= sizeText
	writeTitleAfterNumber(draw,"degrees",afterNx,afterNy,sizeText,radArc,margin)
	return dx,dy

def drawPieceResetTurn(draw,Ox,Oy,radArc,shiftToSetArrow,length,margin,direction):
#pre: draw=dxf.drawing('filename.dxf'), radArc > 0 direction [0,1]
#post: it draws rectangle with corners rounded
#and one slot on top and a tab on bottom
#with other little rectangle on center
#with text: turn degrees
#with arrow
#return point top Right of external rectangle (out of the form)
	drawTmp = dxf.drawing('tmp.dxf')
	oldx = Ox
	oldy = Oy#- radArc
	dx,dy=drawPieceCommandGeneric(draw,oldx,oldy,radArc,length)
	oldx= Ox
	oldy= Oy #return to point origin
	beforeAy = oldy - (radArc *2.5) #line top of little rectangular form
	beforeAx = oldx + shiftToSetArrow
	beforeAx -= margin
	beforeTextAx=beforeAx - margin
	beforeTextAy=beforeAy - sizeText
	#writeTitleBeforeNumber(draw,"turn",beforeTextAx,beforeTextAy,sizeText,radArc,margin)
	#if (direction==0):
	#	afterAx,afterAy=drawArrowToLeft(draw,beforeAx,beforeAy,radArc * 2,colorText)
	#else:
	afterAx,afterAy=drawArrowToRight(drawTmp,beforeAx,beforeAy,radArc * 2,colorText)
	beforeNx=afterAx + margin
	beforeNy=beforeAy#recovery align
	afterNx,afterNy=drawPieceNumberWhite(draw,beforeNx,beforeNy,radArc,radArc * 6, radArc * 3)# mind that this lenght dont include archs
	#afterNx += margin
	#afterNy -= sizeText
	#writeTitleAfterNumber(draw,"degrees",afterNx,afterNy,sizeText,radArc,margin)
	return dx,dy


def drawPieceWait(draw,Ox,Oy,radArc,clear):
#pre:draw=dxf.drawing('filename.dxf'), radArc > 0
#post:
	shiftToHole=20
	lenght=39
	margin=1
	if clear==0:
		dX,dY=drawPieceWaitReset(draw,Ox,Oy,radArcMin,shiftToHole,lenght,margin)
	else:
		dX,dY=drawPieceWaitCustom(draw,Ox,Oy,radArcMin,shiftToHole,lenght,margin)
	return dX,dY

def drawPieceMove(draw,Ox,Oy,radArc,clear):
#pre:draw=dxf.drawing('filename.dxf'), radArc > 0
#post:
	shiftToHole=25
	lenght=50
	margin=1
	if clear==0:
		dX,dY=drawPieceMoveReset(draw,Ox,Oy,radArcMin,shiftToHole,lenght,margin)
	else:
		dX,dY=drawPieceMoveCustom(draw,Ox,Oy,radArcMin,shiftToHole,lenght,margin)
	return dX,dY

def drawPieceTurnLeft(draw,Ox,Oy,radArc,clear):
#pre:draw=dxf.drawing('filename.dxf'), radArc > 0
#post:
	shiftToArrow=25
	length=60
	margin=1
	if clear==0:
		dX,dY=drawPieceResetTurn(draw,Ox,Oy,radArc,shiftToArrow,length,margin,0)
	else:
		dX,dY=drawPieceCustomTurn(draw,Ox,Oy,radArc,shiftToArrow,length,margin,0)
	return dX,dY

def drawPieceTurnRight(draw,Ox,Oy,radArc,clear):
#pre:draw=dxf.drawing('filename.dxf'), radArc > 0
#post:
	shiftToArrow=25
	length=60
	margin=1
	if clear==0:
		dX,dY=drawPieceResetTurn(draw,Ox,Oy,radArc,shiftToArrow,length,margin,1)
	else:
		dX,dY=drawPieceCustomTurn(draw,Ox,Oy,radArc,shiftToArrow,length,margin,1)
	return dX,dY

def drawPieceTopRepeat(draw,Ox,Oy,radArc,clear):
#pre:draw=dxf.drawing('filename.dxf'), radArc > 0
#post:
	shiftToSetHole=30.0
	shiftInitText=1
	if clear==0:
		dX,dY=drawPieceTopRepeatReset(draw,Ox,Oy,radArc,shiftToSetHole,shiftTopLineText,sizeText,shiftInitText)
	else:
		dX,dY=drawPieceTopRepeatCustom(draw,Ox,Oy,radArc,shiftToSetHole,shiftTopLineText,sizeText,shiftInitText)
	return dX,dY

def drawPieceTopForever(draw,Ox,Oy,radArc,clear):
#pre:draw=dxf.drawing('filename.dxf'), radArc > 0
#post:
	shiftToSetHole=30.0
	shiftInitText=1
	if clear==0:
		dX,dY=drawPieceTopForeverReset(draw,Ox,Oy,radArc,shiftToSetHole,shiftTopLineText,sizeText,shiftInitText)
	else:
		dX,dY=drawPieceTopForeverCustom(draw,Ox,Oy,radArc,shiftToSetHole,shiftTopLineText,sizeText,shiftInitText)
	return dX,dY

def drawPieceBottomRepeat(draw,Ox,Oy,radArc,clear):
#pre:draw=dxf.drawing('filename.dxf'), radArc > 0
#post:
	shiftToSetArrow=25.0
	sizeArrow=2
	if clear==0:
		dX,dY=drawPieceBottomRepeatReset(draw,Ox,Oy,radArc,shiftToSetArrow,shiftTopLineText,sizeArrow)
	else:
		dX,dY=drawPieceBottomRepeatCustom(draw,Ox,Oy,radArc,shiftToSetArrow,shiftTopLineText,sizeArrow)
	return dX,dY

def drawPieceBottomForever(draw,Ox,Oy,radArc,clear):
#pre:draw=dxf.drawing('filename.dxf'), radArc > 0
#post:
	shiftToSetArrow=25.0
	sizeArrow=2
	if clear==0:
		dX,dY=drawPieceBottomForeverReset(draw,Ox,Oy,radArc,shiftToSetArrow,shiftTopLineText,sizeArrow)
	else:
		dX,dY=drawPieceBottomForeverCustom(draw,Ox,Oy,radArc,shiftToSetArrow,shiftTopLineText,sizeArrow)
	return dX,dY

def drawSheetClearColour():
	p0x=10.0
	p0y=10.0
	drawing = dxf.drawing('sheetClear.dxf')
	oldX,oldY=drawPoolPiecesNumeredWhite(drawing,p0x,p0y,radArcMin,40,8,space)
	oldX,oldY=shiftNextLine(oldX,oldY,radArcMin,20,4,1,radArcMin * 11,p0x)
	oldX,oldY=drawPoolPiecesCommandsWhite(drawing,oldX,oldY,radArcMin,10,2,space)
	drawing.save()

def drawSheetWhiteColour():
	p0x=10.0
	p0y=10.0
	drawing = dxf.drawing('sheetClear.dxf')
	oldX,oldY=drawPoolPiecesNumered(drawing,p0x,p0y,radArcMin,40,8,space)
	oldX,oldY=shiftNextLine(oldX,oldY,radArcMin,20,4,1,radArcMin * 11,p0x)
	oldX,oldY=drawPoolPiecesCommandsWhite(drawing,oldX,oldY,radArcMin,10,2,space)
	drawing.save()

def creaTroncoCono(drawing,anguloIni,anguloFin,base,altura,colorLine3):
	dibujaArcoRelojColoreado(drawing,centroX,centroY,base,anguloIni,anguloFin,colorLine3)
	dibujaArcoRelojColoreado(drawing,centroX,centroY,altura,anguloIni,anguloFin,colorLine3)
	px0,py0 = damePtoArcoReloj(centroX,centroY,anguloIni,base)
	pxd,pyd = damePtoArcoReloj(centroX,centroY,anguloFin,base)
	px0a,py0a = damePtoArcoReloj(centroX,centroY,anguloIni,altura)
	pxda,pyda = damePtoArcoReloj(centroX,centroY,anguloFin,altura)
	drawLineColoured(drawing, px0, py0, px0a,  py0a, colorLine3)
	drawLineColoured(drawing, pxd, pyd, pxda,  pyda, colorLine3)
	drawing.save()
	return px0,py0,pxd,pyd,px0a,py0a,pxda,pyda

def creaTroncoConoSolido(drawing,anguloIni,anguloFin,base,altura,colorLine3):
	px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoCono(drawing,anguloIni,anguloFin,base,altura,colorLine3)
	for i in range(base, altura):
		dibujaArcoRelojColoreado(drawing,centroX,centroY,i,anguloIni,anguloFin,colorLine3)
		k=0
		for j in range(0, 8):
			k=k+0.1
			dibujaArcoRelojColoreado(drawing,centroX,centroY,i+k,anguloIni,anguloFin,colorLine3)
		drawing.save()
	return px0,py0,pxd,pyd,px0a,py0a,pxda,pyda

def main():
	anguloIni=30
	anguloFin=60
	base=40
	altura=80
	anguloIni1=60
	anguloFin1=100
	base1=40
	altura1=60
	drawing = dxf.drawing('curriculo.dxf')
	px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoConoSolido(drawing,anguloIni,anguloFin,base,altura,colorLine3)
	px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoConoSolido(drawing,anguloIni1,anguloFin1,base1,altura1,colorLine2)
	# px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoCono(drawing,anguloIni,anguloFin,base,altura,colorLine3)
	# px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoCono(drawing,anguloIni1,anguloFin1,base1,altura1,colorLine2
	#--------------------------------
	writeTextNoAling(drawing,'universidad',px0,py0,12,5,currentLayer,0)
	escribeEnArco(drawing,'universidad',centroX,centroY,base,anguloIni,anguloFin,colorLine,5)
	drawing.save()
	#-----------------------------------------------------------------
	# msize, nsize = (altura-base,altura-base)

	# mesh = dxf.polymesh(msize, nsize)
	# delta = math.pi / msize
	# for x in range(msize):
		# sinx = math.sin(float(x)*delta)
		# for y in range(nsize):
			# cosy = math.cos(float(y)*delta)
			# z = sinx * cosy * 3.0
			# mesh.set_vertex(x, y, (x,y,z))
	# drawing.add(mesh)
	#----------------------------
	# solid = dxf.solid([(px0,py0), (pxd,pyd),  (pxda,pyda) ,(px0a,py0a)], color=2)
	# solid['layer'] = 'solids'
	# solid['color'] = 7
	# drawing.add(solid)
	# drawing.save()
	#------------------------------------
	# solid = dxf.solid([(px0,py0), (pxd,pyd), (px0a,py0a)], color=1)
	# solid['layer'] = 'solids'
	# solid['color'] = 7
	# drawing.add(solid)
#	drawing.add_layer(currentLayer, color=colorT)
#-------------------------
	# polyline= dxf.polyline(linetype='CONTINUOUS')
	# polyline.add_vertices( [(px0,py0), (pxd,pyd),  (pxda,pyda) ,(px0a,py0a),(px0,py0)] )
	# drawing.add(polyline)
	# drawing.save()
#-------------------------



if __name__ == '__main__' : main()
