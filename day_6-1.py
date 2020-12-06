file1 = open('day_6-in.txt', 'r')
groups = file1.read()

groups = groups.split('\n\n')
total_yes = 0
for group in groups:
    group = group.replace('\n', '')
    form_answers = set()
    for question in group:
        form_answers.add(question)
    print(form_answers)
    total_yes += len(form_answers)
print(total_yes)
