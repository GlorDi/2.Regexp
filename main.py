from pprint import pprint
import csv
import re


PHONE_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB = r'+7(\2)-\3-\4-\5 \6\7'


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def main(contact_list: list):
    changed_list = list()
    for item in contact_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  re.sub(PHONE_PATTERN, PHONE_SUB, item[5]),
                  item[6]]
        changed_list.append(result)
    return union(changed_list)


def union(contacts: list):
    for contact in contacts:
        first_name = contact[0]
        last_name = contact[1]
        for changed_contact in contacts:
            changed_first_name = changed_contact[0]
            changed_last_name = changed_contact[1]
            if first_name == changed_first_name and last_name == changed_last_name:
                if contact[2] == "": contact[2] = changed_contact[2]
                if contact[3] == "": contact[3] = changed_contact[3]
                if contact[4] == "": contact[4] = changed_contact[4]
                if contact[5] == "": contact[5] = changed_contact[5]
                if contact[6] == "": contact[6] = changed_contact[6]
    final_list = list()
    for i in contacts:
        if i not in final_list:
            final_list.append(i)
    return final_list


with open("phonebookfinal.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(main(contacts_list))