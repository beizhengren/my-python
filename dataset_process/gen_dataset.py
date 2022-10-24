from datetime import datetime
import os, fnmatch
import random
import sys

def find_with_pattern(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def gen_dataset():
    '''
        read all the file name of given dataset
        parition dataset into train, val, test set
    '''
    argc = len(sys.argv)
    
    print('-------------------------------------------')
    print("Amount of arguments is: {}".format(argc))
    if argc < 2:
        sys.exit("Too few args!")
    
    dataset_dir = sys.argv[1]    
    train_sample_number = int(sys.argv[2])
    validation_sample_num = int(sys.argv[3])
    imagesets_main_dir = os.getcwd() if argc < 5 else sys.argv[4] 
    print("Out dir is: {}".format(imagesets_main_dir))

    # get list
    raw_data_list = find_with_pattern("*.bin", dataset_dir)
    gt_list = find_with_pattern("*.txt", dataset_dir)

    print('-------------------------------------------')
    raw_data_name_set = {os.path.splitext(os.path.basename(s))[0] for s in raw_data_list}
    print("Amount of raw data is: {}".format(len(raw_data_name_set)))

    annotations_name_set = {os.path.splitext(os.path.basename(s))[0] for s in gt_list}
    print("Amount of labels is: {}".format(len(annotations_name_set)))

    final_data_set = raw_data_name_set.intersection(annotations_name_set)
    print("Amount of final dataset is: {}".format(len(final_data_set)))

    # partition the set
    total_sample_number = len(final_data_set)
    print('-------------------------------------------')
    print("Amount of total is: {} ".format(total_sample_number))
    print("Amount of train set is: {} ".format(train_sample_number))
    print("Amount of validation set is: {}".format(validation_sample_num))

    test_sample_num = total_sample_number - train_sample_number - validation_sample_num
    
    random.seed(1)
    ## get train_set
    train_set = set(random.sample(final_data_set, train_sample_number))
    
    ## get val_set
    ## A.difference (B) = A - B, for set A and B
    validation_set = set(random.sample(
                            final_data_set.difference(train_set), 
                            validation_sample_num))
    ## get test_set
    test_set = final_data_set.difference(train_set).difference(validation_set)
    ## get trainval_set 
    trainval_set = train_set.union(validation_set)
    # sort name from small to large
    train_name_list = sorted(list(train_set))
    val_name_list = sorted(list(validation_set))
    trainval_name_list = sorted(list(trainval_set))
    test_name_list = sorted(list(test_set))

    print('-------------------------------------------')
    print("Writing to txt files ...")
    name_list = [train_name_list, val_name_list, trainval_name_list, test_name_list]
    time_sec = str(datetime.now()).replace(' ', '_').replace(':', '-')
    out_prefix = time_sec[:-7]

    filename_list = [out_prefix+'_train', out_prefix+'_val', out_prefix+'_trainval', out_prefix+'_test']

    for i in range(len(filename_list)):
        with open(imagesets_main_dir + '/' + filename_list[i] + '.txt', 'w') as f:
            for s in name_list[i]:
                f.write(s + "\n")
        print("Saving {}...".format(filename_list[i]))

    print('-------------------------------------------')
    print("Finished.")
    return

if __name__ == '__main__':
    gen_dataset()
