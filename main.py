# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
            
 class HashMap:
    def __init__(self):
        self.bucket_count = 1000
        self.buckets = [[] for _ in range(self.bucket_count)]
        self._multiplier = 263
        self._prime = 1000000007

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans*self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, string):
        hashed = self._hash_func(str(string.number))
        bucket = self.buckets[hashed]
        if string.type == 'add':
            for i in range(len(bucket)):
                if bucket[i].number == string.number:
                    bucket[i].name = string.name
                    break
            else:
                self.buckets[hashed] = [string] + bucket

    def delete(self, number):
        hashed = self._hash_func(str(number))
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i].number == number:
                bucket.pop(i)
                break
             
    def find(self, string):
        hashed = self._hash_func(string)
        if string in self.buckets[hashed]:
            return "yes"
        return "no"



def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    
    
    
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

