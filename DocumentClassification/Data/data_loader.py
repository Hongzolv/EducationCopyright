
import os
import glob
import numpy as np
from keras.preprocessing.image import  ImageDataGenerator

def dataset_generator(dataset):
    rotation = np.random.rand() * 10
    data_gen = ImageDataGenerator(rescale=1./255)
    # preprocessing_function =
    data_generator = data_gen.flow_from_directory(dataset,target_size=(256,256),batch_size=32,class_mode='categorical')
    data_list = []
    batch_inx = 0
    label_list = []
    while batch_inx <= data_generator.batch_index:
        data = data_generator.next()
        # from matplotlib import pyplot
        # for i in range(len(data[0])):
        #     _data_array = np.asanyarray(data[0][i])
        #     pyplot.imshow(_data_array )
        data_list.append(data[0])
        label_list.append(data[1])
        batch_inx = batch_inx + 1

    data_array = np.asanyarray(data_list)
    label_array = np.asanyarray(label_list)
    return data_array, label_array


def get_dataset_make_labels(root):
    dataset = []
    dir_names = os.listdir(root)
    for n in range(len(dir_names)):
        full_dir_name = os.path.join(root, dir_names[n])
        for full_file_name in glob.iglob(os.path.join(full_dir_name,'*.png')):
            dataset.append((full_file_name,int(n)))

    return dataset
if __name__ == '__main__':
    dataset = get_dataset_make_labels('D:/projects/2017/저작권/EducationCopyright/Data/train')
    generated_dataset = dataset_generator('D:/projects/2017/저작권/EducationCopyright/Data/train')
