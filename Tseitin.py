


# '>' + '(' +v + O + w + ')' + 'Y' + '(' + v+O+w + ')' + '>' + Atomo

def Tseitin(A, LetrasProposicionalesA):
	#A una formula no tiene dobles negaciones, cadena de simbolos, y sus letras proposicionales estan en la lista letraspropA
#'>' + '-' + s + 'Y' + '-' + s + '>' + Atomo 
	
	LetrasProposicionalesB = []
	for i in range(0,100):
		LetrasProposicionalesB.append('x')
	L = [] # Conjunciones
	Pila = []
	I = -1
	s = A[0]
	while(len(A)>0):
		if(s in LetrasProposicionalesA and len(Pila)>0 and Pila[-1] == '-'):
			I+=1
			Atomo = LetrasProposicionalesB[I] + str(I)
			Pila = Pila[:-1]
			Pila.append(Atomo)
			L.append('(' + '-' + Atomo + 'O' + '-' + s + 'Y' + s + 'O' + Atomo + ')')
			#L.append('(' + Atomo + '<->' + '-' + s +')')
			A = A[1:]
			if(len(A)>0):
				s = A[0]
		elif(s == ')'):
			w = Pila[-1]
			O = Pila[-2]
			v = Pila[-3]
			Pila = Pila[:len(Pila)-4]
			I+=1
			Atomo = LetrasProposicionalesB[I] + str(I)
			L.append('(' + '-' + Atomo + 'O' + '(' + v+O+w + ')' + 'Y' + '-'  + '(' + v+O+w + ')' + 'O' + Atomo + ')')
			s = Atomo
		else:
			Pila.append(s)
			A = A[1:]
			if(len(A)>0):
				s = A[0]


	B = ''
	if(I<0):
		Atomo = Pila[-1]
	else:
		Atomo = LetrasProposicionalesB[I] + str(I)
	for X in L:
		Y = X
		B += 'Y' + Y
	B = Atomo + B
	return B
			

def Tclausulas(C):
	# C una clausula como lista de caracteres
	L = []
	s = C[0]
	while(len(C)>0):
		if(s == 'O'):
			C = C[1:]
		elif(s == '-'):
			literal = s + C[1]
			L.append(literal)
			C = C[2:]
		else:
			L.append(s)
			C = C[1:]
		if(len(C)>0):
			s = C[0]
	return L

def ObtClausal(A):
	#A, una formula en FNC como cadena de caracteres
	L = []
	i = 0
	while(len(A)>0):
		if(i <= len(A)):
			if(A[i] == 'Y'):
				L.append(Tclausulas(A[:i]))
				A = A[i+1:]
			else:
				i+=1
		else:
			break
	return L
			


LetrasProposicionalesA = ['p','q']
A = '(pYq)Y(pY-q)'



print(ObtClausal(Tseitin(A, LetrasProposicionalesA)))



"""
a = 'pOqY--aOb->kOl'

def negacion(a):
	a = a.replace('--', '')
	return a
	
negacion(a)

print(negacion(a))

"""

