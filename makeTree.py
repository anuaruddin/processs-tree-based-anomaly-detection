import xml.etree.ElementTree as ET
import os
import create_graph as cgr

i = 0

fomal_list = []

def make_graph(input_file, output_file):
    tree = ET.parse(input_file)

    root = tree.getroot()
    
    for child in root[0]:
        if child.tag not in ['automaticTask', 'manualTask', 'parentsNode']:
            j = 0
            for the_child in root[0]:
                if the_child.tag == 'parentsNode' and the_child.attrib['targetId'] == child.attrib['id']:
                    j += 1
            if j == 0:
                branch_search(root[0], child)
    
    with open(output_file, mode='w') as f:
        j = 0
        for n in fomal_list:
            if (j == len(fomal_list)-1):
                node = len(n.split(' '))
                f.write(n)
            j += 1
    
    fomal_list.clear()

def branch_search(process_tree, top):
    global i
    f = top.tag + ' ( '
    
    for child in process_tree:
        if child.tag == 'parentsNode':
            if child.attrib['sourceId'] == top.attrib['id']:
                for the_child in process_tree:
                    if the_child.attrib['id'] == child.attrib['targetId']:
                        if the_child.tag not in ['automaticTask', 'manualTask', 'parentsNode']:
                            f = f + branch_search(process_tree, the_child) + ' '
                        else:
                            f = f + the_child.attrib['name'].replace(' ', '_').replace('(', '|').replace(')', '|') + ' '

    f = f + ')'
    
    f.replace('\'', '\\'+'\'')
    
    i += 1
    
    fomal_list.append(f)
    
    return f

if __name__ == '__main__':
    model = 'Observed10'
    for x in range(1,4):
        batch = x
        for y in range(1,21):
            size = y*10
            fdirin = './data/'+model+'/'+ str(batch) + '/'+ str(size) +'.ptml'
            fdirout =  './data/'+model+'/'+ str(batch) + '/'+ str(size) +'.ptf'
            fgraph = './data/'+model+'/'+ str(batch) + '/'+ str(size)
            print("Making tree:" + fdirout)
            make_graph(fdirin, fdirout)

            with open(fdirout) as fl:
                for line in fl:
#                    result = []    
#                    result = [cgr.word_to_graph.remote(line, fgraph) for _ in range(10)]
                     cgr.word_to_graph(line, fgraph)
