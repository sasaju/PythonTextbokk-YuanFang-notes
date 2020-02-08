# 引入string库中的Template模块，用于模板字符串的替换
from string import Template

# get_header()函数用于读取模板文件header.html的内容
# 并用参数title_txt(字符串数据)替换模板文件中的$title
def get_header(title_txt):
    with open('template/header.html', 'r', encoding='utf-8') as f:
        txt = f.read()
    txt = Template(txt)         # 将字符串txt转换为Template类型对象
    # substitute()的作用是将txt中的$title替换为变量title_txt的值
    # 并返回txt中的整个字符串数据
    return txt.substitute(title=title_txt)

def get_footer(urls):
    """
    与get_header()类似，参数urls为字典型数据
    """
    with open('template/footer.html', 'r', encoding='utf-8') as f:
        txt = f.read()
    txt_links = ' | '
    
    for name, url in urls.items():
        txt_links = txt_links + '<a href="'+url+'">'+name+'</a>|'
    txt = Template(txt)
    return txt.substitute(urls=txt_links)

def show_data(filename):
    """
    show_data()函数的参数为文件名，用于不读取成绩数据文件
    并将其置于<table></table>表格标签中
    <tr></tr>为表格中的行标签，<td></td>为行标签中的单元格标签
    """
    txt_table = '<table border="1" cellpadding="10" width="200px">'
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            data-line.split(',')
            txt_table += '<tr>'
            for item in data:
                txt_table = txt_table + '<td align="center">' + item + '</td>'
                txt_table += '</tr>'
            txt_table += '</table>'
            return txt_table

def start_form(act_url):
    """
    用于产生网页表单前半部分
    并将表单提交地址设置为参数act_url的值
    """
    txt_form = '<form action="'+act_url+'"method="POST">'
    return txt_form

def form_inputboxs(data):
    """
    form_inputboxs()的参数data为字典类型，其功能是data的数据设置为
    文本框的提示文字和name属性，“键”为提示文字，“值”为name属性
    """
    txt = '</p>'
    for name, text in data.items():
        txt = txt + text + ':<input type="text"name="'+name+'"size=20/><br/>'
    txt = txt + '</p>'
    return txt

def end_form(txt='提交'):
    """
    用于产生表单的后半部分，并提供一个提交按钮，该按钮的显示文字
    由参数txt决定，txt的默认值为"提交"
    """
    txt_form = '<input type="submit"value="'+txt+'"><hr width="250px"\
        align="left"/></form>'
    return txt_form

def para(txt):
    """
    用于为数据的字符串txt增加html段落标签
    """
    return '<p>'+txt+'</p>'

def add_stu_score(filename, stuname, stuscore):
    """
    用于将学生姓名和学生分数值
    追加到filename提供的文件中
    """
    with open(filename, 'a+', encoding='utf-8') as f:
        f.write(stuname+','+stuscore+'\n')

def del_stu(filename, stuname):
    """
    用于将学生姓名和成绩值从filename提供的文件中删除
    """
    stu_dict={}
    with open(filename, 'r', encoding='utf-8') as f:
        for item in f:
            name, score = item.strip().split(',')
            stu_dict[name] = score
        if stu_dict.get(stuname) != None:
            stu_dict.pop(stuname)
        with open(filename, 'w', encoding='utf-8') as f:
            for name, score in stu_dict.items():
                f.write(name+','+score+'\n')

def update_stu(filename, stuname, stuscore):
    """用于更新filename中的学生姓名和成绩"""
    stu_dict = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for item in f:
            name, score = item.strip().split(',')
            stu_dict[name] = score
    if stu_dict.get(stuname) != None:
        stu_dict[stuname] = stuscore
    with open(filename, 'w', encoding='utf-8') as f:
        for name, score in stu_dict.items():
            f.write(name+','+score+'\n')
