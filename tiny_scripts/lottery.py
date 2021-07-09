import random

'''
2018-11-3
庆祝 LPL 战队 IG在 S8 赛场上夺取冠军
抽取 5 人 IG 冠军皮肤
with my friedns
'''

position = ['top', 'mid', 'ad', 'sup', 'jun']

name = ['caoKeWei','fanLei', 'liangFaDong','weiZhiHao','wuJiaQiang']

result = {}

length = len(name)

for i in range(length):
	r = random.choice(position)
	s = random.choice(name)

	result[r] = s
	position.remove(r)
	name.remove(s)

# print(result)
for k,v in result.items():
	print("'"+k+"'" + ":", end = '')
	print("'"+v+"'")