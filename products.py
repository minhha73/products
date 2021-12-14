products = []
while True :
	name = input('請輸入商品：')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	products.append([ name, price])
#print(products)
#for p in products:
#	print(p[0], '的價格為 :' ,p[1])
with open ('products.csv','w',encoding='utf-8') as f:
	for p in products :
		f.write(p[0] + ',' + p[1] + '\n')
# 把清單中的整數寫進test.txt
#data=[2, 4, 6, 8, 10]
#with open ('test.txt', 'w') as f :
#	for d in data :
#		f.write(str(d) + '\n')