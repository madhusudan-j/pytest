def find_possible_ways(n_days, missed_days, missed_days_allowed, possible_ways, missed_grads):
    if n_days==0:
        print("-----", possible_ways, "-----")
        if possible_ways[-1] == 0:
            missed_grads = missed_grads + 1
        return 1, missed_grads
    miss_count = 0 # prevent UnboundLocalError: local variable 'miss_count' referenced before assignment
    if missed_days > 0:
        miss_possible_ways, miss_count = find_possible_ways(n_days-1,missed_days-1,missed_days_allowed,possible_ways+[0],missed_grads)
    else:
        miss_possible_ways = 0
    no_miss_possible_ways, no_miss_count = find_possible_ways(n_days-1,missed_days_allowed,missed_days_allowed,possible_ways+[1],missed_grads) 
    print("n_days=", n_days, "missed_days=", missed_days, "miss_possible_ways=", miss_possible_ways, "no_miss_possible_ways=", no_miss_possible_ways)
    return missed_grads + miss_count + no_miss_count, miss_possible_ways + no_miss_possible_ways

n_days = 5
missed_days_allowed = 3
missed_grads = 0 
possible_ways = []
print(find_possible_ways(n_days, missed_days_allowed, missed_days_allowed, possible_ways, missed_grads))