def remove_duplicates():
    name = "shanmukharao maradana"
    nodulicates_name = {}

    for i in name:
        if i not in nodulicates_name:
            nodulicates_name[i] = 1
        else:
            nodulicates_name[i] += 1
        print(nodulicates_name)




