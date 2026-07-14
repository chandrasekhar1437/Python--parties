        #dictory--------> dict
# symbol-----> {}
# dict:to store data in key:value pairs
# keys must be unique
#not working indexing
        # empty dictionary -------->"{}", x="{}"
        #non-empty dictionary examples---->  course={"name":"python","class":"live_class ","duration":"2months"}
"""       
        #predfined function in dictionary.
        clear(): it removes all element from the dictionary.
        copy():it returns copy of the dictionary.
        fromkeys():returns a dictionary  with the specified keys and value
        get():returns the values of the specified key.
        item():returns a list containing a tuple for each key-values pair example====>dict_items([(k1,v1),(k2,v2)......])
        keys():its returns list of all keys in the dictionary example====>dict_keys(["",""]).
        pop(keys):its removes the element with the specified key
        popitem():its removes last element from the dictionary
        setdefault(): returns the values of specified key(if key exists) inserts the key with specified values(if key does not exists)
        update():updates the dictionary with the specified key-values example ---->update({key:values}) if key exists====>it updates the values
        if key does not exists====> it insert the key-value pair
    
        
        values():returns list of all values in the dictionary 
"""

user={"name":"chandu","age":27,"mobile":"7989578182","address":"kudupuru"}
print(user,type(user))
print(user["name"])
y={1:23,2:2.3,3:True,4:"chandu"}
print(y,type(y))
print(y[2])
course={"name":"python","class":"live_class ","duration":"2months"}
print(course,type(course),id(course))
course.clear()
print(course,type(course),id(course))
course={"name":"python","class":"live_class ","duration":"2months"}
print(course,id(course))
c=course.copy()
print(c,type(c),id(c))
c.clear()
print(c,type(c),id(c))
print(course,type(course),id(course))
print(course.get("name"))
print(course.pop("class"))
print(course,id(course))
course={"name":"python","class":"live_class ","duration":"2months"}
print(course,type(course),id(course))
print(course.popitem())
print(course,type(course),id(course))
course={"name":"python","class":"live_class ","duration":"2months"}
print(course,type(course),id(course))
print(course.setdefault("name","java"))
print(course.setdefault("name","java"))
print(course,type(course),id(course))
print(course.update({"name":"python_live-1"}))
print(course,id(course))
print(course.update({1:5}))
print(course,id(course))
print(course.keys())
print(course.values())
print(course.items())
x=("a","b","c")
y=0
new=(dict.fromkeys(x,y))
print(new)