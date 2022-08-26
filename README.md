# abbreviate_journal_names_in_bib
### (In English)
One-sentence description: Quickly generate a bib file containing the items of all the references you want, and replace the full journal names in the file with official abbreviated names, or do the opposite.

Latex provides a wonderful method to include references in your paper. To do this, you need to save the information (title, journal, authours, year, etc) of your references into a `.bib` file. Each reference corresponds to an bib item, which can be copied from Google scholar.

However, if you have many bib items, it would be tedious to copy them all by hands. A better way is to pull the pdf files of these papers into Mendeley (a reference management software), and then output the bib items of all these papers using the output function of Mendeley.

But Mendeley often outputs some unnecessary information of papers, such as abstract，DOI，keywords. I write a bash file update_bib_from_mendeley.sh to remove these content. Additionally, Mendeley sometimes would mistake the type of some papers into 'generic' or 'report', which actually should be 'article'. I also add some commands into my bash file to remove these errors.

Usage of update_bib_from_mendeley.sh: In windows, put this file and your library.bib file under the same directory, and then double click the bash file; In Linux, `. update_bib_from_mendeley.sh` or `source update_bib_from_mendeley.sh`.

In this way you can quickly get a library.bib file, but the journals in this file are in their full names, while many publishers require them to be abbriviated. I write a python code to replace the full names in a bib file into their official abbreviated names. This code needs a reference file journal_list.txt which keeps most journal's full names and the corresponding official abbreviated names.

Usage of abbriviate.py: `python abbriviate.py library.bib`

I also write a python code extend.py to do the reverse thing, i.e., extending the abbreviated names into their full form. As a result, each time you only need to update one of the bib files.

### (In Chinese)
一句话描述：快速生成一个bib文件，里面包含你想要的所有参考文献的条目，把文件中的期刊全名替换成官方缩写名，或者反之。更多信息见知乎文章：https://zhuanlan.zhihu.com/p/503375837。

Latex提供了很方便的文献引用。你需要把你想引用的文献的信息（题目，期刊，作者，年份，等等）存入一个bib文件。每篇文献对应一个bib item，这些item都可以从谷歌学术上下载到。

但如果需要加入大量的items，一个一个下载太tedious了，更好的办法是把这些文章的pdf全部拖入Mendeley（或者手动载入信息），然后用Mendeley一次性全部导出bib形式的items。

但是这些items包含了很多不必要的信息，比如abstract，DOI，keywords，所以我写了一个脚本update_bib_from_mendeley.sh来删除这些内容。此外，Mendeley有时候会把文章类型错弄成generic或report，我也用上面的脚本把它们更改为article。脚本使用方法：windows下把它和其他文件放到同一目录下，然后双击；Linux下，直接`. update_bib_from_mendeley.sh` 或者 `source update_bib_from_mendeley.sh`。

这样得到的library.bib包含了完整的期刊名。很多杂志要求用期刊名的缩写。同样，一个一个改太慢了，我写了abbriviate.py，又下载了最全的期刊名全写与缩写的对照表，存于journal_list.txt，
使用方法：`python abbriviate.py library.bib`
就能得到期刊名缩写的library_abbreviated.bib。

我又写了extend.py来实现逆转换。后面只需要更新一个，另一个用代码转换即可。
