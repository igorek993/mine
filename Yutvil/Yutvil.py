# -*- coding: utf-8 -*-

from __future__ import print_function

from mailmerge import MailMerge
from datetime import date

template = "C:\\Users\igorek\PycharmProjects\mine\Yutvil\contract.docx"

document = MailMerge(template)

document.merge(Test="Here")
document.write('test-output.docx')
# print(document.get_merge_fields())
