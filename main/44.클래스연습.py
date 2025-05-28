class MemberInfo:
    def MemberInfo(self,idx,passwd,name):
        self.idx = idx
        self.passwd = passwd
        self.name = name

    def getMemeber(self):
        return f'{self.idx}, {self.passwd}, {self.name}'