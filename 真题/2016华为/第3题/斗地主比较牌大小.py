import sys
 
while True:
    s=sys.stdin.readline().strip()
    if len(s)==0:break
    #定义大小顺序
    orders=['3','4','5','6','7','8','9','10','J','Q','K','A','2','joker','JOKER']
    p1,p2=s.split('-')#分开两手牌
    p1_cards,p2_cards=p1.split(),p2.split()#拆成单张牌
    #有两个大鬼，直接返回那副牌
    if 'joker' in p1_cards and 'JOKER' in p1_cards:
        print(p1)
        continue
    if 'joker' in p2_cards and 'JOKER' in p2_cards:
        print(p2)
        continue
         
    #找炸，看谁的炸大
    p1_bomb='3'
    p2_bomb='3'
    card_p1='3'
    card_p2='3'
    card_p1_count=0
    card_p2_count=0
    for i in range(len(p1_cards)):
        if p1_cards[i]==card_p1:
            card_p1_count+=1
            if card_p1_count==3 and orders.index(card_p1)>orders.index(p1_bomb):p1_bomb=card_p1
        else:
            card_p1=p1_cards[i]
            card_p1_count=0
     
    for i in range(len(p2_cards)):
        if p2_cards[i]==card_p2:
            card_p2_count+=1
            if card_p2_count==3 and orders.index(card_p2)>orders.index(p2_bomb):p2_bomb=card_p2
        else:
            card_p2=p2_cards[i]
            card_p2_count=0
     
    if orders.index(p1_bomb)>orders.index(p2_bomb):
        print(p1)
        continue
    if orders.index(p1_bomb)<orders.index(p2_bomb):
        print(p2)
        continue
         
    #大家都没炸
    #是顺子的先处理
    if len(p1_cards)>=2 and not p1_cards[0]==p1_cards[1]:
        if not len(p1_cards)==len(p2_cards):
            print('ERROR')
            continue
        print(p1 if orders.index(p1_cards[0])>orders.index(p2_cards[0]) else p2)
     
    #不是顺子（单双三）
    if len(p1_cards) in [1,2,3]:
        if not len(p2_cards)==len(p1_cards):#不同长度无法比较
            print('ERROR')
            continue
        #到这，p2也是张数和p1一样
        print(p1 if orders.index(p1_cards[0])>orders.index(p2_cards[0]) else p2)
        continue