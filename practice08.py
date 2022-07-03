menu = {"커피", "우유", "주스"}
print(menu,type(menu))

menu = list(menu)           # {'주스', '커피', '우유'} <class 'set'>
print(menu,type(menu))      # ['주스', '커피', '우유'] <class 'list'>

menu = tuple(menu)          # ('주스', '커피', '우유') <class 'tuple'>
print(menu,type(menu))

menu = set(menu)            # {'주스', '커피', '우유'} <class 'set'>
print(menu, type(menu))
