def findSum(numbers, queries):
    a=[0]
    b=[0]
    for x in numbers:
        a.append(a[-1]+x)
        b.append(b[-1]+(x==0))
    return [a[r]-a[l-1]+x*(b[r]-b[l-1]) for l,r,x in queries]      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(raw_input().strip())

    numbers = []

    for _ in xrange(numbers_count):
        numbers_item = int(raw_input().strip())
        numbers.append(numbers_item)

    queries_rows = int(raw_input().strip())
    queries_columns = int(raw_input().strip())

    queries = []

    for _ in xrange(queries_rows):
        queries.append(map(int, raw_input().rstrip().split()))

    result = findSum(numbers, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
