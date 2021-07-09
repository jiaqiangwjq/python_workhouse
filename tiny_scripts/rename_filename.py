import os

filepath = 'E:\\下载下载下载下载\\Camera\\back_up\\PNG'

# 改变当前工作目录到指定的路径
os.chdir(filepath)

# 列出当前目录下的所有文件
files = os.listdir(".")

for filename in files:
	portion = os.path.splitext(filename)

	# 如果后缀是 .PNG
	if portion[1] == '.PNG':

		# 重新组合文件名和后缀
		newname = portion[0] + '.JPG'
		os.rename(filename, newname)
