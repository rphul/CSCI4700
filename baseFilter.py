'''
    Author:     Matthew Ogden
    Created:    29 Oct 2019
    Altered:    29 Oct 2019
Description:    For quick implementation of testing nueral network model filter
Ex Execution:   python3 baseFilter.py -imageLoc path/to/img.png -modelLoc model2.h5
'''

from sys import \
        exit, \
        argv

from os import \
        path, \
        listdir

printAll = True
imageLoc = ''
modelJsonLoc = ''
modelH5Loc = ''

imageLoc = './587727222471131318_bad_test/587727222471131318_223_init_diff.png'
modelJsonLoc = './model2.json'
modelH5Loc = './model2.h5'
arglist = '-imageLoc ./587727222471131318_bad_test/587727222471131318_223_init_diff.png -modelJsonLoc ./model2.json -modelH5Loc ./model2.h5'


def main(arglist):

    print('hi')
    #endEarly = readArg(argList)

    if printAll:
        print("Image Loc: %s" % imageLoc)
        print("Model Json Loc: %s" % modelJsonLoc)
        print("Model H5 Loc: %s" % modelH5Loc)

    if endEarly:
        print("Exiting...")
        return False

    # load the Keras model
    loadedModel = loadModelFunc(modelJsonLoc, modelH5Loc)

    # Load the image
    image = loadImage( imageLoc )

    # Get prediction
    prediction = predictImg( image, loadedModel )

    # do something with prediction
    doSomething( prediction )

# End main

def loadModelFunc( modelJsonLoc, modelH5Loc ):
    
    from keras.models import model_from_json
    
    # load json and create model
    json_file = open(modelJsonLoc, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(modelH5Loc)
    print("Loaded model from disk")

    # evaluate loaded model on test data
    loaded_model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adam(),
                  metrics=['accuracy'])
    #score = model.evaluate(data_test, data_test_labels, verbose=1)
    #print('Test loss:', score[0])
    #print('Test accuracy:', score[1])


    print("Loading Keras model")
    
    return loaded_model

    #return 'keras model class thing'



def loadImage( imageLoc ):
    
    from keras.preprocessing import image

    print("Loading image")
    
    img = image.load_img(imageLoc, target_size=(128, 128), color_mode = "grayscale")
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return x

    # return "image in needed format for model prediction"


def predictImg( image, loadedModel ):
    print("Making prediction")
    
    prediction = loadedModel.predict(image)

    # Take image and get prediction from keras model
    
    return prediction

    #return 'keras prediction'

def doSomething( prediction ):

    # Just print the prediction contents for now to check if working
    print(prediction)

def readArg(argList):

    global printAll, imageLoc, modelJsonLoc, modelH5Loc

    endEarly = False
    print("hi")
    
    arglist = arglist.split(' ')
    

    for i,arg in enumerate(argList):
        

        if arg[0] != '-':
            print(arg[0])
            continue

        elif arg == '-argFile':
            argFileLoc = argList[i+1]
            argList = readArgFile( argList, argFileLoc ) 

        elif arg == '-noprint':
            printAll = False

        elif arg == '-imageLoc':
            imageLoc = arglist[i+1]
            print(imageLoc)

        elif arg == '-modelJsonLoc':
            modelJsonLoc = arglist[i+1]
            print(modelJsonLoc)
            
        elif arg == '-modelH5Loc':
            modelH5Loc = arglist[i+1]
            print(modelH5Loc)

    # Check if input arguments are valid

    if not path.exists(imageLoc):
        print("Image does not exist: %s" % imageLoc)
        endEarly = True

    if not path.exists(modelJsonLoc):
        print("Keras model JSON does not exist: %s" % modelJsonLoc)
        endEarly = True
        
    if not path.exists(modelH5Loc):
        print("Keras model H5 does not exist: %s" % modelH5Loc)
        endEarly = True

    return endEarly

# End reading command line arguments


def readArgFile(argList, argFileLoc):

    try:
        argFile = open( argFileLoc, 'r')
    except:
        print("Failed to open/read argument file '%s'" % argFileLoc)
    else:

        for l in argFile:
            l = l.strip()

            # Skip line if empty
            if len(l) == 0:
                continue

            # Skip line if comment
            if l[0] == '#':
                continue

            lineItems = l.split()
            for item in lineItems:
                argList.append(item)

        # End going through file

    return argList
# end read argument file


def readFile( fileLoc ):

    if not path.isfile( fileLoc ):
        print("File does not exist: %s" % fileLoc)
        return False, []
    
    try:
        inFile = open( fileLoc, 'r' )

    except:
        print('Failed to open/read file at \'%s\'' % fileLoc)
        return False, []

    else:
        inList = list(inFile)
        inFile.close()
        return True, inList

# End simple read file

# Run main after declaring functions
if __name__ == '__main__':
    argList = argv
    main(argList)
