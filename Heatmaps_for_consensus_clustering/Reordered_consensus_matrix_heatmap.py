import pandas
import numpy
import seaborn
from matplotlib import pyplot

for number_of_clusters in range(2, 21):
    filename = "/Users/anusha/Downloads/consensus_"+str(number_of_clusters)+".csv"
    consensus_matrix = pandas.read_csv(filename)
    consensus_matrix = consensus_matrix.set_index(consensus_matrix["nspnID"])
    consensus_matrix.index.name = None
    consensus_matrix = consensus_matrix.drop('nspnID', axis=1)

    ID_array = []
    for id_ in consensus_matrix.columns:
        ID_array.append(id_)

    consensus_matrix = consensus_matrix.sort_values(by=ID_array, ascending=False)

    row_array = []
    for id_ in pandas.DataFrame(numpy.transpose(consensus_matrix)).columns:
        row_array.append(id_)

    consensus_matrix = pandas.DataFrame(numpy.transpose(pandas.DataFrame(numpy.transpose(consensus_matrix)).sort_values(by=row_array, ascending=False)))
    seaborn.heatmap(consensus_matrix)
    pyplot.title("Number of clusters="+str(number_of_clusters))
    pyplot.show()
