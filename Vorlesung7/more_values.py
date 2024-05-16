def get_tax(net_price : float) -> tuple:
    return (net_price, net_price * 0.19, net_price + net_price*0.19)

net, tax, gross = get_tax(10.0)
print(net)
print(tax)
print(gross)
