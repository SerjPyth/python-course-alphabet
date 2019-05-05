
    name = data['name']
    language = data['language']
    position = data['position']
    pr = Programmer(name=name, language=language, position=position)
    pr.enough_coffee = data.get('enough_coffee', False)
    return pr


def to_json(obj: Programmer):
    data = {"name": obj.name, "language": obj.language, "position": obj.position}
    return data
# Serialization 
    
## JSON
    
    - load from json  
    - save to json
    - simple_json with json
    - json encoder
        cls, default для сереалізація кастомних чи не дефолтний типів
        
    - json hook
        object_hook для десереалізації кастомних типів
  
### Useful links

https://medium.com/python-pandemonium/json-the-python-way-91aac95d4041

Коротке описанння способів збереження конфігів
https://martin-thoma.com/configuration-files-in-python/
## Pickle 

    What is the difference from json
    When to use pickle 
    Example of usage
    __setstate__
    __getstate__
    

### Useful links

https://docs.python.org/3/library/pickle.html

Стаття важка. Буде багато сленгу. Як бонус тим, хто не боїться глибше розібратися

https://habr.com/ru/company/otus/blog/353480/  

## Yaml

    What is it
    When to use
    examples

### Useful links

https://yaml.readthedocs.io/en/latest/install.html

https://docs.python.org/3/library/typing.html

### Decorators