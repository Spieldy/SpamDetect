#import csv
#import sys
#import os
#from math import sqrt

import csv
import math

class Normalizer(object):

    def __init__(self):
        pass
    '''
    def __init__(self,dataset):
        self.load_csv(dataset)
        self.data_to_tab()
    '''
    def load_csv(self,s):
        iris_file=s
        iris_data= open(iris_file,'r')
        self.data=csv.reader(iris_data)
        self.data_to_tab()
        return self.myTab

    def data_to_tab(self):
        tab=[]
        for l in self.data:
            ligne=[]
            for c in l:
                try:
                    v=float(c)
                    ligne.append(v)
                except ValueError or TypeError:
                    ligne.append(c)
            if len(ligne)!=0:
                tab.append(ligne)
        self.myTab=tab

    def get_col(self,tab,x):
        t=[]
        for l in tab:
            t.append(l[x])
        return t

    def max(self,data):
        max=data[0]
        for l in data:
            if max<l:
                max=l
        return max

    def min(self,data):
        min=data[0]
        for l in data:
            if min>l:
                min=l
        return min

    def normalize_col(self,col, min, max,Min,Max):
        t=[]
        for l in col:
            t.append((math.fabs(max)+math.fabs(min))*(l-Min)/(Max-Min)-math.fabs(min))
        return t

    def normalization(self):
        i=0
        res=[]
        while i < 58:
            colonne=self.get_col(self.myTab, i)
            max=self.max(colonne)
            min=self.min(colonne)
            res.append(self.normalize_col(colonne, 0, 1.0, min, max))
            i+=1
        return res;

    def moyenne(self,tableau):
        return sum(tableau, 0.0) / len(tableau)

    def variance(self,tableau):
        m=self.moyenne(tableau)
        return self.moyenne([(x-m)**2 for x in tableau])

    def ecartype(self,tableau):
        return self.variance(tableau)**0.5

    def stats(self,spam,nospam):
    #def stats(self,spam):
        stat = []
        s =[]
        ns=[]
        tab_avg = []
        tab_min = []
        tab_max = []
        tab_et=[]
        for l in spam:
            tab_avg.append(self.truncate(self.moyenne(l),5))
            tab_et.append(self.truncate(self.ecartype(l),5))
            tab_max.append(self.truncate(self.max(l),5))
            tab_min.append(self.truncate(self.min(l),5))
            '''
            tab_avg.append(self.moyenne(l))
            tab_et.append(self.ecartype(l))
            tab_max.append(self.max(l))
            tab_min.append(self.min(l))
            '''
        s.append(tab_min)
        s.append(tab_max)
        s.append(tab_avg)
        s.append(tab_et)
        stat.append(s)
        tab_avg = []
        tab_min = []
        tab_max = []
        tab_et=[]
        for l in nospam:
            tab_avg.append(self.truncate(self.moyenne(l),5))
            tab_et.append(self.truncate(self.ecartype(l),5))
            tab_max.append(self.truncate(self.max(l),5))
            tab_min.append(self.truncate(self.min(l),5))
        ns.append(tab_min)
        ns.append(tab_max)
        ns.append(tab_avg)
        ns.append(tab_et)
        stat.append(ns)
        return stat

    def split(self,data):
        res = []
        data_spam =[]
        data_nospam =[]
        for j in range(len(data)):
            ligneSpam=[]
            ligneNonSpam=[]
            for i in range(len(data[57])):
                if(data[57][i] == 1.0):
                    ligneSpam.append(data[j][i])
                else:
                    ligneNonSpam.append(data[j][i])
            data_spam.append(ligneSpam)
            data_nospam.append(ligneNonSpam)
        res.append(data_spam)
        res.append(data_nospam)
        return res

    def truncate(self, f, n):
        '''Truncates/pads a float f to n decimal places without rounding'''
        s = '%.5f' % f
        i, p, d = s.partition('.')
        return '.'.join([i, (d+'0'*n)[:n]])

    def get_splitedData(self,champs):
        spams =[]
        nospams = []
        for j in range(len(self.myTab)):
            ligne=[]
            for k in champs:
                ligne.append(self.myTab[j][k])
            if(self.myTab[j][57]==1.0):
                spams.append(ligne)
            else:
                nospams.append(ligne)
        res =[]
        res.append(spams)
        res.append(nospams)
        return res

if __name__ == '__main__':
    norm = Normalizer('dataset/spambase.data.txt')
    champs = [0,1,2]
    normalizedData = norm.normalization()
    normSplitedData = norm.split(normalizedData)
    normNospams = normSplitedData[1]
    normSpams = normSplitedData[0]
    splitedData = norm.get_splitedData(champs)
    spams = splitedData[0]
    nospams = splitedData[1]
    print "@@@@@@@@@@@@@@@@@@@@@ SPAMS @@@@@@@@@@@@@@@@@@@@@"
    for s in spams:
        print s
    print "@@@@@@@@@@@@@@@@@@@@@ NO SPAMS @@@@@@@@@@@@@@@@@@@@@"
    for s in nospams:
        print s
    '''
    iris_file="../../../../../datasets/spambase.csv"
    iris_data= open(iris_file,'r')
    data=csv.reader(iris_data)
    tab=[]
    for l in data:
        ligne=[]
        for c in l:
            try:
                v=float(c)
                ligne.append(v)
            except ValueError or TypeError:
                ligne.append(c)
        if len(ligne)!=0:
            tab.append(ligne)
    data=[]
    i=0
    while i < 58:
        colonne=norm.get_col(tab, i)
        data.append(colonne)
        i+=1
    stat = norm.stats(data)'''
    stat = norm.stats(normSpams,normNospams)
    print("STATS SPAM")
    for s in stat[0]:
        print s
    print("STATS NO SPAM")
    for s in stat[1]:
        print s



