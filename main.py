import os,vk_api,requests,praw,urllib.request,filecmp,time
from stealer import way_to_pict,id_owner_red,secret_key,Info_VK,access_token_0,Teg_Red
from array import *

r=praw.Reddit(client_id=id_owner_red,client_secret=secret_key,user_agent='Mozila')
titleRed=[]

def upload_wall(token,identify,i,n):
    vk_session = vk_api.VkApi(token=token)
    session_api=vk_session.get_api()
    Upload_on_server = session_api.photos.getWallUploadServer(group_id=identify)
    b = requests.post(Upload_on_server['upload_url'],files={'photo':open( way_to_pict+'\\'+i.__str__()+n.__str__()+'1.jpg','rb')}).json()
    On_album = session_api.photos.saveWallPhoto(group_id=identify,photo=b['photo'],server=b['server'],hash=b['hash'])[0]
    session_api.wall.post(owner_id="-"+identify,friends_only=0,from_group=1,message='#'+titleRed[i],attachments='photo'+On_album['owner_id'].__str__()+'_'+On_album['id'].__str__()+'_'+On_album['access_key'],signed=0)#,publish_date=time.time()+30+n*10800)

def __get_gif_reddit(self,teg,n):
    i = 0
    subreddit = self.subreddit(teg).hot(limit=25)
    for post in subreddit:
        if str(post.url).endswith('.gif'):
            try:
                response = urllib.request.urlopen(post.url)
            except:
                break
            self.img = response.read()
            with open(str(post.id) + '.gif', 'wb') as f:
                f.write(self.img)
            os.rename(str(post.id + '.gif'), i.__str__() + n.__str__() + '_1_gif.gif')
            i = i + 1

def get_post_reddit(self,teg,n):
    i=0
    subreddit = self.subreddit(teg).hot(limit=25)
    for post in subreddit:
        print(titleRed[i])
        print(post.url)
        if str(post.url).endswith('.jpg'):
            try:
                response = urllib.request.urlopen(post.url)
            except:
                break
            self.img = response.read()
            with open(str(post.id)+'.jpg','wb') as f:
                f.write(self.img)
            os.rename(str(post.id + '.jpg'), i.__str__()+n.__str__()+'1.jpg')
        elif str(post.url).endswith('.png'):
            try:
                response = urllib.request.urlopen(post.url)
            except:
                break
            self.img = response.read()
            with open(str(post.id) + '.png', 'wb') as f:
                f.write(self.img)
            os.rename(str(post.id + '.png'), i.__str__() + n.__str__() + '1.jpg')
#            print('Download='+i.__str__() + n.__str__() + '1.jpg')
        elif str(post.url).endswith('.m3u8'):
            try:
                response = urllib.request.urlopen(post.url)
            except:
                break
            self.img = response.read()
            with open(str(post.id) + '.m3u8', 'wb') as f:
                f.write(self.img)
            os.rename(str(post.id + '.m3u8'), i.__str__() + n.__str__() + '_1_vid.mp4')
#            print('Download='+i.__str__() + n.__str__() + '_1_vid.mp3')
        i = i + 1
def __Compare__(n):
    i=0
    while i<25:
        a=0
        while a<25:
          try:
            if filecmp.cmp(i.__str__()+n.__str__()+'1.jpg',a.__str__()+n.__str__()+'0.jpg'):
   #             print('copy='+a.__str__()+n.__str__()+'0.jpg')
                os.remove(i.__str__()+n.__str__()+'1.jpg')
                a=a+25
            else:
                pass
            a=a+1
          except FileNotFoundError:
              a=a+1
        i=i+1

def __get_title_post__(self,teg,n):
    i=0
    for submission in self.subreddit(teg).hot(limit=25):
        titleRed.insert(i,submission.title)
        i=i+1


def recycle(n):
    i=0
    global titleRed
    titleRed=[]
    while i<25:
        if (i.__str__()+n.__str__()+'1.jpg'):
            try:
                os.remove(i.__str__()+n.__str__()+'1.jpg')
            except FileNotFoundError:
                pass
        i=i+1

def __ForCmp__(n):
    i = 0
    while i < 25:
      try:

        if os.path.isfile(way_to_pict + '\\' + i.__str__() + n.__str__() + '1.jpg'):
          print('Removed='+i.__str__()+n.__str__()+'0.jpg')
          os.remove(i.__str__()+n.__str__()+'0.jpg')
          os.replace(src=i.__str__()+n.__str__()+'1.jpg',dst=i.__str__()+n.__str__()+'0.jpg')
          i=i+1
        else:
            i=i+1
            pass
      except FileNotFoundError:
          i=i+1
          print('fuck')

def __Posted__(n):
    i=0
    New_Memes=0
    while i<25:
        try:
            if os.path.isfile(way_to_pict+'\\'+i.__str__() + n.__str__() + '1.jpg'):
                act = Info_VK[1][New_Memes]
                upload_wall(access_token_0,act, i,n)
                print('act=' + act + ' ,Posted=' + i.__str__() + n.__str__() + '1.jpg')
                New_Memes=New_Memes+1
                i=i+1
            else:
                i=i+1
                pass
        except FileNotFoundError:
            i=i+1
            pass
        if New_Memes==5:
            print('Enough')
            break


def __main__():
    i=0
    while i<=2:
        recycle(i)
        __get_title_post__(r,Teg_Red[i],i)
#        __get_gif_reddit(r,Teg_Red[i],i)
        get_post_reddit(r,Teg_Red[i],i)
        __Compare__(i)
        __Posted__(i)
        __ForCmp__(i)
        print('main_circle '+i.__str__()+' is end')
        i=i+1

__main__()