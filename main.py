# python3

# hashmap=dict()
# result = []
# n = int(input())
# count = 0

# def func(query):
#     number=int(query[1])
#     if query[0] == "add":
#         hashmap.update({number: str(query[2])})
        
#     elif query[0] == "del":
#         try:
#             hashmap.pop(number)
#         except KeyError:
#             pass
        
#     elif query[0] == "find":
#         val = hashmap.get(number)
#         if val==None:
#             result.append("not found")
#         else:
#             result.append(str(val))
            
# while (count!=n):
#     query = input().split()
#     count+=1
#     func(query)
    
# print('\n'.join(result))

--------------------------------------------------------------------------------

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def hash_function(number):
        ans = 0
        for c in reversed(number):
                ans = (ans*255 + ord(c)) %1000043
        return ans % 1000

def add (buckets,number, name):
        hash = hash_function(str(number))
        bucket = buckets[hash]
        if number in bucket:
                buckets[hash] = Query(['add', number, name])
                return
       
        bucket[hash]= [Query(['add', number, name])] +bucket
                
def delete (buckets, number):
        hash = hash_function(str(number))
        bucket = buckets[hash]
        for i in range(len(bucket)):
                if bucket [i].number == number:
                        bucket.pop(i)
                        break
                        
def find(buckets, number):
        hash = hash_function(str(number))
        if number in buckets[hash]:
                return number.name
        return "not found"

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    buckets= [[] for j in range (1000)]
        
       
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
              add(cur_query.number, cur_query.name)
           
        elif cur_query.type == 'del':
            delete(cur_query.number)
        else:
                response= find(cur_query.number)
                result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

