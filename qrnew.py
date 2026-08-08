import qrcode
print(dir(qrcode)) # dir  هي داله استكشافيه ترجع لي كل الاوامر الموجوده في مكتبة ال qrcode
data = 'www.linkedin.com/in/taraf-saleh-b4a176286'
img = qrcode.make(data)
img.save('qr_code.png') 