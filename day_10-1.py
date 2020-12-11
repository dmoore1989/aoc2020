file1 = open('day_10-in.txt', 'r')
adapters_raw = file1.readlines()
adapters = [0]
for adapter in adapters_raw:
    adapters.append(int(adapter))

adapters.sort()
adapters.append(adapters[-1] + 3)
print(adapters)
diff1 = 0
diff3 = 0

for index, adapater in enumerate(adapters):
    if index == len(adapters) - 1:
        print(diff1, diff3)
        print(diff1 * diff3)
        continue
    next_adapter = adapters[index + 1]
    if adapater + 1 == next_adapter:
        diff1 += 1
    elif adapater + 3 == next_adapter:
        print('there')
        diff3 += 1