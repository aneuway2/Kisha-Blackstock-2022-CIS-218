""" Eggs Lab, Kisha Blackstock, https://www.nelliesfreerange.com/blog/egg-sizes """

while (True):

    Eggs = float( input ("Please type in egg weight in ounces "))

    if Eggs >= 30:
        size = "Jumbo"
    elif Eggs >= 27:
        size = "Extra-Large"
    elif Eggs >= 24:
        size = "Large"
    elif Eggs >= 21:
        size = "Medium"
    elif Eggs >= 18:
        size = "Small"
    elif Eggs >= 15:
        size = "Peewee"
        
    print ("An egg weighing ", Eggs, "ounces is the size ", size)
