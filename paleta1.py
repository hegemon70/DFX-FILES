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

def posicionaTexto(angIni,angFin,xCenter,yCenter,radio):
	ang =(angIni+angFin)/2
	x,y = damePtoArcoReloj(xCenter,yCenter,ang,radio)
	return x,y

def dameGradosRotacionTexto(anguloIni,anguloFin):
	cuadIni=dameCuadrante(anguloIni)
	cuadFin=dameCuadrante(anguloFin)
	print ("el angulo de la bisectriz es ",(anguloIni+anguloFin)/2)
	angDef=((anguloIni+anguloFin)/2)+270.0
	if (cuadIni==1):
		if(cuadFin==4):#implica un angulo especial hay que decidir si es mas o menos que 0 grados
			print("caso especial ini cuadrante1, fin cuadrante4")
			angAux= 360.0 - anguloFin#con esto averiguo el angulo real a sumar
			print("angulo por debajo del eje x:",angAux)
			if (angAux==anguloIni):#si son iguales el angulo resultante es 0
				angDef=0.0
			else:#hay que calcular la bisectriz
				angAux = (angAux + anguloIni)/2#con esto sacamos la bisectriz de los dos angulos
				print("la bisectrix es:",angAux)
				if(angAux > anguloIni):#es un angulo negativo por debajo de 0
					angAux = angAux - anguloIni#esto es lo que sobra y hay que traducir a su opuesto
					angAux = 360.0 - angAux
					print("es el peor de los casos el angulo de la bisectrix es:",angAux)
				angDef=angAux+270.0
	if(angDef > 360.0):
		print ("resultado es un angulo mayor de 360")
		angDef = angDef - 360.0
	print ("el angulo de rotacion es:",angDef)
	return angDef

def escribeEnArcoCapa(draw,texto,xCenter,yCenter,anguloIni,anguloFin,radio,color,tamFte,capa,espejo=0):
#pre: espejo valor 0,1,2
#post: espejo=0 sin mirror, espejo=1 con mirror en X, espejo=2 con mirror en Y
#		anguloIni, anguloFin son angulos como el reloj desde las 12
	'''print ("este es el angulo inicial:",anguloIni)
	print ("este es el angulo final:",anguloFin)'''
	anIni = traduceElAnguloRelojATrigonometria(anguloIni)
	anFin = traduceElAnguloRelojATrigonometria(anguloFin)
	'''print ("este es el angulo calculo inicial:",anIni)
	print ("este es el angulo calculo final:",anFin)'''
	rot = dameGradosRotacionTexto(anIni,anFin)
#	print ("EL ANGULO DE ROTACION DEL TEXTO ES :",rot)
	pX,pY=posicionaTexto(anguloIni,anguloFin,xCenter,yCenter,radio)#importante el angulo es de reloj
	text = dxf.mtext(texto,(pX,pY))
	text.layer = capa
	text.color = color
	text.height = tamFte
	text.rotation = rot
	text.valign = dxfwrite.MIDDLE
	text.halign = dxfwrite.CENTER
	if (espejo != 0):
		if (espejo == 1):
			text.mirror = dxfwrite.MIRROR_X
		else:
			text.mirror = dxfwrite.MIRROR_Y
	draw.add(text)
	draw.save()
	print("escrito:",texto)

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

def damePtoArcoReloj(xCenter,yCenter,ang,radio):
#pre: x e y del cetro del arco
#una angulo en grados y un radio
#post: devuelve el otro punto extremo de la hipotenusa
	'''
	print ("el radio es: ",radio)
	print ("el anguloOriginal es:",ang) 
	'''
	ang=traduceElAnguloRelojATrigonometria(ang)
