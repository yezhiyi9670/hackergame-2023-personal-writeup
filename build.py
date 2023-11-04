import os
import shutil
import re

BUILD_DIR = './_build/'

shutil.rmtree(BUILD_DIR)
os.mkdir(BUILD_DIR)

def md_sanitize(content: str, label: str):
    lines = content.replace("\r\n", "\n").split("\n")
    try:
        index = lines.index('### 尝试与解决')
        lines = [lines[0], '', *lines[index:]]
    except ValueError:
        print('W: Solution header not found for ' + label)
        return content
    return "\n".join(lines)

def ref_paths(content: str):
    matches = re.findall(r'!\[(.*?)\]\((.*?)\)', content)
    r1 = list(map(lambda x: x[1], matches))
    matches = re.findall(r'<img(.+?)src="(.*?)"', content)
    r1 = r1 + list(map(lambda x: x[1], matches))
    return r1

dir_list = os.listdir('./')
for subdir in dir_list:
    subdir_path = './' + subdir + '/'
    md_path = subdir_path + 'README.md'
    dst_path = BUILD_DIR + subdir + '/'
    if not os.path.isdir(subdir_path) or not os.path.exists(md_path):
        continue
    print('I: Processing writeup for ' + subdir)
    os.mkdir(dst_path)

    md_content = open(md_path, 'r', encoding='utf-8').read()
    md_content = md_sanitize(md_content, subdir)
    print('I: Writing markdown for '+ subdir)
    open(dst_path + 'README.md', 'w', encoding='utf-8').write(md_content)

    refs = ref_paths(md_content)
    for ref in refs:
        ast_src = subdir_path + ref
        ast_dst = dst_path + ref
        ast_dstd = os.path.dirname(ast_dst)
        if not os.path.exists(ast_src):
            print('E: Referenced image ' + ref + ' does not exist')
            continue
        if not os.path.exists(ast_dstd):
            os.makedirs(ast_dstd)
        shutil.copyfile(ast_src, ast_dst)

print('I: Copying root README.md')
shutil.copyfile('README.md', BUILD_DIR + 'README.md')
shutil.copyfile('LICENSE', BUILD_DIR + 'LICENSE')
