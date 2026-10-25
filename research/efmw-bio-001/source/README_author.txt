
1.System requirements

-MATLAB2020a with signal processing, statistics, and machine learning tool boxes. 
-Scripts have been tested on Windows 7 (x64), and Windows 10
-At least 64GB of RAM 

2. Installation guide
-Purchase a MATLAB liscence and download version 2020a. Follow installation steps.
-https://www.mathworks.com/products/new_products/release2020a.html
-Typical install time is about 30 minutes to one hour.
-Unzip Code_files.zip to view the custom code associated with processing and plotting data.
-To access the source MCF10A supplementary data tables, unzip SourceData.zip (in the same folder as you unzipped Code_files.zip)
-To access the (large) cancer cell line data files needed to run the figure generation code, unzip Data_files.zip WITHIN the MATLABfiles subfolder that was extracted from Code_files.zip

3. Demo
-Open 'DEMO.m' to load ERK data and corresponding ETG measurements.This demo fits a regression model that predicts the mean of ERK activity using nuclear ETG measurements. 
-The expected output is a predicted vs observed plot showing the predict ERK mean on the x-axis and the oberseved ERK mean on the y-axis. The console will display the regression statistics. (R^2 ~ .36)
-Typical run time of this DEMO is about 10 minutes, as it takes some time to load the data.

4. Instructions for use
-All plots can be recreated by running Figure_script.m
-The convolutional neural network models were trained on Google Colab notebooks, the resulting data files were saved as .csv files and plotted in MATLAB. The CNN fitting procedure can be trained/reproduced by uploading the 'ETGPredictionModel' folder into your google drive and running the PredictionModel_exp2.ipynb notebooks on google colab. Please follow the directions on the README.ipynb file within that ETGPredictionModel\cell2cell folder.

5. Description of MCF10A Supplementary Data
-The "SourceData\SupplementaryData1 folder contains data from MCF10A cells. Cells are identidcal row-wise across the following excel files: 
--df_erk: EKAR time series data of single-cells (calibrated and normalized-see methods)
--df_erk_paramterized: parameterized/feature extracted EKAR data
--df_ETGs: antibody staining data normalized across replicates
--df_narea: nuclear area measurements for each cell
--df_tx: Conditions, well of origin, and replicate plate ID for each cell. 
-The SourceDataCancerCells folder contains data from three cancer cell lines. Cells are identidcal row-wise across the following excel files: 
--df_erk: EKAR time series data of single-cells (not calibrated)
--df_erk_paramterized: parameterized/feature extracted EKAR data
--df_ETGs: antibody staining data normalized across replicates
--df_narea: nuclear area measurements for each cell
--df_tx: Conditions, well of origin, and replicate plate ID for each cell.
--df_cell_types: Cell type identidies for each cell

6. Description of Cancer Cell Supplementary Data
-The "Matlabfiles/SupplementaryData2" folder contains data from three cancer cell types. Excel files contain similar names/information as described above. However, df_cell_types indicates the cell type of each row in the excel files. 
