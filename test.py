import csv
with open('eggs2.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|')
    spamwriter.writerow(['Spam'] + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# https://docs.python.org/fr/3/library/csv.html