import sys   
sys.path.append("/home/anas/ASAC/401/data-structures-and-algorithms/python/code_challenges/graphs")   
from graphs.graphs import Vertex,Graph




def business_trip(graph,arr):
    """
    Determine whether the trip is possible with direct flights, and how much it would cost.



    Args:
        graph (Graph): contains all the list of the cities and its cost
        arr (list): List of the cities
    Return
        tuple : (cost, Bool).
            
            cost: Total cost for Trip.
            Bool: True or False.
     

    """
    
    cost=0
    i=0
    length=len(arr)-1

    def check_cost(city1,city2):
     ''' Calculate the Cost value for the Trip between two City  '''
     neighbors=graph.get_neighbors(city1)
     for city in neighbors:
            if city.vertex.value == city2:
             nonlocal cost , i
             cost += city.weight
             i+=1
             
            if i == length:
                return
     check_cost(arr[length-i-1],arr[length-i])
     

    try:
     check_cost(arr[length-1],arr[length])
    except:
     return (bool(cost),cost)
 
    return (bool(cost),cost)




if __name__ == '__main__':
    ver=Vertex('Metroville')
    ver2=Vertex('Pandora')
    ver3=Vertex('Arendelle')
    ver4=Vertex('Monstropolis')
    ver5=Vertex('Naboo')
    
    # ver3=Vertex('d')
    # ver4=Vertex('p')

    graph=Graph()
    graph.add_vertex(ver)
    graph.add_vertex(ver2)
    graph.add_vertex(ver3)
    graph.add_vertex(ver4)
    graph.add_vertex(ver5)
    graph.add_edges(ver,ver2,50)
    graph.add_edges(ver3,ver4,150)
    graph.add_edges(ver5,ver4,250)

    # graph.add_vertex(ver3)
    # graph.add_vertex(ver4)

    # graph.add_edges(ver,ver3)
    # graph.add_edges(ver,ver4)

    print(business_trip(graph,['Arendelle','Monstropolis', 'Naboo']	))
