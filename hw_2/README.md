#### Homework 2.

The function `result_p_value_adj` allows to create table of comparison gene expressions of two cell type for every genes pair:
The function `result_p_value_adj` requests arguments:
1. table1: file contained first cell type expressions (csv file)
2. table2: file contained first cell type expressions (csv file)
3. ci_test: method used for determinating the conduct of the test with confidence intervals (by default=True)
4. alpha: method used as threshold of tests (by default = 0.05)
5. multiplete: method used for testing and adjustment of pvalues (by default = None - no adjustment)

Can be either the full name or initial letters. Available methods are:

1. bonferroni : one-step correction
2. sidak : one-step correction
3. holm-sidak : step down method using Sidak adjustments
4. holm : step-down method using Bonferroni adjustments
5. simes-hochberg : step-up method (independent)
6. hommel : closed method based on Simes tests (non-negative)
7. fdr_bh : Benjamini/Hochberg (non-negative)
8. fdr_by : Benjamini/Yekutieli (negative)
9. fdr_tsbh : two stage fdr correction (non-negative)
10. fdr_tsbky : two stage fdr correction (non-negative)=None

The result presents this columns:
1. Studied gene
2. The mean difference
2. The presence or absence of differences based on check intervals (alpha - threshold parameter) - optionally
3. The p-value of z-test
4. The p-value of z-test adjusted multyiple test
5. The presence or absence of differences based on multiple z-test (alpha - threshold parameter)

You can see example of execution in *Example.csv*

> It is better to run from Colab, in Jupiter it gives a strange error
> (KeyError: '0.83330345')
