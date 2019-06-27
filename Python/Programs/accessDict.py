myList = {'k1':[{'nest_key':['this_is_deep',['hello']]}]}

#To print hello we need to access the dictionary in the following way
print(myList['k1'][0]['nest_key'][1][0])