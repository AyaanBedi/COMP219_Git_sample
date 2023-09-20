import csv
from collections import defaultdict

# Define the job titles of interest
job_titles = ['Data Architect', 'Senior Business Analyst', 'Data Scientist', 'Machine Learning Engineer']

# Initialize dictionaries to store the sum and count of salaries for each job title
salary_sums = defaultdict(int)
salary_counts = defaultdict(int)

# Read data from the CSV file
with open('job_data.csv', 'r', newline='') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        title = row['job_title']
        num_of_salaries = int(row['num_of_salaries'])

        if title in job_titles:
            salary_sums[title] += num_of_salaries
            salary_counts[title] += 1

# Calculate the average salaries and print the results
for titles in job_titles:
    if salary_counts[titles] > 0:
        average_salary = salary_sums[titles] / salary_counts[titles]
        print(f"Average salary for {titles}: {average_salary:.2f}")
    else:
        print(f"No data found for {titles}")
