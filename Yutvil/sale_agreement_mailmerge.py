# -*- coding: utf-8 -*-

from __future__ import print_function

from mailmerge import MailMerge
from datetime import date

template = "C:\\Users\igorek\PycharmProjects\mine\Yutvil\sale_agreement_new.docx"

document = MailMerge(template)

# document.merge(full_name="Жуквов Игорь Павлович", birth_date="31.10.1993", contract_number="01:01/20:20",
#                todays_date="{}".format(date.today()))
# document.write('test-output.docx')
print(document.get_merge_fields())
