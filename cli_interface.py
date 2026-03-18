import data_operations as do
import score_calculator as sc

def show_menu():
    """显示菜单"""
    print("\n===== 学生成绩管理系统 =====")
    print("1. 添加学生成绩")
    print("2. 查看所有成绩")
    print("3. 查看成绩统计（平均分/最高分/最低分）")
    print("4. 退出")
    print("============================")

def add_score():
    """添加成绩"""
    name = input("请输入学生姓名：")
    # todo-pk
    score = int(input("请输入成绩（0-100）："))
    do.save_score(name, score)

def view_all_scores():
    """查看所有成绩"""
    scores = do.load_all_scores()
    if not scores:
        print("暂无成绩数据！")
        return
    
    print("\n学生成绩列表：")
    for idx, item in enumerate(scores, 1):
        # todo-pk
        print(f"{idx}. 姓名：{item['name']} 成绩：{item['score']}")

def view_score_stats():
    """查看成绩统计"""
    scores = do.load_all_scores()
    if not scores:
        print("暂无成绩数据，无法统计！")
        return
    
    average = sc.calculate_average(scores)
    stats = sc.get_score_stats(scores)
    print(f"\n成绩统计：")
    print(f"平均分：{average}")
    print(f"最高分：{stats['max']}")
    print(f"最低分：{stats['min']}")