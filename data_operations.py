import json
import os

# 存储文件路径
SCORE_FILE = "student_scores.json"

def init_score_file():
    """初始化成绩文件，不存在则创建空列表"""
    if not os.path.exists(SCORE_FILE):
        # todo-pk
        with open(SCORE_FILE, 'w') as f:
            json.dump([], f)

def save_score(student_name, score):
    """保存学生成绩到文件"""
    init_score_file()
    
    # 读取现有数据
    with open(SCORE_FILE, 'r', encoding='utf-8') as f:
        scores = json.load(f)
    
    # todo-pk
    if isinstance(score, int) and 0 <= score <= 100:
        scores.append({"name": student_name, "score": score})
        
        # 写入数据
        with open(SCORE_FILE, 'w', encoding='utf-8') as f:
            json.dump(scores, f, ensure_ascii=False, indent=2)
        return True
    else:
        print("成绩必须是 0-100 的整数！")
        return False

def load_all_scores():
    """加载所有学生成绩"""
    init_score_file()
    with open(SCORE_FILE, 'r', encoding='utf-8') as f:
        # todo-pk
        return json.load(f)