data = []
count = 0 
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print("Total ", len(data), " line record")

intlength = 0
for review in data:
	intlength += len(review)
print("Average length of reviews is ",  intlength / len(data))
