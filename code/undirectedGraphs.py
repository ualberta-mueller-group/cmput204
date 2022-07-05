# Examples of undirected graphs which are used as test cases
# for graph algorithms

westernCanada = { 'BC': ['AB'],
                  'AB': ['BC', 'SK'],
                  'SK': ['AB', 'MB'],
                  'MB': ['SK'],
                }


westernCanadaPlus2 = { 'BC': ['AB'],
                       'AB': ['BC', 'SK'],
                       'SK': ['AB', 'MB'],
                       'MB': ['SK'],
                       'XX': ['YY'],
                       'YY': ['XX']
                      }

bookFigure3Point2 =  {  'G': ['D', 'H'],
                        'H': ['G', 'D'],
                        'D': ['A', 'G', 'H'],
                        'A': ['B', 'C', 'D'],
                        'C': ['A', 'F'],
                        'B': ['A', 'E', 'F'],
                        'F': ['B', 'C'],
                        'E': ['B', 'I', 'J'],
                        'I': ['E', 'J'],
                        'J': ['E', 'I'],
                        'K': ['L'],
                        'L': ['K']
                     }

mostlyDisconnected = { 1:[5],
                       2:[],
                       3:[4],
                       4:[3],
                       5:[1],
                       6:[],
                       7:[]
                     }
