import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import glob
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Process images from two groups for statistical comparison.")
    parser.add_argument('--groupA', type=str, required=True, help="Path to the folder containing Group A images")
    parser.add_argument('--groupB', type=str, required=True, help="Path to the folder containing Group B images")
    return parser.parse_args()
def load_images_from_folders(folder_paths):
    images = []
    for folder_path in folder_paths:
        images.extend(
            [cv2.imread(filename, cv2.IMREAD_GRAYSCALE) for filename in glob.glob(os.path.join(folder_path, '*.tif')) if cv2.imread(filename, cv2.IMREAD_GRAYSCALE) is not None] )
    return images
def preprocess_images(images):
    """Apply Gaussian Blur to a list of images."""
    return [cv2.GaussianBlur(image, (5, 5), 0) for image in images]

def segment_images(images):
    """Apply Otsu's thresholding to a list of images."""
    return [cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] for image in images]
def find_contours(images):
    """Find contours for a list of thresholded images."""
    return [cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] for image in images]

def measure_areas(contours):
    """Measure areas of detected contours."""
    return [cv2.contourArea(c) for contour_list in contours for c in contour_list]

def statistical_comparison(areas1, areas2):
    """Perform t-test on two sets of areas."""
    return stats.ttest_ind(areas1, areas2)

def visualize_area_distribution(areas1, areas2):
    """Visualize the distribution of areas using histograms."""
    plt.figure(figsize=(12, 6))
    plt.hist(areas1, alpha=0.5, label='Nucleus24', bins=30)
    plt.hist(areas2, alpha=0.5, label='Nucleus38', bins=30)
    plt.title('Nucleus Size Distribution')
    plt.xlabel('Area (pixels)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def save_results_to_pdf(t_statistic, p_value, areas_nucleus24, areas_nucleus38):
    """Save statistical results and area means to a PDF file."""
    c = canvas.Canvas("results.pdf", pagesize=letter)
    c.drawString(100, 750, f"Nucleus24 Mean Area: {np.mean(areas_nucleus24):.2f} pixels")
    c.drawString(100, 730, f"Nucleus38 Mean Area: {np.mean(areas_nucleus38):.2f} pixels")
    c.drawString(100, 710, f"T-statistic: {t_statistic:.2f}, P-value: {p_value:.4f}")
    
    # Visualization
    plt.figure(figsize=(12, 6))
    plt.hist(areas_nucleus24, alpha=0.5, label='Group 1', bins=30)
    plt.hist(areas_nucleus38, alpha=0.5, label='Group 2', bins=30)
    plt.title('Nucleus Size Distribution')
    plt.xlabel('Area')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig("nucleus_distribution.png")  # Save the figure
    c.drawImage("nucleus_distribution.png", 100, 400, width=400, height=300)  # Add image to PDF
    c.save()
    
def main():
    # Parse arguments
    args = parse_arguments()

    # Define folder paths
    nucleus24_folder = os.path.expanduser('Images/groupA/')
    nucleus38_folder = os.path.expanduser('Images/groupB/')
    
    # Load images from specified folders
    nucleus24_images = load_images_from_folders([nucleus24_folder])
    nucleus38_images = load_images_from_folders([nucleus38_folder])
    
    # Preprocess images
    nucleus24_blur = preprocess_images(nucleus24_images)
    nucleus38_blur = preprocess_images(nucleus38_images)
    
    # Segment images
    thresh_nucleus24 = segment_images(nucleus24_blur)
    thresh_nucleus38 = segment_images(nucleus38_blur)
    
    # Find contours
    contours_nucleus24 = find_contours(thresh_nucleus24)
    contours_nucleus38 = find_contours(thresh_nucleus38)
    
    # Measure areas
    areas_nucleus24 = measure_areas(contours_nucleus24)
    areas_nucleus38 = measure_areas(contours_nucleus38)
    
    # Statistical comparison
    t_statistic, p_value = statistical_comparison(areas_nucleus24, areas_nucleus38)
    
    # Call the function to save results
    save_results_to_pdf(t_statistic, p_value, areas_nucleus24, areas_nucleus38)

if __name__ == "__main__":
    main()
