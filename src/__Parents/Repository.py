
class Repository:

    @staticmethod
    def get_dict_items(obj):
        dict_item = {}

        if not obj:
            return obj

        for key, value in obj.__dict__.items():
            if not key == '_sa_instance_state':
                if value.__class__.__name__ == 'Position' \
                        or value.__class__.__name__ == 'Sphere'\
                        or value.__class__.__name__ == 'Unit' \
                        or value.__class__.__name__ == 'Firm' \
                        or value.__class__.__name__ == 'Role' \
                        or value.__class__.__name__ == 'ProductType'\
                        or value.__class__.__name__ == 'IncomeType'\
                        or value.__class__.__name__ == 'ExpenseType' \
                        or value.__class__.__name__ == 'Permission' \
                        or value.__class__.__name__ == 'Invoice' \
                        or value.__class__.__name__ == 'InvoiceNameList' \
                        or value.__class__.__name__ == 'UserRoleFirm' \
                        or value.__class__.__name__ == 'FirmPermission':
                    dict_item[key] = Repository.get_dict_items(value)

                else:
                    dict_item[key] = value

        return dict_item

    @staticmethod
    def get_page_items(page):
        page_items: dict = {'total': page.total,
                            'page': page.page,
                            'pages': page.pages,
                            'per_page': page.per_page,
                            'items': []}

        for item in page.items:
            page_items['items'].append(Repository.get_dict_items(item))

        return page_items

    @staticmethod
    def get_array_items(array):
        items: list = []

        for item in array:
            items.append(Repository.get_dict_items(item))

        return items
