#Quiz 11a:  select data based on target values:


def select_data(data, target, labels = None):
    if labels == None:
        return data,target
    else:
        selected = [(d,t) for (d,t) in zip(data,target) if t in labels]
        d_sel,t_sel = zip(*selected)
        return d_sel, t_sel
