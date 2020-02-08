import libs
import codecs, sys

# 保证浏览器以utf-8浏览文本
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
# 获取模板header.html内容并将$title替换为文字“数据查询”
header = libs.get_header("数据查询")
# 使用socres.txt内容产生数据表
table = libs.show_data('data\\scores.txt')
urls={'返回首页':'../index.html'}   # 设置urls字典
# 获取模板footer.html内容,并将$title替换为urls字典生成的超级链接标签
footer = libs.get_footer(urls)
# 生成增加学生成绩的表单HTML代码
start_add_form = lins.start_add_form('addstu.py')
add_text = libs.para('增加学生成绩')
add_items = libs.form_inputboxs({'u_name':'姓名','u_score':'成绩'})
end_add_form = libs.end_form('增加')
txt_add = start_add_form + add_text + end_add_form
# 生成修改学生成绩的HTML代码
start_update_form = libs.start_form('update.py')
update_text = libs.para('修改学生成绩')
update_items = libs.form_inputboxs({'u_name':'姓名', 'u_score':'成绩'})
end_update_form = libs.end_form('修改')
txt_update = start_update_form + update_text +update_items +end_update_form
# 生成删除学生记录的HTML代码
start_del_form = libs.start_form('delstu.py')
del_text = libs.para('删除学生记录')
del_items = libs.form_inputboxs({'u_name':'姓名'})
end_del_form = libs.end_form('删除')
txt_del = start_del_form + del_text + del_items + end_del_form
# 将以上代码组合输出至浏览器
print(header+table+txt_add+txt_update+txt_del+footer)
