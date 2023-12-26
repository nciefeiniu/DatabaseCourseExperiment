# 学生管理系统
## 概述
数据库实验作业，通过一个数据库具体设计实例，掌握数据库设计的方法。  

## 系统功能
系统功能要求：  
1）新生入学信息增加，学生信息修改。  
2）课程信息维护（增加新课程，修改课程信息，删除没有选课的课程信息）。  
3）录入学生成绩，修改学生成绩。  
4）按系统计学生的平均成绩、最好成绩、最差成绩、优秀率、不及格人数。  
5）按系对学生成绩进行排名，同时显示出学生、课程和成绩信息。  
6）输入学号，显示该学生的基本信息和选课信息  

## 使用说明
### 程序的运行
首先，使用pip安装依赖
```bash
#根目录下
pip install -r requirements.txt
```

然后，执行__init__.py即可
```bash
#根目录下
python ./student_management/__init__.py
```
### 数据库的连接
需要先在mysql中创建指定的数据库才能连接  
连接建立后，程序会自动创建student,sc以及course表，然后自动创建constraint和trigger
由于mysql的安全策略，当`log_bin_trust_function_creators = 0`的时候（也就是默认设置），没有`SUPER`或`SYSTEM_VARIABLES_ADMIN`权限的用户无法创建触发器；为了创建trigger，请使用管理员账号登录或者设置`log_bin_trust_function_creators = 1`  
创建trigget或constraint之前，需要访问`information_schema`来确定之前是否已经创建相关规则；请确保用户有该数据库的访问权限  