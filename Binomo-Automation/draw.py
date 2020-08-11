from PIL import ImageGrab



T_cordinates = { 
 '80' : 383, '70' : 423, '60' : 463,'50' : 503, '40' : 543,'30' : 583, '20' : 623}

B_coordinates = {                                                                                                                                                                                        
'20' : 624, 588, '30' : 584, '40' : 544, '50' : 504, '60' : 464, '70' : 424, '80' : 384} 

top = input('Enter Overbought value:')
bottom = input('Enter Oversold value:')

image = ImageGrab.grab().convert('L')
data = image.load()

for i in range(1117, 1138):
	for j in range(300, T_cordinates[top]):
		data[i, j] = 0

for i in range(1117, 1138):
	for j in range(B_coordinates[bottom], 700):
		data[i, j] = 0

image.show()
