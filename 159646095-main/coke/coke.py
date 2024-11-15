acceptable_coins = ['5', '10', '25']
coin_sum = 0

while coin_sum < 50:
    coin_provided = input('Insert Coin: ')
    if coin_provided in acceptable_coins:
        coin_sum += int(coin_provided)
    print('Amount Due:', 50 - coin_sum)

if coin_sum >= 50:
    change_owed = coin_sum - 50
    print('Change Owed:', change_owed)
