#!/usr/bin/python3
"""pasacal traingle
    """


def pascal_triangle(n):
    """tkes n and returns pascal triangle

    Args:
        n (int): num to be managed

    Returns:
        list_: in a pascal mode
    """
    if n <= 0:
        return []
    m_list = [[1]]
    # print ( "this before loop", m_list)
    new_list = []
    m = 1
    while m < n:
        loop_list = m_list[-1]
        # print ("this before loop after assignng the last list ", loop_list)
        new_list = []
        for i in range(len(loop_list)):
            # print ("this is i", i)
            if i != len(loop_list) - 1:
                new_list.append(loop_list[i] + loop_list[i + 1])
            # print ( "this after elemnt ", new_list)
        new_list = [1] + new_list + [1]
        # print ( "this after adding 1 loop", new_list)
        m_list.append(new_list)
        # print ( "this after each  loop", m_list)
        m += 1
    return m_list
