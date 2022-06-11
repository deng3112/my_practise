import re

# content = "Hello 123 4567 World_This is a Regex Demo"
# print(len(content))
# result = re.match("^Hello\s\d\d\d\s\d{4}\s\w{10}",content)
"""用它来匹配这个长字符串。开头的 ^ 是匹配字符串的开头，
也就是以 Hello 开头；然后 \s 匹配空白字符，用来匹配目标字符串的空格；
\d 匹配数字，3 个 \d 匹配 123；然后再写 1 个 \s 匹配空格；后面还有 4567，
我们其实可以依然用 4 个 \d 来匹配，但是这么写比较烦琐，
所以后面可以跟 {4} 以代表匹配前面的规则 4 次，也就是匹配 4 个数字；
后面再紧接 1 个空白字符，最后的 \w{10} 匹配 10 个字母及下划线。我们注意到，
这里其实并没有把目标字符串匹配完，不过这样依然可以进行匹配，
只不过匹配结果短一点而已。"""
# print(result)
# print(result.group())
# print(result.span())

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# """这里可以使用括号 () 将想提取的子字符串括起来。
# () 实际上标记了一个子表达式的开始和结束位置，
# 被标记的每个子表达式会依次对应每一个分组，
# 调用 group 方法传入分组的索引即可获取提取的结果。"""
# print(result.group())
# print(result.group(1))
# """这里用的是 group(1)，它与 group()
# 有所不同，后者会输出完整的匹配结果，
# 而前者会输出第一个被 () 包围的匹配结果。"""
# print(result.span())

# content = "Hello 123 4567 World_This is a Regex Demo"
# result =re.match('^Hello.*Demo$',content)
# print(result)
# print(result.group())
# group 方法输出了匹配的全部字符串，
# 也就是说我们写的正则表达式匹配到了目标字符串的全部内容；
# span 方法输出 (0, 41)，这是整个字符串的长度。
# print(result.span())

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$', content)
# print(result)
# 这里我们依然想获取中间的数字，
# 所以中间依然写的是 (\d+)。而数字两侧由于内容比较杂乱，
# 所以想省略来写，都写成 .*。最后，组成 ^He.*(\d+).*Demo$，
# print(result.group(1))
# 在贪婪匹配下，.* 会匹配尽可能多的字符。
# 正则表达式中 .* 后面是 \d+，也就是至少一个数字，并没有指定具体多少个数字，
# 因此，.* 就尽可能匹配多的字符，这里就把 123456 匹配了，
# 给 \d+ 留下一个可满足条件的数字 7，最后得到的内容就只有数字 7 了。

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# 贪婪匹配是尽可能匹配多的字符，非贪婪匹配就是尽可能匹配少的字符。
# 当 .*? 匹配到 Hello 后面的空白字符时，再往后的字符就是数字了，
# 而 \d+ 恰好可以匹配，那么这里 .*? 就不再进行匹配，交给 \d+ 去匹配后面的数字。
# 所以这样 .*? 匹配了尽可能少的字符，\d+ 的结果就是 1234567 了。
# print(result.group(1))


html = '''
<div id="songs-list">
  <h2 class="title">经典老歌</h2>
  <p class="introduction">经典老歌列表</p>
  <ul id="list" class="list-group">
    <li data-view="2">一路上有你</li>
    <li data-view="7">
      <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
    </li>
    <li data-view="4" class="active">
      <a href="/3.mp3" singer="齐秦">往事随风</a>
    </li>
    <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
    <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
    <li data-view="5">
      <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
    </li>
  </ul>
</div>
'''

# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
# if result:
#     print(result.group(1),result.group(2))


# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if result:
#     print(result.group(1), result.group(2))
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])