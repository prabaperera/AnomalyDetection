from sklearn.externals import joblib
import os
from sklearn.neighbors import LocalOutlierFactor
print(__doc__)


def load_x_train (filename_read) :
    list_data=[[]]
    j=0
    with open(filename_read) as f:
        for line in f:
            array_split=line.split(',')
            #array_split.pop(0)
            #array_split.pop()
            
            for i in array_split:
                #print(float(i))
                list_data[j].append(float(i))
            list_data.append([])
            j=j+1
    
    list_data.pop()
    return list_data
    #print(list_data)        
    #implement_cluster(list_data)



def load_x_test (filename_read) :
    list_data=[[]]
    j=0
    with open(filename_read) as f:
        for line in f:
            array_split=line.split(',')
            #array_split.pop(0)
            array_split.pop(0)
            
            for i in array_split:
                #print(float(i))
                list_data[j].append(float(i))
            list_data.append([])
            j=j+1
    
    list_data.pop()
    return list_data


    
def load_x_outliner (filename_read) :
    list_data=[[]]
    j=0
    with open(filename_read) as f:
        for line in f:
            array_split=line.split(',')
            array_split.pop(0)
            #array_split.pop()
            
            for i in array_split:
                #print(float(i))
                list_data[j].append(float(i))
            list_data.append([])
            j=j+1
    
    list_data.pop()
    return list_data
    

def view_performance():
    accuracy =''
    error_rate =''
    recall =''
    precisiion=''
    print('Accuracy ' + accuracy)
    print('error_rate ' + error_rate)
    print('recall ' + recall)
    print('precisiion ' + precisiion)
    
dir_base = '/Users/praba/Documents/NTU/AI/project/Base'
dir_read_train='/Users/praba/Documents/NTU/AI/project/Base/temp_feactures/'
X_test = load_x_test('/Users/praba/Documents/workspace/Algo/AnomalyDetection/feactures_auth_2.txt')
X_outliers = load_x_outliner('/Users/praba/Documents/workspace/Algo/AnomalyDetection/feactures_readteam.txt')


def train_model():
    filenames=os.listdir(dir_read_train)
    filenames.sort()
    
    for trainFile in filenames:
        if(trainFile.startswith( 'x' ) is False):
            continue
        print(trainFile)
        trainFile_path = dir_read_train+trainFile
        X_train =load_x_train(trainFile_path)
        clf.fit(X_train)
        
        #y_pred_train = clf.fit_predict(X_train)
        y_pred_test = clf.fit_predict(X_test)
        y_pred_outliers = clf.fit_predict(X_outliers)
        #n_error_train = y_pred_train[y_pred_train == -1].size
        n_error_test = y_pred_test[y_pred_test == -1].size
        n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
        
        #print(y_pred_train.size)
        print(y_pred_test.size)
        print(y_pred_outliers.size)
        
       # print(n_error_train)
        print(n_error_test)
        print(n_error_outliers) 
        
 

def load_train_model():
    #X_train=load_x_train()
    dump_file=dir_base+'/model_dump/model_if.pkl'
    if os.path.isfile(dump_file):
        clf = joblib.load(dump_file)
    else:
        clf = LocalOutlierFactor(n_neighbors=20)
        train_model()
        joblib.dump(clf,dump_file)
    
    return clf
     

    
#Start main process

clf = load_train_model()  

#y_pred_train = clf.fit_predict(X_train)
y_pred_test = clf.fit_predict(X_test)
y_pred_outliers = clf.fit_predict(X_outliers)
#n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size

#print(y_pred_train.size)
print(y_pred_test.size)
print(y_pred_outliers.size)

   # print(n_error_train)
print(n_error_test)
print(n_error_outliers) 

#xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
# Generate train data
#X = 0.3 * np.random.randn(100, 2)
#X_train = np.r_[X + 2, X - 2]
#X_train =load_x_train('/Users/praba/Documents/workspace/Algo/AnomalyDetection/feactures_auth_1.txt')
# Generate some regular novel observations
#X = 0.3 * np.random.randn(20, 2)
#X_test = np.r_[X + 2, X - 2]
#X_test = load_x_test('/Users/praba/Documents/workspace/Algo/AnomalyDetection/feactures_auth_2.txt')
# Generate some abnormal novel observations
#X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
#X_outliers = load_x_outliner('/Users/praba/Documents/workspace/Algo/AnomalyDetection/feactures_readteam.txt')


# fit the model


