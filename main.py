# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class PhoneBook:
    def __init__(self):
        self.bucket_count = 1000
        self._prime = 10000019
        self._multiplier = 263
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans*self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, string):
        hashed = self._hash_func(str(string.number))
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed] = [string] + bucket

    def delete(self, string):
        hashed = self._hash_func(str(string))
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i] == string:      
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
    phone_book = PhoneBook()
    for cur_query in queries:
        if cur_query.type == 'add':
            phone_book.add(cur_query)
        elif cur_query.type == 'del':
            phone_book.delete(cur_query.number)
        else:
            response = 'not found'
            if phone_book.find(cur_query.number) == "yes":
                for contact in phone_book.buckets[phone_book._hash_func(str(cur_query.number))]:
                    if contact.number == cur_query.number:
                        response = contact.name
                        break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
