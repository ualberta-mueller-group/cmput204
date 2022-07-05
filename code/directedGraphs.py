from reverse import reverse

simple =  {  'A': ['B', 'C'],
             'B': ['C'],
             'C': []
          }

bookfigure3point7 =  {  'A': ['B', 'C', 'F'],
                        'B': ['E'],
                        'C': ['D'],
                        'D': ['A', 'H'],
                        'E': ['F', 'G', 'H'],
                        'F': ['B', 'G'],
                        'G': [],
                        'H': ['G']
                     }

bookfigure3point8 =  {  'A': ['C'],
                        'B': ['A', 'D'],
                        'C': ['E', 'F'],
                        'D': ['C'],
                        'E': [],
                        'F': []
                     }

bookfigure3point9 =  {  'A': ['B'],
                        'B': ['C','D','E'],
                        'C': ['F'],
                        'D': [],
                        'E': ['B', 'F', 'G'],
                        'F': ['C', 'H'],
                        'G': ['H', 'J'],
                        'H': ['K'],
                        'I': ['G'],
                        'J': ['I'],
                        'K': ['L'],
                        'L': ['J']
                     }

bookfigure3point10 = reverse(bookfigure3point9)
