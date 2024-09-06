'''
what is the difference between a shallow copy and Deep copy
'''

import copy

original1 = ['1','2','3','4']

# #deep copy usage
# deep = copy.deepcopy(original1)
# deep[2] = "deep"
# print(original)
# print(deep)

#shallow copy useage
original2 = ['1',['2','3'],'4']
shallow = copy.copy(original2)
shallow[1][0] = "shallow"
print(original2)
print(shallow)

