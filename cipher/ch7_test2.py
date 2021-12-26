f = open("score.txt", "r")
lines = f.readlines()

sum_score = 0
for score in lines :
    sum_score +=int(score)
print(sum_score)
