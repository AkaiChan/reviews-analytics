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

listnew = []
for review in data:
	if len(review) < 100:
		listnew.append(review)
print("count of reviews that less than 100 ", len(listnew)) 

listnew = []
for review in data:
	if "good" in review:
		listnew.append(review)
print("count of reviews that include 'good'", len(listnew)) 

good = [d for d in data if 'good' in d]
print("count of reviews that include 'good'", len(good)) 