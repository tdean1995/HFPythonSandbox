import io

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def extract_times(file_name):
    try:
        with open(file_name,'r') as data:
            data_line = data.readline().strip().split(',')
        return sorted(set([sanitize(each_t) for each_t in data_line]))
    except IOError as err:
        print('File error:' + str(err))
        return(None)

      

james = extract_times('james.txt')

julie = extract_times('julie.txt')

mikey = extract_times('mikey.txt')

sarah = extract_times('sarah.txt')

print(james[0:3])
print(julie[0:3])
print(mikey[0:3])
print(sarah[0:3])


    

