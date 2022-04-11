def recommendations(dataframe, ladies_men, age, max_price, colour, clothing_style, pattern):
    if ladies_men!=None and ladies_men in list(dataframe["index_group_name"].unique()):
        ladies_men = ladies_men.lower()
        result = dataframe[dataframe.index_group_name==ladies_men]
    
    if age!=None:
        if age>93 or age<0:
            return "Age is not valid. Please try again"
        elif age>=0 and age<7:
            age_group = "Generation Alpha"
        elif age>=8 and age<24:
            age_group = "Generation Z"
        elif age>=24 and age<40:
            age_group = "Millenials"
        elif age>=40 and age<56:
            age_group = "Generation X"
        elif age>=56 and age<75:
            age_group = "Baby Boomers"
        elif age>=75 and age<=93:
            age_group = "The Silent Generation"
        else:
            uselessvar = 1
    result = result[result.age_group==age_group]
    
    if max_price!=None:
        max_price = float(max_price)
        if max_price > 0: 
            result = result[result.price <= max_price]
    else:
        return "Invalid price inputted. Please input a monetary value more than 0."
    
    if colour!=None and colour in list(dataframe["colour_group_name"].unique()):
        colour = colour.lower()
        result = result[result.colour_group_name==colour]
    
    if clothing_style!=None:
        clothing_style = clothing_style.lower()
        result = result[result['department_name'].str.contains(clothing_style)]
    
    if pattern!=None:
        pattern = pattern.lower()
        result = result[result['graphical_appearance_name'].str.contains(pattern)]
    
    return result