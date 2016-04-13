import csv
import random
import math
import os

class KMeanClusterer(object) :
    def __init__(self,k,datacsv, champs):
        self.k = k
        self.nb_champs = len(champs)
        iris_data=open(datacsv,'r')
        data=csv.reader(iris_data)
        tab=[]
        for l in data:
            cols=[]
            for i in champs:
                col=float(l[i])
                cols.append(col)
            #cols.append(l[57])
            if len(cols)!=0:
                tab.append(cols)
        self.myTab=tab
        self.cluster=[]
        self.initialisation()


    def getTab(self):
        return self.myTab

    def getClusterNumber(self):
        return self.k

    def getCluster(self,i):
        return self.cluster[i]

    def initialisation(self):
        n = []
        for i in range(self.k):
            nb = random.randint(0, len(self.myTab)-1)
            while n.__contains__(nb):
                nb = random.randint(0, len(self.myTab)-1)
            n.append(nb)
            c = Cluster(self.myTab[nb])
            self.cluster.append(c)
            #print c.getCentroid()

    def computeDistance(self,obs,c):
        #calcul distance entre deux points sur 4 dimensions
        d = 0.0
        for n in range(self.nb_champs):
            d = d + (((obs[n])-(c[n]))**2)
        d = math.sqrt(d)
        return d

    def plusProche(self,obs):
        min_dist=9999999.9
        cen_pproche= 0
        for k in range(self.k):
            cen = (self.getCluster(k)).getCentroid()
            dist = self.computeDistance(obs,cen)
            if(dist<min_dist):
                min_dist=dist
                cen_pproche=k

        return cen_pproche

    def assignement(self):

        for c in self.cluster:
            c.mvObservations()

        for i in self.myTab:
            pp = self.plusProche(i)
            (self.cluster[pp]).addPoint(i)

        redo = 0
        for c in self.cluster:
            new_centroid = [0]*self.nb_champs
            p = len(c.getPoints())
            if(p!=0):
                for i in c.getPoints():
                    for j in range(self.nb_champs):
                        new_centroid[j]+=i[j]
                for j in range(self.nb_champs):
                    new_centroid[j] = new_centroid[j]/p

                for j in range(self.nb_champs):
                    if(new_centroid[j]!=c.getCentroid()[j]):
                        c.setCentroid(new_centroid)
                        redo = 1

        if redo==1:
            self.assignement()



class Cluster(object) :

    def __init__(self,c):
        self.centroid=[]
        for i in range(len(c)):
            self.centroid.append(c[i])
        self.points = []

    def getCentroid(self):
        return self.centroid

    def setCentroid(self,c):
        self.centroid=[]
        for i in range(len(c)):
            self.centroid.append(c[i])

    def getObservations(self):
        return self.points

    def mvObservations(self):
        self.points =[]

    def addPoint(self,i):
        self.points.append(i)

    def getPoints(self):
        return self.points


if __name__ == '__main__':
    k = 2
    workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
    datafile = os.path.join(workpath, 'dataset/spambase.data.txt')
    champs = [5, 15, 45]
    kMeanClusterer = KMeanClusterer(k, datafile, champs)
    kMeanClusterer.assignement()

    for i in range(k):
        print kMeanClusterer.getCluster(i).getCentroid()
    for i in range(k):
        print kMeanClusterer.getCluster(i).getPoints()