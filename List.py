from sys import argv

#aggiungi elememto alla lista
def add_task(list,task):
    list.append(task)

#fill the list with the task_list.txt
def create_list(filename):
    file = open(filename,'r')
    list=file.read().split('\n')
    file.close()
    remove_task(list,'')
    return list

#elimina le task uguali dalla lista con funzione sopra
# 1: ha rimosso
# 0: non c'erano, e non ha rimosso
def remove_task(list, task):
    if list.count(task) > 0:
        list.remove(task)
        return 1
    else:
        return 0

#rimuovo gli elementi con la ricorsione con sottostringhe
def remove_task_substring(list,substring):
    removed= []
    recursive_remove(list,substring,removed)
    return removed
def recursive_remove(list,substring,removed):
    for task in list:
        if substring in task:
            list.remove(task)
            removed.append(task)
            recursive_remove(list,substring,removed)

#stampa a schermo tutte le task in lista
def show_tasks(list):
    if len(list) > 0:
        return sorted(list)
    else:
        return None

#salva la lista nel file
def save_list(list, filename):
    file=open(filename, 'w')
    for task in list:
        file.write(task+'\n')
    file.close()