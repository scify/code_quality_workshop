myascii = 'ABCDEFGHIJKLMNOPQRSTUVXYWZ'
freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

#sinartisi pou pairnei ena text ws eisodo kai epistrefei to index of coincidence
def ic(txtinput):
	d = 0.0
	txtlen = len(txtinput)
	for a in myascii:
		c=txtinput.count(a)
		d+= c*(c-1.0)/(txtlen*(txtlen-1.0))
	return d

#sinartisi pou pairnei ena text ena megethos kleidiou kai to megethos tou text kai epistrefei to meso oro tou index of coincidence gia to dedomeno megethos kleidiou. vriskei diladi to index of coincidence twn N text pou prokiptoun an xwrisoume se N meri to arxiko keimeno kai epistrefei to meso oro tous
def av_ic(ortxt,key_l,txtlen):
	k=0
	m=0
	while k<key_l:
		i=k
		txt=[]
		while i<txtlen:
			txt.append(ortxt[i])
			i+=key_l
		#print(txt)
		m+=ic(txt)
		k+=1
	return m/key_l

#vriskei to megethos kleidiou pou megistopoiei to meso oro tou index of coincidence
def find_best_match(read_data):
	y = sum_freq(freq)
	x = len(read_data)
	best_diff = 10
	for i in range(1,11):
		d = av_ic(read_data, i,x)
		if abs(y-d)<best_diff:
			key_l = i
			best_diff = abs(y-d)

	return key_l

#sinartisi pou athroizei ta tetragwna mias listas apo arithmous
def sum_freq(freq):
	m=0
	for a in freq:
		m+=a*a
	return m
#sinartisi pou vriskei to chi-squared statistic pou ekfrazei poso omoies einai 2 katanomes pithanotitas

def find_chi_sq(txtinput):
	txtlen = len(txtinput)
	d=0
	for a in myascii:
		c=txtinput.count(a)
		myfreq = txtlen*freq[ord(a)-65]
		d+=(c-myfreq)*(c-myfreq)/(myfreq)
	return d

#kanei rotate ta grammata tou keimenou kata rotation theseis (encrypt me kaisara)
def rotate(rotation,txt):
	x=''
	for a in txt:
		y = ord (a)+rotation
		if y>90:
			y = y-26
		x=x+ chr(y)
	return x

#xrisimopoioume to chi-squared statistic gia na vroume to rotation gia to opoio auto elaxistopoieite. to rotation auto antistoixei sto pio pithano gramma tou kleidiou gia tin ipo eksetasi thesi
def find_letter(txtinput):
	best_fit = find_chi_sq(txtinput)
	for a in myascii:
		rotation = ord(a)-65
		rotated_txt=rotate(rotation,txtinput)
		x = find_chi_sq(rotated_txt)
		if x<best_fit:
			best_fit = x
			best_rot = a
	return best_rot

#ftiaxnei key_l ipolistes kai efarmozei tin find_letter gia na vrei olokliro kleidi
def find_word(txt,key_l):
	k=0
	x=''
	txtlen = len(txt)
	while k<key_l:
		i=k
		ctxt=[]
		while i<txtlen:
			ctxt.append(txt[i])
			i+=key_l
		#print(ctxt)
		x=x+find_letter(ctxt)
		k+=1
	return x

#pairnei to arxiko kriptografimeno keimeno to kleidi pou vrikame kai epistrefei to pithano plaintext
def decrypt(txt,key):
	out=''
	i=0
	keylen = len(key)
	for a in txt:
		i = i%keylen
		y = ord(a)+ord(key[i])-65
		i+=1
		if y>90:
			y=y-26
		out=out+chr(y)
	return out

#kiria sinartisi pou kalei tis ipolipes
def analyze():
	with open('test.txt','r') as f:
		new_str = f.read()
	f.closed
	x = len(new_str)-1
	read_data = new_str[:x]
	key_l = find_best_match(read_data)
	word = find_word(read_data,key_l)
	print(word)
	final=decrypt(read_data,word)
	print(final)
	return 0

if __name__ == '__main__':
    analyze()
