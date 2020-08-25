import os
import pandas as pd
import numpy as np
from PIL import Image as img
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix

def RenamePictures(path_to_dataset,start_number=8042):
    """
    arguements:
        path_to_dataset- folder that contains subfolders with the pictures to rename
        start_number- Number to start naming pictures
        
    returns:
        prints a counter starting at start_number to show progress. 
    """
    
    folders = os.listdir(path_to_dataset)
    paths = ['{}/{}'.format(path_to_dataset,x) for x in folders if x != '.DS_Store']
    picture_source = []
    picture_dest = []
    
    
    for folder in paths:
        pics = os.listdir(folder)
        
        for pic in pics:
            picture_source.append('{}/{}'.format(folder,pic))
            picture_dest.append('{}/{}.jpg'.format(folder,start_number))
            start_number += 1
         
    for i in range(len(picture_dest)):
        dest = picture_dest[i]
        src = picture_source[i]
        os.rename(src,dest)
        print(i)

def CheckSameData(directory_1, directory_2):
    """
    arguements:
        Directory_1 - Path to directory containing data
        Directory_2 - Path to directory containing data
        
    Returns:
    
        Prints missing values. Function will still print headline announcing which values are contained right under it
        even if no values are missing.
    """
    dir1 = os.listdir(directory_1)
    dir2 = os.listdir(directory_2)
    
    for i in dir1:
        print('Directory 1 missing values not in directory 2:')
        if i not in dir2:
            print(i)
    
    for i in dir2:
        print('Directory 2 missing values not in directory 1:')
        if i not in dir1:
            print(i)

def CarDataFrame(data,dataset):
    """
    Parameters:
        data- Contains car information Make, Model, Body Type, and Year in that order.
        dataset- train or test? **LOWER CASE**
    Returns:
        A Data Frame with a list of what pictures belong to what car and car info.
    """
    dataset = dataset.lower()
    
    full = [car for car in data if car !='.DS_Store']
    make = [car.split(' ')[0] for car in data if car != '.DS_Store']
    year = [car.split(' ')[-1] for car in data if car != '.DS_Store']
    bodyType = [car.split(' ')[-2] for car in data if car != '.DS_Store']
    model = [" ".join(car.split(' ')[0:-2]) for car in data if car != '.DS_Store']
    picsDirectory = []

    for i in data:
        if i != '.DS_Store':
            directory = 'car_data/{}/{}'.format(dataset,i)
            pics = os.listdir(directory)
            picsDirectory.append(pics)
    
    return pd.DataFrame({'full':full,'make':make,'year':year,'body_type':bodyType,'model':model,'pictures':picsDirectory,'set':dataset})

def Counter(data):
    """
    Parameters:
        data - A list of values
    returns:
        dictionary with values counted in descending order.
    """
    
    dictionary = {}
    
    for i in data:
        if i in dictionary:
            num = dictionary.get(i) + 1
            dictionary[i] = num
        else:
            dictionary[i] = 1
            
    orderedDict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1],reverse= True)}
    
    return orderedDict

def MakeFolders(datasets,by,set_name):
    '''
    Parameters:
        datasets: A list containing instances of a pandas data frame.
        by: Column used to sort images.
        set_name: Name to give to folder holding the training and testing set.
    
    Function uses pandas data frame to sort images into a new dataset.
    '''
    
    for dataset in datasets:
        kinds = dataset[by].unique()
        set_type = dataset.set[0]
        print(set_type)

        for kind in kinds:
            folder = 'car_data/{}/{}/{}'.format(set_name,set_type,kind)
            os.makedirs(folder)

        for row in range(len(dataset.index)):
            car_path = 'car_data/{}/{}'.format(dataset.set[row],dataset.full[row])
            for i in dataset.pictures[row]:
                if i != '.DS_Store':
                    pic_path = car_path+'/'+i
                    new_path = 'car_data/{}/{}/{}/{}'.format(set_name,set_type,dataset[by][row],i)
                    pic = img.open(pic_path)
                    pic_copy = pic.copy()
                    pic_copy.save(new_path)

def visualize_training_results(results):
    '''
    Parameters:
        -results: Results of training deep learning model.
    
    Function plots validation loss vs training loss over epochs, and validation accuracy and training accuracy over epochs.
    '''
    
    history = results.history
    plt.figure()
    plt.plot(history['val_loss'])
    plt.plot(history['loss'])
    plt.legend(['val_loss', 'loss'])
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.show()
    
    plt.figure()
    plt.plot(history['val_accuracy'])
    plt.plot(history['accuracy'])
    plt.legend(['val_acc', 'acc'])
    plt.title('Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.show()

def RenameBodyCategories(x):
    '''
    Parameters:
        -X: data point of pandas data frame.
    
    Function used for pandas apply function.
    '''
    if x == 'Convertible':
        return 'Coupe'
    elif x == 'Cargo-van':
        return 'Van'
    else:
        return x   
    
def VisualizeResults(y_test,y_pred):
    '''
    Parameters:
        -y_test: True y values in array form.
        -y_pred Predicted y values in array form.
    Returns:
        -Prints a classification report, accuracy score, confusion matrix, and heat map using seaborn.
    '''
    print('Classification Report')
    print(classification_report(y_test,y_pred))
    print('Accuracy')
    print(accuracy_score(y_test,y_pred))

    sns.heatmap(confusion_matrix(y_test,y_pred))
    plt.show()
 
 
 
 
 
    