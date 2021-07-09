from PIL import Image
import os

filepath = 'E:\\下载下载下载下载\\Camera\\back_up\\PNG'

# 改变当前工作目录到指定的路径
os.chdir(filepath)

# 列出当前目录下的所有文件
files = os.listdir(".")

for filename in files:
	portion = os.path.splitext(filename)
	name = portion[0] + '.JPEG'
	try:
		img = Image.open(filename)

		# OSError: cannot write mode RGBA as JPEG
		# 将 PNG 格式的 RGBA 改为 JPG 格式的 RGB
		img = img.convert('RGB')
		img.save(name, 'JPEG')
	
	# 有一张图片 cannot indetify, 我也不知道咋回事
	except Exception as e:
		print(e)