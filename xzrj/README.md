## 13. 惜字如金 2.0

惜字如金一向是程序开发的优良传统。无论是「creat」还是「referer」，都无不闪耀着程序员「节约每句话中的每一个字母」的优秀品质。上一届信息安全大赛组委会在去年推出「惜字如金化」（XZRJification）标准规范后，受到了广大程序开发人员的好评。现将该标准辑录如下。

#### 惜字如金化标准

惜字如金化指的是将一串文本中的部分字符删除，从而形成另一串文本的过程。该标准针对的是文本中所有由 52 个拉丁字母连续排布形成的序列，在下文中统称为「单词」。一个单词中除「`AEIOUaeiou`」外的 42 个字母被称作「辅音字母」。整个惜字如金化的过程按照以下两条原则对文本中的每个单词进行操作：

- 第一原则（又称 creat 原则）：如单词最后一个字母为「`e`」或「`E`」，且该字母的上一个字母为辅音字母，则该字母予以删除。
- 第二原则（又称 referer 原则）：如单词中存在一串全部由完全相同（忽略大小写）的辅音字母组成的子串，则该子串仅保留第一个字母。

容易证明惜字如金化操作是幂等的：惜字如金化多次和惜字如金化一次的结果相同。

#### 你的任务

附件包括了一个用于打印本题目 flag 的程序，且已经经过惜字如金化处理。你需要做的就是得到程序的执行结果。

#### 附注

本文已经过惜字如金化处理。解答本题不需要任何往届比赛的相关知识。

### 题目描述

> 附件：[print_flag.py](./print_flag.py)

一个被暴力惜字如金后出现损坏的程序，还原后应当可以打印出 flag。

### 尝试与解决

> 关键词：推理

首先先简单恢复一下程序，

```python
#!/usr/bin/python3

# The size of the file may reduce after XZRJification

def check_equals(left, right):
    # check whether left == right or not
    if left != right: exit(1)

def get_code_dict():
    # prepare the code dict
    code_dict = []
    code_dict += ['nymeh1niwemflcir}echaet']
    code_dict += ['a3g7}kidgojernoetlsup?h']
    code_dict += ['ulw!f5soadrhwnrsnstnoeq']
    code_dict += ['ct{l-findiehaai{oveatas']
    code_dict += ['ty9kxborszstguyd?!blm-p']
    check_equals(set(len(s) for s in code_dict), {24})
    return ''.join(code_dict)

def decrypt_data(input_codes):
    # retrieve the decrypted data
    code_dict = get_code_dict()
    output_chars = [code_dict[c] for c in input_codes]
    return ''.join(output_chars)

if __name__ == '__main__':
    # check some obvious things
    check_equals('create', 'cre' + 'at')
    check_equals('referrer', 'refer' + 'rer')
    # check the flag
    flag = decrypt_data([53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
                         17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
                         31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
                         25, 63, 77, 36, 5, 32, 60, 67, 113, 28])
    check_equals(flag.index('flag{'), 0)
    check_equals(flag.index('}'), len(flag) - 1)
    # print the flag
    print(flag)
```

这题的核心是还原 `code_dict` 部分，每一行都是 23 个字符，少了个字符。

```python
def get_code_dict():
    # prepare the code dict
    code_dict = []
    code_dict += ['nymeh1niwemflcir}echaet']
    code_dict += ['a3g7}kidgojernoetlsup?h']
    code_dict += ['ulw!f5soadrhwnrsnstnoeq']
    code_dict += ['ct{l-findiehaai{oveatas']
    code_dict += ['ty9kxborszstguyd?!blm-p']
    check_equals(set(len(s) for s in code_dict), {24})
    return ''.join(code_dict)
```

如果不对 `code_dict` 做更改，flag 的前五个字符 `flag{` 和最后一个字符 `}` 会在这些地方：

```python
    code_dict += ['nymeh1niwemflcir}echaet']
    code_dict += ['a3g7}kidgojernoetlsup?h']
                 #     }            l
    code_dict += ['ulw!f5soadrhwnrsnstnoeq']
                 #      f
    code_dict += ['ct{l-findiehaai{oveatas']
                 #    {         a
    code_dict += ['ty9kxborszstguyd?!blm-p']
                 #              g
```

因此一种可能的还原是（插入的字符用 `#` 标示）：

```python
    code_dict += ['nymeh1niwemflcir}echaet#']
                 #                        #
    code_dict += ['a3g7}kidgojernoetl#sup?h']
                 #     }            l#
    code_dict += ['ulw!#f5soadrhwnrsnstnoeq']
                 #     #f
    code_dict += ['ct#{l-findiehaai{oveatas']
                 #   #{         a
    code_dict += ['ty9kxborszst#guyd?!blm-p']
                 #             #g
```

运行即可得到一个看起来很正常的 flag：

```plain
flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}
```

这个问号让人非常不自信，但是既然已经有一个 flag 了，为何不交呢？

### Flag

```plain
flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}
```

You've recovered the answer right? Yes!
