import cv2
import os
import json
import time

def load_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Cannot load image at {image_path}")
    return img

def detect_coupons(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
  
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
  
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    
    return contours

def crop_and_save_coupons(image, contours, base_name, output_dir):
    saved_files = []
    start_time = time.time()
    
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        
        
        cropped_coupon = image[y:y+h, x:x+w]
        file_name = f"{base_name}_{i+1}.png"
        file_path = os.path.join(output_dir, file_name)
        cv2.imwrite(file_path, cropped_coupon)
        saved_files.append(file_name)
    
    end_time = time.time()
    processing_time = end_time - start_time
    
    return saved_files, processing_time

def log_to_json(saved_files, processing_time, json_path):
    log_data = {
        "found_images": saved_files,
        "time_taken_seconds": processing_time
    }
    with open(json_path, 'w') as json_file:
        json.dump(log_data, json_file, indent=4)

def main(image_path, base_name, output_dir):
    image = load_image(image_path)
    contours = detect_coupons(image)
    
    # Sort contours by their position to maintain order (left to right, top to bottom)
    contours = sorted(contours, key=lambda c: (cv2.boundingRect(c)[1], cv2.boundingRect(c)[0]))
    
    saved_files, processing_time = crop_and_save_coupons(image, contours, base_name, output_dir)
    
    json_path = os.path.join(output_dir, f"{base_name}_log.json")
    log_to_json(saved_files, processing_time, json_path)
    
    print(f"Processed {len(saved_files)} coupons in {processing_time:.2f} seconds.")
    print(f"Log saved to {json_path}")

if __name__ == "__main__":
    # Example usage:
    image_paths = [
        "C:/Habsy/3_coupons.png",
        "C:/Habsy/4_coupons.png",
        "C:/Habsy/6_coupons.png"
    ]
    
    for image_path in image_paths:
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_dir = os.path.join("output_directory", base_name)
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        main(image_path, base_name, output_dir)







