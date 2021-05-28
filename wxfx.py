import requests
import json
import random,string
#微信分享阅读
#把https://script.baertt.com/count2/visit?type=1&si=改成https://script.baertt.com/count2/callback?si=


#每次改si#
#════════════════════════════════════════
def si():
  # 随机生成数字个数
  Ofnum=random.randint(1,32)
  Ofletter=32-Ofnum
  # 选中ofnum个数字
  slcNum=[random.choice(string.digits) for i in range(Ofnum)]
  # 选中ofletter个字母
  slcLetter=[random.choice(string.ascii_letters) for i in range(Ofletter)]
  # 打乱组合
  slcChar=slcLetter+slcNum
  random.shuffle(slcChar)
  # 生成随机密码
  getPwd=''.join([i for i in slcChar])
  return getPwd
#════════════════════════════════════════



url1 = 'https://script.baertt.com/count2/callback?si='+si()+'5791b518cd4e0328770011079cf0b8b2&referer=https%253A%252F%252Ffocus.youth.cn%252Farticle%252Fshare_fournew%253Fsignature%253DgbJynLeRd3VA29KYqE4gqjDQLH3j0v3aDNrGQloPXZzxvOB6jW%2526scene_id%253Dfire_share%2526share_id%253D48108424385933821622082503379%2526time%253D1622082505503&_=1622085967224&jsonpcallback=jsonp4'

url2 = 'https://script.baertt.com/count2/callback?si='+si()+'56ca05ca7792f13ede846e2d4565bf3a&referer=https%253A%252F%252Ffocu.youth.cn%252Fsixhotnew%252F20210526%253Fsid%253D38637432%2526uid%253D48108266%2526timestamp%253D1622086106%2526signature%253DNqylzJV6MGKj23RQPraW6KdNXtpLDyl7EYOAgBndo9ZkDbepv5%2526scene_id%253Dfire_share%2526share_id%253D48108266386374321622086111504%2526time%253D1622086113134&_=1622086232201&jsonpcallback=jsonp3'

url3 = 'https://script.baertt.com/count2/callback?si='+si()+'f31a82e22ebed6fa30ec30fec5c2214a&referer=https%253A%252F%252Ffocu.youth.cn%252Feighthotnew%252F20210525%253Fsid%253D38617734%2526uid%253D55253598%2526timestamp%253D1622086354%2526signature%253DjE9mdZzRG3lxVgkq8na3X2PKyfnw5ry1yJ6vBKw0oObepWDXrM%2526scene_id%253Dfire_share%2526share_id%253D55253598386177341622086366%2526time%253D1622086366&_=1622086385932&jsonpcallback=jsonp3'

url4 = 'https://script.baertt.com/count2/callback?si='+si()+'2cb5fcd499e86d7fcf8f9a9cb9db33e2&referer=https%253A%252F%252Ffocu.youth.cn%252Feighthotnew%252F20210523%253Fsid%253D38574968%2526uid%253D25442278%2526timestamp%253D1622081104%2526signature%253D6y30XlmbkL9oxwAjJd1PRD3zofrQMMp7gMQE2nZKW8RNpvPrqz%2526scene_id%253Dfire_share%2526share_id%253D25442278385749681622081114%2526time%253D1622081114&_=1622082123236&jsonpcallback=jsonp3'
#多号码

headers={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Host": "script.baertt.com","Referer": "https://focu.youth.cn/","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.6(0x1800062d) NetType/WIFI Language/zh_CN"}



resp = requests.get(url=url1,headers=headers,timeout=60).text

print(resp)
    
    
    
    
    
    
    
    
    
    
    
    

resp = requests.get(url=url2,headers=headers,timeout=60).text

print(resp)


resp = requests.get(url=url3,headers=headers,timeout=60).text

print(resp)


resp = requests.get(url=url4,headers=headers,timeout=60).text

print(resp)
