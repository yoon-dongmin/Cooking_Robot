#!/usr/bin/env python
import csv
import copy
from collections import defaultdict, deque
from os.path import dirname

shrimp_salad = [0, 19] # 20
tuna_sandwich = [20, 43] # 24
club_sandwich = [44, 67] # 24
greek_salad = [68, 87] # 20


def make_v2(in_path, in_file, out_path, out_file):   
    # read csv file
    with open(in_path+in_file) as csvfile_in:
        raw_in = list(csv.reader(csvfile_in))
    
    # remove space in obj name
    for row in raw_in:
        row[1] = "_".join(row[1].split())
        row[3] = "_".join(row[3].split())
        row[4] = "_".join(row[4].split())
        row[5] = "_".join(row[5].split())

    # num_of_task, num_of_obj
    num_of_task = int(raw_in[-1][0])
    num_of_obj = (len(raw_in)-1)/num_of_task
    
    # ing_list
    not_obj_list = ['bowl', 'pan', 'pot', 'stove', 'cooking_pan', 'cutting_board', 'plate'] ## add more
    obj_list = [] 
    for r in raw_in[1:num_of_obj+1]:
        if r[1] not in not_obj_list:
            obj_list.append(r[1])            
    
    # bottled_ing list
    sample_bottled_obj_list = ['mayonnaise', 'salt', 'pepper', 'sugar', 'black_pepper', 'lemon_juice', 'olive_oil', 'chili_sauce', 'mustard', 'hot_sauce', 'relish']
    bottled_obj_list = []
    for r in raw_in[1:num_of_obj+1]:
        if r[1] in sample_bottled_obj_list:
            bottled_obj_list.append(r[1])

    # print(num_of_task, num_of_obj, obj_list)
    print('num_of_task', num_of_task)
    print('num_of_obj', num_of_obj)
    print('obj_list', obj_list)
    print('bottled_obj_list', bottled_obj_list)

    # salad
    salad_idx = 0
    salad_list = ['salad']
    for row in raw_in:
        if (row[1] == 'salad') and (row[2] == 'exist'):
            salad_idx = int(row[0])
            break
    if salad_idx != 0:
        for srow in raw_in[1+(num_of_obj*(salad_idx-1)):1+num_of_obj*salad_idx]:
            if srow[4] == 'bowl':
                salad_list.append(srow[1])
        print('salad_idx', salad_idx)
        # print('salad included data', raw_in[1+(num_of_obj*(salad_idx-1)):num_of_obj*salad_idx])
        print('salad_list', salad_list)
    else:
        print('no salad')

    # tuna spread
    tuna_spread_idx = 0
    tuna_spread_list = ['tuna_spread']
    for row in raw_in:
        if (row[1] == 'tuna_spread') and (row[2] == 'exist'):
            tuna_spread_idx = int(row[0])
            break    
    if tuna_spread_idx != 0:
        for srow in raw_in[1+(num_of_obj*(tuna_spread_idx-1)):1+num_of_obj*tuna_spread_idx]:
            if srow[4] == 'bowl':
                tuna_spread_list.append(srow[1])
        print('tuna_spread_idx', tuna_spread_idx)
        # print('tuna_spread included data', raw_in[1+(num_of_obj*(tuna_spread_idx-1)):num_of_obj*tuna_spread_idx])
        print('tuna_spread_list', tuna_spread_list)
    else:
        print('no tuna_spread')

    # sandwich
    sandwich_idx = 0
    sandwich_list_ = []
    sandwich_list = ['sandwich']
    obj_dict = dict()
    for row in raw_in:
        if (row[1] == 'sandwich') and (row[2] == 'exist'):
            sandwich_idx = int(row[0])
            break
    
    if sandwich_idx != 0:
        sandwich_task = raw_in[1+(num_of_obj*(sandwich_idx-1)):1+num_of_obj*sandwich_idx]
        for idx, srow in enumerate(sandwich_task):
            obj_dict[srow[1]] = idx
            if srow[3] != 'none':
                sandwich_list_.append(srow[1])

        for ing in sandwich_list_:
            ing_is_on = sandwich_task[obj_dict[ing]][3]
            if ing_is_on != 'none' and sandwich_task[obj_dict[ing_is_on]][3] == 'none':
                sandwich_list_.append(ing_is_on)

        bottom_ing = 'none'
        while sandwich_list_:
            for ing in sandwich_list_:
                if sandwich_task[obj_dict[ing]][3] == bottom_ing:
                    bottom_ing = ing
                    sandwich_list.append(ing)
                    sandwich_list_.remove(ing)
                    break
        print('sandwich_idx', sandwich_idx)
        # print('sandwich included data', sandwich_task)
        print('sandwich_list', sandwich_list)
    else:
        print('no sandwich')

    # write csv file
    with open(out_path+out_file, mode='w') as csvfile_out:
        raw_out = csv.writer(csvfile_out, delimiter=',')
        raw_out.writerow([num_of_task, num_of_obj])
        raw_out.writerow(obj_list)
        raw_out.writerow(bottled_obj_list)
        if tuna_spread_idx !=0:
            raw_out.writerow(tuna_spread_list)
        if salad_idx !=0:
            raw_out.writerow(salad_list)
        if sandwich_idx !=0:
            raw_out.writerow(sandwich_list)
        for d in raw_in:
            raw_out.writerow(d)
    return True

def get_object_list(in_path, in_file):
    # read csv file
    with open(in_path+in_file) as csvfile_in:
        raw_in = list(csv.reader(csvfile_in))
    
    # info of file
    ings_1 = raw_in[1] # ingredient
    ings_2 = raw_in[2] # bottled_ingredient
    
    new_i = 3
    while True:
        if raw_in[new_i][0] == 'Task':
            break
        else:
            new_i += 1
    
    ings_sp = []
    for i in range(new_i+1, len(raw_in)):
        if raw_in[i][5] != 'none':
            ings_sp.append(raw_in[i][5])
    
    return ings_1, ings_2, ings_sp

def test():
    total_ing = set()
    total_bottled_ing = set()
    total_spread_ing = set()
    for i in range(88):
        origin_path = 'test_set_v2_temp/'
        origin_file = 'test_{}_predict_v2.csv'.format(i)

        print("-"*30)
        print("file_name = "+origin_file)
        ing, bottled_ing, spread_ing = get_object_list(origin_path, origin_file)
        total_ing |= set(ing)
        total_bottled_ing |= set(bottled_ing)
        total_spread_ing |= set(spread_ing)

    print('='*30)
    print('\ntotal_ing\n{}'.format(total_ing))
    print('\ntotal_ing_except_bottled\n{}'.format(total_ing-total_bottled_ing))
    print('\ntotal_bottled_ing\n{}'.format(total_bottled_ing))
    print('\ntotal_spread_ing\n{}'.format(total_spread_ing))

def main():
    origin_dir = dirname(dirname(__file__)) + '/test_set/original2/'
    v2_dir = dirname(dirname(__file__)) + '/test_set/predict2_v2/'
    for i in range(88):
        origin_file = 'test_{}_predict.csv'.format(i)
        v2_file = origin_file[:-4]+'2_v2.csv'

        print("-"*30)
        print("file_name = "+origin_dir+origin_file)
        make_v2(origin_dir, origin_file, v2_dir, v2_file)

if __name__ == '__main__':
    main()
    # test()