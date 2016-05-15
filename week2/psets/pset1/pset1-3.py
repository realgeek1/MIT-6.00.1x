def item_order(order):
    hb = order.count('hamburger')
    wtr = order.count('water')
    sld = order.count('salad')
    return 'salad:' + str(sld) + ' hamburger:' + str(hb) + ' water:' + str(wtr)