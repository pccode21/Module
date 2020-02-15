import json


class Person:
    def __init__(self, name, age, sex, hometown):  # 类的构造函数
        self.name = name
        self.age = age
        self.sex = sex
        self.hometown = hometown

    def json(self):  # json序列化
        print('JSON对象序列化：')
        print(json.dumps(self, default=lambda obj: obj.__dict__))  # self就是obj
        # lambda是匿名函数，可以把任意class的实例变为dict（字典），语法：lambda 参数：表达式
        # 通常class的实例都有一个__dict__属性，它就是一个dict（字典），用来存储实例变量。也有少数例外，比如定义了__slots__的class。
        # 输出结果：JSON对象序列化：{"name": "Lin", "age": 40, "sex": "man", "hometown": "\u5e7f\u4e1c\u63ed\u9633"}
        # \u5e7f\u4e1c\u63ed\u9633 Python3中的json在做dumps操作时，会将中文转换成unicode编码，并以16进制方式存储，而并不是UTF-8格式！


if __name__ == '__main__':
    # Python的字典类型转JSON
    person = Person('Lin', 40, 'man', '广东揭阳')  # 初始化
    person.json()
    person_dict = {"name": "Lin", "age": 40, "sex": "man", "hometown": "广东揭阳"}
    person_dict_json = json.dumps(person_dict, indent=4)  # indent参数为缩进空格数
    print(person_dict_json, '\n')
    # Python的列表类型转JSON
    person_list = ['Lin', 40, 'man', '广东揭阳']
    person_list_json = json.dumps(person_list)  # 列表中的中文转换后还是中文
    print(person_list, '\n')
    # Python的对象类型转JSON
    person_obj = Person('Lin', 40, 'man', '广东揭阳')
    # 中间的匿名函数lambda是获得对象所有属性的字典形式
    person_obj_json = json.dumps(person_obj, default=lambda obj: obj.__dict__, indent=4)
    print(person_obj_json, '\n')
    # JSON转Python的dict类型
    person_json = '{"name": "Lin", "age": 40, "sex": "man", "hometown": "广东揭阳"}'
    person_json_dict = json.loads(person_json)
    print(person_json_dict)
    print(type(person_json_dict), '\n')
    # JSON转Python的列表类型
    person_json = '["Lin", 40, "man", "广东揭阳"]'
    person_json_list = json.loads(person_json)
    print(person_json_list)
    print(type(person_json_list), '\n')
    # JSON转Python的自定义对象类型
    person_json = '{"name": "Lin", "age": 40, "sex": "man", "hometown": "广东揭阳"}'
    # object_hook参数是将dict对象转成自定义对象
    person_json_obj = json.loads(person_json, object_hook=lambda d: Person(d['name'], d['age'], d['sex'], d['hometown']))
    print(person_json_obj)
    print(type(person_json_obj))
