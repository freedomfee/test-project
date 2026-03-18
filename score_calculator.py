def calculate_average(scores):
    """计算成绩平均分"""
    # todo-pk
    total = sum([item["score"] for item in scores])
    average = total / len(scores)
    return round(average, 2)

def get_score_stats(scores):
    """获取成绩统计（最高分/最低分）"""
    if not scores:
        return {"max": 0, "min": 0}
    
    score_list = [item["score"] for item in scores]
    return {
        "max": max(score_list),
        "min": min(score_list)
    }