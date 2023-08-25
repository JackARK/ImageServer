# 专属图床，本站自用图片API，免费开放



## 简述

很多博客网站和个人博主都在烦的一件事——博客里的背景、壁纸API要么收费，要么请求响应缓慢，主题不适配返回的数据格式。身为博主同样受困于此，于是一拍大腿：自己搭建一个不就得了！

后来这个雏形就诞生了。项目在Github和Gitee上开源，请能人志士鼎力相助！

**Github：**[Jack.H/ImageServer: 图床雏形，能够提供一个随机壁纸的接口和上传图片的接口](https://github.com/JackARK/ImageServer)

**Gitee**：[杰出咸鱼/ImageServer: 图床雏形，能够提供一个随机壁纸的接口和上传图片的接口](https://gitee.com/jackhartwell/ImageServer.git)

但是快开学了，时间或许就不那么充沛，这个项目现在就只有一个雏形。已经实现了基本功能：

- [x] 随机获取一张壁纸
- [x] 上传图片到图床（指定分类）
- [ ] 壁纸分类请求、分辨率请求
- [x] 壁纸爬虫：从wallhaven等允许爬虫的网站上“偷壁纸”
- [ ] 壁纸上传界面可视化
- [ ] 返回格式多样化
- [ ] 壁纸无损压缩加快响应速度
- [ ] 并发能力和防护能力
- [ ] 图片格式验证

## 调用

**随机获取一张壁纸**：

**请求示例**

```http
GET https://img.saltfish.club/random
```

**返回示例：**（直接进行了调用，刷新页面会更新哦）

![img](https://img.saltfish.club/random)



**上传一张壁纸**

下面提供HTTP、Python、Nodejs、Java、C语言的上传脚本，以及Python的**批量**上传脚本

请上传常规格式的照片（jpg，png），否则会出现请求成功但无法加载的问题。

```http
POST /upload HTTP/1.1
Host: img.saltfish.club
Content-Length: 223
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="image"; filename="YOUR_IMAGE_PATH"
Content-Type: image/png

(data)
------WebKitFormBoundary7MA4YWxkTrZu0gW--

```

```python
import requests

url = "https://img.saltfish.club/upload"

payload = {}
files=[
  ('image',('lovelydogs.png',open('/C:/Users/33225/Pictures/screen_shot/lovelydogs.png','rb'),'image/png'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

```

```javascript
var request = require('request');
var fs = require('fs');
var options = {
  'method': 'POST',
  'url': 'https://img.saltfish.club/upload',
  'headers': {
  },
  formData: {
    'image': {
      'value': fs.createReadStream('/C:/Users/33225/Pictures/screen_shot/lovelydogs.png'),
      'options': {
        'filename': '/C:/Users/33225/Pictures/screen_shot/lovelydogs.png',
        'contentType': null
      }
    }
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});

```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = new MultipartBody.Builder().setType(MultipartBody.FORM)
  .addFormDataPart("image","/C:/Users/33225/Pictures/screen_shot/lovelydogs.png",
    RequestBody.create(MediaType.parse("application/octet-stream"),
    new File("/C:/Users/33225/Pictures/screen_shot/lovelydogs.png")))
  .build();
Request request = new Request.Builder()
  .url("https://img.saltfish.club/upload")
  .method("POST", body)
  .build();
Response response = client.newCall(request).execute();
```

```c
CURL *curl;
CURLcode res;
curl = curl_easy_init();
if(curl) {
  curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "POST");
  curl_easy_setopt(curl, CURLOPT_URL, "https://img.saltfish.club/upload");
  curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
  curl_easy_setopt(curl, CURLOPT_DEFAULT_PROTOCOL, "https");
  struct curl_slist *headers = NULL;
  curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
  curl_mime *mime;
  curl_mimepart *part;
  mime = curl_mime_init(curl);
  part = curl_mime_addpart(mime);
  curl_mime_name(part, "image");
  curl_mime_filedata(part, "/C:/Users/33225/Pictures/screen_shot/lovelydogs.png");
  curl_easy_setopt(curl, CURLOPT_MIMEPOST, mime);
  res = curl_easy_perform(curl);
  curl_mime_free(mime);
}
curl_easy_cleanup(curl);

```

**批量上传脚本**

```python
import requests
import os
import time
folder_path = "YOUR_IMAGES_FOLDER_PATH" # 图片所在文件夹的地址

file_names = []
for file_name in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, file_name)):
        file_names.append(file_name)

for files in file_names:
    url = "https://img.saltfish.club/upload"
    file_path = folder_path+"/"+files

    with open(file_path, "rb") as file:
        files = {"image": file}  
        response = requests.post(url, files=files)

    print(file_path+response.text)
    time.sleep(1) # 防止服务器带宽不够引起上传失败，减缓上传速度
```
## 私有部署

### Docker部署

看到没，项目里有个DockerFile文件，拉好文件后执行

```bash
docker build -t imageserver .
```

构建好镜像之后运行一个容器：

```bash
docker run -p 4399:4399 imageserver -d
```

运行开始之后想要查看日志：

```bash
docker ps
docker logs -f <容器id>
```

### 裸机运行

进入项目文件夹下

```bash
node server.js
```


