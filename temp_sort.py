import os

with open('temp.txt', 'r') as f:
	lines =[line.strip() for line in f if line.strip()]

lines.sort(reverse=True)

with open(temp.txt' , 'w') as f:
	f.write(','.join(lines))

os.startfile('temp.txt')