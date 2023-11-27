import math

def main():
    cans_names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "8Z short", "#10", "#211", "#300", "303"]
    cans_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    cans_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    cans_volume = []
    cans_surface_area = []
    cans_storage_efficiency [""]
    
    cans = [cans_names, cans_radius, cans_height]
        
    cans_volume = compute_volume(cans_radius[0], cans_height[0])
    cans_surface_area = compute_surface_area(cans_radius[0], cans_height[0])
    cans_storage_efficiency = compute_storage_efficiency(cans_volume, cans_surface_area)
    print(f"{cans_names[0]} {cans_storage_efficiency:.2f}")
    
    
def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

main()