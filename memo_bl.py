from memo import MemoList
from datetime import datetime

memo_dic = {}
count = memo_dic.len()

user = input('名前を入力してください')
while True:
    menu = {'登録':1,'削除':2,'編集':3,'照会':4}
    print(menu)
    selected_number = input('メニュー番号を選んでください')
    #メモの追加
    if selected_number == '1':
        memo = str(input('メモの内容を入力してください'))
        print(memo)
        time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print(time)
        memo_dic[str(count)] = MemoList(memo,time,user)
        count =+1
        # type(memo_dic)
        # for key,item in memo_dic:
        #     print(key,item.value)


    #メモの削除
    elif selected_number == '2':
        index = input('削除したい番号を選んでください:')
        del memo_dic[str(count)]
        print('メモを削除しました。')

    #メモの照会
    elif selected_number == '3':
        index = input('削除したい番号を選んでください:')
        memo.inquiry(memo_list,index)

    #メモの更新
    elif selected_number == '4':
        index = input('更新したいメモの番号を選んでください：')
        memo.update(memo_list,index)
    # やり直し
    else:
        print('不正な値が入力されました。')
        continue
