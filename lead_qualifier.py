#GTM lead Qualification Automation

# Importing leads from a CSV file, defining each variable
import csv
leads = []
with open("leads.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        company = row[0]
        score = int(row[1])
        industry = row[2]
        employees = int(row[3])

        leads.append([company, score, industry, employees])
processed_leads = []

# Defining thresholds for lead qualification
qualified_count = 0
nurture_count = 0
disqualified_count = 0

def classify_lead(score,employees):
    if score >= 80 and employees >= 1000:
        return "Qualified"
    elif score >= 60 and employees >= 100: 
        return "Nurture"
    else:
        return "Disqualified"
def assign_priority(status):
    if status == "Qualified":
        return "High"
    elif status == "Nurture":
        return "Medium"
    else:
        return "Low"


# Process and classify leads
for lead in leads:
    company = lead[0]
    score = lead[1]
    industry = lead[2]
    employees = lead[3]

    status = classify_lead(score, employees)
    priority = assign_priority(status)
    processed_leads.append([
        company, 
        score, 
        industry, 
        employees, 
        status, 
        priority
        ])
    if status == "Qualified":
        qualified_count += 1
    elif status == "Nurture":
        nurture_count += 1
    else:
        disqualified_count += 1
    print(company, "| Score:", score, "| Industry:", industry, "| Employees:", employees, "->", status, "Priority:", priority)

print()
print("Summary")
print("Qualified:", qualified_count)
print("Nurture:", nurture_count)
print("Disqualified:", disqualified_count)

# Exporting the processed leads to a new CSV file
with open("processed_leads.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Company", "Score", "Industry", "Employees", "Status", "Priority"])
    writer.writerows(processed_leads)
