def maxSequence(pinakas, i, a, j):
    sum_1 = 0;
    leftSum = -10000

    q = i - 1
    p = -1
    for n in range(a, q, p):
        sum_1 += pinakas[n]

        if (sum_1 > leftSum):
            leftSum = sum_1
    sum_1 = 0;
    rightSum = -1000

    x = a + 1
    y = j + 1
    for n in range(x, y):
        sum_1 += pinakas[n]

        if (sum_1 > rightSum):
            rightSum = sum_1

    totalSum = leftSum + rightSum
    return totalSum

def megistoSumIpoListas(pinakas, i, j):

    if (i == j):
        return pinakas[i]

    a = (i + j) // 2
    ola = max(megistoSumIpoListas(pinakas, i, a), megistoSumIpoListas(pinakas, a + 1, j), maxSequence(pinakas, i, a, j))

    return ola
o = int(input('Δώσε πλήθος αριθμών που θέλεις να δώσεις: '))
#pinakas=[i for i in range(0,o-1) int(input('Δώσε τους αριθμούς (π.χ 1,-1,0,10,....): '))]
pinakas=[]
for x in range(0, o):
    pinakas.append(int(input('Δώσε τους αριθμούς (π.χ 1,-1,0,10,....): ')))
megethos_pinaka = len(pinakas)
elegxos = megistoSumIpoListas(pinakas, 0, megethos_pinaka - 1)
plithos = 0
megisto=-9999999999999999999999999
lista=[]

i=0
for i in range(len(pinakas)):
    plithos+= pinakas[i]
    if plithos < 0:
        plithos = 0
        lista=[]
    elif plithos > 0:
        lista.append(pinakas[i])
    elif plithos < megisto:
        megisto = plithos

if lista==[]:
    lista.append(max(pinakas))
print('Το μέγιστο άθροισμα της λίστας που δώθηκε είναι ',elegxos,' και αύτο το δίνουν οι αριθμοί: ',lista)
