rost = input()
count = 0
while rost != '!':
    if 150 <= int(rost) <= 190:
        count += 1
    rost = input()

maxim = max(rost)
minim = min(rost)

print(count)
print(minim, maxim)