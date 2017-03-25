import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.externals import joblib


def read_file(filename_rd):     
    global current_time
    global list_childdict
    global list_key
    global list_procchilddict
    global list_prockey
    global dict_key
    global proc_key
    global set_key
    
    with open(filename_rd) as f:
        for line in f:
            process_line(line)
        key_list=list(set_key)
        for item in key_list:
            load_x_train(item)

    model_if()
    
    
            
def load_x_test () :
    filename_read='C:/Users/chamini/Documents/GitHub/AnomalyDetection/feactures_auth_2.txt'
    list_test_data=[[]]
    j=0
    with open(filename_read) as f:
        for line in f:
            array_split=line.split(',')
            
            array_split.pop(0)
            array_split.pop(0)
            array_split.pop(0)
            array_split.pop()
            array_split.pop()
            
            
            #print(array_split)
            #print('J: ' + str (j))
            
            for i in array_split:
                #print(float(i))
                list_test_data[j].append(float(i))
            list_test_data.append([])
            j=j+1
    
    list_test_data.pop()
    return list_test_data


    
def load_x_outliner () :
    filename_read='C:/Users/chamini/Documents/GitHub/AnomalyDetection/feactures_readteam.txt'
    list_test_data=[[]]
    j=0
    with open(filename_read) as f:
        for line in f:
            array_split=line.split(',')
            
            array_split.pop(0)
            array_split.pop(0)
            array_split.pop(0)
            array_split.pop()
            array_split.pop()
            #print(array_split)
            #print('J: ' + str (j))
            
            for i in array_split:
                #print(float(i))
                list_test_data[j].append(float(i))
            list_test_data.append([])
            j=j+1
    
    list_test_data.pop()
    return list_test_data


def load_x_train (key) :
    
          
    global list_key
    global list_net_type
    global list_auth_type
    global dict_key
    global list_data
  
    ind=dict_key.get(key,-1)
    
    list_data.append([])
    j=len(list_data)-1
    
    record=''
    if ind != -1:
        child_dict=list_childdict[ind]
        record=record+str(child_dict.get('dest_u_dom_cnt',0))
        record=record+','+ str(child_dict.get('dest_com_cnt',0))
      
        un_dest=child_dict['un_dest']
        arr_un_dest=un_dest.split(',')
        set_un_dest=set(arr_un_dest)
        record=record+','+ str(len(set_un_dest))
        
                  
        un_dest_dom=child_dict['un_dest_dom']
        arr_un_dest_dom=un_dest_dom.split(',')
        set_un_dest_do = set(arr_un_dest_dom) 
        record=record+','+ str(len(set_un_dest_do))
                     
        un_dest_ratio=int(child_dict.get('dest_com_cnt',0))/len(set_un_dest)
        un_dest_ratio = format(un_dest_ratio, '.4f')
        un_dest_dom_ratio=int(child_dict.get('dest_u_dom_cnt',0))/len(set_un_dest_do)
        un_dest_dom_ratio = format(un_dest_dom_ratio, '.4f')
        record=record+','+str(un_dest_ratio)
        record=record+','+str(un_dest_dom_ratio)                            

                      
        for auth_type in list_auth_type:
            auth_type='auth_'+auth_type
            record=record+','+ str(child_dict.get(auth_type,0))
        for net_type in list_net_type :
            net_type='log_'+net_type
            record=record+','+ str(child_dict.get(net_type,0))
        for auth_ori in list_auth_ori:
            record=record+','+ str(child_dict.get(auth_ori,0))
        for suc_fail in list_suc_fail:
            record=record+','+ str(child_dict.get(suc_fail,0))
        
        array_split=record.split(',')
        for i in array_split:
            list_data[j].append(float(i))
        file_wr_auth.write(record)
        file_wr_auth.write('\n')

            
         
    
    
    #record=key
   
def check_time(line):
    global current_time    
    time,u_domain,com,prc,st_end=line.split(",")
    
    if time == current_time:
        return True
    else:
        return False
    

