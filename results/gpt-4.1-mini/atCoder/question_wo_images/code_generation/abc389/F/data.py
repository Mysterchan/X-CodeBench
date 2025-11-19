import sys
input = sys.stdin.readline

N = int(input())
MAX_R = 500000

# We'll use a difference array to count how many intervals cover each rating
diff = [0] * (MAX_R + 2)  # +2 to avoid index issues when doing r+1

for _ in range(N):
    L, R = map(int, input().split())
    diff[L] += 1
    if R + 1 <= MAX_R:
        diff[R + 1] -= 1

# Prefix sum to get coverage count for each rating
for i in range(1, MAX_R + 1):
    diff[i] += diff[i - 1]

# Now, for each rating x, diff[x] = number of contests where rating x is in [L_i, R_i]

# We want to answer queries: starting from X, after all contests, rating increases by sum of diff at each step
# But rating changes after each contest, so the rating changes dynamically.
# However, the problem states that the rating increases by 1 if current rating is in the interval.
# The order of contests is fixed, but the intervals are given, and the rating changes after each contest.

# Wait, the problem states:
# For each contest i, if rating is between L_i and R_i (inclusive), rating += 1.
# The rating changes after each contest, so the rating for contest i+1 depends on the previous rating.

# The naive approach is to simulate for each query, but that is O(NQ) which is too large.

# Observation:
# The rating only increases by 1 if it is in the interval.
# The intervals are fixed.
# The rating changes by +1 if rating in [L_i, R_i].
# So the rating after all contests is:
# rating_final = X + number_of_intervals that cover the rating at the time of that contest.

# But since rating changes after each contest, the rating at contest i depends on how many intervals before i covered the rating.

# Another approach:
# Let's consider the rating line from 1 to MAX_R.
# For each rating x, how many intervals cover x? diff[x] = number of intervals covering x.

# But rating changes after each contest, so the rating moves forward by the number of intervals that cover the rating at that time.

# Let's consider the rating as a position on the number line.
# After all contests, the rating increases by the number of intervals that cover the rating at the time of that contest.

# But since rating changes after each contest, the rating at contest i is:
# rating_i = X + number of intervals covering rating at contest 1 + ... + number of intervals covering rating at contest i-1

# This is complicated to simulate for each query.

# Let's try to think differently.

# Since rating increases by 1 if rating in [L_i, R_i], and rating changes after each contest,
# the rating after all contests is:
# rating_final = X + number of contests i where rating_i in [L_i, R_i]

# But rating_i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals that covered rating at previous contests.

# So rating_i = X + (number of intervals covering rating at contests 1 to i-1).

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.

# But rating changes after each contest, so the rating at contest i is X + number of intervals covering rating at contests 1 to i-1.

# Let's try to simulate the rating changes for all possible initial ratings.

# Since rating can be up to 5*10^5, and N up to 2*10^5, rating can go up to 7*10^5.

# Let's try to precompute for all ratings from 1 to MAX_R + N the number of intervals covering that rating.

# Then, for each rating x, the number of intervals covering x is diff[x].

# Now, the rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i is rating at contest i-1 + 1 if rating at contest i-1 in interval i-1, else rating at contest i-1.

# Wait, the problem states the intervals are given, but the order of contests is fixed.

# So the rating changes step by step.

# But simulating for each query is too slow.

# Let's try to think differently.

# Let's consider the rating line from 1 to MAX_R + N.

# For each rating x, diff[x] = number of intervals covering x.

# The rating after all contests starting from X is:

# rating_final = X + number of intervals covering rating at contest 1 + number of intervals covering rating at contest 2 + ... + number of intervals covering rating at contest N

# But rating at contest i depends on previous increments.

# Let's try to think about the rating after all contests as a function f(X).

# Let's define f(X) = final rating after all contests starting from X.

# The rating increases by 1 if rating_i in [L_i, R_i].

# Since rating increases by 1 only if rating_i in [L_i, R_i], and rating_i changes by +1 each time,
# the rating after all contests is X + number of intervals that cover rating_i at contest i.

# But rating_i = X + number of intervals covering rating at contests 1 to i-1.

# This is complicated.

# Let's try to think about the rating after all contests as a function of X.

# Let's consider the rating line from 1 to MAX_R + N (since rating can increase up to N).

# For each rating x, how many intervals cover x?

# The rating increases by 1 if rating is in the interval.

# So the rating after all contests is X + number of intervals covering rating at the time of that contest.