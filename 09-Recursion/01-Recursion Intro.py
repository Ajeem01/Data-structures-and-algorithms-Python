# a function that calls itself until itt doesnt.

def open_the_gift():
    if ball:
        return ball  #return should be there so that it doesnot get into stackoverflow.
    open_the_gift()