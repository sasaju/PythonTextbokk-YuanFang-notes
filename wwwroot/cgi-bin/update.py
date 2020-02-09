import libs
import cgi
import codecs, sys

print('Content-type:text/html \n\n')
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
form_data = cgi.FieldStorage()
stu_name = form_data['u_name'].value
stu_score = form_data['u_score'].value
libs.update_stu('data\\scores.txt', stu_name, stu_score)
txt = libs.para('{},成绩{},已更新.'.format(stu_name, stu_score))
header = libs.get_header('更新数据')
urls={'首页':'../index.html', '返回查询':'viewdata.py'}
footer = libs.get_footer(urls)
print(header+txt+footer)
