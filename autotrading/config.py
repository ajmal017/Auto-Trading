class DictObj(object):
    def __init__(self, mp):
        import pprint
        self.map = mp
        pprint.pprint(mp)

    def __setattr__(self, name, value):
        if name == 'map':
            # print("init set attr", name ,"value:", value)
            object.__setattr__(self, name, value)
            return
        # print('set attr called ', name, value)
        self.map[name] = value

    def __getattr__(self, name):
        # print('get attr called ', name)
        return  self.map[name]


Config = DictObj({
    'SYMBOL': 'AAPL',
    'STRATEGY': "CAT",
    'TRAIN_VALID_SPLIT_DATE': "2017-01-01",
    'CASH': 10000.0,
    'FEE': 0.002,
    'LEBELLING_METHOD': 'FTH',
    'KFOLD': 10,
    'HYPEROPT_MAX_EVAL': 10,
    'MODEL_SAVE_PATH': "./checkpoints",
    'SEED': 1016
})