#	print ("el anguloReal es:",ang) 
	cuad=dameCuadrante(ang)
	'''
	print ("el cuadrante del angulo real es:",cuad)
	print ("este es el coseno de ang",math.cos(math.radians(ang)))
	print ("este es el seno de ang",math.sin(math.radians(ang)))
	'''
	a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
	b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
	if cuad==1:
		'''
		print ("este es el angulo de calculo",ang)
		print ("este es el coseno de ang",math.cos(math.radians(ang)))
		print ("este es el seno de ang",math.sin(math.radians(ang)))
		'''
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter + a
		yd=yCenter + b
	elif cuad==2:
		ang=180-ang#complementario
		'''
		print ("este es el angulo de calculo",ang)
		print ("este es el coseno de ang",math.cos(math.radians(ang)))
		print ("este es el seno de ang",math.sin(math.radians(ang)))
		'''
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter - a
		yd=yCenter + b
	elif cuad==3:
		ang=ang-180
		'''
		print ("este es el angulo de calculo",ang)
		print ("este es el coseno de ang",math.cos(math.radians(ang)))
		print ("este es el seno de ang",math.sin(math.radians(ang)))
		'''
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter - a
		yd=yCenter - b
	else:#cuad=4
		ang=360-ang
		'''
		print ("este es el angulo de calculo",ang)
		print ("este es el coseno de ang",math.cos(math.radians(ang)))
		print ("este es el seno de ang",math.sin(math.radians(ang)))
		'''
		a=math.cos(math.radians(ang))* radio #math.cos acepta radianes solo
		b=math.sin(math.radians(ang))* radio #math.sin acepta radianes solo
		xd=xCenter + a
		yd=yCenter - b
	'''
	print ("esto es el tamaño del lado adyacente:",a)
	print ("esto es el tamaño del lado opuesto:",b)
	'''
	return xd,yd



def creaTroncoConoCapa(drawing,centroX,centroY,anguloIni,anguloFin,base,altura,colorLine3,capa):
#prev: drawing un dxf.drawing valido
#post: dibuja un tronco cono y devuelve sus puntos extremos
#		px0,py0 es el punto inferior del angulo inicial
#		pxd,pyd es el punto inferior del angulo final
#		px0a,py0a es el punto superior del angulo inicial
#		pxda,pyda es el punto superior del anngulo inicial
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


def creaTroncoConoSolidoCapa(drawing,centroX,centroY,anguloIni,anguloFin,base,altura,colorLine3,capa):
	px0,py0,pxd,pyd,px0a,py0a,pxda,pyda=creaTroncoConoCapa(drawing,centroX,centroY,anguloIni,anguloFin,base,altura,colorLine3,capa)
	for i in range(base, altura):
		dibujaArcoRelojColoreadoCapa(drawing,centroX,centroY,i,anguloIni,anguloFin,colorLine3,capa)
		k=0
		for j in range(0, 8):
			k=k+0.1
			dibujaArcoRelojColoreadoCapa(drawing,centroX,centroY,i+k,anguloIni,anguloFin,colorLine3,capa)
		drawing.save()
	return px0,py0,pxd,pyd,px0a,py0a,pxda,pyda

def dibujaArcoRelojColoreadoCapa(draw,centroX,centroY,base,anguloIni,anguloFin,colorLine2,capa): 
	angI=traduceElAnguloRelojATrigonometria(anguloIni)
	angF=traduceElAnguloRelojATrigonometria(anguloFin)
	drawArcColouredLayer(draw,centroX,centroY,base,angF,angI,colorLine2,capa)

def traduceElAnguloRelojATrigonometria(angO):
#pre: el angulo que esta en ang0 se basa  en las 12 del reloj
#post: se devuelve el valor de un angulo correspondiente los angulos matematicos partiendo del eje X  hacia la izquierda
#360 + 90=450 
	angD=450 - angO
	if angD > 360:
		angD = angD -360
	if angD < 0:
		angD=360 + angD
	return angD

def drawArcColouredLayer(draw, pxCentre, pyCentre, radio, AngIni, AngEnd, colorA, capa):
	arcx = dxf.arc(radio, (pxCentre,pyCentre), AngIni, AngEnd)
	arcx['color'] = colorA
	arcx['layer'] = capa
	draw.add(arcx)
	draw.add_layer(capa, color=colorA)

def drawLineColouredLayer(draw, pxOrig, pyOrig, pxDstn, pyDstn, colorL,capa):
	linex = dxf.line((pxOrig, pyOrig), (pxDstn, pyDstn))
	linex['color'] = colorL
	linex['layer'] = capa
	draw.add(linex)
	draw.add_layer(capa, color=colorL)
	return pxDstn,pyDstn

def main():
	centroX = 1.0
	centroY = 10.0
	drawing = dxf.drawing('paleta1.dxf')
	for i in range(256):
		creaTroncoConoSolidoCapa(drawing,centroX,centroY,80.0,90.0,20,25,i,'paleta')
		escribeEnArcoCapa(drawing,str(i),centroX,centroY,80.0,90.0,20,1,3.0,'letras',0)
		centroY = centroY + 10.0
		if (i%25==0): #cada 25 
			centroX = centroX + 20 #salta a la derecha
		print ('imprimiendo:',i)
if __name__ == '__main__' : main()