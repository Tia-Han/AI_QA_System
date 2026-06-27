# AI开发任务说明书（Cursor / Claude Code）

## 项目目标

请开发一个《小型人工智能基础问答系统》。

技术要求：

* Python
* Streamlit
* Python标准库
* Git管理

禁止使用：

* 数据库
* 大语言模型
* 向量数据库
* 第三方分词库

---

# Task 1：创建项目

创建以下目录：

```
AI_QA_System/

app.py
knowledge.py
matcher.py
history.py
utils.py

requirements.txt
README.md
```

---

# Task 2：知识库模块

创建 knowledge.py。

要求：

* 使用 Dictionary
* 包含20条人工智能基础知识
* 每条数据包含：

```
question

answer

keywords
```

keywords 使用 List 保存。

---

# Task 3：关键词匹配

创建 matcher.py。

要求：

实现函数：

```
match_question(user_question)
```

实现流程：

* 提取用户关键词
* 转为 Set
* 与知识库关键词计算交集
* 返回交集最大的答案
* 若没有匹配，返回默认提示

---

# Task 4：历史记录

创建 history.py。

要求：

使用 List 保存用户历史问题。

提供：

```
add_history()

get_history()
```

---

# Task 5：Streamlit 页面

创建 app.py。

页面包含：

* 标题
* 输入框
* 查询按钮
* 回答区域
* 历史记录

点击查询后：

调用 matcher.py 返回答案。

---

# Task 6：README

编写 README：

包含：

* 项目介绍
* 环境安装
* 启动方式

```
pip install streamlit

streamlit run app.py
```

---

# Task 7：代码要求

要求：

* 添加函数注释
* 添加必要注释
* 模块之间职责清晰
* 不允许重复代码

---

# Task 8：测试

完成后请检查：

✅ 可以正常启动

✅ 可以连续提问

✅ 可以查看历史记录

✅ 可以正确匹配答案

✅ 未匹配时提示默认信息

若发现 Bug，请自动修复并优化代码。

最后输出完整项目代码。
