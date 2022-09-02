'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''


N = int(input())

if 2<=N<=5:
    records = {}
    for i in range(N):
        name = input()
        score = float(input())
        if name not in records:
            records[name] = score
    
    scores_list = sorted([score for score in records.values()])
    scores_list_unique = sorted(set([score for score in records.values()]))
    second_lowest_score = scores_list_unique[1]
    
    name = [k for k,v in records.items() if v == second_lowest_score]
    count_lowest_scores = scores_list.count(second_lowest_score)
    
    [print(item, end='\n') for item in sorted(name[0:count_lowest_scores])]
