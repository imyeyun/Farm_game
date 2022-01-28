class Seed():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return "%s=> 가격:%d" % (self.name, self.price)

    def print_sell_list():
        carot_seed = Seed("당근씨앗", "200")
        print(carot_seed)
        been_seed = Seed("콩씨앗","200")
        print(been_seed)
        cabbage_seed=Seed("배추씨앗","300")
        print(cabbage_seed)
    
