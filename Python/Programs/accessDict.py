myList = {'k1':[{'nest_key':['this_is_deep',['hello']]}]}

#To print hello we need to access the dictionary in the following way
print(myList['k1'][0]['nest_key'][1][0])

myList2 = {'k1':[1,2,{'k2':['this is tricky', {'tough':[1,2,['hello']]}]}]}

print(myList2['k1'][2]['k2'][1]['tough'][2][0])