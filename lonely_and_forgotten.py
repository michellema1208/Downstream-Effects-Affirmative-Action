
# from posterior.py

def askPosterior(self, type_and_scores):
    filtered_type_and_scores = filter(lambda x: x[1] > self.threshold, type_and_scores)
    """maxIndex = 0
    sorted_list = sorted(typeAndScores, key=lambda x: x[1])
    for i in range(len(sorted_list)):
        if sorted_list[i].second >= self.threshold:
            maxIndex = i
            break

    final_list = typesAndScores[maxIndex:]
    type_list = []
    for i in range(len(final_list)):
        type_list.append(final_list[i].first)"""

    return filtered_type_and_scores


"""
Parameters: takes in a list of the true types accepted by the college
Returns: a hashtable with key = type, value = percentage of people who have those types
"""
""" def trueTypePercentages(type_list):

    type_map = {}
    total_people = len(type_list)
    for type in type_list:
        if !type_map[type]:   #TODO: fix this syntax
            type_map[type] = 0
        type_map[type] += 1

    for type in type_map:
        type_map[type] = float(type_map[type])/total_people

    return type_map"""

"""def trueType(type_list):

    for i in range(len(type_list)):
        type_list[i] = float(type_list[i])/len(type_list)

    return type_list"""
