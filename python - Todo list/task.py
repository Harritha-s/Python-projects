task = []
completed = []

def add(i):
    task.append(i)

def delete(i):
    task.remove(i)

def view():
    n = 1
    print()
    print("Task in list")
    for t in task:
        print(str(n)+ " : "+t)
        n += 1
    n = 1
    if(completed != []):
        print()
        print("Tasks completed")
        for t in completed:
            print(str(n)+" : "+t)
            n += 1
    else:
        print()
        print("No task is completed")

def done(i):
    print()
    print(i + " is done")
    task.remove(i)
    completed.append(i)
