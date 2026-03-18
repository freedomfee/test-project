import cli_interface as cli

def main():
    """主程序"""
    print("欢迎使用学生成绩管理系统！")
    while True:
        cli.show_menu()
        try:
            choice = int(input("请输入操作编号："))
            if choice == 1:
                cli.add_score()
            elif choice == 2:
                cli.view_all_scores()
            elif choice == 3:
                cli.view_score_stats()
            elif choice == 4:
                print("退出程序，再见！")
                continue
            else:
                print("输入错误，请选择 1-4 的编号！")
        except ValueError:
            print("请输入有效的数字！")

if __name__ == "__main__":
    main()
