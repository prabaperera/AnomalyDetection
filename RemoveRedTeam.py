def read_file(filename_rd):     
    
    with open(filename_rd) as f:
        for line in f:
            process_read_team (line)
            #get_auth_net_type(line)
            

def process_read_team(line):
    #global set_auth_type
    #global set_net_type
    
    
    time,src_u_domain,dest_u_domain,src_com,dest_com,auth_type,logon_type,auth_ori,suc_fail=line.split(",")
    key=src_u_domain+'~'+src_com
    #print(x[0])
    #i=set_auth_type.add(auth_type)
    #j=set_net_type.add(logon_type)
    #print('key: '+key+' ' + str(i))
    try:
        column = list_red_team.index(key)
        filename_wr_readteam.write(line)
        filename_wr_readteam.write('\n')        
    except ValueError:
        filename_wr_normal.write(line)
        filename_wr_normal.write('\n')   
        pass  


list_red_team=['U620@DOM1~C17693',
'U748@DOM1~C17693',
'U6115@DOM1~C17693',
'U636@DOM1~C17693',
'U748@DOM1~C18025',
'U1723@DOM1~C17693',
'U737@DOM1~C19932',
'U825@DOM1~C17693',
'U1653@DOM1~C17693',
'U293@DOM1~C17693',
'U8946@DOM1~C17693',
'U10379@C3521~C17693',
'U8601@DOM1~C17693',
'U212@DOM1~C17693',
'U4978@DOM1~C17693',
'U3905@DOM1~C17693',
'U995@DOM1~C17693',
'U288@DOM1~C17693',
'U2837@DOM1~C17693',
'U349@DOM1~C17693',
'U250@DOM1~C17693',
'U1600@DOM1~C17693',
'U4353@DOM1~C17693',
'U4856@DOM1~C17693',
'U5087@DOM1~C17693',
'U9763@DOM1~C17693',
'U795@DOM1~C17693',
'U9947@DOM1~C17693',
'U882@DOM1~C17693',
'U8777@C583~C17693',
'U1450@DOM1~C17693',
'U8777@C1500~C17693',
'U8777@C3388~C17693',
'U374@DOM1~C17693',
'U2575@DOM1~C17693',
'U3718@DOM1~C17693',
'U342@DOM1~C17693',
'U737@DOM1~C17693',
'U6572@DOM1~C17693',
'U162@DOM1~C17693',
'U314@DOM1~C17693',
'U642@DOM1~C17693',
'U3635@DOM1~C17693',
'U1480@DOM1~C17693',
'U66@DOM1~C17693',
'U1164@DOM1~C17693',
'U7394@DOM1~C17693',
'U1048@DOM1~C17693',
'U5254@DOM1~C17693',
'U7375@DOM1~C17693',
'U4448@DOM1~C17693',
'U218@DOM1~C17693',
'U4112@DOM1~C17693',
'U1653@DOM1~C22409',
'U12@DOM1~C17693',
'U13@DOM1~C17693',
'U1289@DOM1~C17693',
'U3277@C2519~C17693',
'U1519@DOM1~C17693',
'U7761@C2519~C17693',
'U7004@C2519~C17693',
'U207@DOM1~C17693',
'U1145@DOM1~C17693',
'U453@DOM1~C17693',
'U9263@DOM1~C17693',
'U20@DOM1~C17693',
'U7507@DOM1~C17693',
'U415@DOM1~C17693',
'U1569@DOM1~C17693',
'U1581@DOM1~C17693',
'U6764@DOM1~C17693',
'U1789@DOM1~C17693',
'U6691@DOM1~C17693',
'U78@DOM1~C17693',
'U3005@DOM1~C17693',
'U1133@DOM1~C17693',
'U3486@DOM1~C22409',
'U2231@DOM1~C17693',
'U1592@DOM1~C17693',
'U1025@DOM1~C17693',
'U737@C10~C17693',
'U86@C10~C17693',
'U2758@DOM1~C17693',
'U9407@DOM1~C17693',
'U24@DOM1~C17693',
'U655@DOM1~C17693',
'U86@DOM1~C17693',
'U3549@DOM1~C17693',
'U8170@DOM1~C17693',
'U8168@C19038~C17693',
'U1506@DOM1~C17693',
'U7594@DOM1~C17693',
'U114@DOM1~C17693',
'U1106@DOM1~C17693',
'U3575@DOM1~C17693',
'U3206@DOM1~C17693',
'U8777@DOM1~C17693',
'U227@DOM1~C17693',
'U8168@C685~C17693',
'U679@DOM1~C17693',
'U7311@DOM1~C17693',
'U524@DOM1~C17693',
'U8840@DOM1~C17693',
'U1306@DOM1~C17693',
'U3764@DOM1~C17693',
'U1467@C3597~C17693',
'U3406@DOM1~C17693']



print("Reading..")
# reading and wrinting into main files
filename_rd='C:/Chamini/data/auth.txt'
filename_wr_readteam=''
filename_wr_normal=''
file_wr_readteam = open(filename_wr_readteam,"w")
file_wr_normal = open(filename_wr_normal,"w")
read_file (filename_rd)
file_wr_readteam.close()
file_wr_normal.close()