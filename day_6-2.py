file1 = open('day_6-in.txt', 'r')
groups = file1.read()

groups = groups.split('\n\n')
total_yes = 0
for group in groups:
    group_answers = []
    
    group = group.split('\n')
    for person in group:
        form_answers = set()
        for question in person:
            form_answers.add(question)
        group_answers.append(form_answers)
    all_group_answers = None
    for group_answer in group_answers:
        print(group_answer)
        if all_group_answers is None:
            all_group_answers = group_answer
        else:
            all_group_answers = all_group_answers.intersection(group_answer)
    print(all_group_answers)
    print('----')
    total_yes += len(all_group_answers)
print(total_yes)

