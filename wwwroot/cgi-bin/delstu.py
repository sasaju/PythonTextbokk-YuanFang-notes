import libs
import cgi
import codecs, sys

print('Content-type:text/html \n\n')
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
form_data = cgi.FieldStorage()
stu_name = form_data['u_name'].value
libs.del_stu('data\\scores.txt', stu_name)
txt = libs.para('操作已完成.')
header = libs.get_header('删除数据')
urls = {'首页':'../index.html', '返回查询':'viewdata.py'}
footer = libs.get_footer(urls)
print(header+txt+footer)