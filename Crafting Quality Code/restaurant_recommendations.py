'''
The Problem:

Write a function that has three parameters
    -a restaurant file that is open for reading
    -the price range(one of $, $$, $$$, or $$$$)
    -list of cuisines
It returns a list of restaurants (in that price range, serving at least one
of those cuisines) and their ratings sorted from highest to lowest.


##    PLANNING THE PROGRAM! / NOTES
##    Keep track of restaurant rating using a dictionary
##        - key = resaurant anem
##        - value = percent recommended

# dict{str: int}
name_to_rating = {'Georgie Porgie': 87,
'Queen St. Cafe': 82,
'Mexican Grill': 85,
'Deep Fried Everything': 52}

##    Make list of the restaurents based on $

# dict of {str: list of str}
price_to_names = {'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
'$$': ['Mexican Grill'],
'$$$': ['Georgie Porgie'],
'$$$$': []}

##    List of each type of food

# dict{str: list of str]}
cuisine_to_names = {'Canadian': ['Georgie Porgie'],
'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
'Malaysian': ['Queen St. Cafe'],
'Thai': ['Queen St. Cafe'],
'Chinese': ['Dumplings R Us'],
'Mexican': ['Mexican Grill'] }


With this data, for a price of '$' and cuisines of ['Chinese', 'Thai']
we would produce this list:
[[82, 'Queen st. Cafe'], [71, 'Dumplngs R Us']]
'''

#The file containing the restaurant data.
FILENAME = 'restaurants_small.txt'

def recommend(file, price, cuisines_list):
    '''(file for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that
    are tagged with any of the items in the cuisines_list. Returna a list of
    the form [rating%, restaurant name], sorted by rating%
    '''
    # Read the file and build the data structures
    # - a dict of {restaurant name: rating}
    # - a dict of {price: list of restaurant names
    # - a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names =  read_restaurants(file)
    
    #Look for price
    #Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]
    
    #Now we have a list of restaurants in the right price range.
    #Need a new list of restaurants that serve one of the cuisines
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)
    
    #Now we have a list of restaurants that are in the right price range and served the requested cuisine.
    #Need to look at rating and sort this list
    result = build_rating_list(name_to_rating, names_final)

    #We're done! Return that sorted list.
    return result


def build_rating_list(name_to_rating, names_final):
    '''(dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name] soted by rating%.

    >>>name_to_rating = {'Georgie Porgie': 87,
        'Queens St. Cafe': 82,
        'Dumplings R Us': 71,
        'Mexican Grill': 85,
        'Deep Fried Everything': 52}
    >>> names = ['Queens St. Cafe', 'Dumplings R Us']
    >>> build_rating_list(name_to_rating, names)
    [[82, Queens St. Cafe'],[71, 'Dumplings R Us']]
    '''
    sorted_list = []
    for name in names_final:
        #make a list [rating%, restaurant name] for each restaurant in names_final
        rating_list = [name_to_rating[name], name]
        #add the first item to the list, else insert the restaurant to the corrent index based on rating%
        if len(sorted_list) == 0:
            sorted_list.append(rating_list)
        else:
            for index in range(len(sorted_list)):
                if name_to_rating[name] > sorted_list[index][0]:
                    sorted_list.insert(rating_list, index)
                else:
                    sorted_list.append(rating_list)
    return sorted_list

def filter_by_cuisine(names, cuisine_to_names, cuisines_list):
    '''(list of str, dict of {str: list of str}, list of str) -> list of str

    Returns a list of restaurant names that are filterd by the cuisines list

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = {'Canadian': ['Georgie Porgie'],
        'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
        'Malaysian': ['Queen St. Cafe'],
        'Thai': ['Queen St. Cafe'],
        'Chinese': ['Dumplings R Us'],
        'Mexican': ['Mexican Grill'] }
    >>> cuisines = ['Chinese', 'Thai']
    
    >>>filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    
    '''
    price_and_cuisine = []
    for cuisine in cuisines_list:
        for name in names:
            if name in cuisine_to_names[cuisine]:
                price_and_cuisine.append(name)
    return price_and_cuisine


def read_restaurants(filename):
    '''(file)-> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file.

     - a dict of {restaurant name: rating}
     - a dict of {price: list of restaurant names
     - a dict of {cuisine: list of restaurant names}
    '''
    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    #Get information from file as a list of list of [str, int, str, [str, str]] that contains restaurant info
    #example: [['Georgie Porgie', 87, '$$$', ['Canadian', 'Pub Food']]]
    list_of_restaurant_info = get_info_from_file(filename)
    
    
    #Build the different dictionaries!!
    for rest in list_of_restaurant_info:
        #build name_to_rating dict
        name_to_rating[rest[0]] = rest[1]

        #build the price_to_names dict
        if rest[2] not in price_to_names:
            price_to_names[rest[2]] = [rest[0]]
        else:
            price_to_names[rest[2]].append(rest[0])

        # build cuisine_to_names
        for c in rest[3]:
            if c not in cuisine_to_names:
                cuisine_to_names[c] = [rest[0]]
            else:
                cuisine_to_names[c].append(rest[0])

    return (name_to_rating, price_to_names, cuisine_to_names)


def get_info_from_file(filename):
    ''' (file) -> list of list of restaurant information

    Return a list containing a list with each restaurant information formatted

    Example:
    [['Georgie Porgie', 87, '$$$', ['Canadian', 'Pub Food']]]
    '''
    rest_file = open(filename, 'r')

    # Set up the lists to store the information
    # [name, rating%, price, cuisine]
    restaurant = []
    list_of_restaurant_info = []

    #read the information into the lists
    line = rest_file.readline()
    while line != '':
        if line != '\n':
            restaurant.append(line[:-1])
        else:
            list_of_restaurant_info.append(restaurant)
            restaurant = []
        line = rest_file.readline()
    #append the last restaurant in the list
    list_of_restaurant_info.append(restaurant)   
    rest_file.close()
    
     
    # Now have a list of lists:
    #[[name, percent, price, type], [name, ... etc ]
    #We want to format the data in our lists
    for rest in list_of_restaurant_info:
        #Format the percents from string to int
        rest[1] = int(rest[1][:-1])
        #Format the cuisine string into a list ['Canadian', 'Pub Food']
        rest[3] = rest[3].split(', ')
    
    return list_of_restaurant_info



 
    



