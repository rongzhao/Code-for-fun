"""This program is used to count the number of occurence of all words in the file"""
import csv
def count(file_name, file_name2):
    count_dic = {}
    with open(file_name, 'rb') as file_reader:
        file_object = csv.reader(file_reader, delimiter=' ')
        for line in file_object:
            for word in line:
                if word in count_dic:
                    count_dic[word] = count_dic[word] + 1
                else:
                    count_dic[word] = 1
    file_write = open(file_name2, 'w')
    file_write.write('\n'.join('%s, %s' % pair for pair in count_dic.items()))
    file_write.close()
    print "finished!"

def main():
    file_name = "test1.csv"
    file_name2 = "test2.txt"
    count(file_name, file_name2)

if __name__ == '__main__':
    main()
