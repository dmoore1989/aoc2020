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
def search_bag(bag, rules_list):
    for inner_bag in rules_list[bag]:
        bag_name = inner_bag[2:]
        if bag_name[-1] != 's':
            bag_name += 's'
        if bag_name == 'shiny gold bags' or search_bag(bag_name, rules_list):
            return True
    return False

bags_with_gold = 0
for rule, bags in rules_list.items():
    print(rule, search_bag(rule, rules_list))
    if search_bag(rule, rules_list):
        bags_with_gold += 1
print(bags_with_gold)