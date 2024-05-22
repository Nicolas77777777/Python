def is_simmetric(tree: list[int]):
    pass


def are_mirrorred(tree: list[int], left_index: int, right_index: int):
    if left_index >= len(tree) or right_index >= len(tree):
        return left_index == right_index
    

    if tree[left_index] != tree[right_index]:
        return False
    

    left_of_left = 2* left_index +1 
    right_of_left = 2* left_index +2

    left_of_right = 2* right_index+1
    right_of_right = 2*right_index+ 2


    simmetric_extrems = are_mirrorred(tree,left_of_left,right_of_right)


    simmetric_inner = are_mirrorred(tree, right_of_left,left_of_right)


    return simmetric_extrems and simmetric_inner


#