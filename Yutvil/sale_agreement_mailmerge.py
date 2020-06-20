# -*- coding: utf-8 -*-

from __future__ import print_function

from tkinter.filedialog import asksaveasfile

from mailmerge import MailMerge
from datetime import date

TEMPLATE = "C:\\Users\igorek\PycharmProjects\mine\Yutvil\sale_agreement_new.docx"


class SaleAgreement:

    def save_doc(self, file_name, **kwargs):
        document = MailMerge(TEMPLATE)
        document.merge(**kwargs)
        path = asksaveasfile(mode="w", defaultextension=".doc", initialfile=file_name)
        if path:
            path = path.name
            document.write(path)
        else:
            pass
        # print(document.get_merge_fields())
        # print(**kwargs)
