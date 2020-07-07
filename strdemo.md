# 字符串 方法
1. capitalize（）将字符串的第一个字符转换为大写
2. center（width，fillchar）返回一个指定的宽度width居中的字符串，fillchar为填充的字符，默认为空格。
3. count（str，beg=0，end=len（string）返回 str在string里面出现的次数，如果beg或者end指定则返回指定范围内 str出现的次数
4. bytes.decode（encoding="utf-8"，errors="strict"）Python3中没有 decode方法，但我4们可以使用bytes对象的decode（）方法来解码给定的bytes对象，这个bytes对象可以由str.encode（）来编码返回。
5. encode（encoding='UTF-8，errors='strict）以encoding指定的编码格式编码字符串，如果出错默认报一个ValueError的异常，除非 errors 指定的是ignore'或者’replace'
6. endswith（suffix，beg=0，end=len（string））检查字符串是否以obj结束，如果beg 或者end指定则检查指定的范围内是否以obj结束，如果是，返回True，否则返回False.
7. expandtabsttabsize=8）把字符串 string中的tab符号转为空格，tab符号默认的空格数是8。
8. rstrip() 删除字符串字符串末尾的空格
9. find(str, beg=0, end=len(string)) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
10. index(str, beg=0, end=len(string)) 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
11. isalnum() 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回False
12. isalpha() 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
13. isdigit() 如果字符串只包含数字则返回 True 否则返回 False
14. islower() 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
15. isnumeric() 如果字符串中只包含数字字符，则返回 True，否则返回 False
16. isspace() 如果字符串中只包含空白，则返回 True，否则返回 False
17. istitle() 如果字符串是标题化的(见 title())则返回 True，否则返回 False
18. isupper() 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
19. join(seq) 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
20. len(string) 返回字符串长度
21. [ljust(width, fillchar]) 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格
22. lower() 转换字符串中所有大写字符为小写
23. lstrip() 截掉字符串左边的空格或指定字符
24. maketrans() 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标
25. max(str) 返回字符串 str 中最大的字母
26. min(str) 返回字符串 str 中最小的字母
27. [replace(old, new , max]) 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次
28. rfind(str, beg=0,end=len(string)) 类似于 find()函数，不过是从右边开始查找
30. rindex( str, beg=0, end=len(string)) 类似于 index()，不过是从右边开始
31. [rjust(width,, fillchar]) 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度width 的新字符串

