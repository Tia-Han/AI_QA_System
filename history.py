"""
历史记录模块

使用List保存用户的问答历史记录，并持久化到JSON文件，
确保重启后历史记录不会丢失。
提供添加、获取和清空历史记录的功能。
"""

import json
import os
from datetime import datetime

# 历史记录文件路径
HISTORY_FILE = os.path.join(os.path.dirname(__file__), "history.json")

# 全局历史记录列表
history_list = []


def _load_history():
    """
    从JSON文件加载历史记录

    Returns:
        None
    """
    global history_list
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history_list = json.load(f)
        except (json.JSONDecodeError, IOError):
            history_list = []


def _save_history():
    """
    将历史记录保存到JSON文件

    Returns:
        None
    """
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history_list, f, ensure_ascii=False, indent=2)
    except IOError:
        pass


def add_history(question, answer):
    """
    添加一条问答历史记录

    Args:
        question (str): 用户提出的问题
        answer (str): 系统返回的答案

    Returns:
        None
    """
    history_item = {
        "question": question,
        "answer": answer,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    history_list.append(history_item)
    _save_history()


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
    history_list.clear()
    _save_history()


def get_history_count():
    """
    获取历史记录的数量

    Returns:
        int: 历史记录的总数量
    """
    return len(history_list)


_load_history()