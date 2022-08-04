import pandas
import numpy
import seaborn
from sklearn.decomposition import non_negative_factorization
from sklearn.decomposition import PCA
from matplotlib import pyplot

dataset = pandas.read_csv('/Users/anusha/Downloads/Dataset_factors_ques_decParams.csv')
dataset = dataset.drop('Unnamed: 0', axis=1)

ques_params = [
    'sex',
    'age hqp done',
    'mfqtot',
    'rcmastot',
    'loitot',
    'loi_compulsions',
    'loi_obsessions',
    'loi_cleanliness',
    'behtot',
    'selftot',
    'k10total',
    'apsdtotal',
    'apsd_narc',
    'apsd_imp',
    'apsd_callous',
    'cads_prosoc',
    'cads_negemot',
    'cads_daring',
    'spq_total',
    'spq_ideas',
    'spq_social',
    'spq_magic',
    'spq_perceptual',
    'spq_behaviour',
    'spq_friends',
    'spq_speech',
    'spq_affect',
    'spq_paranoid',
    'spq_odd_self',
    'spq_social_diff',
    'spq_threat_perc',
    'wemwbs_total',
    'icutotal',
    'icu_unemotional',
    'icu_callous',
    'icu_uncaring',
    'bistotal',
    'bis_attention',
    'bis_motor',
    'bis_selfcont',
    'bis_cogcomplx',
    'bis_persevere',
    'bis_coginstab',
    'bis_att_imp',
    'bis_mot_imp',
    'bis_nonplan_imp',
    'fadtotal',
    'cfqtotal',
    'cfq_goodqual',
    'cfq_frienddiff',
    'apq_positive',
    'apq_inconsistent',
    'apq_poorsup',
    'apq_involve',
    'apq_punish',
    'mops_mat_indiff',
    'mops_mat_control',
    'mops_mat_abuse',
    'mops_pat_indiff',
    'mops_pat_control',
    'mops_pat_abuse',
    # 'Edinburgh Handedness score',
    'Vocabulary Raw Score',
    'Matrix Reasoning Raw Score',
    'IQ (Full-2)'
]

for col in ques_params:
    dataset[col] = dataset[col]/numpy.linalg.norm(dataset[col])

number_of_iterations = 10
sampling_fraction = 0.8
stable = []

for components in range(2, 21):
    print("Number of clusters="+str(components))
    consensus_matrix = pandas.DataFrame(0, index=dataset["nspnID"], columns=dataset["nspnID"], dtype=int)
    count_of_same_subsamples = pandas.DataFrame(0, index=dataset["nspnID"], columns=dataset["nspnID"], dtype=int)
    for iteration in range(number_of_iterations):
        print("Iteration number="+str(iteration))
        sampled_dataset = dataset.sample(frac=sampling_fraction, replace=False)
        sampled_dataset = sampled_dataset.reset_index(drop=True)
        w_and_h = non_negative_factorization(numpy.transpose(sampled_dataset[ques_params]), n_components=components, max_iter=20000, init='nndsvd')
        w = pandas.DataFrame(w_and_h[0])
        if iteration == 0:
            filename = "/Users/anusha/Downloads/w_"+str(components)+".csv"
            w.to_csv(filename)
        h = pandas.DataFrame(w_and_h[1])

        h_idxmax = h.idxmax()
        print(h_idxmax.value_counts())
        for i in range(len(h_idxmax)):
            for j in range(len(h_idxmax)):
                count_of_same_subsamples.loc[sampled_dataset.loc[i, 'nspnID'], sampled_dataset.loc[j, 'nspnID']] = count_of_same_subsamples.loc[sampled_dataset.loc[i, 'nspnID'], sampled_dataset.loc[j, 'nspnID']] + 1
                if h_idxmax[i] == h_idxmax[j]:
                    consensus_matrix.loc[sampled_dataset.loc[i, 'nspnID'], sampled_dataset.loc[j, 'nspnID']] = consensus_matrix.loc[sampled_dataset.loc[i, 'nspnID'], sampled_dataset.loc[j, 'nspnID']] + 1

        # Code snippet to plot the clusters with PC0 and PC1
        # pca = PCA(n_components=2)
        # ques_data = pandas.DataFrame(pca.fit_transform(sampled_dataset[ques_params]))
        # print(pca.explained_variance_ratio_)
        #
        # for i in range(len(h_idxmax)):
        #     pyplot.scatter(ques_data.loc[numpy.where(h_idxmax == i), 0], ques_data.loc[numpy.where(h_idxmax == i), 1])
        # pyplot.show()

    for i in range(len(consensus_matrix)):
        for j in range(len(consensus_matrix)):
            if count_of_same_subsamples.iloc[i, j] != 0:
                consensus_matrix.iloc[i, j] = consensus_matrix.iloc[i, j] / count_of_same_subsamples.iloc[i, j]

    consensus_matrix_filename = "/Users/anusha/Downloads/consensus_"+str(components)+".csv"
    consensus_matrix.to_csv(consensus_matrix_filename)

    # Code snippet to plot the total number of samples that have their values as 0 to 0.1 or 0.9 to 1.0
    # [counts, edges] = numpy.histogram(consensus_matrix.to_numpy().flatten(), bins=10)
    # stable.append(counts[0]+counts[len(counts)-1])
    # seaborn.heatmap(consensus_matrix.loc[consensus_matrix["nspnID"], consensus_matrix["nspnID"]])
    # pyplot.show()

# pyplot.plot(range(2, 21), stable)
# pyplot.show()
