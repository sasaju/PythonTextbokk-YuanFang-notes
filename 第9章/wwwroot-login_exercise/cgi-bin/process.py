s_header = '''
<html>
<head>
<title>Web Demo By Python</title>
</head>
</html>
'''
s_footer = '''
</body>
</html>
'''
import cgi

form = cgi.FieldStorage()
user_name = form['u_name'].value
user_psw = form['u_psw'].value

if user_name=='admin' and user_psw == '123456':
    s_body='<p>用户' + user_name + ',你好。你已成功登陆。</p>'
else:
    s_body='<p>你输入的用户名或密码错误</p>'

s_page = s_header + s_body + s_footer
print(s_page)
