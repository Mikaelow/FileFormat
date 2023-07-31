def insert_into(lane : str) ->str :
    pozycja = lane.find('values')+7
    new_line = (lane[pozycja:]+',')
    new_line = new_line.replace('(','[')
    new_line = new_line.replace(')',']')
    print(new_line)