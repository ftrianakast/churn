from models import Field
from models import DataTable
from models import DataPackage


def decode_data_package(dictionary_data_package):
    data_package = dictionary_data_package["datapkg"]
    resources = data_package["resources"]
    real_resources = []

    for i, resource in enumerate(resources):
        real_fields = []
        schema = resource["schema"]
        fields = schema["fields"]
        for i, field in enumerate(fields):
            field_object = Field(field["columnId"], field[
                                 "label"], field["description"], field["dataType"])
            real_fields.append(field_object)
        data_table = DataTable(real_fields, resource["tableId"], resource[
                               "label"], resource["format"], resource["s3Url"])
        real_resources.append(data_table)

    return DataPackage('a', real_resources)