'''
class Normalizer(object):

    def load_csv(self, data_path):
        file = data_path
        data_file = open(file, 'r')
        data = csv.reader(data_file)
        return data

    @staticmethod
    def min_data_col(data, length):
        mins = [float(sys.maxsize)]*length
        for k in range(length):
            for d in data:
                if(mins[k] > float(d[k])):
                    mins[k] = float(d[k])
        return mins

    @staticmethod
    def max_data_col(data, length):
        maxs = [float(-sys.maxsize-1)]*length
        for k in range(length):
            for d in data:
                if(maxs[k] < float(d[k])):
                    maxs[k] = float(d[k])
        return maxs

    def normalization(self, data_save, min_range, max_range, length):
        mins = self.min_data_col(data_save, length)
        maxs = self.max_data_col(data_save, length)

        for i in range(length):
            for nb in range(len(data_save)):
                data_save[nb][i] = ((float(data_save[nb][i])-mins[i])/(maxs[i]-mins[i]))*(max_range-min_range)+min_range

        return data_save

    def statistics(self, data, nb_col):
        stats = []
        stats_spam = [[] for x in range(4)]
        stats_nospam = [[] for x in range(4)]
        data_spam = []
        data_nospam = []
        col_spam = 57
        nb_data = 0.0
        nb_data_spam = 0.0
        nb_data_nospam = 0.0
        min_spam = [99999]*nb_col
        min_nospam = [99999]*nb_col
        max_spam = [0]*nb_col
        max_nospam = [0]*nb_col
        avg_spam = [0]*nb_col
        avg_nospam = [0]*nb_col
        std_spam = [0]*nb_col
        std_nospam = [0]*nb_col

        for d in data:
            nb_data += 1
            if(float(d[col_spam]) == 1.0):
                data_spam.append(d)
            else:
                data_nospam.append(d)

        #calcul du min et max
        for d in data_spam:
            nb_data_spam += 1
            for i in range(nb_col):
                if(min_spam[i] > float(d[i])):
                    min_spam[i] = float(d[i])
                if(max_spam[i] < float(d[i])):
                    max_spam[i] = float(d[i])
                avg_spam[i] += float(d[i])

        for d in data_nospam:
            nb_data_nospam += 1
            for i in range(nb_col):
                if(min_nospam[i] > float(d[i])):
                    min_nospam[i] = float(d[i])
                if(max_nospam[i] < float(d[i])):
                    max_nospam[i] = float(d[i])
                avg_nospam[i] += float(d[i])

        #calcul de la moyenne
        for i in range(nb_col):
            avg_spam[i] = avg_spam[i]/nb_data
            avg_nospam[i] = avg_nospam[i]/nb_data

        #calcul de l'ecart-type
        for d in data_spam:
            for i in range(nb_col):
                std_spam[i] += (float(d[i])-avg_spam[i])**2

        for d in data_nospam:
            for i in range(nb_col):
                std_nospam[i] += (float(d[i])-avg_nospam[i])**2

        for i in range(nb_col):
            std_spam[i] = sqrt((1/nb_data)*std_spam[i])
            std_nospam[i] = sqrt((1/nb_data)*std_nospam[i])

        for i in range(nb_col):
            stats_spam[0].append("%.5f" % min_spam[i])
            stats_spam[1].append("%.5f" % max_spam[i])
            stats_spam[2].append("%.5f" % avg_spam[i])
            stats_spam[3].append("%.5f" % std_spam[i])

            stats_nospam[0].append("%.5f" % min_nospam[i])
            stats_nospam[1].append("%.5f" % max_nospam[i])
            stats_nospam[2].append("%.5f" % avg_nospam[i])
            stats_nospam[3].append("%.5f" % std_nospam[i])

        stats.append(stats_spam)
        stats.append(stats_nospam)

        return stats

    def __init__(self):
        pass

if __name__ == '__main__':
    norm = Normalizer()
    data_save = []
    workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
    data = norm.load_csv(os.path.join(workpath, 'dataset/spambase.data.txt'))
    for line in data:
        try:
            data_save.append(line)
        except IndexError:
            pass

    data_normalized = norm.normalization(data_save, 0.0, 1.0, 58)
    stats = norm.statistics(data_normalized, 58)

    print("SPAM")
    for s in stats[0]:
        print s
    print("NO SPAM")
    for s in stats[1]:
        print s
'''
