team1_num = int(input('Введите количество участников в команде "Мастера кода":'))
team2_num = int(input('Введите количество участников в команде "Волшебники данных":'))
score_1 = int(input('Введите количество решенных задач "Мастерами кода":'))
score_2 = int(input('Введите количество решенных задач "Волшебниками данных":'))
team1_time = int(input('Введите время решения задач "Мастерами кода":'))
team2_time = int(input('Введите время решения задач "Волшебниками данных":'))
tasks_total = score_1 + score_2
time_total = team1_time + team2_time
time_avg = round((tasks_total / time_total), 1)

print('В команде Мастера кода участников: %s!' % (team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда "Волшебники данных" решила задач: {}!'. format(score_2))
print('Волшебники данных решили задачи за {}с!'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач!')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды "Мастера кода"!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'Победа команды "Волшебники Данных"!')
else:
    print(f'Ничья!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')