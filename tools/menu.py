from pick import pick

TITLE = "========================= Julia Set Generator =========================\n\n"


#   OPERATION MAP:
#
#   0-Video
#       00-MP4
#       01-GIF
#   1-Static Image
#       10-PNG
#       11-PGM
#

def menu():
    title = TITLE+'Please choose the type of file you want to create: '
    options = ['Video', 'Static Image']
    option, index = pick(options, title, indicator='=>', default_index=0)
    if index == 0:
        title_0 = 'Please choose your prefered format: '
        options_0 = ['MP4', 'GIF']
        option_0, index_0 = pick(options_0, title_0, indicator='=>', default_index=0)
        if index_0 == 0:
            return "00"
        if index_0 == 1:
            return "01"
    if index == 1:    
        title_1 = 'Please choose your prefered format: '
        options_1 = ['PNG', 'PGM']
        option_1, index_1 = pick(options_1, title_1, indicator='=>', default_index=0)        
        if index_1 == 0:
            return "10"
        if index_1 == 1:
            return "11"
        
