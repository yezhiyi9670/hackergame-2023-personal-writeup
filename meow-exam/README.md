## 2. 猫咪小测

省流：猫咪问答续集

提示：解出谜题不需要是科大在校猫咪。

### 题目描述

> 网址：http://202.38.93.111:10001/

1. 想要借阅世界图书出版公司出版的《A Classical Introduction To Modern Number Theory 2nd ed.》，应当前往中国科学技术大学西区图书馆的哪一层？**（30 分）**  
   *提示：是一个非负整数。*
2. 今年 arXiv 网站的天体物理版块上有人发表了一篇关于「可观测宇宙中的鸡的密度上限」的论文，请问论文中作者计算出的鸡密度函数的上限为 10 的多少次方每立方秒差距？**（30 分）**  
   *提示：是一个非负整数。*
3. 为了支持 TCP BBR 拥塞控制算法，在**编译** Linux 内核时应该配置好哪一条内核选项？**（20 分）**  
   *提示：输入格式为 CONFIG_XXXXX，如 CONFIG_SCHED_SMT。*
4. 🥒🥒🥒：「我……从没觉得写类型标注有意思过」。在一篇论文中，作者给出了能够让 Python 的类型检查器 ~~MyPY~~ mypy 陷入死循环的代码，并证明 Python 的类型检查和停机问题一样困难。请问这篇论文发表在今年的哪个学术会议上？**（20 分）**  
   *提示：会议的大写英文简称，比如 ISCA、CCS、ICML。*

提交会显示总分，因此容易验证单个问题是否答对。几乎不限提交频率。

### 尝试与解决

> 关键词：枚举、GitHub 搜索、学术搜索

#### 适合枚举的问题

前两个问题的答案是非负整数。

西区图书馆是一个比较高的楼，但也不是太高，楼层数绝对不会超过 25。因此第一题经过简单枚举即可获得答案 12。

根据对物理常量的经验，第二题的答案也很难超过 120，同样采用枚举获得答案，为 23。

#### 启用 TCP BBR 的内核编译选项

在网上搜索 Linux TCP BBR，很难找到答案。许多搜索结果都是指出在 Linux 发行版中如何启用 TCP BBR，而不是编译时如何启用。即使加入“内核 编译”关键词似乎也无济于事。

这种情况并非无解。一个非常可靠的方法是，直接[前往 GitHub 搜索找到 Linux 内核源代码](https://github.com/torvalds/linux)。在代码仓库内搜索“TCP BBR”，可以找到 `net/ipv4/Makefile` 文件内的线索：

```makefile
obj-$(CONFIG_INET_TCP_DIAG) += tcp_diag.o
obj-$(CONFIG_INET_UDP_DIAG) += udp_diag.o
obj-$(CONFIG_INET_RAW_DIAG) += raw_diag.o
obj-$(CONFIG_TCP_CONG_BBR) += tcp_bbr.o
obj-$(CONFIG_TCP_CONG_BIC) += tcp_bic.o
obj-$(CONFIG_TCP_CONG_CDG) += tcp_cdg.o
obj-$(CONFIG_TCP_CONG_CUBIC) += tcp_cubic.o
```

这里的 `CONFIG_TCP_CONG_BBR` 就很可能是答案了。提交验证，确实是。

#### Python 类型检查死循环问题

寻找这样的论文，一个很好的去处是 Google 学术搜索。根据“Python 类型检查死循环”可以拟定关键词“python type check infinite loop”（注意死循环一般不叫“Dead loop”）。但是，这样找到的结果非常多，相关性也不够强。这里很可能存在的问题是，死循环“Infinite loop”很可能不会出现在论文的标题里。

但是，题面还给出了一句话，“Python 的类型检查和停机问题一样困难”。停机问题是指判断一个一般的图灵机在给定输入下能否停机（即能否运行结束），可以用反证法证明不存在一般的解法。因此，可以将“死循环”关键词换成“图灵完备”，即“Turing complete”。

现在就可以在 Arxiv 上找到一个看起来很像的论文了：[Python Type Hints are Turing Complete](https://arxiv.org/abs/2208.14755)。但是，Arxiv 并没有指出论文在什么学术会议上使用。不妨使用论文的标题再次进行网页搜索，很快就可以找到“ECOOP 2023”字样，看来 ECOOP 就是答案了。

### Flags

```plain
flag{w3lCoM3-7o-@7tEND-7HE-nEk0-EXAM-Z0z3}
```

```plain
flag{R3al-M@S73R-of-The-NekO-3X@M-iN-u$7c}
```
