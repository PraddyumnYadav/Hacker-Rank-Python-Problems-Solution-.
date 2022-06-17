# Checking if file is main or not
if __name__ == '__main__':

    # creat a dictionary and list
    dic = {}
    s = list()

    # running the for loop
    for _ in range(int(input())):

        # inpput the name and score
        name = input()
        score = float(input())

        # add the name in dictionary if score already exists
        if score in dic:
            dic[score].append(name)
        else:
            dic[score] = [name]

        # append the score to the list if it is not in list
        if score not in s:
            s.append(score)
    
    # find the minimum score and add it to the dictionary m
    m=min(s)

    # remove minimum score from s
    s.remove(m)

    # find the second minimum score and store it in m1
    m1=min(s)

    # sort the m1
    dic[m1].sort()

    # print the name of students alphabetically
    for name in dic[m1]:
        print(name)
