import pandas as pd
import numpy as np
import copy 

def get_min_nmatrix(rnmatrix):
    list_nmatrix = [min(x, key=lambda df: df[1]) for x in rnmatrix]
    resmin = list_nmatrix[0]
    for kdx in range(1,len(list_nmatrix)):
        if resmin[7] > list_nmatrix[kdx][7]:
            resmin = list_nmatrix[kdx]
    return resmin

def get_max_nmatrix(rnmatrix):
    list_nmatrix = [max(x, key=lambda df: df[3]) for x in rnmatrix]
    resmax = list_nmatrix[0]
    for kdx in range(1,len(list_nmatrix)):
        if resmax[7] < list_nmatrix[kdx][7]:
            resmax = list_nmatrix[kdx]
    return resmax

def main(df_file):
    dfnp = df_file.to_numpy()

    matrix = []
    row = [dfnp[0]]
    rdx, idx = 0, 1
    while idx < len(dfnp):
        if row[rdx][7] == dfnp[idx][7]:
            row.append(dfnp[idx])
            rdx += 1  
        else:
            matrix.append(row)
            row = [dfnp[idx]]
            rdx = 0
        idx += 1
        if idx == len(dfnp) - 1:
            matrix.append(row)  
    for idx in range(len(matrix)):
        matrix[idx] = [matrix[idx]]

    nmatrix = [matrix[0]]
    idnmatrix = 0
    for idx in range(1,len(matrix)):
        rmin = get_min_nmatrix(nmatrix[idnmatrix])
        rnmax = get_max_nmatrix(matrix[idx])

        delta_r_rn = rmin[1] - rnmax[3]

        if delta_r_rn > 10:
            nmatrix.append(matrix[idx])
            idnmatrix = idnmatrix + 1
        else:
            nmatrix[len(nmatrix)-1].append(matrix[idx][0])  
            idnmatrix = len(nmatrix) - 1

    final_matrix = []

    nnmatrix = copy.deepcopy(nmatrix)
    for idx in range(len(nnmatrix)):
        submatrix = [[x[5] for x in nmatrix[idx][0]]]
        lnmatrix0 = len(nnmatrix[idx][0])
        for jdx in range(1,len(nnmatrix[idx])):
            none_list = [None]*lnmatrix0
            for kdx in range(len(nnmatrix[idx][jdx])):
                center =  (nnmatrix[idx][jdx][kdx][0] + nnmatrix[idx][jdx][kdx][2])/2
                r0dx = 0
                while r0dx < lnmatrix0: 
                    if center >= nnmatrix[idx][0][r0dx][0] and center <= nnmatrix[idx][0][r0dx][2]:
                        none_list[r0dx] = nnmatrix[idx][jdx][kdx][5]
                        break
                    r0dx = r0dx + 1
            submatrix.append(none_list)
        final_matrix.append(submatrix)
    
    return final_matrix