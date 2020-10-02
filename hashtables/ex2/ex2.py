#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}

    route = [None] * length

    for ticket in tickets:
        dict[ticket.source] = ticket.destination
    next = dict["NONE"]

    for j in range(0, length):
        route[j] = next
        
        next = dict[next]
    return route
