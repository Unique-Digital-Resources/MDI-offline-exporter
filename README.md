# MDI Icon Offline Exporter

This Python script is designed to process a list of Material Design Icons (MDI) in SVG format, modify their size and color, and export them as PNG files. It utilizes the `cairosvg` library to convert SVG files to PNG format and provides an easy way to customize icon appearance by changing the size and fill color.

## Features

- **Batch Processing:** Convert multiple SVG icons to PNG format in one go.
- **Customizable Size:** Modify the width and height of the SVG icons to your desired size.
- **Customizable Color:** Change the fill color of all SVG paths to your preferred color.
- **Error Handling:** Skips icons that are not found in the input directory and informs the user.

## Usage

To use this script, you need to provide:

1. **Icon Names:** A list of icon names (without the `.svg` extension).
2. **Input Folder:** The absolute path to the folder containing the SVG files.
3. **Output Folder:** The absolute path where the PNG files will be saved.
4. **Size:** The desired size of the icons (e.g., 48 for 48x48).
5. **Color:** The desired fill color in hexadecimal format (e.g., `#330044`).


## Example Outputs

The following table demonstrates the result of converting icons using different colors.

| **Color** | **Resulting Icons** |
|-----------|---------------------|
| Blue  | ![Blue Icon](path/to/blue_icon.png) |
| Green  | ![Green Icon](path/to/green_icon.png) |
| Orange  | ![Orange Icon](path/to/orange_icon.png) |
| Purple  | ![Purple Icon](path/to/purple_icon.png) |

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Author

This script was developed by [Abdo Mahmoud](https://github.com/Unique-Digital-Resources).