def process_line(line):
    time,src_u_domain,dest_u_domain,src_com,dest_com,auth_type,logon_type,auth_ori,suc_fail=line.split(",")
    suc_fail=suc_fail.strip()
    
    global dict_key
    global list_childdict
    global list_key
    global set_auth_type
    global set_net_type
    global set_key
    global list_auth_ori
    global list_suc_fail
    

    
    if (src_com==dest_com) and (auth_ori == list_auth_ori[0]) and (suc_fail == list_suc_fail[0]):
        action=list_auth_ori[0]
    elif(src_com==dest_com) and (auth_ori == list_auth_ori[1]) and (suc_fail == list_suc_fail[0]):
        action=list_auth_ori[1]
    else:
        action='no_action'
     
    key=src_u_domain+'~'+src_com
    ind=dict_key.get(key,-1)
   
    
    error='1'
    if(action==list_auth_ori[0]) and ind !=-1:
        error='error1'
    elif(action==list_auth_ori[1]) and ind==-1:
        error='error2'
    elif 'SERVICE' in key:
        error='error3'
    elif(action==list_auth_ori[1]) and ind !=-1:
        load_x_train(key)
        dict_key.pop(key)
        list_childdict[ind]=None
        set_key.remove(key)
        ind=dict_key.get(key,-1)
    elif ind != -1 and key in set_key and action not in list_auth_ori and auth_ori in list_auth_ori :
       
        child_dict=list_childdict[ind]
        dest_u_dom_cnt=child_dict.get('dest_u_dom_cnt',0)
        dest_u_dom_cnt=dest_u_dom_cnt+1
        child_dict['dest_u_dom_cnt']=dest_u_dom_cnt
            
        dest_com_cnt=child_dict.get('dest_com_cnt',0)
        dest_com_cnt=dest_com_cnt+1
        child_dict['dest_com_cnt']=dest_com_cnt
            
        auth_type='auth_'+auth_type
        auth_type_ind=child_dict.get(auth_type,0)
        if auth_type_ind == 0:
            child_dict[auth_type]=1
        else:
            auth_type_cnt=child_dict[auth_type]
            auth_type_cnt=auth_type_cnt+1
            child_dict[auth_type]=auth_type_cnt
                          
        logon_type='log_'+logon_type        
        logon_type_ind=child_dict.get(logon_type,0)
        if logon_type_ind == 0:
            child_dict[logon_type]=1
        else:
            logon_type_cnt=child_dict[logon_type]
            logon_type_cnt=logon_type_cnt+1
            child_dict[logon_type]=logon_type_cnt
            
        auth_ori_ind=child_dict.get(auth_ori,0)
        if auth_ori_ind == 0:
            child_dict[auth_ori]=1
        else:
            auth_ori_cnt=child_dict[auth_ori]
            auth_ori_cnt=auth_ori_cnt+1
            child_dict[logon_type]=auth_ori_cnt
                          
        suc_fail_ind=child_dict.get(suc_fail,0)
        if suc_fail_ind == 0:
            child_dict[suc_fail]=1
        else:
            suc_fail_cnt=child_dict[suc_fail]
            suc_fail_cnt=suc_fail_cnt+1
            child_dict[suc_fail]=suc_fail_cnt
        
        #unique set of dest
        un_dest=child_dict['un_dest']
        un_dest=un_dest+','+dest_com
        child_dict['un_dest']=un_dest
                  
        un_dest_dom=child_dict['un_dest_dom']
        un_dest_dom=un_dest_dom+','+dest_u_domain
        child_dict['un_dest_dom']=un_dest_dom
        
    elif ind == -1 and key not in set_key and action not in list_auth_ori and auth_ori in list_auth_ori :
       set_key.add(key)
       child_dict={}
       child_dict['start_time'] =time
       child_dict['dest_u_dom_cnt']=1
       child_dict['dest_com_cnt']=1
       auth_type='auth_'+auth_type
       child_dict[auth_type]=1
       logon_type='log_'+logon_type  
       child_dict[logon_type]=1
       child_dict[auth_ori]=1
       child_dict[suc_fail]=1
       #unique dest and dest_user_domain
       child_dict['un_dest']=''
       child_dict['un_dest_dom']=''
                
       list_childdict.append(child_dict)
       new_indx=len(list_childdict)-1
       dict_key[key]=new_indx
      
        
            
    if (action==list_auth_ori[0]) and ind ==-1 and 'SERVICE' not in key:
      set_key.add(key)
      child_dict={}
      child_dict['start_time'] =time
      child_dict['dest_u_dom_cnt']=1
      child_dict['dest_com_cnt']=1
      auth_type='auth_'+auth_type
      child_dict[auth_type]=1
      logon_type='log_'+logon_type  
      child_dict[logon_type]=1
      child_dict[auth_ori]=1
      child_dict[suc_fail]=1
      #unique dest and dest_user_domain
      child_dict['un_dest']=''
      child_dict['un_dest_dom']=''
                
      list_childdict.append(child_dict)
      new_indx=len(list_childdict)-1
      dict_key[key]=new_indx
            
           
def model_if():
    rng = None
    print('size1: '+ str (len(list_data)))
    list_data.pop()
    print('size2: '+ str (len(list_data)))
    X_train=list_data
    X_test=load_x_test()
    X_outliers=load_x_outliner()


# fit the model
    clf = IsolationForest(max_samples=100, random_state=rng)
    clf.fit(X_train)
    joblib.dump(clf, 'F:/dataset_AI/model_dump/model_if.pkl') 
    clf = joblib.load('F:/dataset_AI/model_dump/model_if.pkl') 


    y_pred_train = clf.predict(X_train)
    y_pred_test = clf.predict(X_test)
    y_pred_outliers = clf.predict(X_outliers)

    n_error_train = y_pred_train[y_pred_train == -1].size
    n_error_test = y_pred_test[y_pred_test == -1].size
    n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
                                  
    print(y_pred_train.size)
    print(y_pred_test.size)
    print(y_pred_outliers.size)

    print(n_error_train)
    print(n_error_test)
    print(n_error_outliers)



#'F:/dataset_AI/auth.txt'
filename_rd_auth='F:/dataset_AI/splitted_files/auth_orignal.txt'
filename_wr_auth='F:/dataset_AI/splitted_files/fect_auth_new.txt'

dict_key={}
list_childdict=[]
set_key=set()
list_data=[[]]


  
list_auth_type= ['MICROSOFT_AUTHENTICATION_PACKAGE_','Kerberos','MICROSOFT_AUTHENTICATION_PACK','?',
'MICROSOFT_AUTHENTICATION_PAC','MICROSOFT_AUTHENTICATION_PA','MICROSOFT_AUTHENTICATION_PACKAG',
'MICROSOFT_AUTHENTICATION_PACKAGE_V1','MICROSOFT_AUTHENTICATION_PACKAGE_V1_0','Negotiate','NTLM','MICROSOFT_AUTHENTICATION_PACKAGE']
list_net_type=['Interactive','Network','RemoteInteractive','?','Batch','NewCredentials','Unlock','Service','NetworkCleartext','CachedInteractive']
list_auth_ori=['LogOn','LogOff']
list_suc_fail=['Success','Fail']
list_st_end=['Start','End']


print("Reading..")
file_wr_auth = open(filename_wr_auth,"w")
read_file (filename_rd_auth)
file_wr_auth.close()
