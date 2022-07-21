import pandas as pd
import numpy as np

freq_scores = pd.read_csv('prostateSNP_chances.csv')
alleles = freq_scores['rs*'].to_list()
rng = np.random.default_rng()
df_rows = []
for i in range(25000):
    current_row=[]
    for row in freq_scores.itertuples():
        array = []
        array = rng.integers(1000, size = (1,2))
        if array.flat[0] < row.European_bound and array.flat[1] < row.European_bound:
            allele_freq = 1.0
        elif array.flat[0] < row.European_bound or array.flat[1] < row.European_bound:
            allele_freq = 0.5
        else:
            allele_freq = 0
        current_row.append(allele_freq)
    df_rows.append(list(current_row))
european_genomes = pd.DataFrame(df_rows, columns = [alleles])
european_genomes.to_csv('european_genomes_269.csv', index = False)

df_rows = []
for i in range(25000):
    current_row=[]
    for row in freq_scores.itertuples():
        array = []
        array = rng.integers(1000, size = (1,2))
        if array.flat[0] < row.African_bound and array.flat[1] < row.African_bound:
            allele_freq = 1.0
        elif array.flat[0] < row.African_bound or array.flat[1] < row.African_bound:
            allele_freq = 0.5
        else:
            allele_freq = 0
        current_row.append(allele_freq)
    df_rows.append(list(current_row))
African_genomes = pd.DataFrame(df_rows, columns = [alleles])
African_genomes.to_csv('african_genomes_269.csv', index = False)

df_rows = []
for i in range(25000):
    current_row=[]
    for row in freq_scores.itertuples():
        array = []
        array = rng.integers(1000, size = (1,2))
        if array.flat[0] < row.East_Asian_bound and array.flat[1] < row.East_Asian_bound:
            allele_freq = 1.0
        elif array.flat[0] < row.East_Asian_bound or array.flat[1] < row.East_Asian_bound:
            allele_freq = 0.5
        else:
            allele_freq = 0
        current_row.append(allele_freq)
    df_rows.append(list(current_row))
East_Asian_bound_genomes = pd.DataFrame(df_rows, columns = [alleles])
East_Asian_bound_genomes.to_csv('East_Asian_genomes_269.csv', index = False)

df_rows = []
for i in range(25000):
    current_row=[]
    for row in freq_scores.itertuples():
        array = []
        array = rng.integers(1000, size = (1,2))
        if array.flat[0] < row.Hispanic_bound and array.flat[1] < row.Hispanic_bound:
            allele_freq = 1.0
        elif array.flat[0] < row.Hispanic_bound or array.flat[1] < row.Hispanic_bound:
            allele_freq = 0.5
        else:
            allele_freq = 0
        current_row.append(allele_freq)
    df_rows.append(list(current_row))
Hispanic_bound_genomes = pd.DataFrame(df_rows, columns = [alleles])
Hispanic_bound_genomes.to_csv('hispanic_genomes_269.csv', index = False)