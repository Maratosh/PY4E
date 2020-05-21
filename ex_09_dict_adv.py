'''To count some items from mail-box'''

def count():
    find = 'from'
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened: ', fname)
        exit()
    dict_w = {}    
    for line in fhand:
        line = line.rstrip()
        line = line.lower()
        if not line.startswith('{}'.format(find)): continue
        #print(line)  # from cwen@iupui.edu thu jan  3 16:23:48 2008
        words = line.split()
        #print(words) #['from', 'cwen@iupui.edu', 'thu', 'jan', '3', '16:23:48', '2008']
        if len(words) < 3: continue
        dict_w[words[1]] = dict_w.get(words[1], 0) + 1
    print(dict_w) # done!

    
        
