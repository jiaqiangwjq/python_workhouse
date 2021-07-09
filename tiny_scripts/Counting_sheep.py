from wxpy import *
import time

# 初始化机器人，并设置登陆缓存，以免每次要扫码
bot = Bot(cache_path=True)	

# 找到要发送信息的好友(好友微信昵称: 拥友)
my_friend = bot.friends().search('拥友')[0]

# 阻塞当前进程，进入 Python 命令行界面，可在命令行界面手动操作 bot
# embed()

num = 0
sheep = "🐏"
sheeps = " "
contents = " 只 "

def send_news(contents):

	# 在python的函数中，修改操作应该是针对局部变量，
	# 如果有和全局同名的变量，在修改之前对该变量进行操作会出现 reference before assignment 的报错,，
	# 所以，如果在函数中引用全局变量，并且要对它修改，就必须加上global关键字
	global sheeps

	if num == 0:
		msg = "0 只羊"

	if num > 0:
		sheeps = sheeps + sheep
		msg = str(num) + contents + sheeps

	try:
		# 发送 msg
		my_friend.send(msg)

		# 发送图片消息
		# my_friend.send('example.jpg')

	except ResponseError as e:
		print(e.err_code, err_msg)

if __name__ == '__main__':
	
	# 实验测试只发送 5 条消息
	while num <= 5:
		send_news(contents)
		num += 1
		time.sleep(2)
