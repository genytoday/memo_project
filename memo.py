class MemoList:

    def __init__(self,memonaiyou,makeTime,user):
        self.memonaiyou=memonaiyou
        self.makeTime=makeTime
        self.user=user

    def delete(memo_dic,index):
        del memo_dic[index]
        return memo_list


    def inquiry(memo_dic,index):
        return memo_dic[index]

    def update(memo_dic,str,index):
        memo_dic[index] = str
