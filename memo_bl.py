from memo import*
from datetime import datetime



while True:
    user = input('名前を入力してください')

    menus = ['登録:1','削除:2','編集:3','照会:4']
    for menu in menus:
        print(menu)
    selected_number = input('メニュー番号を選んでください')
    #メモの追加
    if selected_number == '1':
        memonaiyou = str(input('メモの内容を入力してください'))
        print('メモの内容：'+ memonaiyou)
        makeTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        makeTime = str(makeTime)
        print('作成日時:'+makeTime)
        createdata(user,memonaiyou, makeTime)


    #メモの削除
    elif selected_number == '2':
        index = input('削除したい番号を選んでください:')
        print('メモを削除しました。')

    #メモの照会
    elif selected_number == '3':
        memo.inquirydata()

    #メモの更新
    elif selected_number == '4':
        index = input('更新したいメモの番号を選んでください：')
        memo.update(memo_list,index)
    # やり直し
    else:
        print('不正な値が入力されました。')
        continue
