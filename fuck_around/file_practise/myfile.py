testfile = open('test.txt')

# print "name :", testfile.read()

name = "sam"

for x in testfile.read(10):
    print x

testfile.close()
