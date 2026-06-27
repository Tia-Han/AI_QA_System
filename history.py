"""
历史记录模块

使用List保存用户的问答历史记录，
提供添加、获取和清空历史记录的功能。
"""

from datetime import datetime


# 全局历史记录列表
history_list = []


def add_history(question, answer):
    """
    添加一条问答历史记录

    Args:
        question (str): 用户提出的问题
        answer (str): 系统返回的答案

    Returns:
        None
    """
    # 创建历史记录项，包含问题、答案和时间戳
    history_item = {
        "question": question,
        "answer": answer,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    # 将记录添加到历史列表
    history_list.append(history_item)


def get_history():
    """
    获取所有历史记录

    Returns:
        list: 包含所有问答历史记录的列表，
              每条记录包含question、answer和timestamp字段
    """
    return history_list


def clear_history():
    """
    清空所有历史记录

    Returns:
        None
    """
    # 清空历史记录列表
    history_list.clear()


def get_history_count():
    """
    获取历史记录的数量

    Returns:
        int: 历史记录的总数量
    """
    return len(history_list)