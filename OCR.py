import easyocr
import cv2
 
def perform_ocr(image_path):
    # Create an OCR reader with the specified language (custom recognition model)
    #custom_model_path = 'custom_model3'
    #reader =  easyocr.Reader(['en'],recog_network='best_accuracy',model_storage_directory=custom_model_path,user_network_directory=custom_model_path) 

    # Create an OCR reader with the specified language (Pretrained model) 
    reader =  easyocr.Reader(['en']) 
    
    recognized_text =""

    # Read the image using OpenCV
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    detection_result = reader.detect(image,
                                     slope_ths=1,
                                 height_ths =1
                                 )
    text_coordinates = detection_result[0][0]


    results = reader.recognize(image,
                               horizontal_list=text_coordinates,
                               free_list=[],
                               detail=0,
                               )

    for result in results:
        recognized_text += result + '\n'
    
    return recognized_text

img = '../OCR Prototype/Text_segmentation/sample_img (5).jpg'
print(perform_ocr(img))
