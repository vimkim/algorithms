

def main():

    airports = []
    connectingTime = []
    with open("Hawaiian-airports.txt") as f:
        for line in f:
            airport, time = line.split()
            airports.append(airport)
            connectingTime.append(time)

    N = len(airports)
    convert = {airports[i]:i for i in range(N)}

    with open("Hawaiian-flights.txt") as f:
        for line in f:
            #print(line.strip())
            pass
    G = []


if __name__ == "__main__":
    main()