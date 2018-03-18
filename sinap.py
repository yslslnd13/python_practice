
names='이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'.split(',')

#1
a = [i[0] for i in names]
print('kim: %d, lee: %d' % (a.count('김'), a.count('이')))

#2 
print(names.count('이재영'))

#3
print(set(names))

#4
print(sorted(list(set(names))))
