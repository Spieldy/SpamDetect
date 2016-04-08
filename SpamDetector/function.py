import csv

class Normalizer(object):

    def show_matrix_dataset(self, data_matrix):
        print("Show matrix dataset")
        for row in data_matrix:
            print(row)

    def load_txt(self, data_file):

        data_matrix = []

        data_tmp = open(data_file,'r')
        data = data_tmp.read()
        row_length=0
        for row in data:
            if (len(row) == row_length):#otherwise remove void lines
                data_matrix.append(row)
        data.close()
        return data_matrix

