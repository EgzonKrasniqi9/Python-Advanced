scores = [12,23,45,56,78,98]
total = 0
count = 0

for score in scores:
    if score < 50:
        continue

    total += score
    count += 1

    print("the total is ", total)
    print("the amout of score", count)