from geopy import distance
try:
    n = int(input())
    if n<=1 or n < 100000:

        x = list(map(float, input().split()))
        y = list(map(float, input().split()))
        z = list(map(float, input().split()))
        cord = list(map(float, input().split()))

        count=0
        c=0

        while n!=0:
            coordinates = x[c],y[c]
            dis = distance.distance(coordinates, cord).km
            d = (2*z[c]*6371)**(0.5)
            if dis<=d:
                count =count+1
            c =c+1
            n=n-1

        print(count)

    else:
        exit()
except:
    exit()
