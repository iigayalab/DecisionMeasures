import pandas
import numpy
import seaborn
from matplotlib import pyplot

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

for number_of_clusters in range(2, 21):
    filename = "/Users/anusha/Downloads/w_"+str(number_of_clusters)+".csv"
    w = pandas.read_csv(filename)
    w = w.drop('Unnamed: 0', axis=1)

    seaborn.heatmap(w, yticklabels=ques_params)
    pyplot.title("Number of clusters="+str(number_of_clusters))
    pyplot.show()
