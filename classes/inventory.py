class Items:
    def __init__(self, item_dict):
        self.name = item_dict["item"]
        self.type = item_dict["type"]
        self.quantity = item_dict["quantity"]
        self.prop = item_dict["prop"]
