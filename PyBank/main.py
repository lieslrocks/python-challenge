#importing csv data
import csv

# reading csv file
with open(budget_data.csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # skip header row
    print(f"Header: {csv_header}")

    # find net amount of profit and loss
    P = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    # find revenu change
    revenue_change = []

    for x in range(11, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))

    # calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)

    # calculate total length of months
    total_months = len(months)

    #greatest increase in profits
    greatest_increase = max(revenue_change)

    #greatest decrease in losses
    greatest_decrease = min(revenue_change)



    #print the Results

    print("Financial Analysis")

    print("_____________________")

    print(f"Total Months: {row_count}")

    print(f"Total: ${net_total}")

    print(f"Average Change: ${average_change}")

    print(f"Greatest Increase in Profits: {increase_date} (${grt_increase})")

    print(f"Greatest Decrease in Profits: {decrease_date} (${grt_decrease})")



    # output to a text file

    file = open("output","w")

    file.write("Financial Analysis" + "\n")

    file.write("______________________" + "\n")

    file.write(f"Total Months: {row_count}" + "\n")

    file.write(f"Total: ${net_total}" + "\n")

    file.write(f"Average Change: ${average_change}" + "\n")

    file.write(f"Greatest Increase in Profits: {increase_date} (${grt_increase})" + "\n")

    file.write(f"Greatest Decrease in Profits: {decrease_date} (${grt_decrease})" + "\n")

    file.close()

