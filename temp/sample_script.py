import csv
import time

a = [['temp1', 'temp2'], [1,2], [3,4]]

with open("/tmp/sample_csv.csv", "w") as csvfile:
    write = csv.writer(csvfile)
    write.writerows(a)

# wait = 2

# while wait > 0:
#     wait = wait - 1
#     time.sleep(10)
#     print(f"Sleep for 10 seconds. wait: {wait}")
