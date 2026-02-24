import cv2

user_path=input("Enter Your Image Path: ")
image=cv2.imread(user_path)

is_grayscale=False
if len(image.shape)==2:
    is_grayscale=True
elif len(image.shape)==3 and image.shape[2]==1:
    is_grayscale=True
    
if is_grayscale:    
    if image is not None:
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
        print("\nEnter Your Choice: ")
        print("1-Show Image: ")
        print("2-Store Image: ")
    
        choice=input("Enter Your Choice(1/2): ")
        
        if choice=='1':
            print("\nWhat do you want to show?")
            print("a-Original Image: ")
            print("b-Grayscale Image: ")
            print("c-Both: ")
        
            choice_show=input("Enter your Choice_show (a/b/c): ")
            
            if choice_show=='a':
                cv2.imshow("Original Image",image)
            elif choice_show=='b':
                cv2.imshow("Grayscale Image",gray)
            elif choice_show=='c':
                cv2.imshow("Original Image",image)
                cv2.imshow("Grayscale Image",gray)
            else:
                print("INVALID Choice_Show...")
                
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    
        elif choice=='2':
            print("\nwhat do you want to store?")
            print("A-Original Image: ")
            print("B-Grayscale Image: ")
            print("C-Both: ") 
    
            choice_store=input("Enter your Choice_show (A/B/C): ")
            if choice_store=='A':
                output_name=input("Enter Your Output Image Name (With .jpg/.png): ")
                cv2.imwrite(output_name,image)
            elif choice_store=='B':
                output_name=input("Enter Your Output Image Name (With .jpg/.png): ")
                cv2.imwrite(output_name,gray)
            elif choice_store=='C':
                output_name=input("Enter Your Output Image Name (With .jpg/.png): ")
                cv2.imwrite(output_name,image)
                output_name=input("Enter Your Output Image Name (With .jpg/.png): ")
                cv2.imwrite(output_name,gray)
            else:
                print("INVALID Choice_Store...")
    
        else:
            print("WRONG Choice...")
    
    else:
        print("ERROR! Couldn't Load The Image: ")
else:
    print("Image Allready Grayscale...")
