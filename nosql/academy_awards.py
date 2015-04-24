import csv

def get_nominations():
    """ Returns a list of academy award nominations.
        Each nomination is represented as a dictionary.
    """
    with open('academy_awards.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        is_header = True
        nominations = []
        for row in reader:
            if is_header:
                fields = row
                is_header = False
            else:
                nominations.append(zip(fields, row))
    return nominations

if __name__ == '__main__':
    noms = get_nominations()
    print noms[0]