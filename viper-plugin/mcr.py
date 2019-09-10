from viper.common.abstracts import Module
from .mcrtools.baoge import train,predict
from .mcrtools.backup import backup,backup2

'''
将trainFun函数与identifyFun函数修改为对应的训练模型接口与识别接口
将上面的import修改为对应的接口路径即可
本文件与总文件夹放在viper/viper/modules下即可
'''

class MCR(Module):
    '''
    Malicious classification and recognition
    '''

    cmd = 'mcr'
    description = 'Malicious program classification and recognition.'
    authors = ['Why not stop?']

    def __init__(self):
        super(MCR, self).__init__()
        self.parser.add_argument('-T', '--train', nargs=2, default=None, help='train your model.')

        self.parser.add_argument('-I', '--identify', nargs=3, default=None, help='classify executables.')
    
                
    def run(self):

        super(MCR, self).run()
        if self.args is None:
            return
        if self.args.train is not None:
            backup(self.args.train[0])
            backup(self.args.train[1])
            #trainFun(self.args.train)
            print(self.args.train)
            
            train(self.args.train[0],self.args.train[1])
			
        if self.args.identify is not None:
            backup2(self.args.identify[0])
            backup2(self.args.identify[1])
            #backup(self.args.identify[2])
            # identifyFun(self.args.identify)
            print(self.args.identify)
            predict(self.args.identify[0],self.args.identify[1],self.args.identify[2])
			
