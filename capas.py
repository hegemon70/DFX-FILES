


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
'''
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
'''

def escribeEnArcoCapa(draw,texto,centroX,centroY,base,anguloIni,anguloFin,color,tamFte,capa,espejo=0,rotacion=0):
#pre: espejo valor 0,1,2
#post: espejo=0 sin mirror, espejo=1 con mirror en X, espejo=2 con mirror en Y

	text = dxf.mtext(texto,(centroX,centroY))
	text.layer = capa
	text.color = color
	text.height = tamFte
	text.rotation = rotacion
	if (espejo != 0):
		if (espejo == 1):
			text.mirror = dxfwrite.MIRROR_X
		else:
			text.mirror = dxfwrite.MIRROR_Y
	draw.add(text)
	draw.save()

def dibujaArcoRelojColoreadoCapa(draw,centroX,centroY,base,anguloIni,anguloFin,colorLine2,capa): 
	angI=traduceElAnguloRelojATrigonometria(anguloIni)
	angF=traduceElAnguloRelojATrigonometria(anguloFin)
	drawArcColouredLayer(draw,centroX,centroY,base,angF,angI,colorLine2,capa)
 
def dibujaArcoRelojColoreado(draw,centroX,centroY,base,anguloIni,anguloFin,colorLine2): 
	angI=traduceElAnguloRelojATrigonometria(anguloIni)
	angF=traduceElAnguloRelojATrigonometria(anguloFin)
	drawArcColoured(draw,centroX,centroY,base,angF,angI,colorLine2)

# def dibujaArcoRelojColoreadoGrueso(draw,centroX,centroY,base,anguloIni,anguloFin,colorLine2,grosor):
	# angI=traduceElAnguloRelojATrigonometria(anguloIni)
	# angF=traduceElAnguloRelojATrigonometria(anguloFin)
	# drawArcColouredWithThickness(draw,centroX,centroY,base,angF,angI,colorLine2,grosor)

# def drawArcColouredWithThickness(draw, pxCentre, pyCentre, radio, AngIni, AngEnd,colorA,thickness):
	# arcx = dxf.arc(radio, (pxCentre,pyCentre), AngIni, AngEnd)
	# arcx['color'] = colorA
	# arcx['thickness'] = thickness
	# draw.add(arcx)
	# draw.add_layer(currentLayer, color=colorA)

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

def drawArcColouredLayer(draw, pxCentre, pyCentre, radio, AngIni, AngEnd, colorA, capa):
	arcx = dxf.arc(radio, (pxCentre,pyCentre), AngIni, AngEnd)
	arcx['color'] = colorA
	arcx['layer'] = capa
	draw.add(arcx)
	draw.add_layer(capa, color=colorA)
	#set value
	draw.header['$ANGBASE'] = 90.0
	draw.header['$ANGDIR'] = 1
	#get value
	contrareloj = draw.header['$ANGDIR'].value
	print ('el valor de direccion del Angulo es: ',contrareloj)
	anguloBase = draw.header['$ANGBASE'].value
	print ('elvalor del angulo base es:',anguloBase)

def drawCircleColoured(draw,radio,pxCentre,pyCentre,colorA):
	circlex = dxf.circle(radio, (pxCentre,pyCentre))
	circlex['color']=colorA
	draw.add(circlex)

def drawCircleColouredLayer(draw,radio,pxCentre,pyCentre,colorA,capa):
	circlex = dxf.circle(radio, (pxCentre,pyCentre))
	circlex['layer'] = capa
	circlex['color'] = colorA
	draw.add(circlex)
	draw.add_layer(capa, color=colorA)


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

def drawLineColouredLayer(draw, pxOrig, pyOrig, pxDstn, pyDstn, colorL,capa):
	linex = dxf.line((pxOrig, pyOrig), (pxDstn, pyDstn))
	linex['color'] = colorL
	draw.add(linex)
	draw.add_layer(capa, color=colorL)
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


def creaTroncoConoCapa(drawing,anguloIni,anguloFin,base,altura,colorLine3,capa):
	dibujaArcoRelojColoreadoCapa(drawing,centroX,centroY,base,anguloIni,anguloFin,colorLine3,capa)
	dibujaArcoRelojColoreadoCapa(drawing,centroX,centroY,altura,anguloIni,anguloFin,colorLine3,capa)
	px0,py0 = damePtoArcoReloj(centroX,centroY,anguloIni,base)
	pxd,pyd = damePtoArcoReloj(centroX,centroY,anguloFin,base)
	px0a,py0a = damePtoArcoReloj(centroX,centroY,anguloIni,altura)
	pxda,pyda = damePtoArcoReloj(centroX,centroY,anguloFin,altura)
	drawLineColouredLayer(drawing, px0, py0, px0a,  py0a, colorLine3,capa)
	drawLineColouredLayer(drawing, pxd, pyd, pxda,  pyda, colorLine3,capa)
	drawing.save()
	return px0,py0,pxd,pyd,px0a,py0a,pxda,pyda

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

def creaTroncoConoSolidoCapa(drawing,anguloIni,anguloFin,base,altura,colorLine3,capa):
	px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoConoCapa(drawing,anguloIni,anguloFin,base,altura,colorLine3,capa)
	for i in range(base, altura):
		dibujaArcoRelojColoreadoCapa(drawing,centroX,centroY,i,anguloIni,anguloFin,colorLine3,capa)
		k=0
		for j in range(0, 8):
			k=k+0.1
			dibujaArcoRelojColoreadoCapa(drawing,centroX,centroY,i+k,anguloIni,anguloFin,colorLine3,capa)
		drawing.save()
	return px0,py0,pxd,pyd,px0a,py0a,pxda,pyda

def main():
	anguloIni=0
	anguloFin=300
	base=40
	altura=80
	anguloIni1=60
	anguloFin1=100
	base1=40
	altura1=60
	drawing = dxf.drawing('capa.dxf')
	drawCircleColouredLayer(drawing,80,105,148.5,1,currentLayer)
	drawCircleColouredLayer(drawing,40,105,148.5,2,'sector1')
	drawArcColouredLayer(drawing,105,148.5,60,anguloIni,anguloFin,3,'sector2')
	escribeEnArcoCapa(drawing,'adios',105,148.5,base,anguloIni,anguloFin,colorLine3,24.0,currentLayer,2,254.0)
#set value
#	drawing.header['$ANGBASE'] = 90
#	drawing.header['$ANGDIR'] = 1
	#px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoConoSolidoCapa(drawing,anguloIni,anguloFin,base,altura,colorLine3,'sector1')
	#px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoConoSolidoCapa(drawing,anguloIni1,anguloFin1,base1,altura1,colorLine2,'sector2')
	# px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoCono(drawing,anguloIni,anguloFin,base,altura,colorLine3)
	# px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoCono(drawing,anguloIni1,anguloFin1,base1,altura1,colorLine2
	#--------------------------------
	#writeTextNoAling(drawing,'universidad',px0,py0,12,5,currentLayer,0)
	#escribeEnArco(drawing,'universidad',centroX,centroY,base,anguloIni,anguloFin,colorLine,5)
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
