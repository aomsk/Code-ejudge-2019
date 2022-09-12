"""Filter"""
def main():
    """Filter"""
    import json
    dic = input()
    filterr = float(input())
    num = 0
    dic = json.loads(dic)
    id_num_all = sorted(list(dic))
    for num_id in id_num_all:
        if dic.get(num_id) >= filterr:
            print(num_id, "%.2f"%dic.get(num_id), sep="\t")
            num = 1
    if num == 0:
        print("Nope")
main()
