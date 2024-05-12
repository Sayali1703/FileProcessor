# FileProcessor
converting dat to csv files 

Functions description:
1) convert_dat_to_csv
   - This function is taking input folder path and output folder path as input.
   - Converting all .dat files from input folder and creating output files in the format 'filename.csv' and saving in output folder.
   - calling next function for further dat file conversion.

2) process_dat_file
   - Opening input file in 'read' mode.
   - Reading each line from .dat file. As data in dat file is '\t' separated, so spliting data based on that and considering that as row for csv file.
   - Lastly, writing this row in csv file.
   - calling next function to add footer in this output csv file.

3) add_footer
   - We wanted to calculate avg and 2nd highest salary, so fetching salary column from output csv file.
   - after calculations, created footer format and adding the same in the resulted file.
