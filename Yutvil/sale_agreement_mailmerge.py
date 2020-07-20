# -*- coding: utf-8 -*-
from __future__ import print_function
from tkinter.filedialog import asksaveasfile
from mailmerge import MailMerge

TEMPLATE = "data\sale_agreement_new.docx"


class SaleAgreement:

    def save_doc(self, file_name, **kwargs):
        document = MailMerge(TEMPLATE)
        document.merge(**kwargs)
        path = asksaveasfile(mode="w", defaultextension=".doc", initialfile=file_name)
        if path:
            path = path.name
            document.write(path)
