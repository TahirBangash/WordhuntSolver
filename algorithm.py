import dictionary

bank=[]
count=1
previous=[]
word=""
noncons=["a","e","i","o","u","y","s"]
cons=0
vow=0
vowle=["a","e","i","o","u"]


def formGrid(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
  row1 = [a+str(0),b+str(1),c+str(3),d+str(3)]
  row2=[e+str(4),f+str(5),g+str(6),h+str(7)]
  row3=[i+str(8),j+str(9),k+str(10),l+str(11)]
  row4=[m+str(12),n+str(13),o+str(14),p+str(15)]
  node=[row1,row2,row3,row4]
  return (node)



def adjacencyList(grid):
  adjNodes = []
  list = []
  for i in range(4):
    for j in range(4):
      if i > 0: adjNodes.append(grid[i - 1][j])
      if i < 3: adjNodes.append(grid[i + 1][j])
      if j > 0: adjNodes.append(grid[i][j - 1])
      if j < 3: adjNodes.append(grid[i][j + 1])
      if (i > 0 and j > 0): adjNodes.append(grid[i - 1][j - 1])
      if (i < 3 and j < 3): adjNodes.append(grid[i + 1][j + 1])
      if (j > 0 and i < 3): adjNodes.append(grid[i + 1][j - 1])
      if (j < 3 and i > 0): adjNodes.append(grid[i - 1][j + 1])
      list.append(adjNodes)
      adjNodes = []
  return (list)


def paths(start, list, len):
  global bank, count, previous, word, cons, noncons, vow, vowle
  for i in list[start]:
    if (i not in previous):
      word += str(i[0])
      count += 1
      if count == len:
        if(dictionary.dictionary.get(word.upper(),False)):
          if word not in bank:
            bank.append(word)
            #print(word,start)
        word = word[:-1]
        count -= 1
      else:
        previous.append(i)
        paths(int(str(i[1:])), list, len)
        word = word[:-1]
        previous.pop()
        count -= 1
        # if i[0] in vowle:
        #   vow-=1
        # if i[0] not in noncons:
        #   cons-=1

def calculate(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    global bank,count,word,previous
    bank=[]
    grid = formGrid(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
    list = (adjacencyList(grid))
    order = [10,9,8,7,6,5]
    for len in order:
        for c in range(16):
            word = grid[int(c / 4)][c % 4][0]
            previous = [grid[int(c / 4)][c % 4]]
            paths(c, list, len)
    return bank
#calculate('aretllonsdaeings')