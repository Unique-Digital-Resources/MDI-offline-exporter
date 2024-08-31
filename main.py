#Copyright [2024] [Abdo Mahmoud- Unique Digital Resources (https://github.com/Unique-Digital-Resources)]

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

import os
from cairosvg import svg2png

def process_icons(icon_names, input_folder, output_folder, size, color):
    # Ensure the input and output folders are absolute paths
    input_folder = os.path.abspath(input_folder)
    output_folder = os.path.abspath(output_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for icon_name in icon_names:
        input_path = os.path.join(input_folder, f"{icon_name}.svg")
        output_path = os.path.join(output_folder, f"{icon_name}.png")
        
        if not os.path.exists(input_path):
            print(f"Icon {icon_name}.svg not found in {input_folder}. Skipping...")
            continue

        with open(input_path, 'r') as file:
            svg_content = file.read()
        
        # Modify the SVG content to change the size
        svg_content = svg_content.replace('width="24"', f'width="{size}"')
        svg_content = svg_content.replace('height="24"', f'height="{size}"')
        
        # Force change all fill colors in the SVG
        # Add a style to override any fill colors
        style = f'<style> * {{ fill: {color} !important; }} </style>'
        svg_content = svg_content.replace('</svg>', f'{style}</svg>')
        
        # Convert the modified SVG to PNG and save it
        svg2png(bytestring=svg_content.encode('utf-8'), write_to=output_path)
        print(f"Processed {icon_name}.png")

# Example usage:
icon_names = ["account-circle","account-box","toolbox","alert-circle","account-cog","database","check-circle","tooltip"]   # List of icon names
input_folder = "/home/user/node_modules/@mdi/svg/svg"  # Absolute path to SVG folder
output_folder = "/home/user/Desktop/my_shared/my_projects/python_made_projects/mdi_icon_offline_exporter/icon_examples"          # Absolute path to output folder
size = 48                                     # Desired size (e.g., 48x48)
color = "#330044"                             # Desired color

process_icons(icon_names, input_folder, output_folder, size, color)
