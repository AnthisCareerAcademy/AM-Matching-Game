import csv

#display_name = 'tat'
#score = '0:00:02'



    #

scores = {}

class Score:
    def __init__(self, display_name, score):
        self.display_name = display_name
        self.score = score

    def save_score_dictionary_(self):
        scores[display_name] = score

    def save_score(self):
        row = ((self.display_name,self.score))

        with open("scores.csv", "w", newline='') as f:
            writer = csv.writer(f)

            writer.writerow(row)

    # ex:
#display_name = input('dp: ')
#score = input('ns: ')

    #new_score = Score(display_name, score)

    #new_score.save_score_csv()

    #print(scores)

    #with open("scores.csv", 'r') as f:
#        reader = csv.reader(f)
#        for row in reader:
#            print(row)