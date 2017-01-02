#!/usr/bin/python
# encoding:utf-8

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

total_property = int(input('输入总资产：'))

goods_list = {}
for k, lst in enumerate(goods, 1):
    print(k, lst['name'], lst['price'])
    goods_list[k] = (lst['name'], lst['price'])

total_price = 0
shopping = []
show_list = {}
while True:
    i1 = input('请选择商品(Y/y结算):')
    if i1.lower() == 'y':
        break
    if int(i1) not in goods_list.keys():
        print('选择有误')
        continue
    shopping.append(goods_list[int(i1)])
for n in shopping:
    if n[0] in show_list.keys():
        show_list[n[0]] += 1
    else:
        show_list[n[0]] = 1
    total_price += n[1]
print('购物车列表：')
# print(show_list)
for g, p in show_list.items():
    print(g,' x ', p)
print('Total: ', total_price)

if total_price > total_property:
    print('购物车总和：', total_price)
    print('当前可用余额：', total_property)
    delta = total_price - total_property
    print('余额不足，至少充值：' + str(delta) + '，否则购物将会失败，请输入充值金额，直接回车放弃此次购物。')
    i2 = input('>>>')
    if not i2:
        print('本次购物失败')
    else:
        total_property += int(i2)
        if total_price > total_property:
            print('充值后余额不足，购物失败')
            exit()
        else:
            print('购物成功')
else:
    print('购买成功')