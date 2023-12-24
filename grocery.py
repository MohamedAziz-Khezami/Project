def grocery_list():
    g_list=[]
    g_list2=[]
    while True:
        try:
            item=input().upper().strip()

            g_list.append(item)
        except EOFError:
            break



    for item in g_list:
        if item not in g_list2:
            g_list2.append(item)


    g_list2.sort()

    for item in g_list2:
        print(g_list.count(item),item)


def main():
    grocery_list()


main()