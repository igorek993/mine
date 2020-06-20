# -*- coding: utf-8 -*-

from __future__ import print_function

from mailmerge import MailMerge
from datetime import date

TEMPLATE = "C:\\Users\igorek\PycharmProjects\mine\Yutvil\sale_agreement_new.docx"


class SaleAgreement:

    def save_doc(self, **kwargs):
        document = MailMerge(TEMPLATE)
        document.merge(**kwargs)
        document.write('test-output.docx')
        # print(document.get_merge_fields())
        # print(**kwargs)
