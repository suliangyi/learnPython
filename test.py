import csv


# 不用csv操作csv文件，输出内容
# for line in open("file/sample.csv"):
#     title, year, director = line.split(",")
#     print(title,year, title)


# 使用csv模块操作 csv文件，输出内容
# with open('file/sample.csv','w') as file:
    # reader = csv.reader(file)
    # for title, year, director in reader:
    #     print(title, year, director)
with open('file/sample.csv','a') as file:
    writer = csv.writer(file)
    writer.writerows(['title', 'summary', 'year'])
    writer.writerow(['文章标题', '作者', '时间', '阅读量', '评论', '喜欢', '赞赏数', '文章地址'])