import pickle
man = []
other = []

try:
    with open('sketch.txt') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':',1)
                line_spoken = line_spoken.strip()
                if role == 'Other Man':
                    man.append(line_spoken)
                elif role == 'Man':
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError as err:
    print('File Error:' + str(err))
print(man)
print(other)

try:
    with open('man_file.pickle',mode='wb') as man_file, open('other_file.pickle', mode='wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other, other_file)
except pickle.PickleError as ex:
    print('Pickle Error:' + str(ex))

