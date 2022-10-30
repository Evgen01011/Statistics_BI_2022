import pandas as pd
import numpy as np
import scipy.stats as st
from statsmodels.stats.weightstats import ztest


# Function for check intervals intersect
def check_intervals_intersect(first_ci, second_ci):
    list_ci = [first_ci, second_ci]                      # collect ci as list
    list_ci.sort()
    if list_ci[1][0] <= list_ci[0][1] <= list_ci[1][1]:  # compare max of smaller ci with bounders of bigger ci
        are_intersect = True
    else:
        are_intersect = False
    return are_intersect                                 # True or False


# Function for check expression with check intervals
def check_dge_with_ci(first_table, second_table):
    ci_test_results = []
    for col in first_table.columns[0:-1]:                                                # check every genes except last col - Cell Type
        first_ci_gene = st.t.interval(0.95,                                              # calculate first ci
                                      len(first_table[col]) - 1,
                                      loc=np.mean(first_table[col]),
                                      scale=st.sem(first_table[col]))
        second_ci_gene = st.t.interval(0.95,                                            # calculate second ci
                                       len(second_table[col]) - 1,
                                       loc=np.mean(second_table[col]),
                                       scale=st.sem(second_table[col]))
        ci_test_results.append(check_intervals_intersect(first_ci_gene, second_ci_gene))  # estimate intersection
    return ci_test_results


# Function for check expression with ztest
def check_dge_with_ztest(first_table, second_table):
    z_test_results = []
    for col in first_table.columns[0:-1]:
        ztest_param = ztest(first_table[col], second_table[col])          # ztesting of difference
        z_test_results.append(np.array(ztest_param)[1] < .05)             # compare p-value with threshold
    return z_test_results


# Function for measurement of mean difference
def dif_mean(first_table, second_table):
    dif_mean_results = []
    for col in first_table.columns[0:-1]:
        dif_mean_results.append(np.mean(first_table[col]) - np.mean(second_table[col]))
    return dif_mean_results


# Function for measurement of p-value of z-test
def ztest_pvalue(first_table, second_table):
    ztest_pvalue_results = []
    for col in first_table.columns[0:-1]:
        ztest_pvalue_results.append(np.array(ztest(first_table[col], second_table[col]))[1])
    return ztest_pvalue_results


# Input of arguments
first_cell_type_expressions_path = input()
second_cell_type_expressions_path = input()
save_results_table = input()


# Global function for table creation
def result_program_hw5(first_cell_type_expressions_path0,
                       second_cell_type_expressions_path0,
                       save_results_table0):
    b_cells_expression_data = pd.read_csv(f"{first_cell_type_expressions_path0}",
                                          index_col=0)
    nk_cells_expression_data = pd.read_csv(f"{second_cell_type_expressions_path0}",
                                           index_col=0)
    gene_names = b_cells_expression_data.columns[0:-1]
    ci_test_results = check_dge_with_ci(b_cells_expression_data, nk_cells_expression_data)
    z_test_results = check_dge_with_ztest(b_cells_expression_data, nk_cells_expression_data)
    z_test_p_values = ztest_pvalue(b_cells_expression_data, nk_cells_expression_data)
    mean_diff = dif_mean(b_cells_expression_data, nk_cells_expression_data)
    results = {
        "gene": gene_names,
        "ci_test_results": ci_test_results,
        "z_test_results": z_test_results,
        "z_test_p_values": z_test_p_values,
        "mean_diff": mean_diff
        }
    results = pd.DataFrame(results)
    results.to_csv(f"{save_results_table0}.csv")


result_program_hw5(first_cell_type_expressions_path,
                   second_cell_type_expressions_path,
                   save_results_table)
