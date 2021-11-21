def display_time(dict1,dict2):
    s_counter=0
    m_counter=0

    second=dict1["second"]+dict2["second"]
    while second>=60:
        second=second-60
        s_counter+=1
    minute=dict1["minute"] +dict2["minute"]+ s_counter
    while minute>=60:
        minute=minute-60
        m_counter +=1
    hours=dict1["hours"]+dict2["hours"]+m_counter
    display_dict={"hours":hours,"minute":minute,"second":second}
    return display_dict

time_dict1={}
time_dict2={}
display_dict={}

temp_time=input("enter ----> hours:minute:second ---> ").split(":")
time_dict1["hours"]=int(temp_time[0])
time_dict1["minute"]=int(temp_time[1])
time_dict1["second"]=int(temp_time[2])
#print(time_dict1)
temp_time=input("enter ----> hours:minute:second ---> ").split(":")
time_dict2["hours"]=int(temp_time[0])
time_dict2["minute"]=int(temp_time[1])
time_dict2["second"]=int(temp_time[2])
#print(time_dict1)
show_time=display_time(time_dict1,time_dict2)
print(f"Time is {show_time['hours']} hours and {show_time['minute']} minute and {show_time['second']} second")