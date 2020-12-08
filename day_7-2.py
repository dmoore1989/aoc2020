file1 = open('day_7-in.txt', 'r')
List = file1.readlines()
rules_list = {}
for item in List:
    item_array = item.split(' contain ')
    suitcase = item_array[0]
    rules = item_array[1].replace('.', '').replace('\n', '')
    if rules == 'no other bags':
        rules_list[suitcase] = []
    else:
        rules_list[suitcase] = rules.split(', ')

gold_bag = 'shiny gold bags'

def count_bags(bag, rules_list, count):
    if len(rules_list[bag]) == 0:
        return 0
    count = 0
    for inner_bag in rules_list[bag]:
        bag_name = inner_bag[2:]
        number = int(inner_bag[0:1])
        count += number
        # if bag == 'striped gold bags' and inner_bag == '2 clear gray bags':
        #     print('a', count)
        print(count)
        # if bag == 'striped gold bags' and inner_bag == '2 clear gray bags':
        #     print('b', count)
        if bag_name[-1] != 's':
            bag_name += 's'
        print(number, count_bags(bag_name, rules_list, count))
        count += (number * count_bags(bag_name, rules_list, count))
        print(count)
        # if bag == 'striped gold bags' and inner_bag == '2 clear gray bags':
        #     print('c', count)
    print(bag, '-', rules_list[bag])
    print(count)
    print('----')
    return count


print(count_bags(gold_bag, rules_list, 0))