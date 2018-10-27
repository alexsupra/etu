answers_test=["a", "a", "c", "b"]
answers_right=["a", "a", "b", ""]
score=0

for i in range(len(answers_test)):
    print(answers_test[i])

for test, right in zip(answers_test, answers_right):
    print(test, '-->', right)
    if test == right:
        score = score + 4
        print('score increased: ', score)
    if right == "":
        print('none')
    if test != right:
        if right != "":
            score = score - 1
            print('score decreased: ', score)
        else:
            print('score not changed: ', score)
