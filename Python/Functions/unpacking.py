#def fun(a,b,c):
#    print(a,b,c)

#my_list = [1,2,3]
#'''passing the list as a argument'''
#fun(*my_list)


def student_info(*args, **kwargs):
    print('Courses: ' + str(args))
    print('Information:' + str (kwargs))

courses = ['Data Science', 'IoT']
info = {'Name': 'SKK', 'Job' : 'Entrepreneuer'}

student_info(*courses, **info)