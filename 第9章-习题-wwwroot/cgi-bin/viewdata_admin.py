import libs
import codecs, sys

print('Content-type:text/html \n\n')
admin='True'
# 保证浏览器以utf-8浏览文本
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
# 获取模板header.html内容并将$title替换为文字“数据查询”
header = libs.get_header("数据查询")
# 使用socres.txt内容产生数据表
table = libs.show_data('data/scores.txt')
urls={'返回首页':'../index.html'}   # 设置urls字典
# 获取模板footer.html内容,并将$title替换为urls字典生成的超级链接标签
footer = libs.get_footer(urls)
if admin=='True':
    # 生成增加书籍简介的表单HTML代码
    start_add_form = libs.start_form('addstu.py')
    add_text = libs.para('增加书籍简介')
    add_items = libs.form_inputboxs({'u_name':'书籍','u_score':'简介'})
    end_add_form = libs.end_form('增加')
    txt_add = start_add_form + add_text + add_items + end_add_form
    # 生成修改书籍简介的HTML代码
    start_update_form = libs.start_form('update.py')
    update_text = libs.para('修改书籍简介')
    update_items = libs.form_inputboxs({'u_name':'书籍', 'u_score':'简介'})
    end_update_form = libs.end_form('修改')
    txt_update = start_update_form + update_text +update_items +end_update_form
    # 生成删除书籍记录的HTML代码
    start_del_form = libs.start_form('delstu.py')
    del_text = libs.para('删除书籍记录')
    del_items = libs.form_inputboxs({'u_name':'书籍'})
    end_del_form = libs.end_form('删除')
    txt_del = start_del_form + del_text + del_items + end_del_form
    # 将以上代码组合输出至浏览器
    print(header+table+txt_add+txt_update+txt_del+footer)
else:
    login_code = """
    <h1>输入用户名和密码，单击登陆</h1>
<form action="process.py" method="POST">
用户名：<input type="text" name="u_name" size="40"/><br/>
密码：<input type="text" name="u_psw" size="40"/><br/>
<input type="submit" value="登陆"></form>
    """
    print(header+table+login_code+footer)
