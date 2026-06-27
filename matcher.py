"""
匹配器模块

基于关键词交集匹配用户问题与知识库，
返回最相关的答案。
"""

from knowledge import get_knowledge_base


def extract_keywords(user_question, all_keywords):
    """
    从用户输入中提取匹配的关键词

    Args:
        user_question (str): 用户输入的问题
        all_keywords (set): 知识库中所有关键词的集合

    Returns:
        set: 用户问题中包含的关键词集合
    """
    matched = set()
    for kw in all_keywords:
        if kw in user_question:
            matched.add(kw)
    return matched


def match_question(user_question):
    """
    匹配用户问题，返回最相关的答案

    基于关键词交集计算：
    1. 提取用户输入中的关键词
    2. 转换为Set
    3. 与知识库每条数据的keywords求交集
    4. 返回交集最大的答案
    5. 若无匹配，返回默认提示

    Args:
        user_question (str): 用户输入的问题

    Returns:
        str: 匹配到的答案或默认提示
    """
    kb = get_knowledge_base()

    # 收集所有关键词，使用set去重
    all_keywords = set()
    for item in kb.values():
        all_keywords.update(item["keywords"])

    user_keywords = extract_keywords(user_question, all_keywords)

    if not user_keywords:
        return "抱歉，没有找到相关答案。"

    best_match = None
    max_intersection = 0

    for item in kb.values():
        kw_set = set(item["keywords"])
        intersection = user_keywords & kw_set
        intersection_size = len(intersection)
        if intersection_size > max_intersection:
            max_intersection = intersection_size
            best_match = item

    if best_match is None or max_intersection == 0:
        return "抱歉，没有找到相关答案。"

    return best_match["answer"]
