#### Homework 1.

**Features**
Using table of differential gene expressions of two cell type, program evaluate:
1. The difference between means of TMCC1 gene expression levels based on the central limit theorem and check intervals of means - *Task 1*
1. The difference between expression levels of gene pair based on check intervals of mean - *Task 2*
2. The difference between expression levels of gene pair based on z-test - *Task 3*

The separate programm allows to create table of comparison gene expressions of two cell type for every genes pair:
The function `result_program_hw5` requests arguments:
1. first_cell_type_expressions_path: path to file contained first cell type expressions (csv file)
2. second_cell_type_expressions_path: path to file contained second cell type expressions (csv file)
3. save_results_table: name of output csv file

The result presents 
1. The presence or absence of differences based on check intervals
2. The presence or absence of differences based on z-test (threshold - 0.95)
3. The p-value of z-test
4. The difference between means
