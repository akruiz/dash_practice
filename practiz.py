
repository = ['bags', 'baggage', 'banner', 'box', 'cloths']
customerQuery = 'bags'
first_letters = customerQuery[0:2]
third_letters = customerQuery[0:3]
first_rep = []
ans_one = []
for i in repository:
    res_rep = i[:2]
    first_rep.append(res_rep)
for f, i in zip(first_rep, range(len(repository))):
    if first_letters in f:
        ans_one.append(repository[i])