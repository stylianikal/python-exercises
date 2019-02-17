#anigi to ario me onoma test.py 
fopen=open("test.py","r")
#diavase tis grames
gra=fopen.readlines()
fopen.close()

for gra in gra:
	if "#" in gra:
		g=gra.strip()
		#an arizei apo #
		if g[0]!="#": 
			#xorise tin grami 
			t=gra.split("#")
			#metrima " ' 
			p1=t[0].count('"')
			p2=t[0].count("'")
			#an einai monos arithmos eina mesa se protasi
			if  p1%2==1 or p2%2==1:
				print gra
			else:
				print gra.split("#")[0]
	else:
		print gra
