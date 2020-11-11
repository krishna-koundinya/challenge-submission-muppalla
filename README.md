# Insight Population Roll-up Challenge - Submission
## Approach
The code uses dictionary/ hashmaps to summarize the data related to each CSBA (Core Based Statistical Area).  
Performing this reduces the number of records or rows to process.  
Once the calculations needed to create the output are applied, the rows are sorted in ascending order of CSBA code

## Instructions to run the code  
Use the following command to run the program  
```
python3.8 .src/population.py path/to/input/file/input.csv path/to/output/file/output.csv
```  
## Requirements  
You will need Python 3.8 installed to run the program  
## Points to consider while evaluating
1. The input and output folders are not present as git doesn't take in empty directories into repositories  
2. The command to run in the run.sh has been commented as the directories are absent.  
