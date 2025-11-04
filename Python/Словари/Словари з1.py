Student={
    'Иванов':[23,34,45],
    'Петров':[33,30,40],
    'Ронов':[20,14,85],
    'Вывов':[83,37,49],
    'Зовов':[73,44,41],
    'Газманов':[100,99,98]
}
Average_score={}
for name, scores in Student.items():
    averge=sum(scores)/len(scores)
    Average_score[name] = round(averge,2)
print('Средний балл')
for name, avg in Average_score.items():
    print(f'{name} : {avg}')