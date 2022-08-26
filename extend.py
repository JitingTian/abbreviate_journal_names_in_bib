# 本代码将bib file中的academic journals缩写名改成全名，并保存为一个新文件。
# 配套的journal_list.txt包含了几乎所有journals的全名-缩写名；如果没有，可以在http://www.ncbi.nlm.nih.gov/nlmcatalog/journals查询后手动添加。

import os
import re
import sys

# 1. 将bib file的内容存入一个超长string
try:
    bibname = sys.argv[1]
    bibcontent = ''.join(open(bibname, 'r', errors='ignore').readlines())
except IndexError:
    print("Error: Specify the file to be processed!")
    exit(1)
except FileNotFoundError:
    print("Error: Provided filename could not be loaded!")
    exit(1)

# 2. 逐个读取journal_list.txt中的全名-缩写名，并用全名替换超长string中的缩写名
fr = open('journal_list.txt', 'r', errors='ignore')
line = fr.readline()

while(line):
    # 全名在前，缩写名在后
    full, short = line[:-1].split(" = ")[:2]
    # 加{}来变成bib里的期刊名部分，替换以{full}-{short}形式进行，避免替换半个期刊名
    full, short = '{%s}'%full, '{%s}'%short
    
    # 全为大写或只含一个单词的期刊缩写名不需要被替换 
    if short != short.upper() and (' ' in short):
        # 生成一个正则表达式对象，注意用escape取消{和}的特殊含义，并且忽略大小写
        pattern = re.compile(re.escape(short), re.IGNORECASE)
        
        # 用正则表达式对象的subn method实现替换和统计
        (bibcontent, num_repl) = pattern.subn(full, bibcontent)
        
        # 输出替换某个期刊名的次数
        if num_repl > 0:
            print("%i replacements of %s by %s" % (num_repl, short, full))
    
    # 读取下一个期刊
    line = fr.readline()

# 3. 将替换后的超长string写入新文件
with open('library_full.bib', 'w') as outfile:
    outfile.write(bibcontent)
    print("Bibtex database with full names saved into 'library_full.bib'")