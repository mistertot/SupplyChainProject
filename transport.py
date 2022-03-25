from re import findall



def recup_transport(instance: str):
    
    fichier = instance + '-transport.txt'
    with open(fichier, 'r') as f:
        n = int(findall('\d+', instance)[0])
        cpt = 0
        capacites = []
        couts = []
        for line in f:
            helpvar = line.split(' ')
            if cpt < n:
                for i in range(n):
                    capacites.append(int(helpvar[i]))
            else:
                for i in range(n):
                    couts.append(float(helpvar[i]))
            cpt += 1
        helplist = [(capacites[i], couts[i]) for i in range(n*n)]
        data = [helplist[i:i + n] for i in range(0, n*n, n)]
        return(data)





class Transport:
    def __init__(self, instance: str, site_i: int, site_j : int ) -> None:
        donnes = recup_transport(instance)
        self.data = donnes[site_i-1][site_j-1]
        self.site_i = site_i
        self.site_j = site_j
        
    def __repr__(self) -> str:
        return " sites {2}_{3} ( capacite : {0}, cout : {1} ) ".format(self.data[0], self.data[1], self.site_i, self.site_j)
    
    

'''a = Transport('inst\B6b', 1, 3)
b = Transport('inst\B6b', 1, 4)
c = Transport('inst\B7a', 1, 4)
print(a,c, sep = '\n')'''
a = recup_transport('inst\B6b')
print(a)
#b=sorted(a, key=lambda x: x[1])
#print(b)

