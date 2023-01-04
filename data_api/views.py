from rest_framework.generics import CreateAPIView
from data_api.serilizers import AudioSerializer
from rest_framework.response import Response
from data_api.speach_recogination_Functions import *


class AudioUploadView(CreateAPIView):

    serializer_class = AudioSerializer  
    
    def post(self, request,*args, **kwargs):
        # create a serializer instance using the request data
        serializer = self.get_serializer(data=request.data)
        
        # validate the serializer data
        serializer.is_valid(raise_exception=True) 
        
        # create a new instance of the Audio model using the serializer data
        self.perform_create(serializer)
        
        # get the file name of the uploaded audio file from the serializer data
        audio_file_name = serializer.data["audio_file"][22:]
        
        # recognize the text from the audio file
        audio_text = recognizing(audio_file_name).lower()

        # print(outputText)
        # return Response ({ "title" : outputText })

        #  data to be matched with the text of the audio file
        data_to_be_matched = ["india is an independent country","delhi is the capital of india"]
        
        # initialize a flag to False
        pronunciation = False
        
        # checking if audio_text matches with data_to_be_matched to send response
        for i in data_to_be_matched:
             
             if i == audio_text:
                 # set the flag to True if the audio_text matches the data_to_be_matched element
                 print("correct pronunciation") 
                 pronunciation = True
                 break
                
             else:
                 # set the flag to False if the audio_text does not match the data_to_be_matched element
                 print("incorrect pronunciation") 
                 pronunciation = False
                 continue
        
        # check the value of the flag
        if   pronunciation == True:
            # return a response with correct pronunciation message if the flag is True
            return Response({     
                                  "text" : audio_text ,
                                   "data" : " correct pronunciation"
                                })
        elif pronunciation == False:
            # return a response with incorrect pronunciation message if the flag is False
            return Response({      "text" : audio_text ,
                                   "data" : "incorrect correct pronunciation"
                                })















    
        
        








      