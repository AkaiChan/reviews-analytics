data = []
count = 0 
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print("Total ", len(data), " line record")

print(data[0])

wc = {} # word_count
for d in data:
	words = d.split(" ")
	for word in words:
		if word not in wc:
			wc[word] = 1 # add new key
		else:
			wc[word] += 1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc["Allen"])

while True:
	word = input("what do you want to search?")
	if word == "q":
		break
	if work in wc:
		print(word, "count is ", wc[word])
	else:
		print("Error keyword")

print("Thanks for using")