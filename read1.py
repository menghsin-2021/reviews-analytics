data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')
print(data[0])
print('-----------------')
print(data[1])

# 計算每條留言平均長度
sum_len = 0
for message in data:
	sum_len = sum_len + len(message)

avelen = sum_len / len(data)
print('每筆留言平均的長度是', avelen)

# 篩選出留言長度<100的留言
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

#篩選出留言中有 good 的留言
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言中有 good')

print(good[0])
print(good[1])

#清單快寫法
# output = [運算或直接放變數 for 變數 in 清單 篩選條件]
# ex. output = [(number-1) or x for number or x in reference if number % 2 == 0]
# 會把運算結果或變數放到清單去
bad = [b for b in data if 'bad' in b]
print('一共有', len(bad), '筆留言中有 bad')

# 想秀出這是第幾條留言
for b in bad:
    print('這是第', bad.index(b), '條留言', bad[bad.index(b)])
    print('-----------------')
    if bad.index(b) == 10:
        break

# 文字計數 字典應用2
wc = {}
mes = 0
for d in data:
	words = d.split() # split 可以直接留空 直接用空白當分割條件 
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的 key 進字典
	mes += 1
	if mes == 200000:
		break

for word in wc: # word 代表 key 用迴圈叫出來的只有 key
	if wc[word] > 100000:
		print(word, wc[word])
	
print(len(wc)) # 該字典的長度 (key 的數量) = 有幾種字
print(wc['Jason'])

while True:
	word = input('what words are you want to lookup:')
	if word == 'q':
		print('thank you for your search')
		break
	elif word in wc:
		print(word, 'shows in all message for', wc[word], 'times')
	else:
		print('no shows in message')


