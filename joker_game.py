# 抽鬼牌
# random.shuffle(x) 打亂x序列
# pop(x) 刪除x位置東西
import random

def throw(name,player):  # 丟掉成對的牌
    part = [card[1:] for card in player]
    for i in range(1,13+1):
        while part.count(str(i)) >= 2:  # 超過2張丟2或4張
            card_1 = part.index(str(i))         # 第一張
            card_2 = part.index(str(i),card_1+1)# 第二張
            print(name,'丟掉',player[card_1],player[card_2])
            part.pop(card_1)    # 先刪第一張
            part.pop(card_2-1)  # 第二張前面少一張 -1
            player.pop(card_1)
            player.pop(card_2-1)
    return player

suits = ['♠','♥','♦','♣']
deck = [suit+str(num+1) for suit in suits for num in range(13)] + ['♖']
random.shuffle(deck)    # 洗牌
player1 = [deck[i] for i in range(len(deck)) if i%2 == 0]   # 電腦
player2 = [deck[i] for i in range(len(deck)) if i%2 == 1]   # 使用者

print('-原來的牌-')
print(player2)

print('\n-丟牌後-')
throw('電腦',player1)
throw('玩家',player2)
print(player2)

while True:
    shuffle = input('\n要洗牌嗎? (y/n):')
    if shuffle == 'y':
        random.shuffle(player2)
        print('-洗牌完畢-')
        print(player2)
    
    print('\n--電腦抽牌--')
    choose = random.randint(0,len(player2)-1)
    print(player2[choose]+' 被抽走')
    player1.append(player2.pop(choose))
    throw('電腦',player1)
    print(player2)
    random.shuffle(player1) # 電腦洗牌
    
    if len(player1)+len(player2) == 1:
        break

    print('\n--玩家抽牌--')
    choose = eval(input('請選擇1~'+str(len(player1))+':'))
    print('抽到 '+player1[choose-1])
    player2.append(player1.pop(choose-1))
    print(player2)  # 得到牌後
    old_len = len(player2)
    throw('玩家',player2)
    if old_len != len(player2): # 牌數有變
        print(player2)  # 丟掉後

    if len(player1)+len(player2) == 1:
        break

if len(player1) == 1:
    print('\n-玩家勝利!-')

if len(player2) == 1:
    print('\n-玩家失敗!-')
    