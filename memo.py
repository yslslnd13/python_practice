import sys

option = sys.argv[1]

if option == '-w':
    with open('memo.txt', 'w') as f:
        text_to_memo = sys.argv[2]
        f.write(text_to_memo)
        f.write('\n')
elif option == '-a':
    with open('memo.txt', 'a') as f:
        text_to_memo = sys.argv[2]
        f.write(text_to_memo)
        f.write('\n')

elif option == '-d':
    with open('memo.txt', 'w') as f:
        pass
elif option == '-r':
    with open('memo.txt', 'r') as f:
        print(f.read())