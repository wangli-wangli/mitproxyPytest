from string import Template
import csv
from translate import Translator
class caseGenerator:
    def generate(self):
        # 模版文件
        template_file = open(r'default.tmpl', 'r',encoding='utf-8')
        tmpl = Template(template_file.read())
        lines=[]
        file_name = '../test_dir/test_api2.py'
        file = open(file_name, 'a+', encoding='utf-8')
        import_str=['import pytest\n','import json\n','from  sendRequest import interface\n','from interface_parms import api_val\n']
        file.writelines(import_str)
        file.close()
        global num
        global tag_name
        num=0
        tag_name=''
        with open(r'C:\Users\ZL-52S8FFG\Desktop\new2.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i in reader:
                tag=i[0]
                if tag_name==tag:
                    num=num+1

                else:
                    num=0
                    tag_name=tag
                translator = Translator(from_lang="chinese", to_lang="english")
                translation = translator.translate(tag)
                translation = translation[0].lower() + translation[1:]
                list1 = translation.split()
                function_name = '_'.join(list1)
                lines.append(tmpl.substitute(
                    Tag=i[0],
                    FunctionName='test_'+function_name+str(num),
                    Hostname=i[2],
                    Path=i[1],
                    Authoration=i[4],
                    Content_type=i[5],
                    Params=i[6],

                ))

            file=open(file_name,'a+',encoding='utf-8')
            file.writelines(lines)
            file.close()
        print('generator over')


if __name__ == '__main__':
    caseGenerator=caseGenerator()
    caseGenerator.generate()