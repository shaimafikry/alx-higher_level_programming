#!/usr/bin/python3
"""pasacal traingle
    """
 
def pascal_triangle(n):
    if n <= 0:
        return []
    m_list = [[1], [1,1]]
    # print ( "this before loop", m_list)
    new_list = []
    while n > 0:
        loop_list = m_list[-1]
        # print ("this before loop after assignng the last list ", loop_list)
        new_list = []
        for i in range(len(loop_list)):
            # print ("this is i", i)
            if i != len(loop_list) - 1:
                new_list.append(loop_list[i] + loop_list[i+1])
            # print ( "this after elemnt ", new_list)
        new_list = [1] + new_list + [1]
        # print ( "this after adding 1 loop", new_list)
        m_list.append(new_list)
        # print ( "this after each  loop", m_list)
        n -= 1
    return m_list
