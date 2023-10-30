#!/usr/bin/python3
"""divided module for matrix"""


def matrix_divided(matrix, div):
    """Return: (list of lists)
        Args: 
            matrix: (list of lists)
            div: intt
        """
        matrix_errorr = "matrix must be a matrix (list of lists) of integers or floats"
        matrix_lists_length = -1 

        if not isinstance(matrix, list):
            raise TypeError(matrix_errorr)
        
        for list_of_intt in matrix:
            if not isinstance(list_of_intt, list):
                raise TypeError(matrix_errorr)
            if not all(isinstance(num, (int, float)) for num in list_of_int):
                raise TypeError(matrix_errorr)

            if matrix_lists_length == -1:
                matrix_lists_length = len(lists_of_intt)
            elif matrix_lists_length != len(list_of_intt):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            if div == 0:
                raise ZeroDivisionError("division by zero")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")

            new_matrixx = []
            for  list_of_intt in matrix:
                my_roww = []
                for num in list_of_intt:
                    my_roww.append(round(num / div, 2))
                new_matrix
                for num in list_of_intt:
                    my_roww.append(round(num / div, 2))
                new_matrix.append(my_roww)
                return new_matrixx.append(my_roww)
                return new_matrixx
