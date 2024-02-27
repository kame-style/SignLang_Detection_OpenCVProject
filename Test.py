def get_shape(nested_list):
    num_rows = len(nested_list)
    num_cols = max(len(sublist) for sublist in nested_list)
    return num_rows, num_cols


list1=[0,0,0,1]
list2=[[0,0,0],[0,0,0],[0,0,0]]

print(get_shape(list2))

print(list2[0])