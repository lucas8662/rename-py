import os

for x in range(2330):

	dir = 'C:/rename/'

	str33 = '{:02}'.format(x)

	old_file = os.path.join(dir, 'radar' + str(str33) + '_placeholder.png')
	new_file = os.path.join(dir, 'radar' + str(str33) + '.png')
	 
	os.rename(old_file, new_file)