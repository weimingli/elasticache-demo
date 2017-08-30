import sys
sys.path.append('/usr/local/aws/lib/python2.7/site-packages')

import redis
import random

r = redis.Redis(host='my-redis-cluster.b1xens.ng.0001.cnn1.cache.amazonaws.com.cn', port=6379)

for i in range(0,100000):
	key = 'key%s' % (i)
	
	print 'setting:', key, random.randint(1,5000000)
	r.set(key ,random.randint(1,5000000))
	
	#print 'getting:', key, r.get(key)

'''info = r.info() 
for key in info: 
  print "%s: %s" % (key, info[key])
'''
