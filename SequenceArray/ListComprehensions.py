# 列表推导式


def cartesian_product():
    """
    用列表推导式计算笛卡尔积
    :return:
    """
    colors = ['black', 'red']
    sizes = ['S', 'M', 'L']
    t_shirts = [(color, size) for color in colors for size in sizes]
    print(t_shirts)


if __name__ == '__main__':
    cartesian_product()
