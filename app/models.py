class Resource(object):

    """
    Resource Model
    """

    def __init__(self, id, label, format, src):
        self.id = id
        self.label = label
        self.format = format
        self.src = src


class DataTable(Resource):

    def __init__(self, fields, id, label, format, src):
        Resource.__init__(self, id, label, format, src)
        self.fields = fields

    # def get_field_by_id(self, id):
    #     self.fields

class Field(object):

    """
    Field Model
    """

    def __init__(self, id, label, description, dataType):
        self.id = id
        self.label = label
        self.description = description
        self.dataType = dataType


class DataPackage(object):

    """
    Data Package Model
    """

    def __init__(self, id, resources):
        self.id = id
        self.resources = resources

    def get_resource_by_id(self, id):
        resources = filter(lambda resource: resource.id == id, self.resources)
        if len(resources > 0):
            return resources[0]
        else:
            return None    