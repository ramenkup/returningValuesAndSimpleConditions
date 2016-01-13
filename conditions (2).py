'''
Author: Spencer Klinge
Date: 10 / 2 / 2015
Class: ISTA 130
Section Leader: Will Zandler

Description:
This program runs a series of functions described in the homework 4 outline.
'''
def word_length(printer, relation):
    '''
    This function compares two parameters and prints a
    message about their relationship.

    Parameters:
    printer: the word whose length being compared to relation
    relation: the number being compared to printer's length
    
    Returns: None
    '''
    length= len(printer)
    if length > relation:
        print("Longer than", relation, 'characters:', printer)
        return None
    if length == relation:
        print('Exactly', relation, 'characters:', printer )
        return None
    if length < relation:
        print('Shorter than', relation, 'characters:', printer)
        return None


def stop_light(color, time):
    '''
    This function takes a time and stoplight color from the user
    and prints the light's response

    Parameters:
    color: the starting color of the light. is printed if hasent been
    shown long enough

    time: the amount of time the color is being shown, the funciton then
    decides if this is long enought to constitute a change

    Returns: None
    '''
    if color == 'green':
        if(time> 60):
            print('yellow')
            return None
        else: 
            print(color)
            return None
    if color == "yellow":
        if time > 5:
            print('red')
            return None
        else:
            print (color)
            return None
    if color == 'red':
        if time > 55:
            print ('green')
            return None
        else:
            print (color)
            return None
    return None

def is_normal_blood_pressure(sys_blood, dia_blood ):
    '''
    This function takes  systolic and
    diastolic blood and compares tests them against a givin range
    the see if it falls within the bounds of 'normal'
    
    Parameters:
    sys_blood: int, the users systolic blood pressure
    dia_blood: int, the users diastolic blood pressure
    
    Returns: Boolean
    '''
    if(sys_blood < 120 and dia_blood < 80):
        return True
    return False


def doctor():
    '''
    This function take user input of systolic and diastolic readings and outputs
    the classification(normal/ high) after calling the is_normal_blood_pressure()
    
    Parameters: None
    Returns: None
    '''
    if(is_normal_blood_pressure(input('Enter your systolic reading:'), input('Enter your diastolic reading:'))):
        print('Your blood pressure is normal.')
        return None
    else:
        print('Your blood pressure is high.')


def pants_size(waist):
    '''
    This function takes waist size and returns the size
    the waist falls into(small,medium,large)
    Parameters:
    waist- int, waist size in inches
    Returns: string literal, 'small', 'medium', 'large'
    '''
    if(waist >= 34):
        return 'large'
    if(waist >= 30):
        return 'medium'
    return 'small'


def pants_fitter():
    '''
    This function takes information from user input to
    output the price of the total number and type of pants
    the user is trying to buy. it calls on the pants_size()
    function to output the designated size of the user's pants
    Parameters: None
    Returns: None
    '''
    name= input('Enter your name:')
    print('Greetings', name, 'welcome to Pants-R-Us')
    waist= input('Enter your waist size in inches:')
    pairs= input('How many pairs of pants would you like?')
    pant_type= input('Would you like regular or fancy pants?')
    if(pant_type == 'fancy'):
        cost=100
    if(pant_type == 'regular'):
        cost=40
    print(pairs, 'pairs of', pants_size(waist), pant_type, 'pants:','$', cost*pairs)
    return None



def digdug(number):
    '''
    This function take a number from the user
    and outputs the numbers starting from 3 that can be
    evenly divided by 3 or 5. division by 3 prints dig, 5
    dug, and both, digdug.
    
    Parameters:
    number: int, the number up to which that is printed.
    Returns: None
    '''
    count=3
    while (count <= number and number >2):
        if count % 3 == 0 and count % 5 == 0:
            print(count,':','digdug')
            count+= 1
            continue
        if count % 3 == 0:
            print(count, ':', 'dig')
            count+= 1
            continue
        if count % 5 == 0:
            print(count, ':', 'dug')
            count+= 1
            continue      
        count+=1
    return None






def beef_type(percent_lean):
    '''
    this fuction returns the classification of of leanesss
    of a peice of beff.
    Parameters:
    percent_lean: float the percent lean of the beef
    Returns: String literal, the classification of beef
    '''
    if(percent_lean >= 0.0 and percent_lean <78.0):
        return 'Hamburger'
    if(percent_lean >=78.0 and percent_lean <85.0):
        return 'Chuck'
    if(percent_lean >= 85.0 and percent_lean < 90.0):
        return 'Round'
    if(percent_lean >= 90.0 and percent_lean <= 95.0):
        return 'Sirloin'
    return 'Unknown'


def species_height(race, height):
    '''
    This function returns weither the given height
    is below, equel to, or above the average of the
    givin races
    
    Parameters:
    race- string, either Klingon or Human
    height-float, the givin height to be compared to the average
    Returns: None
    '''
    if(race == 'Human' and height < 67.0):
        print('Below Average')
        return None
    if(race == 'Human' and height == 67.0):
        print('Average')
        return None
    if(race == 'Human' and height > 67.0):
        print('Above Average')
        return None
    if(race == 'Klingon' and height < 71.0):
        print('Below Average')
        return None
    if(race == 'Klingon' and height == 71.0):
        print('Average')
        return None
    if(race == 'Klingon' and height > 71.0):
        print('Above Average')
        return None

def sooner_date(month, day, month2, day2):
    '''
    This function takes two dates of the same year and prints
    which comes first
    
    Parameters:
    month; int, the first month
    day: int, the first day
    month2: int, the second month
    day2: int, the second day
    Returns: None
    '''
    if(month < month2):
        print(month, '/', day)
        return None
    if( month > month2):
        print(month2, '/', day2)
        return None
    if(month == month2):
        if(day < day2):
            print(month, '/', day)
            return None
        print(month2, '/', day2)
        return None

'Main does nothing, testing is handeled by test conditions file'
def main():

    if __name__ == '__main__':
        main()