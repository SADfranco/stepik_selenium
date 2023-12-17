def attribute(attr_name):
    attrs = []
    for attr in attr_name.get_property('attributes'):
        attrs.append([attr['name'], attr['value']])
    print(attrs)