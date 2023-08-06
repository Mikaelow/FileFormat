def insert_into(lane : str) ->str :
    pozycja = lane.find('values')+7
    new_line = (lane[pozycja:]+',')
    new_line = new_line.replace('(','[')
    new_line = new_line.replace(')',']')
    print(new_line)

def sec_insert_into(lane: str):
    new_lane = lane.replace('|',',')
    new_lane = '[' + new_lane[1:]
    new_lane = new_lane[:-1]+']'
    new_lane = new_lane.replace(' ','')
    print(new_lane)
