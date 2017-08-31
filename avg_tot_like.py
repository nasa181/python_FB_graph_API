import facebook
import json
import requests

def get_date(str_datetime):
	return str_datetime[8:10]

def get_month(str_datetime):
	return str_datetime[5:7]

def get_year(str_datetime):
	return str_datetime[0:4]

graph = facebook.GraphAPI(access_token="EAACEdEose0cBAKdLfdZC6l79xiEt8RpBTIqBELOxAED5RzbODBYs02mlyFmxaadfdKIOenA00PCPWqwDqGSI2jGVJAVnfWQB0ro2ilGsgu8F4oPuCOUmkXh1Tufhy6TWi8ROA0TS68bj1SM365ajVoOC16ALnk2ylZC3nwLv2xVAkZCX5eHdZACjlA1GI92bc4RfZAsDtSQZDZD", version=2.10)
post = graph.get_object(id='325477731120719/posts?fields=created_time,likes.limit(0).summary(true),comments.limit(0).summary(true)')
posts_count = len(post['data'])
likes_count = 0
comments_count = 0
# print(post)


for i in  range(len(post['data'])):
	likes_count += post['data'][i]['likes']['summary']['total_count']
	comments_count += post['data'][i]['comments']['summary']['total_count']
	# datetime = post['data'][i]['created_time']
	# print(datetime,get_year(datetime),get_month(datetime),get_date(datetime))
print('posts_count',posts_count)
print('likes_count',likes_count)
print('comments_count',comments_count)



next_link = post['paging']['next']
# print(next_link)
c = 0
while(len(next_link) != 0):
	r = requests.get(next_link)
	r = r.text
	r = json.loads(r)
	if 'paging' in r:
		next_link = r['paging']['next']
	else:
		break
	posts_count += len(r['data'])
	for i in  range(len(r['data'])):
		likes_count += r['data'][i]['likes']['summary']['total_count']
		comments_count += r['data'][i]['comments']['summary']['total_count']
	print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<',c,'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	c += 1

print('posts_count',posts_count)
print('likes_count',likes_count)
print('comments_count',comments_count)
print('likes_count/posts_count',likes_count/posts_count)
print('comments_count/posts_count',comments_count/posts_count)




