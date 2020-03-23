import os

os.chdir('/home/skk_thenotorious/Documents/Kids')
#print(os.getcwd())

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    f_title, f_num = file_name.split(' ')
    f_title = f_title.strip()
    f_num = f_num.strip().zfill(2)
    file_ext = file_ext.strip()

    new_name = '{}-{}{}'. format(f_num, f_title, file_ext)
    os.rename(f, new_name)
