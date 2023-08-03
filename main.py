from insert_into import insert_into

with open(r'c:\Users\User\Desktop\programowanie\IdeaProjects\formatowanieTekstu\plik.txt','r') as open_file:
    zmienna = open_file.read()

i = ''
for lane in zmienna.splitlines():
     if lane.startswith('insert into'):
        lane_splited = lane.split(' ')
        index_of_table = lane_splited.index('into')+1
        name_of_table = lane_splited[index_of_table]
        if i == name_of_table:
            pass
        else:
            i = name_of_table
            print('\n'+i)
        insert_into(lane)


