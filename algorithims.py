
def change_finder(testedList, interactive=False):

    changes = []

    for item1, item2 in zip(testedList, testedList[1:]):
        if item1 > item2:
            range_result = '-' + str(item1 - item2)
            if interactive:
                print('Change: ' + range_result)
            changes.append(range_result)
        elif item1 < item2:
            range_result = '+' + str(item2 - item1)
            if interactive:
                print('Change: ' + range_result)
            changes.append(range_result)
        elif item1 == item2:
            range_result = '0'
            if interactive:
                print('Change: None')
            changes.append(range_result)

    return changes

#  This might be useful in the future?
#
# def change_to_int(List):
#
#    processed_list = []
#
#    for item in List:
#        if '-' in item:
#            int_change = item.replace('-', '')
#            processed_list.append(int(int_change))
#        elif '+' in item:
#            int_change = item.replace('+', '')
#            processed_list.append(int(int_change))
#
#    return processed_list


def dict_to_graph(dictionary, title, x_title=None, y_title=None):
    """
    Makes a graph with x and y values.

    DICTONARY STRUCTURE:

    {title_y: [value_y], title_x: [value_x]}
    """

    # METHOD IMPORT
    import matplotlib.pyplot as mpl

    x_value, y_value = [], []
    graph_type_simple = False

    # Check if titles are being used, if so graph_type is simple.
    if x_title is not None and y_title is not None:
        x_graph_title = x_title
        y_graph_title = y_title

        for x, y in dictionary.items():
            x_value.append(x)
            y_value.append(y)

        graph_type_simple = True

    else:

        graph_titles, graph_values = [], []

        for key, value in dictionary.items():
            graph_titles.append(key)
            graph_values.append(value)

        x_graph_title, x_value = graph_titles[1], graph_values[1]
        y_graph_title, y_value = graph_titles[0], graph_values[0]

    try:
        for y in range(0, len(y_value)):
            y_value[y] = float(y_value[y])
    except TypeError:
        pass

    try:
        for x in range(0, len(x_value)):
            x_value[x] = float(x_value[x])
    except TypeError:
        pass

    mpl.plot(x_value, y_value)
    mpl.title(title, fontsize=15)
    mpl.xlabel(x_graph_title, fontsize=12)
    mpl.ylabel(y_graph_title, fontsize=12)
    mpl.tick_params('both', labelsize=10)
    mpl.ticklabel_format(useOffset=False, style='plain')

    mpl.show()


def dict_to_box_plot(input_dict, title, xtitle, ytitle):

    import matplotlib.pyplot as mpl

    data_x = []
    z = 0
    for x in range(0, len(input_dict.values())):
        z += 1
        data_x.append(z)

    data_x_label = []
    for x in input_dict.keys():
        data_x_label.append(int(x))

    data_y = []
    for x in input_dict.values():
        data_y.append(x)

    mpl.boxplot(data_y)
    mpl.title(title, fontsize=15)
    mpl.ylabel(ytitle, fontsize=10)
    mpl.xlabel(xtitle, fontsize=10)
    mpl.xticks(data_x, data_x_label, rotation='vertical')
    mpl.margins(0.2)
    mpl.subplots_adjust(bottom=0.15)
    mpl.show()


def datetime_fmt(pro_list):

    list_of_processed_years = []

    for item in pro_list:
        new_str = ''
        item = list(item)
        del item[4:]
        for x in item:
            new_str = new_str + x
            if len(new_str) == 4:
                list_of_processed_years.append(new_str)

    return list_of_processed_years


def list_half(pro_list):
    x = len(pro_list)
    y = x/2

    if y is float:
        round(y)

    y = int(y)

    return y