import os,argparse
import pandas as pd

from generate_method import shift_code,rotate_code,gradient_shift_code,bg_shift_code,bg_rotate_noise_code

## hyperparameters
parser = argparse.ArgumentParser(description='BiLSTM-CRF for Chinese NER task')
parser.add_argument('--savepath', type=str, default='savepath/', help='train data source')
parser.add_argument('--sample_num', type=int, default='1000', help='generate size number')
parser.add_argument('--val_size', type=float, default='0.1', help='validation_data size')
parser.add_argument('--test_size', type=float, default='0.1', help='test_data size')
parser.add_argument('--method', type=int, default='0', help='method choice')
args = parser.parse_args()

def generate(path,sample_num,method,val_size,test_size):
    if not os.path.isdir(path):
        os.mkdir(path)
    image_list=[]
    code_list=[]

    data_size=[sample_num*(1-val_size-test_size),sample_num*val_size,sample_num*test_size]
    dir_list=['train/','val/','test/']

    for num,datasize in enumerate(data_size):
        dirname=dir_list[num]
        for i in range(int(datasize)):
            if (i%10000)==0 :print(i)

            im,strs=method()
            image_list.append("%06d"%i)
            code_list.append(strs.replace(' ',''))

            imagepath=os.path.join(path,dirname)
            if not os.path.isdir(imagepath):
                os.mkdir(imagepath)

            im.save(imagepath+str("%06d"%i)+'.jpg')

        datadf=pd.DataFrame(list(zip(image_list,code_list)),columns=['filename','code'])
        datadf.to_csv(path+dirname.replace('/','')+'data.csv',index=False)

method_list=[shift_code,rotate_code,gradient_shift_code,bg_shift_code,bg_rotate_noise_code]

'''
0:shift_code,
1:rotate_code,
2:gradient_shift_code,
3:bg_shift_code,
4:bg_rotate_noise_code
'''


path=args.savepath
sample_num=args.sample_num
method=method_list[args.method]
val_size,test_size=args.val_size,args.test_size

generate(path=path,sample_num=sample_num,method=method,val_size=val_size,test_size=test_size)