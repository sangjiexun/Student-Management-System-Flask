# 学生管理系统

## 项目简介
学生管理系统是一个基于Flask框架开发的学生信息管理平台，提供学生信息录入、查询、修改和管理等功能，帮助学校和教育机构实现学生信息的数字化管理，提高管理效率和准确性。

## 技术架构

### 后端技术
- **Flask**: Python Web框架
- **Flask-SQLAlchemy**: ORM数据库工具
- **Flask-Login**: 用户认证管理
- **Flask-WTF**: 表单处理和验证
- **SQLite**: 轻量级数据库

### 前端技术
- **HTML5/CSS3/JavaScript**: 前端基础
- **Jinja2**: 模板引擎
- **Bootstrap**: 响应式UI框架

### 项目结构
```
flask_studentManagement/
├── app.py                # 主应用文件
├── config.py             # 配置文件
├── models.py             # 数据库模型
├── forms.py              # 表单定义
├── routes.py             # 路由定义
├── templates/
│   ├── base.html         # 基础布局
│   ├── index.html        # 首页
│   ├── login.html        # 登录页面
│   ├── register.html     # 注册页面
│   ├── students.html     # 学生列表
│   ├── student_detail.html # 学生详情
│   ├── add_student.html  # 添加学生
│   ├── edit_student.html # 编辑学生
│   └── admin.html        # 管理员页面
└── static/
    ├── css/              # 样式文件
    └── js/               # JavaScript文件
```

## 核心功能

### 用户管理
- 用户注册与登录
- 权限控制（普通用户/管理员）

### 学生信息管理
- 学生基本信息管理（姓名、性别、年龄、学号等）
- 学生联系方式管理
- 学生照片上传

### 班级管理
- 班级信息管理
- 班级学生分配

### 成绩管理
- 学生成绩录入
- 成绩查询与统计
- 成绩分析与报表

### 考勤管理
- 学生考勤记录
- 考勤统计与分析

### 搜索与查询
- 学生信息搜索（按姓名、学号、班级等）
- 多条件组合查询
- 数据导出功能

## 数据库模型

### 主要模型
- **User**: 用户信息
- **Student**: 学生信息
- **Class**: 班级信息
- **Grade**: 成绩信息
- **Attendance**: 考勤信息

## 安装与运行

### 环境要求
- Python 3.6+
- pip包管理器

### 安装步骤
1. 克隆仓库
   ```bash
   git clone https://github.com/sangjiexun/Student-Management-System-Flask.git
   cd Student-Management-System-Flask
   ```

2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

3. 初始化数据库
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

4. 运行应用
   ```bash
   python app.py
   ```

5. 访问应用
   打开浏览器访问 http://localhost:5000

## 配置说明

### 数据库配置
默认使用SQLite数据库，可在`config.py`中修改：

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///student.db'
```

### 应用配置
```python
SECRET_KEY = 'your-secret-key'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## 安全措施
- 密码哈希存储
- CSRF保护
- 权限控制
- 输入验证

## 部署建议
- 使用Gunicorn作为WSGI服务器
- 使用Nginx作为反向代理
- 配置HTTPS
- 数据库定期备份

## 贡献指南
欢迎提交Issue和Pull Request来改进这个项目。

## 许可证
MIT License

---

# Student Management System

## Project Introduction
Student Management System is a student information management platform developed based on the Flask framework, providing student information entry, query, modification and management functions to help schools and educational institutions realize digital management of student information, improve management efficiency and accuracy.

## Technical Architecture

### Backend Technology
- **Flask**: Python Web framework
- **Flask-SQLAlchemy**: ORM database tool
- **Flask-Login**: User authentication management
- **Flask-WTF**: Form handling and validation
- **SQLite**: Lightweight database

### Frontend Technology
- **HTML5/CSS3/JavaScript**: Frontend basics
- **Jinja2**: Template engine
- **Bootstrap**: Responsive UI framework

### Project Structure
```
flask_studentManagement/
├── app.py                # Main application file
├── config.py             # Configuration file
├── models.py             # Database models
├── forms.py              # Form definitions
├── routes.py             # Route definitions
├── templates/
│   ├── base.html         # Base layout
│   ├── index.html        # Home page
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── students.html     # Student list
│   ├── student_detail.html # Student details
│   ├── add_student.html  # Add student
│   ├── edit_student.html # Edit student
│   └── admin.html        # Admin page
└── static/
    ├── css/              # Style files
    └── js/               # JavaScript files
```

## Core Features

### User Management
- User registration and login
- Permission control (ordinary user/admin)

### Student Information Management
- Student basic information management (name, gender, age, student ID, etc.)
- Student contact information management
- Student photo upload

### Class Management
- Class information management
- Class student allocation

### Grade Management
- Student grade entry
- Grade query and statistics
- Grade analysis and report

### Attendance Management
- Student attendance recording
- Attendance statistics and analysis

### Search and Query
- Student information search (by name, student ID, class, etc.)
- Multi-condition combination query
- Data export function

## Database Models

### Main Models
- **User**: User information
- **Student**: Student information
- **Class**: Class information
- **Grade**: Grade information
- **Attendance**: Attendance information

## Installation and Running

### Environment Requirements
- Python 3.6+
- pip package manager

### Installation Steps
1. Clone the repository
   ```bash
   git clone https://github.com/sangjiexun/Student-Management-System-Flask.git
   cd Student-Management-System-Flask
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

4. Run the application
   ```bash
   python app.py
   ```

5. Access the application
   Open a browser and visit http://localhost:5000

## Configuration Instructions

### Database Configuration
SQLite is used by default, which can be changed in `config.py`:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///student.db'
```

### Application Configuration
```python
SECRET_KEY = 'your-secret-key'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Security Measures
- Password hash storage
- CSRF protection
- Permission control
- Input validation

## Deployment Recommendations
- Use Gunicorn as WSGI server
- Use Nginx as reverse proxy
- Configure HTTPS
- Regular database backups

## Contribution Guide
Welcome to submit Issues and Pull Requests to improve this project.

## License
MIT License