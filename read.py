data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')
print(data[0])
print('-----------------')
print(data[1])

sum_len = 0
for message in data:
	sum_len = sum_len + len(message)


avelen = sum_len / len(data)
print('每筆留言平均的長度是', avelen)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])