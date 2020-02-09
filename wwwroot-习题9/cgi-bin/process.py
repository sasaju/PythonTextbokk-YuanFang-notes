s_header = '''
<html>
<head>
<title>中转页面</title>
</head>
</html>
'''
s_footer = '''
</body>
</html>
'''
admin = '''
<body>
<h3>登陆成功</h3>
<h3>单击下方链接，进入书籍修改界面</h3>
<p><a href="viewdata_admin.py">开始修改</a></p>
'''
unadmin = '''
<body>
<h3>登陆失败</h3>
<h3>单击下方链接，进入返回游客界面</h3>
<p><a href="viewdata.py">返回</a></p>
'''
import libs
import cgi

form = cgi.FieldStorage()
user_name = form['u_name'].value
user_psw = form['u_psw'].value

if user_name=='admin' and user_psw == '123456':
    s_body = admin
else:
    s_body = unadmin

s_page = s_header + s_body + s_footer
print(s_page)
