#lists part2
study=["python","java","c++","php","html","css","script","css"]
tutorial=["extend","list1","list2"]
study.append("c#")
study.insert(1,"Ghada")
study.remove("python")
study.clear()
study.pop()
what_was_pop=study.pop()
print(what_was_pop)
print(study.index("php"))
print(study.count("css"))
study.sort()
print(study)
list_new=study.copy()
study.append("chibo")
print(list_new)
print(study)
print(study,tutorial)
study.extend(tutorial) # == study+=tutorial
print(study)
