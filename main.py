import os
import csv

def convert_dat_to_csv(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.dat'):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename.replace('.dat', '.csv'))
            process_dat_file(input_file_path, output_file_path)

def process_dat_file(input_file, output_file):
    # Function to read the .dat file and write its content to a .csv file
    # You can customize this according to your .dat file's structure

    with open(input_file, 'r') as dat_file, open(output_file, 'w', newline='') as csv_file:
        # Example: Assuming each line in .dat file represents a CSV row
        csv_writer = csv.writer(csv_file)
        for line in dat_file:
            #print(line)
            row=line.strip().split('\t')
            csv_writer.writerow(row)
            
    add_footer(output_file)

def add_footer(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        #print(data)
        salaries = [int(row[5]) for row in data[1:]]
        #print(salaries)
        sorted_salaries = sorted(salaries, reverse=True)
        second_highest_salary = sorted_salaries[6]
        average_salary = sum(salaries) / len(salaries)
        footer = [['Second highest salary', str(second_highest_salary)], ['avg salary', str(average_salary)]]
        data.extend(footer)
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
			
			
def main():
    input_folder = "input_files"
    output_folder = "output_files"

    convert_dat_to_csv(input_folder, output_folder)

if __name__ == "__main__":
    main()
