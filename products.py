products = []
while True :
	name = input('請輸入產品 :')
	if name == 'q' :
		break
	price = input('請輸入價格 :')
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	products.append([name, price])
print(products)
for p in products :
	#print(p)
	print(p[0], '的價格是 :', p[1])