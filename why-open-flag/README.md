## 19. 为什么要打开 /flag 😡

> 至少见一面让我当面道歉好吗？😭我也吓了一跳，没想到事情会演变成那个样子……😭所以我想好好说明一下😭我要是知道就会阻止它们的，但是明明文件描述符都已经关闭了突然间开始 open()😭没能阻止大家真是对不起……😭你在生气对吧……😭我想你生气也是当然的😭但是请你相信我。/flag，本来没有在我们的预定打开的文件里的😭真的很对不起😭我答应你再也不会随意打开文件了😭我会让各个函数保证再也不打开这个文件😭能不能稍微谈一谈？😭我真的把这里的一切看得非常重要😭所以说，擅自打开 /flag 的时候我和你一样难过😭我希望你能明白我的心情😭拜托了。我哪里都会去的😭我也会好好跟你说明我不得不这么做的理由😭我想如果你能见我一面，你就一定能明白的😭我是你的同伴😭我好想见你😭
---

挽留失败后，她决定在程序启动时做些手脚，让所有访问 `/flag` 的请求都以某种方式变成打开 `/fakeflag` 的请求。

「我不会再打开 `/flag` 了」。真的吗？

[题目附件下载](./fakeflag-backend.zip)（第二小题需要 Linux kernel >= 5.9）

### 题目描述

> 网址：http://202.38.93.111:10140/

这是一个用来提交二进制文件（Linux ELF）的界面。

- 子问题 1：LD_PRELOAD, love! [LD_PRELOAD]
- 子问题 2：都是 seccomp 的错 [seccomp-unotify]

### 尝试与解决

> 关键词：LD_PRELOAD、静态链接

#### LD_PRELOAD

首先搜索，知道 [LD_PRELOAD 是什么](https://zhuanlan.zhihu.com/p/598346458)。

> LD_PRELOAD是Linux/Unix系统的一个环境变量，它可以影响程序的运行时的链接，它允许在程序运行前定义优先加载的动态链接库。通过这个环境变量，可以在主程序和其动态链接库的中间加载别的动态链接库，甚至覆盖系统的函数库。

也就是让程序优先使用自定义的动态链接库，覆盖系统的函数。看一下附件中的 `lib.c`，果真如此。`lib.c` 覆盖了包括 `freopen` `fopen` `open` `openat` 在内的函数，还禁用了 `system` `execl` 等函数阻止程序通过调用外部程序绕开限制。

但是等等，动态链接？

哦...

```cpp
#include <stdio.h>
#include <stdlib.h>

char buf[2048];

int main(int argc, char **argv) {
    FILE *fp = fopen("/flag", "r");
    fgets(buf, 2048, fp);
    printf("%s\n", buf);
}
```

```plain
$ gcc --static main.c -o main # 静态链接
```

好的，已经结束力！

#### seccomp-unotify

Seccomp 是监视或限制程序使用系统调用的手段，一旦设置不能取消，并且会继承到子进程中，无法通过调用外部程序绕过。

代码 `main.rs` 的意思似乎是劫持 `open` 和 `openat`，但是不知道为什么，`name_to_handle_at` `openat2` `symlink` 等各类系统调用都失效了，会获得 `128: Operation already in progress` 错误。这就没活了。

### Flag

```plain
flag{nande_ld_preload_yattano_d7b67c550b}
```
