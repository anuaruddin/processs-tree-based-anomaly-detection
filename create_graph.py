from graphviz import Graph
import os
import ray as ray

ray.init()

A = 'sequence ( a xorLoop ( sequence ( b d ) sequence ( c e ) ) f )'

def word_to_graph(inp, out_name):
    idd = 0
    branch_list = list()
    operator = ['sequence', 'xor', 'xorLoop', 'and']
    
    split_word = inp.split(' ')
    
    G = Graph(format='eps')
    G.attr('node', shape='circle')
    G.attr('graph', pad='0', margin='0',ratio='auto', size='8.3,11!', layout='dot', overlap='prism', fixedsize='true')

    for now in split_word:
        print(branch_list)
        if now in operator and not branch_list:
            if now == 'sequence':
                oper = 'seq'
            elif now == 'xorLoop':
                oper = 'loop'
            else:
                oper = now
            G.node('0', label=oper)
            branch_list.append(idd)
            idd += 1
        elif now in operator and branch_list:
            if now == 'sequence':
                oper = 'seq'
            elif now == 'xorLoop':
                oper = 'loop'
            else:
                oper = now
            G.node(str(idd), label=oper)
            G.edge(str(branch_list[-1]), str(idd))
            branch_list.append(idd)
            idd += 1
        elif now == '(':
            pass
        elif now == ')' and branch_list:
            branch_list.pop(-1)
        elif now == 'tau' and branch_list:
            G.node(str(idd), shape='box', label='T')
            G.edge(str(branch_list[-1]), str(idd))
            idd += 1
        elif branch_list:
            G.node(str(idd), shape='box', label=now)
            G.edge(str(branch_list[-1]), str(idd))
            idd += 1
        else:
            pass
                
    G.render(out_name)
    os.remove(out_name)
            
if __name__ == '__main__':
    word_to_graph(A,'da')