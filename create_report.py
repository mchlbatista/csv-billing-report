import csv

class ReportGenerator:

    def __init__(self, filename, month):
        self.filename = filename
        self.month = month

    def open_report(self):
        with open(self.filename, newline='') as csvfile:
            report_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            self.report = Processor(report_reader).process()

    def write_report(self):
        with open(f'./BillingReports/HITADS_support_hours_{self.month}.csv', mode='w') as report_file:
            report_writer = csv.writer(report_file, quoting=csv.QUOTE_ALL)
            for row in self.report:
                report_writer.writerow(row)

class Processor:

    def __init__(self, rows):
        self.rows = rows
        self.report = [['Date', 'Duration', ' Comments', 'Tags']]
        self.total_hours = 0

    def process(self):
        next(self.rows) # Skip header
        for row in self.rows:
            self.report.append([row[1], row[3], row[4], row[5]])
            if row[3] is not None:
                self.total_hours += float(row[3])
        self.report.append(['TOTAL HOURS', self.total_hours])
        return self.report

    
print('Insert name of the file to read: ', end='')
filename = input()
print('Insert Month to process: ', end='')
month = input()

report = ReportGenerator(filename, month)
report.open_report()
report.write_report()