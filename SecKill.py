
# coding: utf-8

# 1、导入所需要的包

# In[1]:


import requests as r
import json
import datetime


# 2、创建Session，为了登录后保持会话状态

# In[2]:

sess = r.Session()


# 3、post请求登录

# In[3]:

data = {"username":"****","password":"****"}
login = sess.post("http://www.dcjingsai.com/user/common/login.json",data=data)


# 4、登录结果输出

# In[4]:

login.text


# 5、先将比赛预测的结果由json字符串转换成字符串，post请求提交预测的结果

# In[5]:

predict = json.dumps("home,away,result1,result2\n比利时,英格兰,胜,负")
response = sess.post("http://www.dcjingsai.com/user/file/uploadSubmissionFileByString.json",data=predict)


# 5、提交结果输出

# In[6]:

response.text


# 6、将结果转换为json

# In[7]:

data = json.loads(response.text)
print(data)


# 7、获取刚才提交的字符串存放的文件地址

# In[8]:

path = data['data']['fullPath']
print(path)


# 8、获取文件名

# In[9]:

paths = path.split('/')
print(paths[-1])


# 9、准备需要传送的数据

# In[10]:

d = {
    "description": "",
    "stageId": "124",
    "cmpId": "228",
    "name": paths[-1],
    "filePath": path
}


# 10、真正直接提交结果

# In[11]:

ans = sess.post("http://www.dcjingsai.com/user/cmpt/commitResult.json",data=d)


# 11、最后提交的结果

# In[12]:

ans.text


# 12、获取当前时间，定时提交

# In[13]:

while True:
    now_time = str(datetime.datetime.now())
    if '2018-07-12 22:10:00'==now_time[:19]:
        ans = sess.post("http://www.dcjingsai.com/user/cmpt/commitResult.json",data=d)
        print(now_time)
        print(ans.text)
    if '2018-07-12 22:10:05'==now_time[:19]:
        break


# In[ ]:



