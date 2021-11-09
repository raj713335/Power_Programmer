# Python3 implementation of the approach

# Function to perform the queries
def PerformQueries(a, vec):
    ans = [];

    # Size of the array with
    # 1-based indexing
    n = len(a) - 1;

    # Number of queries
    q = len(vec);

    # Iterating through the queries
    for i in range(q):

        t = vec[i][0];
        m = vec[i][1];

        # If m is more than the
        # size of the array
        if (m > n):
            ans.append(-1);
            continue;

        # Count of turns
        turn = t // n;

        # Find the remainder
        rem = t % n;

        # If the remainder is 0 and turn is
        # odd then the array is empty
        if (rem == 0 and turn % 2 == 1):
            ans.append(-1);
            continue;

        # If the remainder is 0 and turn is
        # even then array is full and
        # is in its initial state
        if (rem == 0 and turn % 2 == 0):
            ans.append(a[m]);
            continue;

        # If the remainder is not 0
        # and the turn is even
        if (turn % 2 == 0):

            # Current size of the array
            cursize = n - rem;

            if (cursize < m):
                ans.append(-1);
                continue;

            print(a)

            ans.append(a[m + rem]);

        else:

            # Current size of the array
            cursize = rem;

            if (cursize < m):
                ans.append(-1);
                continue;

            #print(a)

            ans.append(a[m]);

    # Print the result
    for i in ans:
        print(i);


# Driver code
if __name__ == "__main__":
    # The initial array, -1 is for
    # 1 base indexing
    a = [1,2,3,4,5];

    # Queries in the form of the pairs of (t, M)
    vec = [
        [1, 4],
        [2,1],
        [9,4],
        [4,2],
        [21,1]
    ];

    PerformQueries(a, vec);