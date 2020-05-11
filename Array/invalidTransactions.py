def invalidCheck(transdict):
    invalid = set()
    for k, v in transdict.items():
        for item in range(len(v)):
            if int(v[item][2]) > 1000:
                invalid.add(','.join(v[item]))
            print('>>')
            for i in range(len(v)):
                if i != item:
                    print(v[i])
                    print(v[item])
                    print(i, item)
                    if abs(int(v[i][1]) - int(v[item][1])) <= 60 and v[i][3] != v[item][3]:
                        invalid.add(','.join(v[item]))
                        invalid.add(','.join(v[i]))
                        print('YES')
    print(list(invalid))

def createDict(transactions):
    transdict = dict()
    for ele in transactions:
        ele = ele.split(',')
        if ele[0] not in transdict:
            transdict[ele[0]] = []
        transdict[ele[0]].append([ele[0], ele[1], ele[2], ele[3]])
    print(transdict)
    return transdict

def invalidTransactions(transactions):
    transdict = createDict(transactions)
    invalidCheck(transdict)

def main():
    transactions = ["alex,676,260,bangkok","bob,656,1366,bangkok","alex,393,616,bangkok","bob,820,990,amsterdam","alex,596,1390,amsterdam"]
    invalidTransactions(transactions)

if __name__ == '__main__':
    main()