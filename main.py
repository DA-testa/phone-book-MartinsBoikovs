# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
        else:
            self.name = None

class PhoneBook:
    def __init__(self):
        self.bucket_count = 1000
        self._prime = 10000211
        self._multiplier = 341
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans*self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, number, name):
        hashed = self._hash_func(str(number))
        bucket = self.buckets[hashed]
        for i, contact in enumerate(bucket):
            if contact.number == number:
                bucket[i] = Query(['add', number, name])
                return
        self.buckets[hashed] = [Query(['add', number, name])] + bucket 

    def delete(self, number):
        hashed = self._hash_func(str(number))
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i].number == number:      
                bucket.pop(i)
                break
                    
    def find(self, number):
        hashed = self._hash_func(str(number))
        for contact in self.buckets[hashed]:
            if contact.number == number:
                return contact.name
        return "not found"
    


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    phone_book = PhoneBook()
    for cur_query in queries:
        if cur_query.type == 'add':
            phone_book.add(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            phone_book.delete(cur_query.number)
        else:
            result.append(phone_book.find(cur_query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
