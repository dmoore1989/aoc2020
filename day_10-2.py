file1 = open('day_10-in.txt', 'r')
adapters_raw = file1.readlines()
adapters = [0]
max_adapter = 0 
for adapter in adapters_raw:
    adapter = int(adapter)
    adapters.append(adapter)
    if adapter > max_adapter:
        max_adapter = adapter

adapters.sort(reverse=True)
adapter_set = set(adapters)
end_value = max_adapter + 3
adapter_set.add(end_value)
number_hash = {}

def count_permutations(value, number_hash):
    if value in number_hash:
        return number_hash[value]
    elif value == end_value:
        return 1
    count = 0 
    for interval in [1,2,3]:
        if value + interval in adapter_set:
            count += count_permutations(value + interval, number_hash)
        
    return count
full_count = 0 
print(adapters)
for adapter in adapters:
    new_count = count_permutations(adapter, number_hash)
    number_hash[adapter] = new_count

print(new_count)