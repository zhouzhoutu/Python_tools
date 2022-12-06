import sys
import re


def get_tid(file):
    """
    传入文件名，读取文件每行内容，正则匹配，获得匹配的tid并返回
    """
    tids_set = set()
    ptr = re.compile("\d{6,}")
    with open(file, "r") as f:
        for line in f:
            tids = ptr.search(line).group(0)
            tids_set.add(tids)
    return tids_set


def diff_tid(new, old):
    """
    传入new_file的值，用于对比该值中tid是否与tidlist中的数字一致，并返回不一样的值的列表。
    即这个函数可以得到已保存的list中没有的tid.
    """
    new_set = set()
    old_set = set()
    for old_id in get_tid(old):
        old_set.add(old_id)
    for new_id in get_tid(new):
        new_set.add(new_id)
    get_set = new_set - old_set
    print(get_set)
    # for i in get_set():
    #     print(i)
    return get_set


def get_diff_title(tid, file):
    """
    传入tid参数和要对照的文件，返回文件标题
    """
    for id in tid:
        with open(file, "r") as f:
            for title in f.readlines():
                title = title.strip("\n")
                if id in title:
                    print(title)
                else:
                    pass


ids = diff_tid("2022-12-0615.md", "2022-12-0513.md")
new_file = "2022-12-0615.md"

if __name__ == "__main__":
    get_diff_title(ids, new_file)

