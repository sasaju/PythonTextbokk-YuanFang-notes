import libs
import cgi
import codecs, sys

print('Content-type:text/html \n\n')
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
# form_data使用cgi库的FieldStorage()方法获取表单提交出来的数据
form_data = cgi.FieldStorage()
stu_name = form_data['u_name'].value    # 获取表单元素u_name
stu_score = form_data['u_score'].value  # 获取表单元素u_score
libs.add_stu_score('data\\scores.txt', stu_name, stu_score)
txt = libs.para('{},成绩{},已添加.'.format(stu_name, stu_score))
header = libs.get_header('增加数据')
urls = {'首页':'../index.html','返回查询':'viewdata.py'}
footer = libs.get_footer(urls)
print(header+txt+footer)
